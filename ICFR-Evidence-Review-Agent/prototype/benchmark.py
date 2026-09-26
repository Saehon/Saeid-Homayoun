from __future__ import annotations

import json
from pathlib import Path

from icfr_engine import ControlInput, review_control

def run_benchmark(path: str | Path | None = None) -> dict:
    cases_path = Path(path) if path else Path(__file__).with_name("benchmark_cases.json")
    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    passed = 0
    results = []
    for case in cases:
        result = review_control(
            ControlInput(
                control_id=case["control_id"],
                objective=case["objective"],
                required_evidence=case["required_evidence"],
                evidence_text=case["evidence_text"],
            )
        )
        actual_status = result["primary_review"]["status"]
        actual_missing = sorted(result["primary_review"]["missing_requirements"])
        expected_missing = sorted(case["expected_missing"])
        ok = actual_status == case["expected_status"] and actual_missing == expected_missing
        passed += int(ok)
        results.append({
            "id": case["id"],
            "pass": ok,
            "actual_status": actual_status,
            "expected_status": case["expected_status"],
            "actual_missing": actual_missing,
            "expected_missing": expected_missing,
        })

    return {
        "cases": len(cases),
        "passed": passed,
        "pass_rate": 0.0 if not cases else passed / len(cases),
        "results": results,
    }

if __name__ == "__main__":
    print(json.dumps(run_benchmark(), indent=2))
