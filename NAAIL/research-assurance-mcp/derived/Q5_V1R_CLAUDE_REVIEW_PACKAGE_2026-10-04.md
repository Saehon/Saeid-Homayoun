# Q5 v1-R Independent Review Package — 2026-10-04

Author: GPT repair operator  
PR: #103  
Branch: `naail/research-assurance-pr-b-q5-covid`  
PR head before this packaging commit: `e9ad107ab86f4d583cc07339c72bb1f88bd89ec4`

## Decision being implemented

Claude:

`Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`

`CREATE_VERSIONED_V2_WITH_UNOBSERVED_HOLDOUT = NO` for the POC.

`GPT_MAY_PROCEED_WITH_R3 = NO` until v1-R is independently reviewed.

No SEC retrieval was performed while creating this package.

## Historical artifacts preserved unchanged

- `covid_rule_v1.json`: Git blob `d7760b4909ae84896cae8797fb8536f59d36053c`
- original v1 scanner at pre-amendment commit `702c117f62d9f2653cd4f44110679bbefa41c788`: Git blob `1b65c3cc60b0305aed244a642923ea50c95b0045`
- amended historical v1 scanner currently on PR #103: Git blob `4602d71d9a1db84405a17470fea03638a8595758`

Expected historical fingerprints remain:
- rule: `d7760b4909ae84896cae8797fb8536f59d36053c`
- original scanner: `1b65c3cc60b0305aed244a642923ea50c95b0045`
- amended v1 scanner: `4602d71d9a1db84405a17470fea03638a8595758`

## New v1-R review fingerprints

- v1-R protocol: `4851cbac193eb222f7bccd6c02c46e396b91f003`
- v1-R scanner: `ffb3f6401fa45491aec400ee92147f1a8d84a5b6`
- v1→v1-R review diff: `3da2c25a836e53d50aefb712399f99c16d9f5297`
- October-1 correction entry: `55a6a385e3fed2b35c4f44504fabbd4b2710b785`
- prior-exposure schema: `82e60c78bcbbcc6ce0c1c2970598fd0bc619acdc`
- prior-exposure registry: `a2c1318d3e51c6d73131e136983889d5a51d295d`
- prior-exposure guard test: `d77840090be7c53ffdbe1c3316a01d0ed5c06c2d`
- prior-exposure CI workflow: `309cca7205cf25b787374b39d4bf3ea3ba04293d`

These are Git blob IDs and are recomputable from the exact texts below.

---

# 1. COMPLETE v1-R PROTOCOL

Path:

`NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json`

Git blob:

`4851cbac193eb222f7bccd6c02c46e396b91f003`

```json
{
  "schema_version": "1.0.0",
  "protocol_id": "NAAIL-MSFT-COVID-REDERIVATION-V1R",
  "status": "RETROSPECTIVE_REDERIVATION",
  "created_date": "2026-10-04",
  "case_id": "MNSC-2023-4670",
  "company": "Microsoft Corporation",
  "cik": "0000789019",
  "prior_exposure": true,
  "prior_exposure_basis": {
    "description": "COVID-presence outcomes for the same 10 Microsoft observations were already present in repository artifacts before the v1 rule/scanner freeze.",
    "earliest_outcome_artifact": {
      "path": "case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.csv",
      "commit": "6dd3f0f30e851a13713d3c4ed6e48e3ee413611e",
      "timestamp_utc": "2026-10-01T09:12:54Z"
    },
    "additional_outcome_artifacts": [
      {
        "path": "case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.json",
        "commit": "bc783cef59b35e58b278544c14704cb248648d50",
        "timestamp_utc": "2026-10-01T09:12:57Z"
      },
      {
        "path": "case-001-management-science/reexecution/sec_one_company_msft/FINAL_REPORT.md",
        "commit": "53b25b530e0dccb1c2677eae1ba3e8b5a5cec7b8",
        "timestamp_utc": "2026-10-01T09:12:59Z"
      }
    ],
    "v1_freeze_commit": "2b278315a1ca38f67bab6e97b265e57ce28c3a5e",
    "v1_freeze_timestamp_utc": "2026-10-02T12:13:34Z",
    "governance_decision": "Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION"
  },
  "base_rule": {
    "path": "derived/covid_rule_v1.json",
    "git_blob": "d7760b4909ae84896cae8797fb8536f59d36053c",
    "reuse": "filing set, primary-document scope, exclusions, FilingLag integrity checks, and primary term set are reused as historical base logic; v1 remains unchanged."
  },
  "data_scope": {
    "filings": "the same 10 Microsoft accessions in covid_rule_v1.json",
    "document_scope": "primary filing document only",
    "exclude_exhibits": true,
    "fetch_rule": "download each primary filing document once and apply every frozen term set to the same bytes",
    "case_sensitive": false
  },
  "term_sets": {
    "PRIMARY": {
      "label": "v1 primary pattern unchanged",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b"
    },
    "S1": {
      "label": "primary plus compact COVID19, plural coronavirus, and SARS-CoV-2 forms",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b"
    },
    "S2": {
      "label": "S1 without corona to reduce non-disease ambiguity such as Corona beer",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b"
    },
    "S3": {
      "label": "S1 plus pandemic",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b|\\bpandemic\\b"
    }
  },
  "binary_rule": "For each term set separately: covid_present = 1 iff that term set has match_count > 0 in the normalized primary-document text; otherwise 0.",
  "normalization": "HTMLParser text extraction; exclude script/style/head/ix:hidden; collapse whitespace; regex IGNORECASE. No stemming, semantic expansion, or section cherry-picking.",
  "sensitivity_decision_rule": {
    "agreement_required": "For each of all 10 filings, PRIMARY, S1, S2 and S3 must produce the same binary value.",
    "any_term_set_disagreement": "FLAGGED",
    "q4_2019_special": "If any term set produces a match in Q4-2019, FLAGGED.",
    "automated_all_agree_state": "HUMAN_REVIEW",
    "assurance_ceiling": "VERIFIED only after all 10 binaries agree across PRIMARY/S1/S2/S3 and Claude independently reviews the snippets.",
    "note": "The scanner itself cannot emit VERIFIED."
  },
  "historical_reference": {
    "source": "case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.csv",
    "purpose": "retrospective comparison only; not treated as preregistered expected outcomes",
    "values": "2019 rows = 0; Q1-2020 through Q2-2021 = 1"
  },
  "required_output": {
    "top_level": [
      "protocol_id",
      "protocol_status",
      "prior_exposure",
      "scanner_git_blob",
      "base_rule_git_blob",
      "protocol_git_blob",
      "provenance",
      "observations",
      "agreement_table",
      "summary"
    ],
    "per_filing": [
      "calendar_quarter",
      "form",
      "accession",
      "period_end",
      "filing_date",
      "filing_lag_days",
      "primary_document",
      "document_sha256",
      "historical_reference_covid_present",
      "term_sets"
    ],
    "per_term_set": [
      "pattern",
      "match_count",
      "covid_present",
      "snippets"
    ],
    "failure_record": "On any execution/integrity/retrieval failure, write a partial failure JSON record to the result path before exiting non-zero."
  },
  "secret_policy": {
    "identity_secret": "EDGAR_IDENTITY",
    "use": "SEC HTTP User-Agent header only",
    "never_print_or_write_value": true
  },
  "immutability": "This protocol must be reviewed before execution. After the first SEC retrieval under v1-R, changes require a new versioned retrospective protocol and must not overwrite v1-R.",
  "v1_future_boundary": "A genuinely preregistered confirmatory COVID-disclosure study with unseen filings is deferred to V1, not this POC."
}

```

