# Q5 v1-R Claude Review Round 2 — 2026-10-04

Author: GPT repair operator

## Current gate

`V1R_PROTOCOL_DECISION = CHANGES_REQUIRED` — addressed below.  
`V1R_SCANNER_DECISION = CHANGES_REQUIRED` — addressed below.  
`PRIOR_EXPOSURE_CONTROL_DECISION = CHANGES_REQUIRED` — moved to separate non-blocking PR #117.  
`GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = NO` — preserved.  

No v1-R SEC retrieval or Microsoft COVID workflow dispatch has occurred.

POC remains:

`7 MET / 3 PARTIAL / 0 NOT_MET`

`POC_COMPLETE = FALSE`

## Review fingerprints

Historical base rule, unchanged:

`d7760b4909ae84896cae8797fb8536f59d36053c`

New amended v1-R protocol:

`83af7a6859b2d44b782b5d838420f07717ea79d3`

New amended v1-R scanner:

`5b0b31de72f67fd14439875db58cab7f6427f5a1`

New infrastructure workflow on draft PR #116:

`a3bef871f827674c2b24123dd25746b792ca9dc4`

Instrument commit checked out by PR #116 workflow:

`7b23810af2f4a38fdefa54b242600593c804ea91`

This commit contains the protocol/scanner blobs above.

## A. Pre-execution amendment rationale

Path:

`NAAIL/research-assurance-mcp/derived/Q5_V1R_PREEXECUTION_AMENDMENT_S3_2026-10-04.md`

Git blob:

`b5f62d11ebecd6c38b54d9bd0048a8cc7f2b0a5b`

```markdown
# Q5 v1-R Pre-Execution Amendment — S3 Diagnostic Reclassification — 2026-10-04

Author: GPT repair operator  
Status: additive pre-execution amendment  
SEC retrieval under v1-R before this amendment: **NONE**  
Historical v1 rule modified: **NO**

## Independent-review decision

Claude reviewed v1-R candidate protocol blob `4851cbac193eb222f7bccd6c02c46e396b91f003` and scanner blob `ffb3f6401fa45491aec400ee92147f1a8d84a5b6`.

Decision:

- `V1R_PROTOCOL_DECISION = CHANGES_REQUIRED`
- `V1R_SCANNER_DECISION = CHANGES_REQUIRED`
- `GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = NO`

## Reason for amendment

The candidate S3 sensitivity set added the generic term `pandemic`. That term measures broader pandemic-risk language rather than COVID-19 specifically. In the independent reviewer's offline mocked test, generic pre-COVID wording such as "affected by a pandemic, war or natural disaster" caused all four 2019 filings, including Q4-2019, to match.

That is a construct-validity defect in S3 as a deciding sensitivity set. It is not a data-driven repair to observed v1-R SEC results because no v1-R SEC retrieval has occurred.

## Amended term-set roles

### Deciding sets

- `PRIMARY`
- `S1`
- `S2`

All three explicitly name the disease or virus.

### Broad diagnostic

- `S3`

S3 remains frozen and executed, but it is reclassified as `BROAD_DIAGNOSTIC` and is **not** part of the automated agreement rule.

## Amended decision rule

1. Any disagreement among PRIMARY/S1/S2 for any filing → `FLAGGED`.
2. Any PRIMARY/S1/S2 match in Q4-2019 → `FLAGGED`.
3. If PRIMARY/S1/S2 are all zero but S3 is one for a filing, that filing is `S3_ONLY`.
4. S3-only does not automatically FLAG the run. Automated state remains `HUMAN_REVIEW`.
5. For every S3-only filing, **all S3 match snippets are retained with no count cap**, each snippet limited to ≤15 words.
6. Independent reviewer must classify every S3-only snippet as either:
   - COVID reference without an explicit virus/disease term → final claim remains subject to review and may be `FLAGGED`; or
   - generic pandemic-risk language → no effect on the bounded COVID-term claim.
7. VERIFIED ceiling remains unavailable to automation. It requires:
   - PRIMARY/S1/S2 agreement on all 10 filings;
   - no PRIMARY/S1/S2 match in Q4-2019; and
   - independent Claude classification of every S3-only snippet.

## Preservation

The candidate protocol/scanner remain in Git history. The historical `covid_rule_v1.json` and both historical v1 scanner blobs remain unchanged.

This amendment precedes any v1-R SEC retrieval.

```

## B. COMPLETE amended v1-R protocol

Path:

`NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json`

