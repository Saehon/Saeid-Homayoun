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

SECONDARY_ONLY = ("FOREIGN_SALES", "AUDITOR", "INST_CON", "LITIGATION")
UNRESOLVED = {
    "SIZE": "PROVENANCE_CONFLICT",
    "RGROWTH": "PROVENANCE_CONFLICT",
    "%LOSS": "BLOCKED_MISSING_YEAR_RULE",
    "RZSCORE": "BLOCKED_RAW_CONSTRUCTION",
}


def _clone_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def test_registry_covers_exact_model_input_set():
    registry = validator.load_registry(REGISTRY_PATH)
    validator.assert_registry_matches_model(registry, REQUIRED)


@pytest.mark.parametrize("name", SECONDARY_ONLY)
def test_r005_secondary_only_variables_fail_closed(name):
    registry = validator.load_registry(REGISTRY_PATH)
    assert registry["variables"][name]["raw_construction_status"] == "SECONDARY_SOURCE"
    with pytest.raises(ValueError, match=name):
        validator.require_raw_construction_allowed(registry, [name])


@pytest.mark.parametrize("name,expected_status", UNRESOLVED.items())
def test_known_unresolved_raw_construction_fails_closed(name, expected_status):
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(registry, [name])
    assert result == {"passed": False, "violations": [f"{name}: {expected_status}"]}


@pytest.mark.parametrize("name", [*UNRESOLVED, *SECONDARY_ONLY])
def test_end_to_end_raw_execution_stops_before_constructor(name):
    registry = validator.load_registry(REGISTRY_PATH)
    called = []

    def tripwire(raw_record, proposed_rule):
        called.append((raw_record, proposed_rule))
        return "SHOULD_NOT_RUN"

    with pytest.raises(ValueError, match=name):
        validator.execute_raw_construction_request(
            registry,
            name,
            {"dummy": 1},
            tripwire,
            {"attempt": "raw execution"},
        )
    assert called == []


@pytest.mark.parametrize(
    "name,proposed_rule",
    [
        ("SIZE", {"transformation": "ln_market_value_equity"}),
        ("SIZE", {"transformation": "level_market_value_equity"}),
        ("SIZE", {"unit": "USD"}),
        ("SIZE", {"unit": "USD_billions"}),
        ("SIZE", {"missing_year": "available_year_average"}),
        ("RGROWTH", {"window": "2001-2003"}),
        ("RGROWTH", {"window": "2002-2004"}),
        ("RGROWTH", {"ranking_direction": "reverse"}),
        ("%LOSS", {"denominator": "observed_years"}),
        ("%LOSS", {"missing_year": "zero_fill"}),
        ("RZSCORE", {"formula": "Altman1968"}),
        ("RZSCORE", {"formula": "Altman1980"}),
        ("RZSCORE", {"ranking_direction": "reverse"}),
    ],
)
def test_adversarial_rule_claims_cannot_bypass_fail_closed(name, proposed_rule):
    registry = validator.load_registry(REGISTRY_PATH)
    called = []

    def tripwire(raw_record, rule):
        called.append(rule)

    with pytest.raises(ValueError, match=name):
        validator.execute_raw_construction_request(
            registry, name, {}, tripwire, proposed_rule
        )
    assert called == []


def test_unknown_model_input_fails_closed():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(
        registry, ["MYSTERY_MODEL_INPUT"]
    )
    assert result == {
        "passed": False,
        "violations": ["MYSTERY_MODEL_INPUT: UNREGISTERED_MODEL_INPUT"],
    }


def test_full_raw_construction_plan_is_blocked():
    registry = validator.load_registry(REGISTRY_PATH)
    result = validator.validate_raw_construction_request(registry, REQUIRED)
    assert not result["passed"]
    for name in [*UNRESOLVED, *SECONDARY_ONLY]:
        assert any(v.startswith(f"{name}:") for v in result["violations"])


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


def test_constructor_exception_is_not_silently_swallowed():
    registry = _clone_registry()
    registry["variables"]["SEGMENTS"]["raw_construction_status"] = "VERIFIED"

    def boom(raw_record, proposed_rule):
        raise RuntimeError("constructor failure")

    with pytest.raises(RuntimeError, match="constructor failure"):
        validator.execute_raw_construction_request(
            registry, "SEGMENTS", {}, boom, {"test": True}
        )