---

# 2. COMPLETE NEW v1-R SCANNER

Path:

`NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py`

Git blob:

`ffb3f6401fa45491aec400ee92147f1a8d84a5b6`

```python
#!/usr/bin/env python3
"""Retrospective Microsoft COVID re-derivation scanner (v1-R).

This is NOT a preregistered/blinded test. It implements the independently
reviewed retrospective sensitivity protocol in covid_rederivation_protocol_v1r.json.

Execution rules:
- Preserve and verify the historical v1 base rule by Git blob.
- Declare prior exposure explicitly.
- Fetch each of the 10 primary SEC filing documents once.
- Apply PRIMARY + S1/S2/S3 to the same normalized bytes.
- Never print or write EDGAR_IDENTITY.
- Emit HUMAN_REVIEW when all sensitivity binaries agree and Q4-2019 has no match.
- Emit FLAGGED on any sensitivity disagreement or any Q4-2019 match.
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
    limit: int = 3,
    max_words: int = 15,
) -> list[str]:
    words = list(re.finditer(r"\S+", text))
    if not words:
        return []
    starts = [word.start() for word in words]
    out: list[str] = []
    for match in matches[:limit]:
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

        for name in required_sets:
            matches = list(compiled[name].finditer(text))
            count = len(matches)
            binary = 1 if count > 0 else 0
            sample_snippets = snippets(text, matches, limit=3, max_words=15)
            if any(len(snippet.split()) > 15 for snippet in sample_snippets):
                raise RuntimeError(f"{accession}/{name}: snippet word limit violated")
            set_results[name] = {
                "pattern": term_sets[name]["pattern"],
                "match_count": count,
                "covid_present": binary,
                "snippets": sample_snippets,
            }
            binary_values[name] = binary

        all_sets_agree = len(set(binary_values.values())) == 1
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
                "all_term_sets_agree": all_sets_agree,
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
                "all_term_sets_agree": all_sets_agree,
                "historical_reference": historical_reference,
            }
        )

    CURRENT_STAGE = "decision_rule"
    any_disagreement = any(not row["all_term_sets_agree"] for row in agreement_table)
    q4 = next(row for row in observations if row["calendar_quarter"] == "Q4-2019")
    q4_any_match = any(
        result["covid_present"] == 1 for result in q4["term_sets"].values()
    )

    state = "FLAGGED" if any_disagreement or q4_any_match else "HUMAN_REVIEW"
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
            "filings_with_full_term_set_agreement": sum(
                row["all_term_sets_agree"] for row in agreement_table
            ),
            "filings_with_term_set_disagreement": sum(
                not row["all_term_sets_agree"] for row in agreement_table
            ),
            "primary_matches_historical_reference": historical_primary_matches,
            "q4_2019_any_term_set_match": q4_any_match,
            "automated_assurance_state": state,
            "verified_ceiling_condition": (
                "VERIFIED is unavailable to automation. It requires all 10 binaries "
                "to agree across PRIMARY/S1/S2/S3 and independent Claude snippet review."
            ),
        },
        "interpretation": (
            "This is retrospective re-derivation, not preregistration. "
            "HUMAN_REVIEW means sensitivity binaries agree and Q4-2019 has no match; "
            "FLAGGED means term-set disagreement or a Q4-2019 match."
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

```

---

# 3. FULL DIFF — AMENDED HISTORICAL v1 SCANNER → v1-R SCANNER

Old v1 scanner Git blob:

`4602d71d9a1db84405a17470fea03638a8595758`

New v1-R scanner Git blob:

`ffb3f6401fa45491aec400ee92147f1a8d84a5b6`

