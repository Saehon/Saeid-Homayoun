import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = ROOT / "v1-preparation" / "b5" / "human_ground_truth_protocol_v1.json"
TEMPLATE_PATH = ROOT / "v1-preparation" / "b5" / "human_ground_truth_preregistration_template_v1.json"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def walk(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def test_protocol_governance_and_blinding_invariants():
    protocol = load_json(PROTOCOL_PATH)
    assert protocol["status"] == "DRAFT"
    assert protocol["governance"]["poc_complete"] is False
    assert protocol["governance"]["v1_complete"] is False
    assert protocol["prior_exposure"]["operator_has_seen_detector"] is True
    assert "holdout probe author" in protocol["prior_exposure"]["operator_exclusions"]
    assert protocol["roles"]["minimum_independent_coders_per_item"] == 2
    assert protocol["blinding"]["independent_submission"] is True
    assert protocol["blinding"]["communication_between_coders_before_lock"] is False
    assert protocol["adjudication"]["raw_labels_immutable"] is True
    assert protocol["missingness_and_deviations"]["no_silent_exclusion"] is True


def test_reliability_rule_is_frozen_and_not_overstated():
    protocol = load_json(PROTOCOL_PATH)
    reliability = protocol["reliability"]
    assert reliability["primary_statistic"] == "Cohen's kappa"
    assert reliability["weighting"] == "unweighted"
    assert reliability["minimum_kappa_threshold"] == 0.70
    assert reliability["threshold_operator"] == ">="
    assert reliability["computed_before_adjudication"] is True
    assert reliability["no_metric_substitution"] is True
    assert "do not treat the threshold as met" in reliability["undefined_kappa_rule"]
    assert "HUMAN_REVIEW" in reliability["below_threshold_rule"]


def test_template_matches_protocol_and_contains_no_results():
    protocol = load_json(PROTOCOL_PATH)
    template = load_json(TEMPLATE_PATH)
    assert template["status"] == "DRAFT_TEMPLATE"
    assert template["protocol_id"] == protocol["protocol_id"]
    assert template["reliability"]["minimum_threshold"] == protocol["reliability"]["minimum_kappa_threshold"]
    assert template["adjudication"]["raw_label_overwrite_permitted"] is False
    assert template["results"] == "MUST_REMAIN_EMPTY_UNTIL_AFTER_FREEZE_AND_EXECUTION"


def test_operator_authored_no_probe_content():
    protocol = load_json(PROTOCOL_PATH)
    template = load_json(TEMPLATE_PATH)
    keys = set(walk(protocol)) | set(walk(template))
    forbidden = {"probe", "probes", "probe_text", "probe_content", "expected_label", "injected_error"}
    assert keys.isdisjoint(forbidden)


if __name__ == "__main__":
    test_protocol_governance_and_blinding_invariants()
    test_reliability_rule_is_frozen_and_not_overstated()
    test_template_matches_protocol_and_contains_no_results()
    test_operator_authored_no_probe_content()
    print("B5 human ground-truth protocol invariants: PASS")
