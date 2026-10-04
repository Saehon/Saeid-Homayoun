import copy
import hashlib
import json
from pathlib import Path

from classifier import evaluate_noncompliance


registry = json.loads(Path("trusted-extraction-records-v0.1.json").read_text(encoding="utf-8"))
record = registry["records"][0]
valid = {key: record[key] for key in (
    "issuer_cik", "accession", "form_type", "period_end", "source_section",
    "speaker", "disclosure_excerpt", "excerpt_sha256", "explicit_framework_version",
    "assertion_polarity", "third_party_quote",
)}
valid["extraction_record_id"] = record["record_id"]

assert evaluate_noncompliance(valid) == {"classification": 0, "reason": None}

arbitrary = copy.deepcopy(valid)
arbitrary["disclosure_excerpt"] = "Management assessed ICFR using Internal Control – Integrated Framework (1992)."
arbitrary["excerpt_sha256"] = hashlib.sha256(arbitrary["disclosure_excerpt"].encode()).hexdigest()
arbitrary["explicit_framework_version"] = "1992"
assert evaluate_noncompliance(arbitrary)["reason"] == "EVIDENCE_RECORD_MISMATCH"

relabeled = copy.deepcopy(valid)
relabeled["assertion_polarity"] = "NEGATED"
assert evaluate_noncompliance(relabeled)["reason"] == "EVIDENCE_RECORD_MISMATCH"

unknown = copy.deepcopy(valid)
unknown["extraction_record_id"] = "UNKNOWN"
assert evaluate_noncompliance(unknown)["reason"] == "UNTRUSTED_EXTRACTION_RECORD"

first = [evaluate_noncompliance(x) for x in (valid, arbitrary, relabeled, unknown)]
second = [evaluate_noncompliance(x) for x in (valid, arbitrary, relabeled, unknown)]
assert first == second