Git blob:

`83af7a6859b2d44b782b5d838420f07717ea79d3`

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
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b",
      "role": "DECIDING"
    },
    "S1": {
      "label": "primary plus compact COVID19, plural coronavirus, and SARS-CoV-2 forms",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b",
      "role": "DECIDING"
    },
    "S2": {
      "label": "S1 without corona to reduce non-disease ambiguity such as Corona beer",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b",
      "role": "DECIDING"
    },
    "S3": {
      "label": "S1 plus pandemic",
      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b|\\bpandemic\\b",
      "role": "BROAD_DIAGNOSTIC"
    }
  },
  "binary_rule": "For each term set separately: covid_present = 1 iff that term set has match_count > 0 in the normalized primary-document text; otherwise 0.",
  "normalization": "HTMLParser text extraction; exclude script/style/head/ix:hidden; collapse whitespace; regex IGNORECASE. No stemming, semantic expansion, or section cherry-picking.",
  "sensitivity_decision_rule": {
    "deciding_sets": "PRIMARY, S1 and S2 only.",
    "agreement_required": "For each of all 10 filings, PRIMARY, S1 and S2 must produce the same binary value.",
    "deciding_set_disagreement": "FLAGGED",
    "q4_2019_special": "If PRIMARY, S1 or S2 produces a match in Q4-2019, FLAGGED.",
    "s3_role": "S3 is BROAD_DIAGNOSTIC only and does not participate in automated agreement.",
    "s3_only_definition": "S3_ONLY when PRIMARY=0, S1=0, S2=0 and S3=1 for a filing.",
    "s3_only_treatment": "S3_ONLY does not itself FLAG the run. Automated state remains HUMAN_REVIEW. Store every S3 match snippet for each S3_ONLY filing with no count cap and no more than 15 words per snippet.",
    "s3_human_classification": "Claude classifies every S3_ONLY snippet as either COVID reference without an explicit deciding-set term (may require FLAGGED) or generic pandemic-risk language (no effect on bounded COVID-term claim).",
    "automated_all_deciding_agree_state": "HUMAN_REVIEW",
    "assurance_ceiling": "VERIFIED only after PRIMARY/S1/S2 agree on all 10 filings, no PRIMARY/S1/S2 match occurs in Q4-2019, and Claude independently classifies every S3_ONLY snippet.",
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
      "term_sets",
      "deciding_sets_agree",
      "s3_only"
    ],
    "per_term_set": [
      "pattern",
      "match_count",
      "covid_present",
      "snippets"
    ],
    "failure_record": "On any execution/integrity/retrieval failure, write a partial failure JSON record to the result path before exiting non-zero, preserving completed filing and agreement rows.",
    "agreement_table": [
      "calendar_quarter",
      "accession",
      "PRIMARY",
      "S1",
      "S2",
      "S3",
      "deciding_sets_agree",
      "s3_only",
      "historical_reference"
    ],
    "summary": [
      "filings_scanned",
      "term_sets",
      "deciding_term_sets",
      "filings_with_deciding_set_agreement",
      "filings_with_deciding_set_disagreement",
      "s3_only_filings",
      "primary_matches_historical_reference",
      "q4_2019_any_deciding_set_match",
      "automated_assurance_state",
      "verified_ceiling_condition"
    ]
  },
  "secret_policy": {
    "identity_secret": "EDGAR_IDENTITY",
    "use": "SEC HTTP User-Agent header only",
    "never_print_or_write_value": true
  },
  "immutability": "This protocol must be reviewed before execution. After the first SEC retrieval under v1-R, changes require a new versioned retrospective protocol and must not overwrite v1-R.",
  "v1_future_boundary": "A genuinely preregistered confirmatory COVID-disclosure study with unseen filings is deferred to V1, not this POC.",
  "amendment": {
    "date": "2026-10-04",
    "record": "derived/Q5_V1R_PREEXECUTION_AMENDMENT_S3_2026-10-04.md",
    "reason": "S3 adds generic pandemic-risk language and therefore is a broad diagnostic rather than a deciding COVID-term sensitivity set. Amendment occurred before any v1-R SEC retrieval."
  },
  "term_roles": {
    "deciding": [
      "PRIMARY",
      "S1",
      "S2"
    ],
    "broad_diagnostic": [
      "S3"
    ]
  }
}

```

## C. COMPLETE amended v1-R scanner

Path:

`NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py`

Git blob:

`5b0b31de72f67fd14439875db58cab7f6427f5a1`

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

```

