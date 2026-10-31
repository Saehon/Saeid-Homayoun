"""Minimal, deterministic finance reasoning evaluation — synthetic cases only."""
from decimal import Decimal, InvalidOperation
import json

def score_case(case):
    failures = []
    required = ("case_id", "gold_value", "model_value", "tolerance", "allowed_evidence_ids", "cited_evidence_ids")
    for key in required:
        if key not in case:
            failures.append("missing_" + key)
    if failures:
        return {"case_id": case.get("case_id", "unknown"), "pass": False, "failure_modes": failures}
    try:
        expected = Decimal(str(case["gold_value"]))
        observed = Decimal(str(case["model_value"]))
        tolerance = Decimal(str(case["tolerance"]))
        numeric_ok = all(x.is_finite() for x in (expected, observed, tolerance)) and tolerance >= 0 and abs(expected - observed) <= tolerance
    except (InvalidOperation, TypeError, ValueError):
        numeric_ok = False
    allowed = set(case["allowed_evidence_ids"])
    cited = set(case["cited_evidence_ids"])
    evidence_ok = bool(cited) and cited.issubset(allowed) and bool(allowed)
    if not numeric_ok:
        failures.append("calculation_or_tolerance_error")
    if not evidence_ok:
        failures.append("unsupported_or_missing_evidence")
    return {"case_id": case["case_id"], "pass": not failures, "numeric_match": numeric_ok,
            "evidence_match": evidence_ok, "failure_modes": failures}

if __name__ == "__main__":
    synthetic_cases = [
        {"case_id": "margin_001", "gold_value": "0.20", "model_value": "0.20",
         "tolerance": "0.001", "allowed_evidence_ids": ["SYNTH-PL-01"],
         "cited_evidence_ids": ["SYNTH-PL-01"]},
        {"case_id": "margin_002", "gold_value": "0.20", "model_value": "0.25",
         "tolerance": "0.001", "allowed_evidence_ids": ["SYNTH-PL-02"],
         "cited_evidence_ids": ["UNVERIFIED-SOURCE"]}
    ]
    print(json.dumps([score_case(case) for case in synthetic_cases], indent=2))
