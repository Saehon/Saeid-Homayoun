# Claude Q5 Scanner Re-Review Evidence Package — 2026-10-04

Author: GPT repair operator
Repository: `Saehon/Saeid-Homayoun`
PR: #103
Branch: `naail/research-assurance-pr-b-q5-covid`
Current PR head while package prepared: `6d427db5c1f13448d2d937beff41980117b42d97`

## Executive finding

A newly reconstructed provenance fact is decisive under Claude's stated decision rule:

**Microsoft SEC filing-text COVID outcomes for the same 10 observations were already recorded on 2026-10-01, before `covid_rule_v1.json` and the v1 scanner were frozen on 2026-10-02.**

Accordingly, GPT does not recommend treating a future v1 run as a clean preregistered/blind confirmation. R3 remains undispatched.

---

# 1. COMPLETE OLD SCANNER

Path:
`NAAIL/research-assurance-mcp/derived/msft_covid_scan.py`

Repository snapshot:
`702c117f62d9f2653cd4f44110679bbefa41c788`

Git blob:
`1b65c3cc60b0305aed244a642923ea50c95b0045`

```python
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
from datetime import date
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
    state = "VERIFIED" if all_match else "FLAGGED"
    if state not in CANONICAL_STATES:
        raise RuntimeError("Non-canonical assurance state generated")

    result = {
        "rule_id": rule["rule_id"],
        "rule_status": rule["status"],
        "rule_path": str(RULE_PATH.relative_to(ROOT)),
        "source_csv": str(CSV_PATH.relative_to(ROOT)),
        "scope": "Microsoft public-SEC primary 10-Q/10-K documents only; exhibits excluded.",
        "regex": rule["pattern"],
        "case_insensitive": True,
        "filinglag_regenerated_rows": len(observations),
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
            "Execution success records the preregistered test. A FLAGGED scientific result is not an execution failure."
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

```

---

# 2. COMPLETE NEW SCANNER

Path:
`NAAIL/research-assurance-mcp/derived/msft_covid_scan.py`

Change commit:
`054dbecd0a7d511fabc054f7135b9d616d072a9f`

Git blob:
`4602d71d9a1db84405a17470fea03638a8595758`

```python
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

```

---

# 3. UNIFIED DIFF OLD → NEW

Scanner-changing commit:
`054dbecd0a7d511fabc054f7135b9d616d072a9f`

Author:
`Saeid Homayoun <113834542+Saehon@users.noreply.github.com>`

Timestamp:
`2026-10-04T11:32:16Z`

Message:
`Q5: require human review and record scan provenance`

```diff
@@ -21,7 +21,7 @@
 import re
 import sys
 import time
-from datetime import date
+from datetime import date, datetime, timezone
 from html.parser import HTMLParser
 from pathlib import Path
 from typing import Any
@@ -137,6 +137,7 @@ def snippets(text: str, matches: list[re.Match[str]], limit: int = 3, max_words:
 
 
 def main() -> int:
+    retrieval_started_at = datetime.now(timezone.utc).isoformat()
     identity = os.getenv("EDGAR_IDENTITY", "").strip()
     if not identity:
         raise RuntimeError("EDGAR_IDENTITY is required and must be supplied by the CI secret.")
@@ -218,10 +219,26 @@ def main() -> int:
 
     all_match = all(o["matches_expectation"] for o in observations)
     q4 = next(o for o in observations if o["calendar_quarter"] == "Q4-2019")
-    state = "VERIFIED" if all_match else "FLAGGED"
+    state = "HUMAN_REVIEW" if all_match else "FLAGGED"
     if state not in CANONICAL_STATES:
         raise RuntimeError("Non-canonical assurance state generated")
 
+    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
+    server_url = os.getenv("GITHUB_SERVER_URL", "").strip()
+    repository = os.getenv("GITHUB_REPOSITORY", "").strip()
+    run_url = f"{server_url}/{repository}/actions/runs/{run_id}" if server_url and repository and run_id else None
+    provenance = {
+        "retrieval_started_at_utc": retrieval_started_at,
+        "retrieval_completed_at_utc": datetime.now(timezone.utc).isoformat(),
+        "source_system": "SEC EDGAR",
+        "executing_commit": os.getenv("GITHUB_SHA", "").strip() or None,
+        "workflow_name": os.getenv("GITHUB_WORKFLOW", "").strip() or None,
+        "workflow_run_id": run_id or None,
+        "workflow_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "").strip() or None,
+        "repository": repository or None,
+        "run_url": run_url,
+    }
+
     result = {
         "rule_id": rule["rule_id"],
         "rule_status": rule["status"],
@@ -231,6 +248,7 @@ def main() -> int:
         "regex": rule["pattern"],
         "case_insensitive": True,
         "filinglag_regenerated_rows": len(observations),
+        "provenance": provenance,
         "observations": observations,
         "summary": {
             "filings_scanned": len(observations),
@@ -243,7 +261,7 @@ def main() -> int:
             "covid_claim_assurance_state": state,
         },
         "interpretation": (
-            "Execution success records the preregistered test. A FLAGGED scientific result is not an execution failure."
+            "Execution success records the preregistered test. Matching expectations remain HUMAN_REVIEW until approval is separately recorded; a FLAGGED scientific result is not an execution failure."
         ),
     }
     OUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
```