## D. Protocol diff — reviewed candidate → amended candidate

Old reviewed protocol blob:

`4851cbac193eb222f7bccd6c02c46e396b91f003`

New protocol blob:

`83af7a6859b2d44b782b5d838420f07717ea79d3`

```diff
--- a/NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json
+++ b/NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json
@@ -45,29 +45,38 @@
   "term_sets": {
     "PRIMARY": {
       "label": "v1 primary pattern unchanged",
-      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b"
+      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b",
+      "role": "DECIDING"
     },
     "S1": {
       "label": "primary plus compact COVID19, plural coronavirus, and SARS-CoV-2 forms",
-      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b"
+      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b",
+      "role": "DECIDING"
     },
     "S2": {
       "label": "S1 without corona to reduce non-disease ambiguity such as Corona beer",
-      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b"
+      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b",
+      "role": "DECIDING"
     },
     "S3": {
       "label": "S1 plus pandemic",
-      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b|\\bpandemic\\b"
+      "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b|\\bcovid-?19\\b|\\bcoronaviruses\\b|\\bsars-cov-2\\b|\\bpandemic\\b",
+      "role": "BROAD_DIAGNOSTIC"
     }
   },
   "binary_rule": "For each term set separately: covid_present = 1 iff that term set has match_count > 0 in the normalized primary-document text; otherwise 0.",
   "normalization": "HTMLParser text extraction; exclude script/style/head/ix:hidden; collapse whitespace; regex IGNORECASE. No stemming, semantic expansion, or section cherry-picking.",
   "sensitivity_decision_rule": {
-    "agreement_required": "For each of all 10 filings, PRIMARY, S1, S2 and S3 must produce the same binary value.",
-    "any_term_set_disagreement": "FLAGGED",
-    "q4_2019_special": "If any term set produces a match in Q4-2019, FLAGGED.",
-    "automated_all_agree_state": "HUMAN_REVIEW",
-    "assurance_ceiling": "VERIFIED only after all 10 binaries agree across PRIMARY/S1/S2/S3 and Claude independently reviews the snippets.",
+    "deciding_sets": "PRIMARY, S1 and S2 only.",
+    "agreement_required": "For each of all 10 filings, PRIMARY, S1 and S2 must produce the same binary value.",
+    "deciding_set_disagreement": "FLAGGED",
+    "q4_2019_special": "If PRIMARY, S1 or S2 produces a match in Q4-2019, FLAGGED.",
+    "s3_role": "S3 is BROAD_DIAGNOSTIC only and does not participate in automated agreement.",
+    "s3_only_definition": "S3_ONLY when PRIMARY=0, S1=0, S2=0 and S3=1 for a filing.",
+    "s3_only_treatment": "S3_ONLY does not itself FLAG the run. Automated state remains HUMAN_REVIEW. Store every S3 match snippet for each S3_ONLY filing with no count cap and no more than 15 words per snippet.",
+    "s3_human_classification": "Claude classifies every S3_ONLY snippet as either COVID reference without an explicit deciding-set term (may require FLAGGED) or generic pandemic-risk language (no effect on bounded COVID-term claim).",
+    "automated_all_deciding_agree_state": "HUMAN_REVIEW",
+    "assurance_ceiling": "VERIFIED only after PRIMARY/S1/S2 agree on all 10 filings, no PRIMARY/S1/S2 match occurs in Q4-2019, and Claude independently classifies every S3_ONLY snippet.",
     "note": "The scanner itself cannot emit VERIFIED."
   },
   "historical_reference": {
@@ -98,7 +107,9 @@
       "primary_document",
       "document_sha256",
       "historical_reference_covid_present",
-      "term_sets"
+      "term_sets",
+      "deciding_sets_agree",
+      "s3_only"
     ],
     "per_term_set": [
       "pattern",
@@ -106,7 +117,30 @@
       "covid_present",
       "snippets"
     ],
-    "failure_record": "On any execution/integrity/retrieval failure, write a partial failure JSON record to the result path before exiting non-zero."
+    "failure_record": "On any execution/integrity/retrieval failure, write a partial failure JSON record to the result path before exiting non-zero, preserving completed filing and agreement rows.",
+    "agreement_table": [
+      "calendar_quarter",
+      "accession",
+      "PRIMARY",
+      "S1",
+      "S2",
+      "S3",
+      "deciding_sets_agree",
+      "s3_only",
+      "historical_reference"
+    ],
+    "summary": [
+      "filings_scanned",
+      "term_sets",
+      "deciding_term_sets",
+      "filings_with_deciding_set_agreement",
+      "filings_with_deciding_set_disagreement",
+      "s3_only_filings",
+      "primary_matches_historical_reference",
+      "q4_2019_any_deciding_set_match",
+      "automated_assurance_state",
+      "verified_ceiling_condition"
+    ]
   },
   "secret_policy": {
     "identity_secret": "EDGAR_IDENTITY",
@@ -114,6 +148,21 @@
     "never_print_or_write_value": true
   },
   "immutability": "This protocol must be reviewed before execution. After the first SEC retrieval under v1-R, changes require a new versioned retrospective protocol and must not overwrite v1-R.",
-  "v1_future_boundary": "A genuinely preregistered confirmatory COVID-disclosure study with unseen filings is deferred to V1, not this POC."
+  "v1_future_boundary": "A genuinely preregistered confirmatory COVID-disclosure study with unseen filings is deferred to V1, not this POC.",
+  "amendment": {
+    "date": "2026-10-04",
+    "record": "derived/Q5_V1R_PREEXECUTION_AMENDMENT_S3_2026-10-04.md",
+    "reason": "S3 adds generic pandemic-risk language and therefore is a broad diagnostic rather than a deciding COVID-term sensitivity set. Amendment occurred before any v1-R SEC retrieval."
+  },
+  "term_roles": {
+    "deciding": [
+      "PRIMARY",
+      "S1",
+      "S2"
+    ],
+    "broad_diagnostic": [
+      "S3"
+    ]
+  }
 }
 

```

