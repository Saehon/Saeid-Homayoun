import json
from pathlib import Path


SPEC_PATH = Path(__file__).with_name("benchmark_v3_holdout_spec_v1.json")


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

    assert spec["specification_id"] == "NAAIL-V1-B4-HOLDOUT-V3-SPEC-V1"
    assert spec["prior_exposure"]["operator_has_seen_detector_code"] is True
    assert spec["phase_boundary"]["probe_authoring_authorized_for_operator"] is False
    assert spec["phase_boundary"]["data_retrieval_authorized"] is False
    assert spec["phase_boundary"]["scoring_authorized"] is False

    composition = spec["holdout_composition"]
    categories = composition["error_categories"]
    assert len(categories) == 8
    assert len({item["id"] for item in categories}) == len(categories)
    assert sum(item["packages"] for item in categories) == composition["error_bearing_packages"]
    assert (
        composition["error_bearing_packages"] + composition["clean_control_packages"]
        == composition["total_packages"]
        == 48
    )

    thresholds = spec["scoring"]["thresholds"]
    assert 0.0 <= thresholds["precision_minimum"] <= 1.0
    assert 0.0 <= thresholds["recall_minimum"] <= 1.0
    assert 0.0 <= thresholds["f1_minimum"] <= 1.0
    assert 0.0 <= thresholds["false_positive_rate_maximum"] <= 1.0

    assert spec["single_run_rule"]["authoritative_scoring_runs"] == 1
    assert len(spec["independence_requirements"]["required_attestation"]) == 4
    assert "raw_detector_output.json" in spec["required_outputs"]
    assert "score_record.json" in spec["required_outputs"]


if __name__ == "__main__":
    main()