```diff
--- a/NAAIL/research-assurance-mcp/derived/msft_covid_scan.py
+++ b/NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py
@@ -1,16 +1,19 @@
 #!/usr/bin/env python3
-"""Pre-registered Microsoft COVID text scan for NAAIL Research Assurance MCP.
+"""Retrospective Microsoft COVID re-derivation scanner (v1-R).
 
-Execution semantics:
-- Reads the immutable derived/covid_rule_v1.json preregistration.
-- Uses EDGAR_IDENTITY from the environment; identity is never hard-coded.
-- Fetches SEC submissions metadata and ONLY each filing's primary 10-Q/10-K document.
-- Excludes script/style/head/ix:hidden text and never fetches exhibits.
-- Regenerates FilingLag for all 10 frozen accessions.
-- Writes per-filing SHA-256, match count, binary flag, expectation comparison,
-  and up to three snippets of at most 15 words.
-- A COVID expectation mismatch is a scientific result, not an execution failure.
-  Integrity/retrieval failures do fail execution.
+This is NOT a preregistered/blinded test. It implements the independently
+reviewed retrospective sensitivity protocol in covid_rederivation_protocol_v1r.json.
+
+Execution rules:
+- Preserve and verify the historical v1 base rule by Git blob.
+- Declare prior exposure explicitly.
+- Fetch each of the 10 primary SEC filing documents once.
+- Apply PRIMARY + S1/S2/S3 to the same normalized bytes.
+- Never print or write EDGAR_IDENTITY.
+- Emit HUMAN_REVIEW when all sensitivity binaries agree and Q4-2019 has no match.
+- Emit FLAGGED on any sensitivity disagreement or any Q4-2019 match.
+- Never emit VERIFIED automatically.
+- Write a partial failure record before any non-zero exit.
 """
 from __future__ import annotations
 
@@ -19,6 +22,7 @@
 import json
 import os
 import re
+import subprocess
 import sys
 import time
 from datetime import date, datetime, timezone
@@ -28,15 +32,28 @@
 from urllib.request import Request, urlopen
 
 ROOT = Path(__file__).resolve().parents[1]
-RULE_PATH = ROOT / "derived" / "covid_rule_v1.json"
-CSV_PATH = ROOT / "case-001-management-science" / "reexecution" / "sec_one_company_msft" / "msft_one_company_final.csv"
-OUT_PATH = ROOT / "derived" / "msft_covid_scan_result.json"
+SELF_PATH = Path(__file__).resolve()
+PROTOCOL_PATH = ROOT / "derived" / "covid_rederivation_protocol_v1r.json"
+BASE_RULE_PATH = ROOT / "derived" / "covid_rule_v1.json"
+CSV_PATH = (
+    ROOT
+    / "case-001-management-science"
+    / "reexecution"
+    / "sec_one_company_msft"
+    / "msft_one_company_final.csv"
+)
+OUT_PATH = ROOT / "derived" / "msft_covid_rederivation_v1r_result.json"
 
 SEC_SUBMISSIONS = "https://data.sec.gov/submissions/CIK0000789019.json"
 SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
+EXPECTED_BASE_RULE_BLOB = "d7760b4909ae84896cae8797fb8536f59d36053c"
 CANONICAL_STATES = {"VERIFIED", "CONSISTENT", "PARTIAL", "FLAGGED", "HUMAN_REVIEW"}
 
+CURRENT_STAGE = "startup"
+PARTIAL_OBSERVATIONS: list[dict[str, Any]] = []
+PARTIAL_AGREEMENT_TABLE: list[dict[str, Any]] = []
 
+
 class PrimaryTextExtractor(HTMLParser):
     SKIP = {"script", "style", "head", "ix:hidden"}
 
@@ -61,6 +78,88 @@
         return re.sub(r"\s+", " ", " ".join(self.parts)).strip()
 
 
+def utc_now() -> str:
+    return datetime.now(timezone.utc).isoformat()
+
+
+def git_blob(path: Path) -> str:
+    return subprocess.check_output(
+        ["git", "hash-object", str(path)],
+        text=True,
+        stderr=subprocess.DEVNULL,
+    ).strip()
+
+
+def safe_blob(path: Path) -> str | None:
+    try:
+        return git_blob(path)
+    except Exception:
+        return None
+
+
+def safe_json(path: Path) -> dict[str, Any] | None:
+    try:
+        return json.loads(path.read_text(encoding="utf-8"))
+    except Exception:
+        return None
+
+
+def execution_provenance(started_at: str) -> dict[str, Any]:
+    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
+    server_url = os.getenv("GITHUB_SERVER_URL", "").strip()
+    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
+    run_url = (
+        f"{server_url}/{repository}/actions/runs/{run_id}"
+        if server_url and repository and run_id
+        else None
+    )
+    return {
+        "retrieval_started_at_utc": started_at,
+        "retrieval_completed_at_utc": utc_now(),
+        "source_system": "SEC EDGAR",
+        "executing_commit": os.getenv("GITHUB_SHA", "").strip() or None,
+        "workflow_name": os.getenv("GITHUB_WORKFLOW", "").strip() or None,
+        "workflow_run_id": run_id or None,
+        "workflow_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "").strip() or None,
+        "repository": repository or None,
+        "run_url": run_url,
+    }
+
+
+def write_failure(error: Exception, started_at: str | None) -> None:
+    protocol = safe_json(PROTOCOL_PATH) or {}
+    record = {
+        "protocol_id": protocol.get("protocol_id", "NAAIL-MSFT-COVID-REDERIVATION-V1R"),
+        "protocol_status": protocol.get("status", "RETROSPECTIVE_REDERIVATION"),
+        "prior_exposure": protocol.get("prior_exposure", True),
+        "execution_status": "FAILED",
+        "assurance_state": "FLAGGED",
+        "failure_stage": CURRENT_STAGE,
+        "error_type": type(error).__name__,
+        "error_message": str(error),
+        "scanner_git_blob": safe_blob(SELF_PATH),
+        "base_rule_git_blob": safe_blob(BASE_RULE_PATH),
+        "protocol_git_blob": safe_blob(PROTOCOL_PATH),
+        "provenance": execution_provenance(started_at or utc_now()),
+        "observations_completed": PARTIAL_OBSERVATIONS,
+        "agreement_rows_completed": PARTIAL_AGREEMENT_TABLE,
+        "note": (
+            "Partial failure record written before non-zero exit. "
+            "EDGAR_IDENTITY is neither printed nor written."
+        ),
+    }
+    try:
+        OUT_PATH.write_text(
+            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
+            encoding="utf-8",
+        )
+    except Exception as write_exc:
+        print(
+            f"ERROR: failed to persist partial failure record: {type(write_exc).__name__}",
+            file=sys.stderr,
+        )
+
+
 def fetch_bytes(url: str, identity: str) -> bytes:
     req = Request(
         url,
@@ -112,18 +211,22 @@
     return parser.text()
 
 
-def snippets(text: str, matches: list[re.Match[str]], limit: int = 3, max_words: int = 15) -> list[str]:
+def snippets(
+    text: str,
+    matches: list[re.Match[str]],
+    limit: int = 3,
+    max_words: int = 15,
+) -> list[str]:
     words = list(re.finditer(r"\S+", text))
     if not words:
         return []
-    starts = [w.start() for w in words]
+    starts = [word.start() for word in words]
     out: list[str] = []
-    for m in matches[:limit]:
-        idx = 0
+    for match in matches[:limit]:
         lo, hi = 0, len(starts)
         while lo < hi:
             mid = (lo + hi) // 2
-            if starts[mid] < m.start():
+            if starts[mid] < match.start():
                 lo = mid + 1
             else:
                 hi = mid
@@ -131,149 +234,241 @@
         left = max(0, idx - 7)
         right = min(len(words), left + max_words)
         left = max(0, right - max_words)
-        snippet = " ".join(w.group(0) for w in words[left:right])
+        snippet = " ".join(word.group(0) for word in words[left:right])
         out.append(snippet)
     return out
 
 
 def main() -> int:
-    retrieval_started_at = datetime.now(timezone.utc).isoformat()
+    global CURRENT_STAGE, PARTIAL_OBSERVATIONS, PARTIAL_AGREEMENT_TABLE
+
+    started_at = utc_now()
+    PARTIAL_OBSERVATIONS = []
+    PARTIAL_AGREEMENT_TABLE = []
+
+    CURRENT_STAGE = "identity_preflight"
     identity = os.getenv("EDGAR_IDENTITY", "").strip()
     if not identity:
         raise RuntimeError("EDGAR_IDENTITY is required and must be supplied by the CI secret.")
 
-    rule = json.loads(RULE_PATH.read_text(encoding="utf-8"))
-    if rule.get("status") != "FROZEN_PREREGISTERED":
-        raise RuntimeError("covid_rule_v1.json is not marked FROZEN_PREREGISTERED")
-    if rule.get("pattern") != r"\bcovid(-19)?\b|\bcoronavirus\b|\bcorona\b":
-        raise RuntimeError("Frozen regex does not match the preregistered v1 rule")
+    CURRENT_STAGE = "protocol_integrity"
+    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
+    if protocol.get("status") != "RETROSPECTIVE_REDERIVATION":
+        raise RuntimeError("v1-R protocol status must be RETROSPECTIVE_REDERIVATION")
+    if protocol.get("prior_exposure") is not True:
+        raise RuntimeError("v1-R protocol must explicitly declare prior_exposure=true")
 
-    with CSV_PATH.open(newline="", encoding="utf-8") as f:
-        frozen_rows = list(csv.DictReader(f))
-    expectations = {x["accession"]: x for x in rule["frozen_expectations"]}
+    protocol_blob = git_blob(PROTOCOL_PATH)
+    scanner_blob = git_blob(SELF_PATH)
+    base_rule_blob = git_blob(BASE_RULE_PATH)
+
+    expected_rule_blob = protocol["base_rule"]["git_blob"]
+    if expected_rule_blob != EXPECTED_BASE_RULE_BLOB:
+        raise RuntimeError("Protocol base-rule fingerprint differs from the reviewed v1 blob")
+    if base_rule_blob != EXPECTED_BASE_RULE_BLOB:
+        raise RuntimeError("Historical covid_rule_v1.json Git blob mismatch")
+
+    CURRENT_STAGE = "base_rule_integrity"
+    base_rule = json.loads(BASE_RULE_PATH.read_text(encoding="utf-8"))
+    if base_rule.get("status") != "FROZEN_PREREGISTERED":
+        raise RuntimeError("Historical v1 base rule is not marked FROZEN_PREREGISTERED")
+
+    term_sets = protocol.get("term_sets", {})
+    required_sets = ["PRIMARY", "S1", "S2", "S3"]
+    if list(term_sets.keys()) != required_sets:
+        raise RuntimeError("v1-R requires term sets in exact order PRIMARY, S1, S2, S3")
+    if term_sets["PRIMARY"]["pattern"] != base_rule["pattern"]:
+        raise RuntimeError("PRIMARY sensitivity pattern must equal the frozen v1 pattern exactly")
+
+    compiled = {
+        name: re.compile(term_sets[name]["pattern"], flags=re.IGNORECASE)
+        for name in required_sets
+    }
+
+    CURRENT_STAGE = "frozen_input_integrity"
+    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
+        frozen_rows = list(csv.DictReader(handle))
+
+    expectations = {entry["accession"]: entry for entry in base_rule["frozen_expectations"]}
     if len(frozen_rows) != 10 or len(expectations) != 10:
-        raise RuntimeError("Q5 requires exactly 10 frozen observations/accessions")
+        raise RuntimeError("v1-R requires exactly 10 frozen observations/accessions")
 
-    needed = {r["accession"] for r in frozen_rows}
+    needed = {row["accession"] for row in frozen_rows}
     if needed != set(expectations):
-        raise RuntimeError("Frozen CSV accessions do not equal preregistered accessions")
+        raise RuntimeError("Frozen CSV accessions do not equal historical v1 accessions")
 
-    meta = submission_index(identity, needed)
-    pattern = re.compile(rule["pattern"], flags=re.IGNORECASE)
-    cik_int = str(int(rule["cik"]))
-    observations: list[dict[str, Any]] = []
+    CURRENT_STAGE = "sec_metadata_retrieval"
+    metadata = submission_index(identity, needed)
 
+    observations = PARTIAL_OBSERVATIONS
+    agreement_table = PARTIAL_AGREEMENT_TABLE
+
     for row in frozen_rows:
-        acc = row["accession"]
-        exp = expectations[acc]
-        m = meta[acc]
-        form = m.get("form")
-        filing_date = m.get("filingDate")
-        report_date = m.get("reportDate")
-        primary_doc = m.get("primaryDocument")
+        accession = row["accession"]
+        CURRENT_STAGE = f"filing_retrieval:{accession}"
+
+        meta = metadata[accession]
+        form = meta.get("form")
+        filing_date = meta.get("filingDate")
+        report_date = meta.get("reportDate")
+        primary_document = meta.get("primaryDocument")
+
         if form not in {"10-Q", "10-K"} or form != row["form"]:
-            raise RuntimeError(f"{acc}: unexpected form {form!r}")
-        if not filing_date or not report_date or not primary_doc:
-            raise RuntimeError(f"{acc}: missing filingDate/reportDate/primaryDocument in SEC metadata")
+            raise RuntimeError(f"{accession}: unexpected form {form!r}")
+        if not filing_date or not report_date or not primary_document:
+            raise RuntimeError(
+                f"{accession}: missing filingDate/reportDate/primaryDocument in SEC metadata"
+            )
 
-        accession_nodash = acc.replace("-", "")
-        doc_url = f"{SEC_ARCHIVES}/{cik_int}/{accession_nodash}/{primary_doc}"
-        raw = fetch_bytes(doc_url, identity)
-        doc_sha256 = hashlib.sha256(raw).hexdigest()
+        accession_nodash = accession.replace("-", "")
+        cik_int = str(int(base_rule["cik"]))
+        document_url = (
+            f"{SEC_ARCHIVES}/{cik_int}/{accession_nodash}/{primary_document}"
+        )
+
+        raw = fetch_bytes(document_url, identity)
+        document_sha256 = hashlib.sha256(raw).hexdigest()
         text = primary_text(raw)
-        found = list(pattern.finditer(text))
-        count = len(found)
-        flag = 1 if count > 0 else 0
 
+        CURRENT_STAGE = f"term_set_application:{accession}"
+        set_results: dict[str, Any] = {}
+        binary_values: dict[str, int] = {}
+
+        for name in required_sets:
+            matches = list(compiled[name].finditer(text))
+            count = len(matches)
+            binary = 1 if count > 0 else 0
+            sample_snippets = snippets(text, matches, limit=3, max_words=15)
+            if any(len(snippet.split()) > 15 for snippet in sample_snippets):
+                raise RuntimeError(f"{accession}/{name}: snippet word limit violated")
+            set_results[name] = {
+                "pattern": term_sets[name]["pattern"],
+                "match_count": count,
+                "covid_present": binary,
+                "snippets": sample_snippets,
+            }
+            binary_values[name] = binary
+
+        all_sets_agree = len(set(binary_values.values())) == 1
+        historical_reference = int(row["covid_present"])
+
         lag = (date.fromisoformat(filing_date) - date.fromisoformat(report_date)).days
         frozen_lag = int(row["filing_lag_days"])
-        if filing_date != row["filing_date"] or report_date != row["period_end"] or lag != frozen_lag:
+        if (
+            filing_date != row["filing_date"]
+            or report_date != row["period_end"]
+            or lag != frozen_lag
+        ):
             raise RuntimeError(
-                f"{acc}: FilingLag integrity mismatch "
+                f"{accession}: FilingLag integrity mismatch "
                 f"SEC=({report_date},{filing_date},{lag}) "
                 f"frozen=({row['period_end']},{row['filing_date']},{frozen_lag})"
             )
 
-        expected = int(exp["expected_covid_present"])
-        if expected != int(row["covid_present"]):
-            raise RuntimeError(f"{acc}: preregistered expectation differs from frozen CSV")
+        observations.append(
+            {
+                "calendar_quarter": row["calendar_quarter"],
+                "form": form,
+                "accession": accession,
+                "period_end": report_date,
+                "filing_date": filing_date,
+                "filing_lag_days": lag,
+                "primary_document": primary_document,
+                "document_sha256": document_sha256,
+                "historical_reference_covid_present": historical_reference,
+                "term_sets": set_results,
+                "all_term_sets_agree": all_sets_agree,
+                "primary_matches_historical_reference": (
+                    binary_values["PRIMARY"] == historical_reference
+                ),
+            }
+        )
+        agreement_table.append(
+            {
+                "calendar_quarter": row["calendar_quarter"],
+                "accession": accession,
+                "PRIMARY": binary_values["PRIMARY"],
+                "S1": binary_values["S1"],
+                "S2": binary_values["S2"],
+                "S3": binary_values["S3"],
+                "all_term_sets_agree": all_sets_agree,
+                "historical_reference": historical_reference,
+            }
+        )
 
-        obs = {
-            "calendar_quarter": row["calendar_quarter"],
-            "form": form,
-            "accession": acc,
-            "period_end": report_date,
-            "filing_date": filing_date,
-            "filing_lag_days": lag,
-            "primary_document": primary_doc,
-            "document_sha256": doc_sha256,
-            "match_count": count,
-            "covid_present": flag,
-            "expected_covid_present": expected,
-            "matches_expectation": flag == expected,
-            "snippets": snippets(text, found, limit=3, max_words=15),
-        }
-        if any(len(s.split()) > 15 for s in obs["snippets"]):
-            raise RuntimeError(f"{acc}: snippet word limit violated")
-        observations.append(obs)
+    CURRENT_STAGE = "decision_rule"
+    any_disagreement = any(not row["all_term_sets_agree"] for row in agreement_table)
+    q4 = next(row for row in observations if row["calendar_quarter"] == "Q4-2019")
+    q4_any_match = any(
+        result["covid_present"] == 1 for result in q4["term_sets"].values()
+    )
 
-    all_match = all(o["matches_expectation"] for o in observations)
-    q4 = next(o for o in observations if o["calendar_quarter"] == "Q4-2019")
-    state = "HUMAN_REVIEW" if all_match else "FLAGGED"
+    state = "FLAGGED" if any_disagreement or q4_any_match else "HUMAN_REVIEW"
     if state not in CANONICAL_STATES:
         raise RuntimeError("Non-canonical assurance state generated")
+    if state == "VERIFIED":
+        raise RuntimeError("v1-R scanner must never emit VERIFIED automatically")
 
-    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
-    server_url = os.getenv("GITHUB_SERVER_URL", "").strip()
-    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
-    run_url = f"{server_url}/{repository}/actions/runs/{run_id}" if server_url and repository and run_id else None
-    provenance = {
-        "retrieval_started_at_utc": retrieval_started_at,
-        "retrieval_completed_at_utc": datetime.now(timezone.utc).isoformat(),
-        "source_system": "SEC EDGAR",
-        "executing_commit": os.getenv("GITHUB_SHA", "").strip() or None,
-        "workflow_name": os.getenv("GITHUB_WORKFLOW", "").strip() or None,
-        "workflow_run_id": run_id or None,
-        "workflow_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "").strip() or None,
-        "repository": repository or None,
-        "run_url": run_url,
-    }
+    historical_primary_matches = sum(
+        observation["primary_matches_historical_reference"]
+        for observation in observations
+    )
 
+    CURRENT_STAGE = "result_write"
     result = {
-        "rule_id": rule["rule_id"],
-        "rule_status": rule["status"],
-        "rule_path": str(RULE_PATH.relative_to(ROOT)),
+        "protocol_id": protocol["protocol_id"],
+        "protocol_status": protocol["status"],
+        "prior_exposure": protocol["prior_exposure"],
+        "scanner_git_blob": scanner_blob,
+        "base_rule_git_blob": base_rule_blob,
+        "protocol_git_blob": protocol_blob,
         "source_csv": str(CSV_PATH.relative_to(ROOT)),
-        "scope": "Microsoft public-SEC primary 10-Q/10-K documents only; exhibits excluded.",
-        "regex": rule["pattern"],
-        "case_insensitive": True,
-        "filinglag_regenerated_rows": len(observations),
-        "provenance": provenance,
+        "scope": (
+            "Retrospective re-derivation of COVID-term presence in the same 10 "
+            "Microsoft primary 10-Q/10-K documents; exhibits excluded."
+        ),
+        "provenance": execution_provenance(started_at),
         "observations": observations,
+        "agreement_table": agreement_table,
         "summary": {
             "filings_scanned": len(observations),
-            "all_10_expectations_match": all_match,
-            "matching_expectations": sum(o["matches_expectation"] for o in observations),
-            "mismatching_expectations": sum(not o["matches_expectation"] for o in observations),
-            "q4_2019_match_count": q4["match_count"],
-            "q4_2019_expected_covid_present": q4["expected_covid_present"],
-            "q4_2019_observed_covid_present": q4["covid_present"],
-            "covid_claim_assurance_state": state,
+            "term_sets": required_sets,
+            "filings_with_full_term_set_agreement": sum(
+                row["all_term_sets_agree"] for row in agreement_table
+            ),
+            "filings_with_term_set_disagreement": sum(
+                not row["all_term_sets_agree"] for row in agreement_table
+            ),
+            "primary_matches_historical_reference": historical_primary_matches,
+            "q4_2019_any_term_set_match": q4_any_match,
+            "automated_assurance_state": state,
+            "verified_ceiling_condition": (
+                "VERIFIED is unavailable to automation. It requires all 10 binaries "
+                "to agree across PRIMARY/S1/S2/S3 and independent Claude snippet review."
+            ),
         },
         "interpretation": (
-            "Execution success records the preregistered test. Matching expectations remain HUMAN_REVIEW until approval is separately recorded; a FLAGGED scientific result is not an execution failure."
+            "This is retrospective re-derivation, not preregistration. "
+            "HUMAN_REVIEW means sensitivity binaries agree and Q4-2019 has no match; "
+            "FLAGGED means term-set disagreement or a Q4-2019 match."
         ),
     }
-    OUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
+    OUT_PATH.write_text(
+        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
+        encoding="utf-8",
+    )
     print(json.dumps(result["summary"], indent=2))
     print(f"output={OUT_PATH}")
     return 0
 
 
 if __name__ == "__main__":
+    started: str | None = None
     try:
+        started = utc_now()
         raise SystemExit(main())
     except Exception as exc:
-        print(f"ERROR: {exc}", file=sys.stderr)
+        write_failure(exc, started)
+        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
         raise
 

```