## E. Scanner diff — reviewed candidate → amended candidate

Old reviewed scanner blob:

`ffb3f6401fa45491aec400ee92147f1a8d84a5b6`

New scanner blob:

`5b0b31de72f67fd14439875db58cab7f6427f5a1`

```diff
--- a/NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py
+++ b/NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py
@@ -9,9 +9,11 @@
 - Declare prior exposure explicitly.
 - Fetch each of the 10 primary SEC filing documents once.
 - Apply PRIMARY + S1/S2/S3 to the same normalized bytes.
+- Use PRIMARY/S1/S2 as deciding sets; report S3 as BROAD_DIAGNOSTIC only.
 - Never print or write EDGAR_IDENTITY.
-- Emit HUMAN_REVIEW when all sensitivity binaries agree and Q4-2019 has no match.
-- Emit FLAGGED on any sensitivity disagreement or any Q4-2019 match.
+- Emit HUMAN_REVIEW when PRIMARY/S1/S2 agree and Q4-2019 has no deciding-set match.
+- Emit FLAGGED on PRIMARY/S1/S2 disagreement or any Q4-2019 deciding-set match.
+- Preserve every S3 snippet with no count cap for S3-only filings.
 - Never emit VERIFIED automatically.
 - Write a partial failure record before any non-zero exit.
 """
@@ -214,7 +216,7 @@
 def snippets(
     text: str,
     matches: list[re.Match[str]],
-    limit: int = 3,
+    limit: int | None = 3,
     max_words: int = 15,
 ) -> list[str]:
     words = list(re.finditer(r"\S+", text))
@@ -222,7 +224,8 @@
         return []
     starts = [word.start() for word in words]
     out: list[str] = []
-    for match in matches[:limit]:
+    selected_matches = matches if limit is None else matches[:limit]
+    for match in selected_matches:
         lo, hi = 0, len(starts)
         while lo < hi:
             mid = (lo + hi) // 2
@@ -275,6 +278,7 @@
 
     term_sets = protocol.get("term_sets", {})
     required_sets = ["PRIMARY", "S1", "S2", "S3"]
+    deciding_sets = ["PRIMARY", "S1", "S2"]
     if list(term_sets.keys()) != required_sets:
         raise RuntimeError("v1-R requires term sets in exact order PRIMARY, S1, S2, S3")
     if term_sets["PRIMARY"]["pattern"] != base_rule["pattern"]:
@@ -333,9 +337,11 @@
         CURRENT_STAGE = f"term_set_application:{accession}"
         set_results: dict[str, Any] = {}
         binary_values: dict[str, int] = {}
+        match_objects: dict[str, list[re.Match[str]]] = {}
 
         for name in required_sets:
             matches = list(compiled[name].finditer(text))
+            match_objects[name] = matches
             count = len(matches)
             binary = 1 if count > 0 else 0
             sample_snippets = snippets(text, matches, limit=3, max_words=15)
@@ -343,13 +349,29 @@
                 raise RuntimeError(f"{accession}/{name}: snippet word limit violated")
             set_results[name] = {
                 "pattern": term_sets[name]["pattern"],
+                "role": term_sets[name].get("role"),
                 "match_count": count,
                 "covid_present": binary,
                 "snippets": sample_snippets,
             }
             binary_values[name] = binary
 
-        all_sets_agree = len(set(binary_values.values())) == 1
+        deciding_sets_agree = len({binary_values[name] for name in deciding_sets}) == 1
+        s3_only = (
+            all(binary_values[name] == 0 for name in deciding_sets)
+            and binary_values["S3"] == 1
+        )
+        if s3_only:
+            all_s3_snippets = snippets(
+                text, match_objects["S3"], limit=None, max_words=15
+            )
+            if any(len(snippet.split()) > 15 for snippet in all_s3_snippets):
+                raise RuntimeError(f"{accession}/S3: snippet word limit violated")
+            set_results["S3"]["snippets"] = all_s3_snippets
+            set_results["S3"]["snippet_policy"] = "ALL_MATCHES_NO_COUNT_CAP"
+        else:
+            set_results["S3"]["snippet_policy"] = "UP_TO_3"
+
         historical_reference = int(row["covid_present"])
 
         lag = (date.fromisoformat(filing_date) - date.fromisoformat(report_date)).days
@@ -377,7 +399,8 @@
                 "document_sha256": document_sha256,
                 "historical_reference_covid_present": historical_reference,
                 "term_sets": set_results,
-                "all_term_sets_agree": all_sets_agree,
+                "deciding_sets_agree": deciding_sets_agree,
+                "s3_only": s3_only,
                 "primary_matches_historical_reference": (
                     binary_values["PRIMARY"] == historical_reference
                 ),
@@ -391,19 +414,39 @@
                 "S1": binary_values["S1"],
                 "S2": binary_values["S2"],
                 "S3": binary_values["S3"],
-                "all_term_sets_agree": all_sets_agree,
+                "deciding_sets_agree": deciding_sets_agree,
+                "s3_only": s3_only,
                 "historical_reference": historical_reference,
             }
         )
 
     CURRENT_STAGE = "decision_rule"
-    any_disagreement = any(not row["all_term_sets_agree"] for row in agreement_table)
+    any_deciding_disagreement = any(
+        not row["deciding_sets_agree"] for row in agreement_table
+    )
     q4 = next(row for row in observations if row["calendar_quarter"] == "Q4-2019")
-    q4_any_match = any(
-        result["covid_present"] == 1 for result in q4["term_sets"].values()
+    q4_any_deciding_match = any(
+        q4["term_sets"][name]["covid_present"] == 1 for name in deciding_sets
     )
+    s3_only_filings = [
+        {
+            "calendar_quarter": row["calendar_quarter"],
+            "accession": row["accession"],
+            "s3_match_count": next(
+                observation["term_sets"]["S3"]["match_count"]
+                for observation in observations
+                if observation["accession"] == row["accession"]
+            ),
+        }
+        for row in agreement_table
+        if row["s3_only"]
+    ]
 
-    state = "FLAGGED" if any_disagreement or q4_any_match else "HUMAN_REVIEW"
+    state = (
+        "FLAGGED"
+        if any_deciding_disagreement or q4_any_deciding_match
+        else "HUMAN_REVIEW"
+    )
     if state not in CANONICAL_STATES:
         raise RuntimeError("Non-canonical assurance state generated")
     if state == "VERIFIED":
@@ -433,24 +476,28 @@
         "summary": {
             "filings_scanned": len(observations),
             "term_sets": required_sets,
-            "filings_with_full_term_set_agreement": sum(
-                row["all_term_sets_agree"] for row in agreement_table
+            "deciding_term_sets": deciding_sets,
+            "filings_with_deciding_set_agreement": sum(
+                row["deciding_sets_agree"] for row in agreement_table
             ),
-            "filings_with_term_set_disagreement": sum(
-                not row["all_term_sets_agree"] for row in agreement_table
+            "filings_with_deciding_set_disagreement": sum(
+                not row["deciding_sets_agree"] for row in agreement_table
             ),
+            "s3_only_filings": s3_only_filings,
             "primary_matches_historical_reference": historical_primary_matches,
-            "q4_2019_any_term_set_match": q4_any_match,
+            "q4_2019_any_deciding_set_match": q4_any_deciding_match,
             "automated_assurance_state": state,
             "verified_ceiling_condition": (
-                "VERIFIED is unavailable to automation. It requires all 10 binaries "
-                "to agree across PRIMARY/S1/S2/S3 and independent Claude snippet review."
+                "VERIFIED is unavailable to automation. It requires PRIMARY/S1/S2 "
+                "agreement on all 10 filings, no PRIMARY/S1/S2 match in Q4-2019, "
+                "and independent Claude classification of every S3-only snippet."
             ),
         },
         "interpretation": (
             "This is retrospective re-derivation, not preregistration. "
-            "HUMAN_REVIEW means sensitivity binaries agree and Q4-2019 has no match; "
-            "FLAGGED means term-set disagreement or a Q4-2019 match."
+            "PRIMARY/S1/S2 are deciding sets. S3 is a BROAD_DIAGNOSTIC only. "
+            "HUMAN_REVIEW means the deciding sets agree and Q4-2019 has no deciding-set "
+            "match; FLAGGED means deciding-set disagreement or a Q4-2019 deciding-set match."
         ),
     }
     OUT_PATH.write_text(

```

