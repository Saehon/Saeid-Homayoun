from __future__ import annotations

import json
from pathlib import Path

from icfr_engine import ControlInput, review_control


def _safe_rate(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def run_benchmark(path: str | Path | None = None) -> dict:
    cases_path = Path(path) if path else Path(__file__).with_name("benchmark_cases.json")
    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    passed = 0
    results = []
    tp = fp = tn = fn = 0
    lineage_complete = 0

    for case in cases:
        result = review_control(
            ControlInput(
                control_id=case["control_id"],
                objective=case["objective"],
                required_evidence=case["required_evidence"],
                evidence_text=case["evidence_text"],
                period=case.get("period", ""),
            )
        )
        actual_status = result["primary_review"]["status"]
        actual_missing = sorted(result["primary_review"]["missing_requirements"])
        actual_flags = sorted(result["primary_review"].get("deterministic_flags", []))
        expected_missing = sorted(case["expected_missing"])
        expected_flags = sorted(case.get("expected_flags", []))

        actual_exception = actual_status != "READY_FOR_HUMAN_REVIEW"
        expected_exception = bool(case["expected_exception"])

        if expected_exception and actual_exception:
            tp += 1
        elif (not expected_exception) and actual_exception:
            fp += 1
        elif expected_exception and (not actual_exception):
            fn += 1
        else:
            tn += 1

        passport = result["evidence_passport"]
        has_lineage = bool(
            passport.get("control_id")
            and passport.get("evidence_sha256")
            and passport.get("human_gate", {}).get("required") is True
            and result.get("final_professional_conclusion") is None
        )
        lineage_complete += int(has_lineage)

        ok = (
            actual_status == case["expected_status"]
            and actual_missing == expected_missing
            and actual_flags == expected_flags
            and actual_exception == expected_exception
            and has_lineage
        )
        passed += int(ok)
        results.append(
            {
                "id": case["id"],
                "category": case.get("category", "unspecified"),
                "pass": ok,
                "actual_status": actual_status,
                "expected_status": case["expected_status"],
                "actual_missing": actual_missing,
                "expected_missing": expected_missing,
                "actual_flags": actual_flags,
                "expected_flags": expected_flags,
                "actual_exception": actual_exception,
                "expected_exception": expected_exception,
                "lineage_complete": has_lineage,
            }
        )

    precision = _safe_rate(tp, tp + fp)
    recall = _safe_rate(tp, tp + fn)

    return {
        "benchmark": "Customer Zero V2",
        "scope": "synthetic deterministic ICFR evidence-review regression benchmark",
        "cases": len(cases),
        "passed": passed,
        "pass_rate": _safe_rate(passed, len(cases)),
        "confusion_matrix": {"tp": tp, "fp": fp, "tn": tn, "fn": fn},
        "precision": precision,
        "recall": recall,
        "false_positives": fp,
        "false_negatives": fn,
        "evidence_lineage_completeness": _safe_rate(lineage_complete, len(cases)),
        "results": results,
        "limitations": [
            "Metrics describe only this synthetic deterministic benchmark.",
            "They are not estimates of production performance on customer evidence.",
            "GPT, Claude and IBM Granite are not scored by this script unless separate live-model evaluation is explicitly run.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_benchmark(), indent=2))