---

# 4. OCTOBER-1 ASSURANCE CORRECTION

Path:

`NAAIL/research-assurance-mcp/derived/Q5_CORRECTION_OCT1_COVID_PROVENANCE_2026-10-04.md`

Git blob:

`55a6a385e3fed2b35c4f44504fabbd4b2710b785`

```markdown
# Q5 Correction — October 1 COVID Provenance — 2026-10-04

This is an additive correction. The original October 1 Microsoft artifacts remain unchanged.

## Affected historical artifact

`case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.json`

Historical field:

`assurance_state.covid_presence_binary = "VERIFIED"`

## Correction

The October 1 binary COVID-presence result did not have a recoverable method specification, executable code path, run ID, or per-document inspection record sufficient to support the project assurance state `VERIFIED`.

Current governance classification:

- evidence class: `EXTERNAL_CLAIM`
- provenance state: `UNRECOVERABLE_PROVENANCE`
- assurance treatment for POC recovery: `PARTIAL`
- original artifact: preserved unchanged

This does **not** assert that the October 1 0/1 values are false. It states that the available repository record cannot establish how those values were produced or independently reproduce the exact historical method.

## Prior exposure

The October 1 CSV, JSON, and final report record COVID outcomes for the same 10 Microsoft observations before `covid_rule_v1.json` was frozen on 2026-10-02. Therefore v1 is rejected as a clean preregistered confirmation.

## Approved recovery design

Claude independent decision:

`Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION`

For the POC, use a separately reviewed retrospective re-derivation protocol:

`derived/covid_rederivation_protocol_v1r.json`

The v1 rule and both historical scanner fingerprints remain unchanged.

A genuinely unobserved/preregistered holdout is deferred to V1.

```