## Later PR #103 commits

The scanner did **not** change after commit `054dbecd0a7d511fabc054f7135b9d616d072a9f`.

- `d0ffd601101da80e820b0437b802de736bdfe2d7` — 2026-10-04T11:36:00Z — records the hourly review-repair log.
- `18f548df86fdab1260d1d56411379174e79b7017` — 2026-10-04T11:37:01Z — updates only dual-save readback status.
- Later GPT evidence-package/protocol-stop commits are additive records only; the scanner blob remains `4602d71d9a1db84405a17470fea03638a8595758`.

---

# 4. REASON FOR EACH SCANNER CHANGE

The scanner-changing commit responded to two review findings before any compliant Q5 execution:

1. **Automatic assurance-state repair**
   - Old behavior: all 10 expectations matching produced `VERIFIED`.
   - New behavior: all 10 expectations matching produces `HUMAN_REVIEW`.
   - Mismatches remain `FLAGGED`.
   - Rationale: automated execution must not self-approve the scientific claim.

2. **Execution/retrieval provenance**
   - Adds UTC retrieval start and completion.
   - Adds source-system label `SEC EDGAR`.
   - Adds executing commit, workflow name, run ID, run attempt, repository and run URL.
   - Rationale: allow the result to be traced to an exact execution context.

3. **No scientific matching-rule change in this delta**
   - Regex unchanged.
   - Ten frozen accessions unchanged.
   - Form set unchanged.
   - Primary-document-only scope unchanged.
   - Exhibit exclusion unchanged.
   - Case-insensitive matching unchanged.
   - Match count logic unchanged.
   - Binary threshold remains `1 iff count > 0`.
   - FilingLag regeneration/integrity checks unchanged.
   - Snippet limits unchanged.

---

# 5. FACTUAL DATA-EXPOSURE STATEMENT

This section is a factual declaration based on live GitHub repository history, GitHub Actions logs, and the canonical Drive master log available to GPT. It is not phrased as an oath and does not claim knowledge of unrecorded activity.

## Finding: YES — the same-observation SEC filing-text outcomes had already been observed before v1 was frozen.

### Repository evidence dated 2026-10-01

The following artifacts were created on 2026-10-01:

- `msft_one_company_final.csv`
  - commit `6dd3f0f30e851a13713d3c4ed6e48e3ee413611e`
  - 2026-10-01T09:12:54Z

- `msft_one_company_final.json`
  - commit `bc783cef59b35e58b278544c14704cb248648d50`
  - 2026-10-01T09:12:57Z

- `FINAL_REPORT.md`
  - commit `53b25b530e0dccb1c2677eae1ba3e8b5a5cec7b8`
  - 2026-10-01T09:12:59Z

The final report says the public-data source included **Official SEC EDGAR filing metadata and filing text** and reports COVID-present values for all 10 observations.

The report states that the 2019 matched filings had no COVID reference in the SEC text checks and that each matched filing from Q1-2020 through Q2-2021 contained COVID/coronavirus discussion.

The final JSON independently records:
`binary presence of covid/corona in SEC filing text; 2019 matched filings=0, 2020-Q2 2021 matched filings=1`.

Therefore the available record supports the conclusion that the same 10-observation COVID outcomes had been inspected before the later v1 protocol freeze.

### Timing of the v1 freeze

The v1 rule/scanner pair was added later:

- commit: `2b278315a1ca38f67bab6e97b265e57ce28c3a5e`
- timestamp: `2026-10-02T12:13:34Z`
- original scanner blob: `1b65c3cc60b0305aed244a642923ea50c95b0045`
- rule blob: `d7760b4909ae84896cae8797fb8536f59d36053c`

Thus the text-result exposure predates the v1 freeze.

### Limits of the recovered provenance