## F. COMPLETE infrastructure workflow YAML — draft PR #116

PR:

https://github.com/Saehon/Saeid-Homayoun/pull/116

Scope verified:

- changed-file count: exactly 1
- changed file: `.github/workflows/naail_msft_covid_scan.yml`
- draft: yes
- merged: no
- no dispatch authorized

Workflow Git blob:

`a3bef871f827674c2b24123dd25746b792ca9dc4`

```yaml
name: NAAIL Microsoft COVID v1-R Re-derivation

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  msft-covid-v1r-rederivation:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout reviewed v1-R instrument
        uses: actions/checkout@v4
        with:
          ref: 7b23810af2f4a38fdefa54b242600593c804ea91
          persist-credentials: false

      - name: Verify reviewed rule, protocol, and scanner blobs before SEC access
        shell: bash
        run: |
          set -euo pipefail

          rule_path="NAAIL/research-assurance-mcp/derived/covid_rule_v1.json"
          protocol_path="NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json"
          scanner_path="NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py"

          expected_rule="d7760b4909ae84896cae8797fb8536f59d36053c"
          expected_protocol="83af7a6859b2d44b782b5d838420f07717ea79d3"
          expected_scanner="5b0b31de72f67fd14439875db58cab7f6427f5a1"

          actual_rule="$(git hash-object "$rule_path")"
          actual_protocol="$(git hash-object "$protocol_path")"
          actual_scanner="$(git hash-object "$scanner_path")"

          echo "expected_rule_blob=$expected_rule"
          echo "actual_rule_blob=$actual_rule"
          echo "expected_protocol_blob=$expected_protocol"
          echo "actual_protocol_blob=$actual_protocol"
          echo "expected_scanner_blob=$expected_scanner"
          echo "actual_scanner_blob=$actual_scanner"

          test "$actual_rule" = "$expected_rule"
          test "$actual_protocol" = "$expected_protocol"
          test "$actual_scanner" = "$expected_scanner"

      - name: Run reviewed retrospective v1-R scanner
        shell: bash
        env:
          EDGAR_IDENTITY: ${{ secrets.EDGAR_IDENTITY }}
        run: |
          set +e
          checked_out_sha="$(git rev-parse HEAD)"
          GITHUB_SHA="$checked_out_sha" python3 NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py
          rc=$?
          echo "exit_code=$rc"
          exit "$rc"

      - name: Upload v1-R result or partial failure record
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: msft-covid-v1r-evidence
          path: NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_v1r_result.json
          if-no-files-found: warn

```

