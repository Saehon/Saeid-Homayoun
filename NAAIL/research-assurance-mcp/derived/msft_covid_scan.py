#!/usr/bin/env python3
"""Pre-registered Microsoft COVID text scan for NAAIL Research Assurance MCP.

Execution semantics:
- Reads the immutable derived/covid_rule_v1.json preregistration.
- Uses EDGAR_IDENTITY from the environment; identity is never hard-coded.
- Fetches SEC submissions metadata and ONLY each filing's primary 10-Q/10-K document.
- Excludes script/style/head/ix:hidden text and never fetches exhibits.
- Regenerates FilingLag for all 10 frozen accessions.
- Writes per-filing SHA-256, match count, binary flag, expectation comparison,
  and up to three snippets of at most 15 words.
- A COVID expectation mismatch is a scientific result, not an execution failure.
  Integrity/retrieval failures do fail execution.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
import time
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
RULE_PATH = ROOT / "derived" / "covid_rule_v1.json"
CSV_PATH = ROOT / "case-001-management-science" / "reexecution" / "sec_one_company_msft" / "msft_one_company_final.csv"
OUT_PATH = ROOT / "derived" / "msft_covid_scan_result.json"

SEC_SUBMISSIONS = "https://data.sec.gov/submissions/CIK0000789019.json"
SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
CANONICAL_STATES = {"VERIFIED", "CONSISTENT", "PARTIAL", "FLAGGED", "HUMAN_REVIEW"}


class PrimaryTextExtractor(HTMLParser):
    SKIP = {"script", "style", "head", "ix:hidden"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in self.SKIP:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in self.SKIP and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def fetch_bytes(url: str, identity: str) -> bytes:
    req = Request(
        url,
        headers={
            "User-Agent": identity,
            "Accept": "application/json,text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
        },
    )
    with urlopen(req, timeout=45) as response:
        data = response.read()
    time.sleep(0.15)
    return data


def fetch_json(url: str, identity: str) -> dict[str, Any]:
    return json.loads(fetch_bytes(url, identity).decode("utf-8"))


def rows_from_recent(recent: dict[str, list[Any]]) -> dict[str, dict[str, Any]]:
    if "accessionNumber" not in recent:
        return {}
    keys = list(recent.keys())
    out: dict[str, dict[str, Any]] = {}
    for i, accession in enumerate(recent["accessionNumber"]):
        out[accession] = {k: recent[k][i] for k in keys if i < len(recent[k])}
    return out


def submission_index(identity: str, needed: set[str]) -> dict[str, dict[str, Any]]:
    root = fetch_json(SEC_SUBMISSIONS, identity)
    out = rows_from_recent(root["filings"]["recent"])
    missing = needed - set(out)
    for extra in root.get("filings", {}).get("files", []):
        if not missing:
            break
        name = extra["name"]
        more = fetch_json(f"https://data.sec.gov/submissions/{name}", identity)
        out.update(rows_from_recent(more))
        missing = needed - set(out)
    if missing:
        raise RuntimeError(f"SEC submissions metadata missing accessions: {sorted(missing)}")
    return out


def primary_text(raw: bytes) -> str:
    parser = PrimaryTextExtractor()
    parser.feed(raw.decode("utf-8", errors="replace"))
    parser.close()
    return parser.text()


def snippets(text: str, matches: list[re.Match[str]], limit: int = 3, max_words: int = 15) -> list[str]:
    words = list(re.finditer(r"\S+", text))
    if not words:
        return []
    starts = [w.start() for w in words]
    out: list[str] = []
    for m in matches[:limit]:
        idx = 0
        lo, hi = 0, len(starts)
        while lo < hi:
            mid = (lo + hi) // 2
            if starts[mid] < m.start():
                lo = mid + 1
            else:
                hi = mid
        idx = max(0, lo - 1)
        left = max(0, idx - 7)
        right = min(len(words), left + max_words)
        left = max(0, right - max_words)
        snippet = " ".join(w.group(0) for w in words[left:right])
        out.append(snippet)
    return out


def main() -> int:
    retrieval_started_at = datetime.now(timezone.utc).isoformat()
    identity = os.getenv("EDGAR_IDENTITY", "").strip()
    if not identity:
        raise RuntimeError("EDGAR_IDENTITY is required and must be supplied by the CI secret.")

    rule = json.loads(RULE_PATH.read_text(encoding="utf-8"))
    if rule.get("status") != "FROZEN_PREREGISTERED":
        raise RuntimeError("covid_rule_v1.json is not marked FROZEN_PREREGISTERED")
    if rule.get("pattern") != r"\bcovid(-19)?\b|\bcoronavirus\b|\bcorona\b":
        raise RuntimeError("Frozen regex does not match the preregistered v1 rule")

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        frozen_rows = list(csv.DictReader(f))
    expectations = {x["accession"]: x for x in rule["frozen_expectations"]}
    if len(frozen_rows) != 10 or len(expectations) != 10:
        raise RuntimeError("Q5 requires exactly 10 frozen observations/accessions")

    needed = {r["accession"] for r in frozen_rows}
    if needed != set(expectations):
        raise RuntimeError("Frozen CSV accessions do not equal preregistered accessions")

    meta = submission_index(identity, needed)
    pattern = re.compile(rule["pattern"], flags=re.IGNORECASE)
    cik_int = str(int(rule["cik"]))
    observations: list[dict[str, Any]] = []

    for row in frozen_rows:
        acc = row["accession"]
        exp = expectations[acc]
        m = meta[acc]
        form = m.get("form")
        filing_date = m.get("filingDate")
        report_date = m.get("reportDate")
        primary_doc = m.get("primaryDocument")
        if form not in {"10-Q", "10-K"} or form != row["form"]:
            raise RuntimeError(f"{acc}: unexpected form {form!r}")
        if not filing_date or not report_date or not primary_doc:
            raise RuntimeError(f"{acc}: missing filingDate/reportDate/primaryDocument in SEC metadata")

        accession_nodash = acc.replace("-", "")
        doc_url = f"{SEC_ARCHIVES}/{cik_int}/{accession_nodash}/{primary_doc}"
        raw = fetch_bytes(doc_url, identity)
        doc_sha256 = hashlib.sha256(raw).hexdigest()
        text = primary_text(raw)
        found = list(pattern.finditer(text))
        count = len(found)
        flag = 1 if count > 0 else 0

        lag = (date.fromisoformat(filing_date) - date.fromisoformat(report_date)).days
        frozen_lag = int(row["filing_lag_days"])
        if filing_date != row["filing_date"] or report_date != row["period_end"] or lag != frozen_lag:
            raise RuntimeError(
                f"{acc}: FilingLag integrity mismatch "
                f"SEC=({report_date},{filing_date},{lag}) "
                f"frozen=({row['period_end']},{row['filing_date']},{frozen_lag})"
            )

        expected = int(exp["expected_covid_present"])
        if expected != int(row["covid_present"]):
            raise RuntimeError(f"{acc}: preregistered expectation differs from frozen CSV")

        obs = {
            "calendar_quarter": row["calendar_quarter"],
            "form": form,
            "accession": acc,
            "period_end": report_date,
            "filing_date": filing_date,
            "filing_lag_days": lag,
            "primary_document": primary_doc,
            "document_sha256": doc_sha256,
            "match_count": count,
            "covid_present": flag,
            "expected_covid_present": expected,
            "matches_expectation": flag == expected,
            "snippets": snippets(text, found, limit=3, max_words=15),
        }
        if any(len(s.split()) > 15 for s in obs["snippets"]):
            raise RuntimeError(f"{acc}: snippet word limit violated")
        observations.append(obs)

    all_match = all(o["matches_expectation"] for o in observations)
    q4 = next(o for o in observations if o["calendar_quarter"] == "Q4-2019")
    state = "HUMAN_REVIEW" if all_match else "FLAGGED"
    if state not in CANONICAL_STATES:
        raise RuntimeError("Non-canonical assurance state generated")

    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
    server_url = os.getenv("GITHUB_SERVER_URL", "").strip()
    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
    run_url = f"{server_url}/{repository}/actions/runs/{run_id}" if server_url and repository and run_id else None
    provenance = {
        "retrieval_started_at_utc": retrieval_started_at,
        "retrieval_completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_system": "SEC EDGAR",
        "executing_commit": os.getenv("GITHUB_SHA", "").strip() or None,
        "workflow_name": os.getenv("GITHUB_WORKFLOW", "").strip() or None,
        "workflow_run_id": run_id or None,
        "workflow_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "").strip() or None,
        "repository": repository or None,
        "run_url": run_url,
    }

    result = {
        "rule_id": rule["rule_id"],
        "rule_status": rule["status"],
        "rule_path": str(RULE_PATH.relative_to(ROOT)),
        "source_csv": str(CSV_PATH.relative_to(ROOT)),
        "scope": "Microsoft public-SEC primary 10-Q/10-K documents only; exhibits excluded.",
        "regex": rule["pattern"],
        "case_insensitive": True,
        "filinglag_regenerated_rows": len(observations),
        "provenance": provenance,
        "observations": observations,
        "summary": {
            "filings_scanned": len(observations),
            "all_10_expectations_match": all_match,
            "matching_expectations": sum(o["matches_expectation"] for o in observations),
            "mismatching_expectations": sum(not o["matches_expectation"] for o in observations),
            "q4_2019_match_count": q4["match_count"],
            "q4_2019_expected_covid_present": q4["expected_covid_present"],
            "q4_2019_observed_covid_present": q4["covid_present"],
            "covid_claim_assurance_state": state,
        },
        "interpretation": (
            "Execution success records the preregistered test. Matching expectations remain HUMAN_REVIEW until approval is separately recorded; a FLAGGED scientific result is not an execution failure."
        ),
    }
    OUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    print(f"output={OUT_PATH}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