The exact local/manual command, machine, process ID, or run ID that produced the October 1 COVID binary fields is not present in the recovered project records. GPT therefore cannot truthfully list an execution ID or exit code for that historical process.

The historical output artifacts themselves, however, are direct evidence that SEC filing text had already been used to establish the COVID-presence outcomes.

---

# 6. WORKFLOW / RUN INVENTORY RELEVANT TO Q5 SEC RETRIEVAL

## Run 37003148170 / job 110825211903

- Date: 2026-10-02
- Workflow: `NAAIL Research Assurance P7`
- Head: `a1e0ea7b449d90a0d4821e45a6c63d1182cdbe3a`
- The scanner command was invoked.
- Log shows `EDGAR_IDENTITY:` empty.
- Scanner raised:
  `RuntimeError: EDGAR_IDENTITY is required and must be supplied by the CI secret.`
- Exit code: 1.
- In the scanner code, this error occurs before rule loading and before `submission_index()`, which is the first SEC network call.
- **Conclusion: this Actions run did not retrieve SEC metadata or SEC filing text.**

## Run 37003872890 / job 110827499066

- Four deterministic engineering CI steps.
- Log does not invoke `msft_covid_scan.py`.
- **No Q5 SEC-text execution.**

## Run 37004149967 / job 110828395512

- Four deterministic engineering CI steps.
- Log does not invoke `msft_covid_scan.py`.
- **No Q5 SEC-text execution.**

## PR #103 review runs

- `37005586281`: Codex Deep Review failure; logs show no scanner/EDGAR/SEC invocation.
- `37199079225`: Codex Deep Review skipped.
- `37199297404`: Codex Deep Review skipped.
- `37199350740`: Codex Deep Review skipped.
- `37200092162`: Codex Deep Review skipped.

## Dedicated workflow-dispatch inventory

Repository Actions inventory for `event=workflow_dispatch` contains no run named `NAAIL Microsoft COVID Scan` after the workflow was registered.

GPT did not manually dispatch R3 after #104 was merged because the scanner fingerprint failed the independent-review gate.

---

# 7. COMPLETE FROZEN RULE

Path:
`NAAIL/research-assurance-mcp/derived/covid_rule_v1.json`

Git blob:
`d7760b4909ae84896cae8797fb8536f59d36053c`

```json
{
  "schema_version": "1.0.0",
  "rule_id": "NAAIL-MSFT-COVID-RULE-V1",
  "status": "FROZEN_PREREGISTERED",
  "frozen_date": "2026-10-02",
  "case_id": "MNSC-2023-4670",
  "company": "Microsoft Corporation",
  "cik": "0000789019",
  "source_csv": "case-001-management-science/reexecution/sec_one_company_msft/msft_one_company_final.csv",
  "identity_secret": "EDGAR_IDENTITY",
  "text_scope": {
    "forms": ["10-Q", "10-K"],
    "document_scope": "primary filing document only",
    "exclude_exhibits": true,
    "case_sensitive": false
  },
  "pattern": "\\bcovid(-19)?\\b|\\bcoronavirus\\b|\\bcorona\\b",
  "match_rule": {
    "covid_present": "1 iff match_count > 0; otherwise 0",
    "count": "count all non-overlapping regex matches in primary filing text",
    "snippets": "store up to 3 snippets per filing; each snippet must be no more than 15 words"
  },
  "filing_lag_rule": {
    "definition": "SEC filing date minus fiscal period end, in calendar days",
    "baseline": "same calendar quarter of 2019",
    "regenerate_all_10_rows": true
  },
  "frozen_expectations": [
    {"calendar_quarter":"Q1-2019","form":"10-Q","accession":"0001564590-19-012709","expected_covid_present":0},
    {"calendar_quarter":"Q2-2019","form":"10-K","accession":"0001564590-19-027952","expected_covid_present":0},
    {"calendar_quarter":"Q3-2019","form":"10-Q","accession":"0001564590-19-037549","expected_covid_present":0},
    {"calendar_quarter":"Q4-2019","form":"10-Q","accession":"0001564590-20-002450","expected_covid_present":0,"decisive":true},
    {"calendar_quarter":"Q1-2020","form":"10-Q","accession":"0001564590-20-019706","expected_covid_present":1},
    {"calendar_quarter":"Q2-2020","form":"10-K","accession":"0001564590-20-034944","expected_covid_present":1},
    {"calendar_quarter":"Q3-2020","form":"10-Q","accession":"0001564590-20-047996","expected_covid_present":1},
    {"calendar_quarter":"Q4-2020","form":"10-Q","accession":"0001564590-21-002316","expected_covid_present":1},
    {"calendar_quarter":"Q1-2021","form":"10-Q","accession":"0001564590-21-020891","expected_covid_present":1},
    {"calendar_quarter":"Q2-2021","form":"10-K","accession":"0001564590-21-039151","expected_covid_present":1}
  ],
  "required_output_per_filing": [
    "calendar_quarter",
    "form",
    "accession",
    "period_end",
    "filing_date",
    "filing_lag_days",
    "document_sha256",
    "match_count",
    "covid_present",
    "expected_covid_present",
    "matches_expectation",
    "snippets"
  ],
  "decision_rule": {
    "all_10_match": "COVID claim may be upgraded to VERIFIED within this bounded Microsoft public-SEC scope.",
    "any_mismatch": "Record the COVID claim as FLAGGED and preserve mismatch evidence.",
    "q4_2019_special": "Any regex match in Q4-2019 makes the frozen expected value 0 false and must be recorded FLAGGED."
  },
  "immutability": "After the first result is observed, this v1 rule must not be altered. Any methodological change requires covid_rule_v2.json with an explicit reason and must not overwrite v1."
}

```

