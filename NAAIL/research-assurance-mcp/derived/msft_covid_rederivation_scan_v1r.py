#!/usr/bin/env python3
"""Retrospective Microsoft COVID re-derivation scanner (v1-R).

This is NOT a preregistered/blinded test. It implements the independently
reviewed retrospective sensitivity protocol in covid_rederivation_protocol_v1r.json.

Execution rules:
- Preserve and verify the historical v1 base rule by Git blob.
- Declare prior exposure explicitly.
- Fetch each of the 10 primary SEC filing documents once.
- Apply PRIMARY + S1/S2/S3 to the same normalized bytes.
- Use PRIMARY/S1/S2 as deciding sets; report S3 as BROAD_DIAGNOSTIC only.
- Never print or write EDGAR_IDENTITY.
- Emit HUMAN_REVIEW when PRIMARY/S1/S2 agree and Q4-2019 has no deciding-set match.
- Emit FLAGGED on PRIMARY/S1/S2 disagreement or any Q4-2019 deciding-set match.
- Preserve every S3 snippet with no count cap for S3-only filings.
- Never emit VERIFIED automatically.
- Write a partial failure record before any non-zero exit.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = Path(__file__).resolve()
PROTOCOL_PATH = ROOT / "derived" / "covid_rederivation_protocol_v1r.json"
BASE_RULE_PATH = ROOT / "derived" / "covid_rule_v1.json"
CSV_PATH = (
    ROOT
    / "case-001-management-science"
    / "reexecution"
    / "sec_one_company_msft"
    / "msft_one_company_final.csv"
)
OUT_PATH = ROOT / "derived" / "msft_covid_rederivation_v1r_result.json"

SEC_SUBMISSIONS = "https://data.sec.gov/submissions/CIK0000789019.json"
SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
EXPECTED_BASE_RULE_BLOB = "d7760b4909ae84896cae8797fb8536f59d36053c"
CANONICAL_STATES = {"VERIFIED", "CONSISTENT", "PARTIAL", "FLAGGED", "HUMAN_REVIEW"}

CURRENT_STAGE = "startup"
PARTIAL_OBSERVATIONS: list[dict[str, Any]] = []
PARTIAL_AGREEMENT_TABLE: list[dict[str, Any]] = []


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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path)],
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()


def safe_blob(path: Path) -> str | None:
    try:
        return git_blob(path)
    except Exception:
        return None


def safe_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def execution_provenance(started_at: str) -> dict[str, Any]:
    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
    server_url = os.getenv("GITHUB_SERVER_URL", "").strip()
    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
    run_url = (
        f"{server_url}/{repository}/actions/runs/{run_id}"
        if server_url and repository and run_id
        else None
    )
    return {
        "retrieval_started_at_utc": started_at,
        "retrieval_completed_at_utc": utc_now(),
        "source_system": "SEC EDGAR",
        "executing_commit": os.getenv("GITHUB_SHA", "").strip() or None,
        "workflow_name": os.getenv("GITHUB_WORKFLOW", "").strip() or None,
        "workflow_run_id": run_id or None,
        "workflow_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "").strip() or None,
        "repository": repository or None,
        "run_url": run_url,
    }


def write_failure(error: Exception, started_at: str | None) -> None:
    protocol = safe_json(PROTOCOL_PATH) or {}
    record = {
        "protocol_id": protocol.get("protocol_id", "NAAIL-MSFT-COVID-REDERIVATION-V1R"),
        "protocol_status": protocol.get("status", "RETROSPECTIVE_REDERIVATION"),
        "prior_exposure": protocol.get("prior_exposure", True),
        "execution_status": "FAILED",
        "assurance_state": "FLAGGED",
        "failure_stage": CURRENT_STAGE,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "scanner_git_blob": safe_blob(SELF_PATH),
        "base_rule_git_blob": safe_blob(BASE_RULE_PATH),
        "protocol_git_blob": safe_blob(PROTOCOL_PATH),
        "provenance": execution_provenance(started_at or utc_now()),
        "observations_completed": PARTIAL_OBSERVATIONS,
        "agreement_rows_completed": PARTIAL_AGREEMENT_TABLE,
        "note": (
            "Partial failure record written before non-zero exit. "
            "EDGAR_IDENTITY is neither printed nor written."
        ),
    }
    try:
        OUT_PATH.write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except Exception as write_exc:
        print(
            f"ERROR: failed to persist partial failure record: {type(write_exc).__name__}",
            file=sys.stderr,
        )


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


def snippets(
    text: str,
    matches: list[re.Match[str]],
    limit: int | None = 3,
    max_words: int = 15,
) -> list[str]:
    words = list(re.finditer(r"\S+", text))
    if not words:
        return []
    starts = [word.start() for word in words]
    out: list[str] = []
    selected_matches = matches if limit is None else matches[:limit]
    for match in selected_matches:
        lo, hi = 0, len(starts)
        while lo < hi:
            mid = (lo + hi) // 2
            if starts[mid] < match.start():
                lo = mid + 1
            else:
                hi = mid
        idx = max(0, lo - 1)
        left = max(0, idx - 7)
        right = min(len(words), left + max_words)
        left = max(0, right - max_words)
        snippet = " ".join(word.group(0) for word in words[left:right])
        out.append(snippet)
    return out


def main() -> int:
    global CURRENT_STAGE, PARTIAL_OBSERVATIONS, PARTIAL_AGREEMENT_TABLE

    started_at = utc_now()
    PARTIAL_OBSERVATIONS = []
    PARTIAL_AGREEMENT_TABLE = []

    CURRENT_STAGE = "identity_preflight"
    identity = os.getenv("EDGAR_IDENTITY", "").strip()
    if not identity:
        raise RuntimeError("EDGAR_IDENTITY is required and must be supplied by the CI secret.")

    CURRENT_STAGE = "protocol_integrity"
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    if protocol.get("status") != "RETROSPECTIVE_REDERIVATION":
        raise RuntimeError("v1-R protocol status must be RETROSPECTIVE_REDERIVATION")
    if protocol.get("prior_exposure") is not True:
        raise RuntimeError("v1-R protocol must explicitly declare prior_exposure=true")

    protocol_blob = git_blob(PROTOCOL_PATH)
    scanner_blob = git_blob(SELF_PATH)
    base_rule_blob = git_blob(BASE_RULE_PATH)

    expected_rule_blob = protocol["base_rule"]["git_blob"]
    if expected_rule_blob != EXPECTED_BASE_RULE_BLOB:
        raise RuntimeError("Protocol base-rule fingerprint differs from the reviewed v1 blob")
    if base_rule_blob != EXPECTED_BASE_RULE_BLOB:
        raise RuntimeError("Historical covid_rule_v1.json Git blob mismatch")

    CURRENT_STAGE = "base_rule_integrity"
    base_rule = json.loads(BASE_RULE_PATH.read_text(encoding="utf-8"))
    if base_rule.get("status") != "FROZEN_PREREGISTERED":
        raise RuntimeError("Historical v1 base rule is not marked FROZEN_PREREGISTERED")

    term_sets = protocol.get("term_sets", {})
    required_sets = ["PRIMARY", "S1", "S2", "S3"]
    deciding_sets = ["PRIMARY", "S1", "S2"]
    if list(term_sets.keys()) != required_sets:
        raise RuntimeError("v1-R requires term sets in exact order PRIMARY, S1, S2, S3")
    if term_sets["PRIMARY"]["pattern"] != base_rule["pattern"]:
        raise RuntimeError("PRIMARY sensitivity pattern must equal the frozen v1 pattern exactly")

    compiled = {
        name: re.compile(term_sets[name]["pattern"], flags=re.IGNORECASE)
        for name in required_sets
    }

    CURRENT_STAGE = "frozen_input_integrity"
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        frozen_rows = list(csv.DictReader(handle))

    expectations = {entry["accession"]: entry for entry in base_rule["frozen_expectations"]}
    if len(frozen_rows) != 10 or len(expectations) != 10:
        raise RuntimeError("v1-R requires exactly 10 frozen observations/accessions")

    needed = {row["accession"] for row in frozen_rows}
    if needed != set(expectations):
        raise RuntimeError("Frozen CSV accessions do not equal historical v1 accessions")

    CURRENT_STAGE = "sec_metadata_retrieval"
    metadata = submission_index(identity, needed)

    observations = PARTIAL_OBSERVATIONS
    agreement_table = PARTIAL_AGREEMENT_TABLE

    for row in frozen_rows:
        accession = row["accession"]
        CURRENT_STAGE = f"filing_retrieval:{accession}"

        meta = metadata[accession]
        form = meta.get("form")
        filing_date = meta.get("filingDate")
        report_date = meta.get("reportDate")
        primary_document = meta.get("primaryDocument")

        if form not in {"10-Q", "10-K"} or form != row["form"]:
            raise RuntimeError(f"{accession}: unexpected form {form!r}")
        if not filing_date or not report_date or not primary_document:
            raise RuntimeError(
                f"{accession}: missing filingDate/reportDate/primaryDocument in SEC metadata"
            )

        accession_nodash = accession.replace("-", "")
        cik_int = str(int(base_rule["cik"]))
        document_url = (
            f"{SEC_ARCHIVES}/{cik_int}/{accession_nodash}/{primary_document}"
        )

        raw = fetch_bytes(document_url, identity)
        document_sha256 = hashlib.sha256(raw).hexdigest()
        text = primary_text(raw)

        CURRENT_STAGE = f"term_set_application:{accession}"
        set_results: dict[str, Any] = {}
        binary_values: dict[str, int] = {}
        match_objects: dict[str, list[re.Match[str]]] = {}

        for name in required_sets:
            matches = list(compiled[name].finditer(text))
            match_objects[name] = matches
            count = len(matches)
            binary = 1 if count > 0 else 0
            sample_snippets = snippets(text, matches, limit=3, max_words=15)
            if any(len(snippet.split()) > 15 for snippet in sample_snippets):
                raise RuntimeError(f"{accession}/{name}: snippet word limit violated")
            set_results[name] = {
                "pattern": term_sets[name]["pattern"],
                "role": term_sets[name].get("role"),
                "match_count": count,
                "covid_present": binary,
                "snippets": sample_snippets,
            }
            binary_values[name] = binary

        deciding_sets_agree = len({binary_values[name] for name in deciding_sets}) == 1
        s3_only = (
            all(binary_values[name] == 0 for name in deciding_sets)
            and binary_values["S3"] == 1
        )
        if s3_only:
            all_s3_snippets = snippets(
                text, match_objects["S3"], limit=None, max_words=15
            )
            if any(len(snippet.split()) > 15 for snippet in all_s3_snippets):
                raise RuntimeError(f"{accession}/S3: snippet word limit violated")
            set_results["S3"]["snippets"] = all_s3_snippets
            set_results["S3"]["snippet_policy"] = "ALL_MATCHES_NO_COUNT_CAP"
        else:
            set_results["S3"]["snippet_policy"] = "UP_TO_3"

        historical_reference = int(row["covid_present"])

        lag = (date.fromisoformat(filing_date) - date.fromisoformat(report_date)).days
        frozen_lag = int(row["filing_lag_days"])
        if (
            filing_date != row["filing_date"]
            or report_date != row["period_end"]
            or lag != frozen_lag
        ):
            raise RuntimeError(
                f"{accession}: FilingLag integrity mismatch "
                f"SEC=({report_date},{filing_date},{lag}) "
                f"frozen=({row['period_end']},{row['filing_date']},{frozen_lag})"
            )

        observations.append(
            {
                "calendar_quarter": row["calendar_quarter"],
                "form": form,
                "accession": accession,
                "period_end": report_date,
                "filing_date": filing_date,
                "filing_lag_days": lag,
                "primary_document": primary_document,
                "document_sha256": document_sha256,
                "historical_reference_covid_present": historical_reference,
                "term_sets": set_results,
                "deciding_sets_agree": deciding_sets_agree,
                "s3_only": s3_only,
                "primary_matches_historical_reference": (
                    binary_values["PRIMARY"] == historical_reference
                ),
            }
        )
        agreement_table.append(
            {
                "calendar_quarter": row["calendar_quarter"],
                "accession": accession,
                "PRIMARY": binary_values["PRIMARY"],
                "S1": binary_values["S1"],
                "S2": binary_values["S2"],
                "S3": binary_values["S3"],
                "deciding_sets_agree": deciding_sets_agree,
                "s3_only": s3_only,
                "historical_reference": historical_reference,
            }
        )

    CURRENT_STAGE = "decision_rule"
    any_deciding_disagreement = any(
        not row["deciding_sets_agree"] for row in agreement_table
    )
    q4 = next(row for row in observations if row["calendar_quarter"] == "Q4-2019")
    q4_any_deciding_match = any(
        q4["term_sets"][name]["covid_present"] == 1 for name in deciding_sets
    )
    s3_only_filings = [
        {
            "calendar_quarter": row["calendar_quarter"],
            "accession": row["accession"],
            "s3_match_count": next(
                observation["term_sets"]["S3"]["match_count"]
                for observation in observations
                if observation["accession"] == row["accession"]
            ),
        }
        for row in agreement_table
        if row["s3_only"]
    ]

    state = (
        "FLAGGED"
        if any_deciding_disagreement or q4_any_deciding_match
        else "HUMAN_REVIEW"
    )
    if state not in CANONICAL_STATES:
        raise RuntimeError("Non-canonical assurance state generated")
    if state == "VERIFIED":
        raise RuntimeError("v1-R scanner must never emit VERIFIED automatically")

    historical_primary_matches = sum(
        observation["primary_matches_historical_reference"]
        for observation in observations
    )

    CURRENT_STAGE = "result_write"
    result = {
        "protocol_id": protocol["protocol_id"],
        "protocol_status": protocol["status"],
        "prior_exposure": protocol["prior_exposure"],
        "scanner_git_blob": scanner_blob,
        "base_rule_git_blob": base_rule_blob,
        "protocol_git_blob": protocol_blob,
        "source_csv": str(CSV_PATH.relative_to(ROOT)),
        "scope": (
            "Retrospective re-derivation of COVID-term presence in the same 10 "
            "Microsoft primary 10-Q/10-K documents; exhibits excluded."
        ),
        "provenance": execution_provenance(started_at),
        "observations": observations,
        "agreement_table": agreement_table,
        "summary": {
            "filings_scanned": len(observations),
            "term_sets": required_sets,
            "deciding_term_sets": deciding_sets,
            "filings_with_deciding_set_agreement": sum(
                row["deciding_sets_agree"] for row in agreement_table
            ),
            "filings_with_deciding_set_disagreement": sum(
                not row["deciding_sets_agree"] for row in agreement_table
            ),
            "s3_only_filings": s3_only_filings,
            "primary_matches_historical_reference": historical_primary_matches,
            "q4_2019_any_deciding_set_match": q4_any_deciding_match,
            "automated_assurance_state": state,
            "verified_ceiling_condition": (
                "VERIFIED is unavailable to automation. It requires PRIMARY/S1/S2 "
                "agreement on all 10 filings, no PRIMARY/S1/S2 match in Q4-2019, "
                "and independent Claude classification of every S3-only snippet."
            ),
        },
        "interpretation": (
            "This is retrospective re-derivation, not preregistration. "
            "PRIMARY/S1/S2 are deciding sets. S3 is a BROAD_DIAGNOSTIC only. "
            "HUMAN_REVIEW means the deciding sets agree and Q4-2019 has no deciding-set "
            "match; FLAGGED means deciding-set disagreement or a Q4-2019 deciding-set match."
        ),
    }
    OUT_PATH.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["summary"], indent=2))
    print(f"output={OUT_PATH}")
    return 0


if __name__ == "__main__":
    started: str | None = None
    try:
        started = utc_now()
        raise SystemExit(main())
    except Exception as exc:
        write_failure(exc, started)
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
