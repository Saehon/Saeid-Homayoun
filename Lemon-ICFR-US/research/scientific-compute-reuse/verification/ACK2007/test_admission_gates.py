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


def _clone_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def test_registry_covers_exact_model_input_set():
    registry = validator.load_registry(REGISTRY_PATH)
    validator.assert_registry_matches_model(registry, REQUIRED)


def test_verified_raw_definition_can_pass_construction_gate():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(
        registry, ["FOREIGN_SALES"]
    )
    assert result == {"passed": True, "violations": []}


@pytest.mark.parametrize(
    "name,expected_status",
    [
        ("SIZE", "PROVENANCE_CONFLICT"),
        ("RGROWTH", "PROVENANCE_CONFLICT"),
        ("%LOSS", "BLOCKED_MISSING_YEAR_RULE"),
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
    assert any(v.startswith("%LOSS:") for v in result["violations"])


def test_duplicate_registry_keys_are_rejected(tmp_path):
    bad = tmp_path / "dup.json"
    bad.write_text(
        '{"schema_version":1,"schema_version":1,"model_id":"LEMON-SCI-ESM-001",'
        '"short_name":"ACK2007","scope":"raw_model_input_construction_only",'
        '"default_policy":"BLOCK","notes":["x"],"variables":{}}',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate JSON key"):
        validator.load_registry(bad)


@pytest.mark.parametrize(
    "field,value,match",
    [
        ("schema_version", 2, "schema_version"),
        ("model_id", "WRONG-MODEL", "model_id"),
        ("short_name", "WRONG", "short_name"),
        ("scope", "wrong_scope", "scope"),
        ("default_policy", "ALLOW", "default to BLOCK"),
    ],
)
def test_registry_identity_and_policy_drift_are_rejected(
    tmp_path, field, value, match
):
    registry = _clone_registry()
    registry[field] = value
    bad = tmp_path / f"{field}.json"
    bad.write_text(json.dumps(registry), encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        validator.load_registry(bad)


def test_registry_missing_model_predictor_is_rejected():
    registry = validator.load_registry(REGISTRY_PATH)
    mutated = json.loads(json.dumps(registry))
    mutated["variables"].pop("SIZE")
    with pytest.raises(ValueError, match="registry/model input mismatch"):
        validator.assert_registry_matches_model(mutated, REQUIRED)


def test_registry_extra_model_predictor_is_rejected():
    registry = validator.load_registry(REGISTRY_PATH)
    mutated = json.loads(json.dumps(registry))
    mutated["variables"]["MYSTERY_MODEL_INPUT"] = {
        "definition": "test only",
        "raw_construction_status": "VERIFIED",
        "reason": "test only",
    }
    with pytest.raises(ValueError, match="registry/model input mismatch"):
        validator.assert_registry_matches_model(mutated, REQUIRED)


def test_nonverified_future_status_fails_closed():
    registry = validator.load_registry(REGISTRY_PATH)
    mutated = json.loads(json.dumps(registry))
    mutated["variables"]["FOREIGN_SALES"]["raw_construction_status"] = (
        "PENDING_FUTURE_RULE"
    )
    result = validator.validate_raw_construction_request(
        mutated, ["FOREIGN_SALES"]
    )
    assert result == {
        "passed": False,
        "violations": ["FOREIGN_SALES: PENDING_FUTURE_RULE"],
    }


def test_unresolved_loss_rule_cannot_be_silently_promoted_to_verified():
    registry = validator.load_registry(REGISTRY_PATH)
    assert registry["variables"]["%LOSS"]["raw_construction_status"] == "BLOCKED_MISSING_YEAR_RULE"
    with pytest.raises(ValueError, match="%LOSS"):
        validator.require_raw_construction_allowed(registry, ["%LOSS"])
