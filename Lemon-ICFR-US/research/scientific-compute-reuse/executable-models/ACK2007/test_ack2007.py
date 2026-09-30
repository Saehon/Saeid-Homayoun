import copy
import json

import pytest

from ack2007 import (
    COEFFICIENTS,
    CONTRACT,
    EXPECTED_PREDICTOR_NAMES,
    INTERCEPT,
    REQUIRED,
    contract_semantic_digest,
    linear_predictor,
    load_coefficient_contract,
    logistic,
    predict,
    validate_compiler_input,
)

ZERO = {k: 0.0 for k in REQUIRED}
EXPECTED_CONTRACT_DIGEST = "530c98d08b5d14236006198509b0cd0ba54812325ad9e6029ff76afea3ddb0f1"


def _write_contract(path, contract):
    path.write_text(
        json.dumps(contract, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def test_contract_is_single_regression_pin():
    assert contract_semantic_digest(CONTRACT) == EXPECTED_CONTRACT_DIGEST
    assert CONTRACT["role"] == "regression_pin_only"
    assert CONTRACT["coefficient_verification"] == "PENDING_PRIMARY_TABLE"
    assert CONTRACT["coefficient_origin"] == "UNKNOWN_ORIGIN"


def test_coefficient_count_and_interface():
    assert len(COEFFICIENTS) == 14
    assert REQUIRED == EXPECTED_PREDICTOR_NAMES
    assert tuple(COEFFICIENTS) == EXPECTED_PREDICTOR_NAMES
    assert INTERCEPT == pytest.approx(CONTRACT["intercept"])


def test_runtime_coefficient_vector_is_immutable():
    with pytest.raises(TypeError):
        COEFFICIENTS["SIZE"] = 999.0
    with pytest.raises(TypeError):
        del COEFFICIENTS["SIZE"]


def test_public_prediction_boundary_is_always_closed_during_scientific_hold():
    for kwargs in ({}, {"input_mode": "RAW_DATA"}, {"input_mode": "PRECONSTRUCTED_SYNTHETIC_COMPILER_TEST"}):
        with pytest.raises(ValueError, match="public prediction is disabled"):
            predict(ZERO, **kwargs)
        with pytest.raises(ValueError, match="public prediction is disabled"):
            linear_predictor(ZERO, **kwargs)


def test_compiler_input_validation_accepts_complete_finite_vector():
    validate_compiler_input(ZERO)


def test_missing_variable_rejected_by_compiler_input_validation():
    x = dict(ZERO)
    x.pop("RZSCORE")
    with pytest.raises(ValueError, match="Missing ACK2007 variables"):
        validate_compiler_input(x)


def test_unknown_variable_rejected_by_compiler_input_validation():
    x = dict(ZERO)
    x["LEAKAGE"] = 1
    with pytest.raises(ValueError, match="Unknown ACK2007 variables"):
        validate_compiler_input(x)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf"), True, "1.0"])
def test_invalid_runtime_value_rejected(value):
    x = dict(ZERO)
    x["SIZE"] = value
    with pytest.raises(ValueError, match="finite numeric"):
        validate_compiler_input(x)


@pytest.mark.parametrize("z", [-1000, -10, 0, 10, 1000])
def test_logistic_stable_and_bounded(z):
    p = logistic(z)
    assert 0 <= p <= 1


@pytest.mark.parametrize("mutation", ["missing", "extra", "renamed", "duplicate", "reordered"])
def test_predictor_identity_mutations_rejected(tmp_path, mutation):
    mutated = copy.deepcopy(CONTRACT)
    if mutation == "missing":
        mutated["predictors"].pop()
    elif mutation == "extra":
        mutated["predictors"].append({"name": "EXTRA", "coefficient": 0.0})
    elif mutation == "renamed":
        mutated["predictors"][0]["name"] = "SEGMENT"
    elif mutation == "duplicate":
        mutated["predictors"][1]["name"] = mutated["predictors"][0]["name"]
    else:
        mutated["predictors"][0], mutated["predictors"][1] = (
            mutated["predictors"][1],
            mutated["predictors"][0],
        )
    path = tmp_path / "contract.json"
    _write_contract(path, mutated)
    with pytest.raises(ValueError):
        load_coefficient_contract(path)


@pytest.mark.parametrize(
    "mutation",
    [
        "coefficient_change",
        "coefficient_zero",
        "coefficient_scale",
        "sign_flip",
        "intercept_mutation",
        "intercept_sign_flip",
        "intercept_scale",
    ],
)
def test_numeric_contract_mutations_break_regression_pin(mutation):
    mutated = copy.deepcopy(CONTRACT)
    if mutation == "coefficient_change":
        mutated["predictors"][0]["coefficient"] += 0.001
    elif mutation == "coefficient_zero":
        mutated["predictors"][0]["coefficient"] = 0.0
    elif mutation == "coefficient_scale":
        mutated["predictors"][0]["coefficient"] *= 100
    elif mutation == "sign_flip":
        mutated["predictors"][1]["coefficient"] *= -1
    elif mutation == "intercept_mutation":
        mutated["intercept"] += 0.001
    elif mutation == "intercept_sign_flip":
        mutated["intercept"] *= -1
    else:
        mutated["intercept"] *= 100
    assert contract_semantic_digest(mutated) != EXPECTED_CONTRACT_DIGEST


@pytest.mark.parametrize("predictor_index", range(14))
@pytest.mark.parametrize("mutation", ["change", "zero", "sign_flip", "scale"])
def test_every_coefficient_mutation_breaks_regression_pin(predictor_index, mutation):
    """Integrity-cover all 14 unverified regression-pin coefficients without executing predictions."""
    mutated = copy.deepcopy(CONTRACT)
    original = mutated["predictors"][predictor_index]["coefficient"]
    assert original != 0.0
    if mutation == "change":
        mutated["predictors"][predictor_index]["coefficient"] = original + 0.001
    elif mutation == "zero":
        mutated["predictors"][predictor_index]["coefficient"] = 0.0
    elif mutation == "sign_flip":
        mutated["predictors"][predictor_index]["coefficient"] = -original
    else:
        mutated["predictors"][predictor_index]["coefficient"] = original * 100
    assert contract_semantic_digest(mutated) != EXPECTED_CONTRACT_DIGEST


@pytest.mark.parametrize(
    "field,value,match",
    [
        ("role", "published_model", "regression_pin_only"),
        ("coefficient_verification", "VERIFIED", "PENDING_PRIMARY_TABLE"),
        ("coefficient_origin", "JAE2007", "UNKNOWN_ORIGIN"),
    ],
)
def test_contract_scientific_status_mutations_rejected(tmp_path, field, value, match):
    mutated = copy.deepcopy(CONTRACT)
    mutated[field] = value
    path = tmp_path / "contract.json"
    _write_contract(path, mutated)
    with pytest.raises(ValueError, match=match):
        load_coefficient_contract(path)


@pytest.mark.parametrize("bad_value", ["0.078", True, float("nan"), float("inf")])
def test_non_numeric_or_nonfinite_coefficient_rejected(tmp_path, bad_value):
    mutated = copy.deepcopy(CONTRACT)
    mutated["predictors"][0]["coefficient"] = bad_value
    path = tmp_path / "contract.json"
    _write_contract(path, mutated)
    with pytest.raises(ValueError, match="coefficient"):
        load_coefficient_contract(path)


@pytest.mark.parametrize("bad_value", ["-3.752", True, float("nan"), float("inf")])
def test_non_numeric_or_nonfinite_intercept_rejected(tmp_path, bad_value):
    mutated = copy.deepcopy(CONTRACT)
    mutated["intercept"] = bad_value
    path = tmp_path / "contract.json"
    _write_contract(path, mutated)
    with pytest.raises(ValueError, match="intercept"):
        load_coefficient_contract(path)


def test_intercept_deletion_rejected(tmp_path):
    mutated = copy.deepcopy(CONTRACT)
    del mutated["intercept"]
    path = tmp_path / "contract.json"
    _write_contract(path, mutated)
    with pytest.raises(ValueError, match="top-level schema"):
        load_coefficient_contract(path)


def test_duplicate_intercept_key_rejected(tmp_path):
    path = tmp_path / "contract.json"
    path.write_text(
        '{"schema_version":1,"model_id":"LEMON-SCI-ESM-001",'
        '"short_name":"ACK2007","role":"regression_pin_only",'
        '"coefficient_verification":"PENDING_PRIMARY_TABLE",'
        '"coefficient_origin":"UNKNOWN_ORIGIN","intercept":-3.752,'
        '"intercept":-3.752,"predictors":[]}',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate coefficient-contract key"):
        load_coefficient_contract(path)


def test_malformed_contract_json_rejected(tmp_path):
    path = tmp_path / "contract.json"
    path.write_text('{"schema_version": 1,', encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_coefficient_contract(path)