### Workflow diff from registered rejected-v1 workflow on main

```diff
--- a/.github/workflows/naail_msft_covid_scan.yml
+++ b/.github/workflows/naail_msft_covid_scan.yml
@@ -1,4 +1,4 @@
-name: NAAIL Microsoft COVID Scan
+name: NAAIL Microsoft COVID v1-R Re-derivation
 
 on:
   workflow_dispatch:
@@ -7,45 +7,60 @@
   contents: read
 
 jobs:
-  msft-covid-scan:
+  msft-covid-v1r-rederivation:
     runs-on: ubuntu-latest
     steps:
-      - name: Checkout
+      - name: Checkout reviewed v1-R instrument
         uses: actions/checkout@v4
-
-      - name: Set up Python
-        uses: actions/setup-python@v5
         with:
-          python-version: "3.12"
+          ref: 7b23810af2f4a38fdefa54b242600593c804ea91
+          persist-credentials: false
 
-      - name: Verify frozen COVID rule
+      - name: Verify reviewed rule, protocol, and scanner blobs before SEC access
         shell: bash
         run: |
-          expected="d7760b4909ae84896cae8797fb8536f59d36053c"
-          actual="$(git hash-object NAAIL/research-assurance-mcp/derived/covid_rule_v1.json)"
-          echo "expected_blob=$expected"
-          echo "actual_blob=$actual"
-          if [ "$actual" != "$expected" ]; then
-            echo "Frozen covid_rule_v1.json blob mismatch" >&2
-            exit 1
-          fi
+          set -euo pipefail
 
-      - name: Run preregistered Microsoft COVID scan
+          rule_path="NAAIL/research-assurance-mcp/derived/covid_rule_v1.json"
+          protocol_path="NAAIL/research-assurance-mcp/derived/covid_rederivation_protocol_v1r.json"
+          scanner_path="NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py"
+
+          expected_rule="d7760b4909ae84896cae8797fb8536f59d36053c"
+          expected_protocol="83af7a6859b2d44b782b5d838420f07717ea79d3"
+          expected_scanner="5b0b31de72f67fd14439875db58cab7f6427f5a1"
+
+          actual_rule="$(git hash-object "$rule_path")"
+          actual_protocol="$(git hash-object "$protocol_path")"
+          actual_scanner="$(git hash-object "$scanner_path")"
+
+          echo "expected_rule_blob=$expected_rule"
+          echo "actual_rule_blob=$actual_rule"
+          echo "expected_protocol_blob=$expected_protocol"
+          echo "actual_protocol_blob=$actual_protocol"
+          echo "expected_scanner_blob=$expected_scanner"
+          echo "actual_scanner_blob=$actual_scanner"
+
+          test "$actual_rule" = "$expected_rule"
+          test "$actual_protocol" = "$expected_protocol"
+          test "$actual_scanner" = "$expected_scanner"
+
+      - name: Run reviewed retrospective v1-R scanner
         shell: bash
         env:
           EDGAR_IDENTITY: ${{ secrets.EDGAR_IDENTITY }}
         run: |
           set +e
-          python NAAIL/research-assurance-mcp/derived/msft_covid_scan.py
+          checked_out_sha="$(git rev-parse HEAD)"
+          GITHUB_SHA="$checked_out_sha" python3 NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_scan_v1r.py
           rc=$?
           echo "exit_code=$rc"
           exit "$rc"
 
-      - name: Upload Microsoft COVID scan evidence
-        if: success()
+      - name: Upload v1-R result or partial failure record
+        if: always()
         uses: actions/upload-artifact@v4
         with:
-          name: msft-covid-scan-evidence
-          path: NAAIL/research-assurance-mcp/derived/msft_covid_scan_result.json
-          if-no-files-found: error
+          name: msft-covid-v1r-evidence
+          path: NAAIL/research-assurance-mcp/derived/msft_covid_rederivation_v1r_result.json
+          if-no-files-found: warn
 

```