---

# 5. PRIOR-EXPOSURE GOVERNANCE CONTROL

## Schema

Path: `NAAIL/research-assurance-mcp/derived/rule_prior_exposure_schema_v1.json`  
Git blob: `82e60c78bcbbcc6ce0c1c2970598fd0bc619acdc`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/Saehon/Saeid-Homayoun/NAAIL/research-assurance-mcp/derived/rule_prior_exposure_schema_v1.json",
  "title": "NAAIL research-rule prior-exposure governance schema",
  "type": "object",
  "required": [
    "rule_id",
    "status",
    "active_for_execution",
    "prior_exposure",
    "freeze_commit",
    "freeze_timestamp_utc",
    "earliest_outcome_artifact",
    "policy_disposition"
  ],
  "properties": {
    "rule_id": {
      "type": "string",
      "minLength": 1
    },
    "status": {
      "type": "string",
      "enum": [
        "FROZEN_PREREGISTERED",
        "RETROSPECTIVE_REDERIVATION",
        "REJECTED_V1_PREREGISTRATION",
        "HISTORICAL"
      ]
    },
    "active_for_execution": {
      "type": "boolean"
    },
    "prior_exposure": {
      "type": "boolean"
    },
    "freeze_commit": {
      "type": "string",
      "pattern": "^[0-9a-f]{40}$"
    },
    "freeze_timestamp_utc": {
      "type": "string",
      "format": "date-time"
    },
    "earliest_outcome_artifact": {
      "oneOf": [
        {
          "type": "null"
        },
        {
          "type": "object",
          "required": [
            "path",
            "commit",
            "timestamp_utc"
          ],
          "properties": {
            "path": {
              "type": "string",
              "minLength": 1
            },
            "commit": {
              "type": "string",
              "pattern": "^[0-9a-f]{40}$"
            },
            "timestamp_utc": {
              "type": "string",
              "format": "date-time"
            }
          },
          "additionalProperties": false
        }
      ]
    },
    "policy_disposition": {
      "type": "string",
      "minLength": 1
    },
    "correction_record": {
      "type": [
        "string",
        "null"
      ]
    },
    "notes": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "status": {
            "const": "FROZEN_PREREGISTERED"
          },
          "active_for_execution": {
            "const": true
          }
        },
        "required": [
          "status",
          "active_for_execution"
        ]
      },
      "then": {
        "properties": {
          "prior_exposure": {
            "const": false
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "prior_exposure": {
            "const": true
          }
        },
        "required": [
          "prior_exposure"
        ]
      },
      "then": {
        "properties": {
          "earliest_outcome_artifact": {
            "type": "object"
          }
        }
      }
    }
  ],
  "additionalProperties": false
}