---

# 8. HISTORICAL OCTOBER 1 EVIDENCE — COMPLETE TEXT

## FINAL_REPORT.md

Git blob:
`b2d92b59a65555a3dd3cfdd20eb9074b9944605a`

```markdown
# Microsoft-only Case 001 — FINAL

## Decision
The one-company proof is **finished**. No additional company is required for this case.

## Company
Microsoft Corporation (MSFT), CIK 0000789019.

## Public-data source
Official SEC EDGAR filing metadata and filing text.

## Reconstructed observations
| Quarter | Form | Period end | Filing date | FilingLag | Change vs same 2019 quarter | LateFiler | COVID present |
|---|---|---|---|---:|---:|---:|---:|
| Q1-2019 | 10-Q | 2019-03-31 | 2019-04-24 | 24 | 0 | 0 | 0 |
| Q2-2019 | 10-K | 2019-06-30 | 2019-08-01 | 32 | 0 | 0 | 0 |
| Q3-2019 | 10-Q | 2019-09-30 | 2019-10-23 | 23 | 0 | 0 | 0 |
| Q4-2019 | 10-Q | 2019-12-31 | 2020-01-29 | 29 | 0 | 0 | 0 |
| Q1-2020 | 10-Q | 2020-03-31 | 2020-04-29 | 29 | **+5** | 0 | 1 |
| Q2-2020 | 10-K | 2020-06-30 | 2020-07-30 | 30 | **-2** | 0 | 1 |
| Q3-2020 | 10-Q | 2020-09-30 | 2020-10-27 | 27 | **+4** | 0 | 1 |
| Q4-2020 | 10-Q | 2020-12-31 | 2021-01-26 | 26 | **-3** | 0 | 1 |
| Q1-2021 | 10-Q | 2021-03-31 | 2021-04-27 | 27 | **+3** | 0 | 1 |
| Q2-2021 | 10-K | 2021-06-30 | 2021-07-29 | 29 | **-3** | 0 | 1 |

## Core result
For Microsoft alone, the within-company change in filing lag relative to the same 2019 quarter is:

**+5, -2, +4, -3, +3, -3 days**

for Q1-2020 through Q2-2021.

Microsoft was not a late filer in any of the ten observations.

The 2019 matched filings contain no COVID reference in the SEC text checks used here. Each matched filing from Q1-2020 through Q2-2021 contains COVID/coronavirus discussion.

## Assurance conclusion
**SEC_ONE_COMPANY_RECONSTRUCTION_COMPLETE**

Verified:
- period end
- SEC filing date
- FilingLag
- same-quarter 2019 comparison
- LateFiler for this issuer
- binary COVID presence

Not claimed:
- full-sample regression reproduction
- population inference
- Audit Analytics/IBES variables
- exact paper-level narrative-count/FOG metrics
- methodological generalization

## Scientific meaning
This is a completed **proof of independent construct reconstruction** using public SEC data. It shows that the central timeliness variable can be rebuilt outside the authors' WRDS pipeline for one issuer and compared across the same calendar-quarter structure used by the paper.

It should be described as a **one-company replication case**, not as a replication of the full Management Science study.

```

## msft_one_company_final.json

Git blob:
`51490106930c255b44773f58a98eb614b960bcd8`

