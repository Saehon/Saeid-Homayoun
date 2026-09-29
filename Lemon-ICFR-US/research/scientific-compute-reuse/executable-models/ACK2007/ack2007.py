"""LEMON-SCI ACK2007 engineering compiler contract.

The coefficient vector is loaded from the single machine-readable coefficient
contract and retained unchanged as a regression pin pending primary-table
verification. This module makes no scientific coefficient-validity claim.

While ACK2007 is SCIENTIFIC_HOLD, the public prediction boundary is disabled.
Frozen synthetic fixture arithmetic is implemented only in the verification
runner so raw-data callers cannot relabel inputs as synthetic.
"""
from dataclasses import dataclass
from math import exp, isfinite
import hashlib
import json
from pathlib import Path
from types import MappingProxyType
from typing import Mapping

CONTRACT_PATH = Path(__file__).with_name("coefficient-contract.json")
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
COEFFICIENTS = MappingProxyType(
    {
        item["name"]: float(item["coefficient"])
        for item in CONTRACT["predictors"]
    }
)
INTERCEPT = float(CONTRACT["intercept"])
REQUIRED = tuple(COEFFICIENTS)


@dataclass(frozen=True)
class ACK2007Prediction:
    linear_predictor: float
    probability: float


def validate_compiler_input(x: Mapping[str, float]) -> None:
    """Validate a fully preconstructed compiler input vector.

    This validates shape and numeric finiteness only. It does not grant
    scientific provenance or raw-construction admission.
    """
    missing = [k for k in REQUIRED if k not in x]
    extra = [k for k in x if k not in COEFFICIENTS]
    if missing:
        raise ValueError(f"Missing ACK2007 variables: {missing}")
    if extra:
        raise ValueError(f"Unknown ACK2007 variables: {extra}")
    for k in REQUIRED:
        _finite_number(x[k], k)


def _scientific_hold_error() -> ValueError:
    return ValueError(
        "ACK2007 public prediction is disabled while SCIENTIFIC_HOLD is active; "
        "raw construction must pass the canonical admission boundary, and "
        "frozen synthetic regression-pin arithmetic is isolated in "
        "verification/ACK2007/run_fixtures.py."
    )


def linear_predictor(x: Mapping[str, float], **kwargs) -> float:
    """Public prediction boundary: disabled until scientific admission."""
    raise _scientific_hold_error()


def predict(x: Mapping[str, float], **kwargs) -> ACK2007Prediction:
    """Public prediction boundary: disabled until scientific admission."""
    raise _scientific_hold_error()


def logistic(z: float) -> float:
    if z >= 0:
        return 1.0 / (1.0 + exp(-z))
    ez = exp(z)
    return ez / (1.0 + ez)