### Execution-path properties

- `workflow_dispatch` only.
- `permissions: contents: read`.
- Checks out exact reviewed instrument commit `7b23810af2f4a38fdefa54b242600593c804ea91`.
- Before the scanner can make an SEC request, verifies:
  - base rule blob `d7760b4909ae84896cae8797fb8536f59d36053c`;
  - protocol blob `83af7a6859b2d44b782b5d838420f07717ea79d3`;
  - scanner blob `5b0b31de72f67fd14439875db58cab7f6427f5a1`.
- Any mismatch exits non-zero.
- Runs only `msft_covid_rederivation_scan_v1r.py`.
- Passes `EDGAR_IDENTITY` only as an environment secret.
- Overrides scanner-process `GITHUB_SHA` with the checked-out commit from `git rev-parse HEAD`, so execution provenance names the actual instrument checkout.
- Uploads `msft_covid_rederivation_v1r_result.json` with `if: always()`.
- No workflow dispatch has occurred.

Supply-chain hardening remains optional: action tags are not pinned to full commit SHAs.

## G. Static pre-execution evidence

The amended instrument head `7b23810af2f4a38fdefa54b242600593c804ea91` triggered the pre-existing static/governance CI before that guard was moved to the separate PR.

Run:

`37202416908`

Job:

`111436633228`

Conclusion:

`SUCCESS`

Observed:
- v1-R protocol JSON PASS;
- `python -m py_compile .../msft_covid_rederivation_scan_v1r.py` PASS;
- no SEC retrieval.

## H. Separate prior-exposure control PR — #117

PR:

https://github.com/Saehon/Saeid-Homayoun/pull/117

This is explicitly **non-blocking for the v1-R re-derivation**.

Changed files: exactly 4:
1. `.github/workflows/naail_rule_prior_exposure_guard.yml`
2. `NAAIL/research-assurance-mcp/derived/rule_prior_exposure_registry.json`
3. `NAAIL/research-assurance-mcp/derived/rule_prior_exposure_registry.schema.json`
4. `NAAIL/research-assurance-mcp/derived/test_rule_prior_exposure_guard.py`

It implements Claude's requested controls:

1. **Automatic source-data exposure check**  
   `git cat-file -e <freeze>:<source_csv>`; if the source already exists at freeze, `prior_exposure` must be true.

2. **Full rule/protocol coverage**  
   The guard scans every JSON file under `derived/**`; any object declaring `rule_id` or `protocol_id` must have exactly one registry entry. The workflow triggers on `derived/**`.

3. **Git-history ordering**  
   `git merge-base --is-ancestor` is used for historical ordering. Author dates are not used to infer ordering.

4. **Real JSON Schema validation**  
   The workflow installs `jsonschema` and validates the registry with Draft 2020-12.

The v1-R registry freeze commit is:

`7b23810af2f4a38fdefa54b242600593c804ea91`

Guard PR CI:

- run `37202675292`
- job `111437379574`
- conclusion `SUCCESS`
- schema validation: PASS
- registry entries checked: 2
- for both v1 and v1-R, `source_csv_exists_at_freeze = true`
- for both, earliest outcome commit is an ancestor of the freeze commit
- both correctly declare `prior_exposure = true`.

## I. Scientific behavior after the amendment

Deciding term sets:

`PRIMARY, S1, S2`

Broad diagnostic only:

`S3`

Automated decision:

- disagreement among PRIMARY/S1/S2 → `FLAGGED`;
- any PRIMARY/S1/S2 match in Q4-2019 → `FLAGGED`;
- otherwise → `HUMAN_REVIEW`.

S3 behavior:

- S3 does not participate in automated agreement;
- `S3_ONLY` means PRIMARY=0, S1=0, S2=0, S3=1;
- every S3 snippet for an S3-only filing is stored, no count cap, ≤15 words each;
- S3-only remains `HUMAN_REVIEW`;
- Claude must classify every S3-only snippet.

VERIFIED remains impossible for automation.

## J. Independent review requested

Please independently recompute and review:

`AMENDED_V1R_PROTOCOL_BLOB = 83af7a6859b2d44b782b5d838420f07717ea79d3`

`AMENDED_V1R_SCANNER_BLOB = 5b0b31de72f67fd14439875db58cab7f6427f5a1`

`V1R_WORKFLOW_BLOB = a3bef871f827674c2b24123dd25746b792ca9dc4`

Then return:

`V1R_PROTOCOL_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

`V1R_SCANNER_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

`V1R_WORKFLOW_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

For the separate non-blocking control:

`PRIOR_EXPOSURE_CONTROL_DECISION = APPROVE / CHANGES_REQUIRED / REJECT`

If the protocol, scanner and workflow are approved, explicitly state:

`AUTHORIZED_V1R_PROTOCOL_BLOB = 83af7a6859b2d44b782b5d838420f07717ea79d3`

`AUTHORIZED_V1R_SCANNER_BLOB = 5b0b31de72f67fd14439875db58cab7f6427f5a1`

`AUTHORIZED_V1R_WORKFLOW_BLOB = a3bef871f827674c2b24123dd25746b792ca9dc4`

and:

`HUMAN_MAY_MERGE_PR_116 = YES`

Do **not** authorize execution before PR #116 is explicitly merged by the human owner.

After human merge, separately state whether:

`GPT_MAY_PROCEED_WITH_V1R_REDERIVATION = YES`

No COVID scientific result is approved by this review.

Current state:

`COVID_R3_STATUS = BLOCKED_INDEPENDENT_REVIEW`

`POC_COMPLETE = FALSE`

`NOT_READY_FOR_HUMAN_POC_APPROVAL`
