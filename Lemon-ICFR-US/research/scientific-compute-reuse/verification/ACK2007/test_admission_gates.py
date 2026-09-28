import importlib.util
import json
from pathlib import Path
import sys

import pytest

HERE = Path(__file__).resolve().parent
MODEL_DIR = HERE.parent.parent / "executable-models" / "ACK2007"
REGISTRY_PATH = (
    HERE.parent.parent
    / "source-definition-recovery"
    / "ACK2007-construction-gates.json"
)

sys.path.insert(0, str(MODEL_DIR))
from ack2007 import REQUIRED

SPEC = importlib.util.spec_from_file_location(
    "ack2007_admission_validator",
    HERE / "ack2007_admission_validator.py",
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def test_registry_covers_exact_model_input_set():
    registry = validator.load_registry(REGISTRY_PATH)
    validator.assert_registry_matches_model(registry, REQUIRED)


def test_verified_raw_definition_can_pass_construction_gate():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(
        registry, ["FOREIGN_SALES", "%LOSS"]
    )
    assert result == {"passed": True, "violations": []}


@pytest.mark.parametrize(
    "name,expected_status",
    [
        ("SIZE", "BLOCKED_MISSING_YEAR_RULE"),
        ("RGROWTH", "BLOCKED_MISSING_DATA_RULE"),
        ("RZSCORE", "BLOCKED_RAW_CONSTRUCTION"),
    ],
)
def test_known_unresolved_raw_construction_fails_closed(
    name, expected_status
):
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(registry, [name])
    assert not result["passed"]
    assert result["violations"] == [f"{name}: {expected_status}"]


def test_unknown_model_input_fails_closed_without_inspecting_raw_source_columns():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(
        registry, ["MYSTERY_MODEL_INPUT"]
    )
    assert result == {
        "passed": False,
        "violations": ["MYSTERY_MODEL_INPUT: UNREGISTERED_MODEL_INPUT"],
    }


def test_full_raw_construction_plan_is_blocked_while_any_gate_is_unresolved():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(registry, REQUIRED)
    assert not result["passed"]
    assert any(v.startswith("SIZE:") for v in result["violations"])
    assert any(v.startswith("RGROWTH:") for v in result["violations"])
    assert any(v.startswith("RZSCORE:") for v in result["violations"])


def test_duplicate_registry_keys_are_rejected(tmp_path):
    bad = tmp_path / "dup.json"
    bad.write_text(
        '{"schema_version":1,"schema_version":1,"model_id":"x",'
        '"short_name":"x","scope":"raw_model_input_construction_only",'
        '"default_policy":"BLOCK","notes":[],"variables":{"SIZE":{'
        '"definition":"x","raw_construction_status":"VERIFIED","reason":"x"}}}',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate JSON key"):
        validator.load_registry(bad)


def test_registry_drift_from_model_required_set_is_rejected():
    registry = validator.load_registry(REGISTRY_PATH)
    mutated = json.loads(json.dumps(registry))
    mutated["variables"].pop("SIZE")
    with pytest.raises(ValueError, match="registry/model input mismatch"):
        validator.assert_registry_matches_model(mutated, REQUIRED)
