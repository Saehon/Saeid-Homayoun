"""Fail-closed ACK2007 raw-construction admission checks.

This module governs raw construction of model inputs only. It intentionally
does not inspect arbitrary source-data columns and is not invoked by the
frozen synthetic compiler fixture runner.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping

ALLOWED_TOP_LEVEL = {
    "schema_version",
    "model_id",
    "short_name",
    "scope",
    "default_policy",
    "notes",
    "variables",
}
REQUIRED_VARIABLE_FIELDS = {"definition", "raw_construction_status", "reason"}
RAW_VERIFIED = "VERIFIED"


def _no_duplicate_object_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def load_registry(path: str | Path) -> dict:
    path = Path(path)
    with path.open("r", encoding="utf-8") as fh:
        registry = json.load(fh, object_pairs_hook=_no_duplicate_object_pairs)

    unknown_top = set(registry) - ALLOWED_TOP_LEVEL
    missing_top = ALLOWED_TOP_LEVEL - set(registry)
    if unknown_top or missing_top:
        raise ValueError(
            f"invalid registry top-level schema; missing={sorted(missing_top)}, "
            f"unknown={sorted(unknown_top)}"
        )
    if registry["default_policy"] != "BLOCK":
        raise ValueError("ACK2007 raw-construction registry must default to BLOCK")
    if registry["scope"] != "raw_model_input_construction_only":
        raise ValueError("unexpected registry scope")

    variables = registry["variables"]
    if not isinstance(variables, dict) or not variables:
        raise ValueError("registry variables must be a non-empty object")

    for name, spec in variables.items():
        if not isinstance(spec, dict):
            raise ValueError(f"{name}: registry entry must be an object")
        fields = set(spec)
        if fields != REQUIRED_VARIABLE_FIELDS:
            raise ValueError(
                f"{name}: invalid registry fields; "
                f"missing={sorted(REQUIRED_VARIABLE_FIELDS-fields)}, "
                f"unknown={sorted(fields-REQUIRED_VARIABLE_FIELDS)}"
            )
        if not all(
            isinstance(spec[field], str) and spec[field].strip()
            for field in REQUIRED_VARIABLE_FIELDS
        ):
            raise ValueError(f"{name}: registry fields must be non-empty strings")
    return registry


def assert_registry_matches_model(
    registry: Mapping, required_inputs: Iterable[str]
) -> None:
    required = tuple(required_inputs)
    registered = tuple(registry["variables"])
    missing = sorted(set(required) - set(registered))
    unknown = sorted(set(registered) - set(required))
    if missing or unknown:
        raise ValueError(
            f"registry/model input mismatch; missing={missing}, unknown={unknown}"
        )


def validate_raw_construction_request(
    registry: Mapping, requested_inputs: Iterable[str]
) -> dict:
    """Validate requested ACK2007 model inputs for raw construction.

    Unknown model inputs fail closed. Raw source dataframe columns are outside
    this function's scope and must not be treated as model inputs.
    """
    violations = []
    variables = registry["variables"]
    for name in requested_inputs:
        if name not in variables:
            violations.append(f"{name}: UNREGISTERED_MODEL_INPUT")
            continue
        status = variables[name]["raw_construction_status"]
        if status != RAW_VERIFIED:
            violations.append(f"{name}: {status}")
    return {"passed": not violations, "violations": violations}


def require_raw_construction_allowed(
    registry: Mapping, requested_inputs: Iterable[str]
) -> None:
    result = validate_raw_construction_request(registry, requested_inputs)
    if not result["passed"]:
        raise ValueError(
            "ACK2007 raw construction blocked: " + "; ".join(result["violations"])
        )
