from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROTOCOL = ROOT / "pilot_comparison_protocol_v1.json"
METRICS = ROOT / "pilot_comparison_metrics_v1.json"
MANIFEST = ROOT / "pilot_comparison_protocol_freeze_manifest_v1.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_b6_protocol_invariants() -> None:
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    metrics = json.loads(METRICS.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert protocol["status"] == "FROZEN_BEFORE_DATA"
    assert protocol["approval_state"] == "DRAFT_PENDING_CLAUDE_AND_HUMAN"
    exposure = protocol["prior_exposure"]
    assert exposure["operator_has_seen_detector_code"] is True
    assert exposure["operator_has_seen_benchmark_v2_probes_and_results"] is True
    assert exposure["operator_has_seen_benchmark_v3_probes"] is False
    assert exposure["operator_has_seen_benchmark_v3_ground_truth"] is False
    assert exposure["operator_has_seen_real_case_evaluation_labels"] is False
    assert exposure["evaluation_data_or_results_existed_at_freeze"] is False

    arms = {item["arm_id"] for item in protocol["comparison_arms"]}
    assert arms == {"SYSTEM_NAAIL", "HUMAN_CODERS", "BASELINE_ALWAYS_NO_ERROR"}
    strata = {item["stratum_id"] for item in protocol["evaluation_strata"]}
    assert strata == {"SEALED_HOLDOUT_V3", "REAL_CASES_001_003"}
    one_run = protocol["one_authoritative_run"]
    assert one_run["maximum_scoring_invocations"] == 1
    assert one_run["selection_across_runs_prohibited"] is True
    assert one_run["rerun_after_success_prohibited"] is True
    assert one_run["rerun_after_failure_prohibited"] is True
    assert protocol["poc_complete"] is False
    assert protocol["v1_complete"] is False

    primary = {item["name"] for item in metrics["primary_metrics"]}
    assert primary == {"precision", "recall", "f1"}
    assert metrics["required_counts"] == ["TP", "FP", "FN", "TN", "N"]
    assert metrics["uncertainty"]["replicates"] == 10000
    assert metrics["uncertainty"]["seed"] == 20261005
    assert metrics["paired_comparisons"]["reference_arm"] == "BASELINE_ALWAYS_NO_ERROR"

    frozen = {item["path"]: item["sha256"] for item in manifest["frozen_files"]}
    assert frozen[PROTOCOL.name] == sha256(PROTOCOL)
    assert frozen[METRICS.name] == sha256(METRICS)
    assert manifest["evaluation_data_or_results_existed_at_freeze"] is False


if __name__ == "__main__":
    test_b6_protocol_invariants()
    print("B6 pilot comparison protocol invariants: PASS")