```json
{
  "case_id": "MNSC-2023-4670",
  "proof_id": "SEC-ONE-COMPANY-MSFT-FINAL",
  "company": {
    "name": "Microsoft Corporation",
    "ticker": "MSFT",
    "cik": "0000789019"
  },
  "scope": "One-company public-SEC reconstruction of core timeliness constructs",
  "status": "COMPLETE_WITHIN_ONE_COMPANY_SCOPE",
  "constructs": {
    "filing_lag": "filing date minus period end",
    "late_filer": "0 for all 10 observations; every filing lag is below even the shortest standard Exchange Act deadline applicable to 10-Q/10-K filers",
    "post": "1 for 2020 onward",
    "covid_presence": "binary presence of covid/corona in SEC filing text; 2019 matched filings=0, 2020-Q2 2021 matched filings=1"
  },
  "matched_changes_days": {
    "Q1-2020_vs_Q1-2019": 5,
    "Q2-2020_vs_Q2-2019": -2,
    "Q3-2020_vs_Q3-2019": 4,
    "Q4-2020_vs_Q4-2019": -3,
    "Q1-2021_vs_Q1-2019": 3,
    "Q2-2021_vs_Q2-2019": -3
  },
  "summary": {
    "n_filings": 10,
    "n_late_filings": 0,
    "mean_2019_filing_lag_days": 27,
    "post_period_changes_days": [
      5,
      -2,
      4,
      -3,
      3,
      -3
    ],
    "covid_presence_2019": 0,
    "covid_presence_post": 1
  },
  "assurance_state": {
    "sec_filing_dates_and_periods": "VERIFIED",
    "filing_lag_calculation": "VERIFIED",
    "same_quarter_change_calculation": "VERIFIED",
    "late_filer_one_company": "VERIFIED",
    "covid_presence_binary": "VERIFIED",
    "full_paper_replication": "OUT_OF_SCOPE_FOR_ONE_COMPANY_CASE",
    "methodological_generalization": "NOT_CLAIMED"
  },
  "limitations": [
    "One company cannot reproduce the paper's cross-sectional regressions or population-level inference.",
    "Audit Analytics, IBES, and proprietary variables are not reconstructed.",
    "COVID presence is binary here; exact section-level counts/FOG/risk-header counts are not claimed as independently reproduced."
  ]
}
```

---

# 9. PRE-EXECUTION PROTOCOL AMENDMENT

An additive correction record has been created on PR #103:

`NAAIL/research-assurance-mcp/derived/Q5_PREEXECUTION_PROTOCOL_AMENDMENT_2026-10-04.md`

It records:
- the prior SEC-text exposure;
- the v1 freeze chronology;
- the scanner amendment chronology;
- the Actions execution history;
- the absence of a recoverable local execution ID for the October 1 text inspection;
- the operator recommendation not to execute v1 as a purported blind/preregistered confirmation.

Neither `covid_rule_v1.json` nor either scanner version was changed by this correction entry.

---

# 10. IMPORTANT IMPLEMENTATION OBSERVATION

The current scanner writes:
- rule ID/status/path;
- execution provenance;
- per-document SHA-256;
- counts/flags/snippets.

It does **not** currently write the scanner Git blob and rule Git blob as explicit fields in `msft_covid_scan_result.json`.

That is a separate output-contract weakness. It should be fixed in a future version before execution if the independent reviewer requires self-contained fingerprint evidence.

Because same-observation COVID outcomes were already observed before v1 was frozen, GPT does not recommend repairing v1 and then calling it a clean preregistered test.

---

# 11. OPERATOR DISPOSITION FOR CLAUDE

Based on Claude's own stated rule:

> REJECT if either version had already retrieved or looked at Microsoft filing text before the change.

The repository evidence meets that condition through the October 1 final artifacts.

GPT therefore recommends:

`SCANNER_DECISION = REJECT`

for **v1 as a clean preregistered confirmation**.

Recommended protocol next step:

1. Preserve `covid_rule_v1.json`, original scanner blob `1b65c3cc60b0305aed244a642923ea50c95b0045`, and amended scanner blob `4602d71d9a1db84405a17470fea03638a8595758` as historical records.
2. Do not dispatch R3 under a claim of blind/preregistered v1 confirmation.
3. Define a new versioned protocol (e.g. v2) with a genuinely unobserved holdout / confirmatory target, or explicitly downgrade the existing Microsoft COVID exercise to retrospective validation rather than preregistration.
4. Have the new protocol independently reviewed before any data retrieval.
5. Keep POC COVID criterion PARTIAL/FLAGGED/HUMAN_REVIEW as appropriate until the governance decision is made.

Current operator state:

`COVID_R3_STATUS = BLOCKED_PROTOCOL_VALIDITY`

`POC_COMPLETE = FALSE`