```

## Registry

Path: `NAAIL/research-assurance-mcp/derived/rule_prior_exposure_registry.json`  
Git blob: `a2c1318d3e51c6d73131e136983889d5a51d295d`

```json
{
  "schema_version": "1.0.0",
  "schema_path": "derived/rule_prior_exposure_schema_v1.json",
  "entries": [
    {
      "rule_id": "NAAIL-MSFT-COVID-RULE-V1",
      "status": "REJECTED_V1_PREREGISTRATION",
      "active_for_execution": false,
      "prior_exposure": true,
      "freeze_commit": "2b278315a1ca38f67bab6e97b265e57ce28c3a5e",
      "freeze_timestamp_utc": "2026-10-02T12:13:34Z",
      "earliest_outcome_artifact": {
        "path": "NAAIL/research-assurance-mcp/case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.csv",
        "commit": "6dd3f0f30e851a13713d3c4ed6e48e3ee413611e",
        "timestamp_utc": "2026-10-01T09:12:54Z"
      },
      "policy_disposition": "Preserve historical v1; do not execute or describe it as a clean preregistered confirmation.",
      "correction_record": "NAAIL/research-assurance-mcp/derived/Q5_PREEXECUTION_PROTOCOL_AMENDMENT_2026-10-04.md",
      "notes": "Claude decision 2026-10-04: Q5_PROTOCOL_DECISION = REJECT_V1_PREREGISTRATION."
    },
    {
      "rule_id": "NAAIL-MSFT-COVID-REDERIVATION-V1R",
      "status": "RETROSPECTIVE_REDERIVATION",
      "active_for_execution": false,
      "prior_exposure": true,
      "freeze_commit": "f0d83c8980d62ef9a61d47564130bf5cbb3c0485",
      "freeze_timestamp_utc": "2026-10-04T12:16:34Z",
      "earliest_outcome_artifact": {
        "path": "NAAIL/research-assurance-mcp/case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.csv",
        "commit": "6dd3f0f30e851a13713d3c4ed6e48e3ee413611e",
        "timestamp_utc": "2026-10-01T09:12:54Z"
      },
      "policy_disposition": "Retrospective sensitivity re-derivation only; execution remains blocked pending independent Claude review.",
      "correction_record": "NAAIL/research-assurance-mcp/derived/Q5_CORRECTION_OCT1_COVID_PROVENANCE_2026-10-04.md",
      "notes": "Once independently approved for execution, active_for_execution may become true because this status is retrospective, not preregistered."
    }
  ]
}

