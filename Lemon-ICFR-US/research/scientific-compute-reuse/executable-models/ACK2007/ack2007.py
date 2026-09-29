"""LEMON-SCI ACK2007 engineering compiler.

The coefficient vector is loaded from the single machine-readable coefficient
contract and retained unchanged as a regression pin pending primary-table
verification. This module makes no scientific coefficient-validity claim.

While ACK2007 is SCIENTIFIC_HOLD, public prediction is restricted to the
explicit preconstructed-synthetic compiler-fixture mode. Raw-data callers must
not bypass the construction-gate boundary by calling this module directly.
"""
from dataclasses import dataclass
from math import exp, isfinite
import hashlib
import json
from pathlib import Path
from typing import Mapping

CONTRACT_PATH = Path(__file__).with_name("coefficient-contract.json")
SYNTHETIC_FIXTURE_MODE = "PRECONSTRUCTED_SYNTHETIC_COMPILER_TEST"
EXPECTED_CONTRACT_FIELDS = {
    "schema_version",
    "model_id",
    "short_name",
    "role",
    "coefficient_verification",
    "coefficient_origin",
    "intercept",
    "predictors",
}
EXPECTED_PREDICTOR_NAMES = (
    "SEGMENTS",
    "FOREIGN_SALES",
    "M&A",
    "RESTRUCTURE",
    "RGROWTH",
    "INVENTORY",
    "SIZE",
    "%LOSS",
    "RZSCORE",
    "AUDITOR_RESIGN",
    "AUDITOR",
    "RESTATEMENT",
    "INST_CON",
    "LITIGATION",
)


def _no_duplicate_object_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate coefficient-contract key: {key}")
        obj[key] = value
    return obj


def _finite_number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be finite numeric")
    value = float(value)
    if not isfinite(value):
        raise ValueError(f"{label} must be finite numeric")
    return value


def load_coefficient_contract(path: str | Path = CONTRACT_PATH) -> dict:
    path = Path(path)
    with path.open("r", encoding="utf-8") as fh:
        contract = json.load(fh, object_pairs_hook=_no_duplicate_object_pairs)

    if set(contract) != EXPECTED_CONTRACT_FIELDS:
        raise ValueError("invalid coefficient-contract top-level schema")
    if contract["schema_version"] != 1:
        raise ValueError("unexpected coefficient-contract schema_version")
    if contract["model_id"] != "LEMON-SCI-ESM-001" or contract["short_name"] != "ACK2007":
        raise ValueError("coefficient-contract model identity mismatch")
    if contract["role"] != "regression_pin_only":
        raise ValueError("coefficient-contract role must remain regression_pin_only")
    if contract["coefficient_verification"] != "PENDING_PRIMARY_TABLE":
        raise ValueError("coefficient verification must remain PENDING_PRIMARY_TABLE")
    if contract["coefficient_origin"] != "UNKNOWN_ORIGIN":
        raise ValueError("coefficient origin must remain UNKNOWN_ORIGIN")
    _finite_number(contract["intercept"], "coefficient-contract intercept")

    predictors = contract["predictors"]
    if not isinstance(predictors, list) or len(predictors) != 14:
        raise ValueError("coefficient-contract must contain exactly 14 predictors")
    names = []
    for item in predictors:
        if not isinstance(item, dict) or set(item) != {"name", "coefficient"}:
            raise ValueError("invalid coefficient-contract predictor schema")
        name = item["name"]
        if not isinstance(name, str) or not name:
            raise ValueError("coefficient-contract predictor name must be non-empty")
        _finite_number(item["coefficient"], f"{name}: coefficient")
        names.append(name)
    if len(names) != len(set(names)):
        raise ValueError("duplicate coefficient-contract predictor name")
    if tuple(names) != EXPECTED_PREDICTOR_NAMES:
        raise ValueError("coefficient-contract predictor identity/order mismatch")
    return contract


def contract_semantic_digest(contract: Mapping) -> str:
    payload = json.dumps(
        contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


CONTRACT = load_coefficient_contract()
COEFFICIENTS = {
    item["name"]: float(item["coefficient"]) for item in CONTRACT["predictors"]
}
INTERCEPT = float(CONTRACT["intercept"])
REQUIRED = tuple(COEFFICIENTS)


@dataclass(frozen=True)
class ACK2007Prediction:
    linear_predictor: float
    probability: float


def _validate_values(x: Mapping[str, float]) -> None:
    missing = [k for k in REQUIRED if k not in x]
    extra = [k for k in x if k not in COEFFICIENTS]
    if missing:
        raise ValueError(f"Missing ACK2007 variables: {missing}")
    if extra:
        raise ValueError(f"Unknown ACK2007 variables: {extra}")
    for k in REQUIRED:
        _finite_number(x[k], k)


def _require_synthetic_fixture_mode(input_mode: str | None) -> None:
    if input_mode != SYNTHETIC_FIXTURE_MODE:
        raise ValueError(
            "ACK2007 prediction is fail-closed while scientific raw-construction "
            "gates are unresolved; only explicit PRECONSTRUCTED_SYNTHETIC_COMPILER_TEST "
            "mode is allowed in the engineering compiler."
        )


def linear_predictor(
    x: Mapping[str, float], *, input_mode: str | None = None
) -> float:
    _require_synthetic_fixture_mode(input_mode)
    _validate_values(x)
    return INTERCEPT + sum(COEFFICIENTS[k] * float(x[k]) for k in REQUIRED)


def logistic(z: float) -> float:
    if z >= 0:
        return 1.0 / (1.0 + exp(-z))
    ez = exp(z)
    return ez / (1.0 + ez)


def predict(
    x: Mapping[str, float], *, input_mode: str | None = None
) -> ACK2007Prediction:
    _require_synthetic_fixture_mode(input_mode)
    _validate_values(x)
    z = INTERCEPT + sum(COEFFICIENTS[k] * float(x[k]) for k in REQUIRED)
    return ACK2007Prediction(z, logistic(z))