```

## Guard test

Path: `NAAIL/research-assurance-mcp/derived/test_rule_prior_exposure_guard.py`  
Git blob: `d77840090be7c53ffdbe1c3316a01d0ed5c06c2d`

```python
#!/usr/bin/env python3
"""Fail-closed prior-exposure governance check for NAAIL research rules.

Policy:
1. Every registry entry declares prior_exposure.
2. Every referenced commit exists and its recorded timestamp matches Git history.
3. If outcome evidence predates a rule/protocol freeze, prior_exposure must be true.
4. An active FROZEN_PREREGISTERED rule must have prior_exposure=false and no outcome
   artifact dated at or before its freeze.
5. Historical/rejected rules may remain in the registry only when inactive and
   accompanied by an additive correction record.

This test performs no network access and retrieves no SEC data.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[1]
REGISTRY_PATH = PROJECT_ROOT / "derived" / "rule_prior_exposure_registry.json"

REQUIRED = {
    "rule_id",
    "status",
    "active_for_execution",
    "prior_exposure",
    "freeze_commit",
    "freeze_timestamp_utc",
    "earliest_outcome_artifact",
    "policy_disposition",
}


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def git_commit_time(commit: str) -> str:
    return subprocess.check_output(
        ["git", "show", "-s", "--format=%aI", commit],
        cwd=REPO_ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    ).strip()


def assert_commit_timestamp(commit: str, declared: str, label: str) -> datetime:
    actual = git_commit_time(commit)
    actual_dt = parse_time(actual)
    declared_dt = parse_time(declared)
    if actual_dt != declared_dt:
        raise AssertionError(
            f"{label}: declared timestamp {declared} != git author timestamp {actual}"
        )
    return actual_dt


def check_entry(entry: dict[str, Any]) -> list[str]:
    missing = sorted(REQUIRED - set(entry))
    if missing:
        raise AssertionError(f"{entry.get('rule_id','UNKNOWN')}: missing fields {missing}")

    rule_id = entry["rule_id"]
    freeze_dt = assert_commit_timestamp(
        entry["freeze_commit"], entry["freeze_timestamp_utc"], f"{rule_id}/freeze"
    )

    earliest = entry["earliest_outcome_artifact"]
    prior_exposure = entry["prior_exposure"]
    active = entry["active_for_execution"]
    status = entry["status"]

    notes: list[str] = []

    if earliest is not None:
        outcome_dt = assert_commit_timestamp(
            earliest["commit"], earliest["timestamp_utc"], f"{rule_id}/earliest_outcome"
        )
        outcome_before_or_at_freeze = outcome_dt <= freeze_dt

        if outcome_before_or_at_freeze and prior_exposure is not True:
            raise AssertionError(
                f"{rule_id}: outcome artifact predates/equal freeze but prior_exposure is not true"
            )
        if not outcome_before_or_at_freeze and prior_exposure is True:
            notes.append(
                f"{rule_id}: prior_exposure=true even though registered earliest outcome is later; review registry completeness"
            )
    elif prior_exposure is True:
        raise AssertionError(
            f"{rule_id}: prior_exposure=true requires earliest_outcome_artifact"
        )

    if status == "FROZEN_PREREGISTERED" and active:
        if prior_exposure:
            raise AssertionError(
                f"{rule_id}: active preregistered rule cannot have prior_exposure=true"
            )
        if earliest is not None and parse_time(earliest["timestamp_utc"]) <= freeze_dt:
            raise AssertionError(
                f"{rule_id}: active preregistered rule froze after outcome data already existed"
            )

    if status in {"REJECTED_V1_PREREGISTRATION", "HISTORICAL"}:
        if active:
            raise AssertionError(f"{rule_id}: rejected/historical rule must be inactive")
        correction = entry.get("correction_record")
        if not correction:
            raise AssertionError(f"{rule_id}: rejected/historical rule needs correction_record")
        if not (REPO_ROOT / correction).exists():
            raise AssertionError(
                f"{rule_id}: correction_record does not exist: {correction}"
            )

    return notes


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise AssertionError("registry.entries must be a non-empty list")

    seen: set[str] = set()
    notes: list[str] = []
    for entry in entries:
        rule_id = entry.get("rule_id")
        if rule_id in seen:
            raise AssertionError(f"duplicate rule_id: {rule_id}")
        seen.add(rule_id)
        notes.extend(check_entry(entry))

    print(
        json.dumps(
            {
                "status": "PASS",
                "entries_checked": len(entries),
                "rule_ids": sorted(seen),
                "notes": notes,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"PRIOR_EXPOSURE_GUARD_FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise

```

## CI workflow

Path: `.github/workflows/naail_rule_prior_exposure_guard.yml`  
Git blob: `309cca7205cf25b787374b39d4bf3ea3ba04293d`

```yaml
name: NAAIL Prior Exposure Guard

on:
  push:
    paths:
      - "NAAIL/research-assurance-mcp/derived/rule_prior_exposure_schema_v1.json"
      - "NAAIL/research-assurance-mcp/derived/rule_prior_exposure_registry.json"
      - "NAAIL/research-assurance-mcp/derived/test_rule_prior_exposure_guard.py"
      - "NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json"
      - "NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py"
      - ".github/workflows/naail_rule_prior_exposure_guard.yml"
  pull_request:
    paths:
      - "NAAIL/research-assurance-mcp/derived/rule_prior_exposure_schema_v1.json"
      - "NAAIL/research-assurance-mcp/derived/rule_prior_exposure_registry.json"
      - "NAAIL/research-assurance-mcp/derived/test_rule_prior_exposure_guard.py"
      - "NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json"
      - "NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py"
      - ".github/workflows/naail_rule_prior_exposure_guard.yml"

permissions:
  contents: read

jobs:
  prior-exposure-guard:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout full history
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Validate v1-R JSON
        run: |
          python - <<'PY'
          import json
          from pathlib import Path
          p = Path("NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json")
          obj = json.loads(p.read_text(encoding="utf-8"))
          assert obj["status"] == "RETROSPECTIVE_REDERIVATION"
          assert obj["prior_exposure"] is True
          assert list(obj["term_sets"]) == ["PRIMARY", "S1", "S2", "S3"]
          print("v1-R protocol JSON PASS")
          PY

      - name: Compile v1-R scanner without execution
        run: python -m py_compile NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py

      - name: Run prior-exposure guard
        run: python NAAIL/research-assurance-mcp/derived/test_rule_prior_exposure_guard.py

```

---

# 6. STATIC / GOVERNANCE CI EVIDENCE

Successful push run:

- workflow: `NAAIL Prior Exposure Guard`
- run: `37201762703`
- job: `111434733660`
- tested head: `c4218a95939205eb6c10bbe0389f577692a3edea`
- conclusion: `success`

The run performed, without SEC execution:

1. v1-R protocol JSON validation — PASS.
2. `python -m py_compile .../msft_covid_rederivation_scan_v1r.py` — PASS.
3. prior-exposure governance guard — PASS.
4. registry entries checked: 2.

Earlier fail-closed evidence is preserved:

- runs `37201706573` and `37201708559` failed because the registry contained a placeholder v1-R freeze timestamp.
- failure message showed the declared time differed from the Git author timestamp.
- registry was corrected to exact Git time `2026-10-04T12:16:34Z`.
- subsequent runs `37201720769` and `37201724096` passed.
- after static scanner checks were added, run `37201762703` also passed.

This demonstrates that the guard rejects inconsistent chronology rather than silently accepting it.

---

# 7. SCIENTIFIC / GOVERNANCE BOUNDARIES

The v1-R protocol is explicitly:

`RETROSPECTIVE_REDERIVATION`

and:

`prior_exposure = true`

It is not preregistered or blinded.

The four frozen term sets are:

- PRIMARY = historical v1 pattern unchanged.
- S1 = PRIMARY + `\\bcovid-?19\\b` + `\\bcoronaviruses\\b` + `\\bsars-cov-2\\b`.
- S2 = S1 without `\\bcorona\\b`.
- S3 = S1 + `\\bpandemic\\b`.

The scanner:
- fetches each primary filing document once;
- applies all four term sets to the same normalized bytes;
- excludes exhibits;
- records each document SHA-256;
- records term-set-specific counts, binaries and snippets;
- records scanner/base-rule/protocol Git blobs;
- records execution provenance;
- never prints/writes EDGAR_IDENTITY;
- writes a partial failure record before a non-zero exit;
- emits `FLAGGED` on any term-set disagreement or any Q4-2019 match;
- otherwise emits `HUMAN_REVIEW`;
- cannot emit `VERIFIED`.

Independent Claude snippet review is required before any bounded VERIFIED conclusion.

---

# 8. FUTURE-CASE INSTITUTIONAL CONTROL

The new governance schema requires `prior_exposure`.

The registry records:
- v1 as `REJECTED_V1_PREREGISTRATION`, inactive, prior_exposure=true;
- v1-R as `RETROSPECTIVE_REDERIVATION`, inactive pending review, prior_exposure=true.

The CI guard checks Git commit chronology. An active `FROZEN_PREREGISTERED` rule fails if:
- `prior_exposure=true`; or
- an outcome artifact exists at or before its freeze.

Rejected historical rules must remain inactive and have an additive correction record.

This preserves v1 without silently rewriting it while enforcing the stronger rule prospectively.

---

# 9. REVIEW REQUEST TO CLAUDE

Please independently recompute the Git blob IDs from the exact protocol/scanner/control texts above and review v1-R before any SEC dispatch.

Return separately:

`V1R_PROTOCOL_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

`V1R_SCANNER_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

`PRIOR_EXPOSURE_CONTROL_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

If v1-R protocol and scanner are approved, explicitly state the authorized blobs:

`AUTHORIZED_V1R_PROTOCOL_BLOB = 4851cbac193eb222f7bccd6c02c46e396b91f003`

`AUTHORIZED_V1R_SCANNER_BLOB = ffb3f6401fa45491aec400ee92147f1a8d84a5b6`

Then state:

`GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = YES / NO`

Do not approve a COVID result before execution and independent snippet review.

Current operator state:

`COVID_R3_STATUS = BLOCKED_PROTOCOL_VALIDITY`

`POC = 7 MET / 3 PARTIAL / 0 NOT_MET`

`POC_COMPLETE = FALSE`

`NOT_READY_FOR_HUMAN_POC_APPROVAL`
