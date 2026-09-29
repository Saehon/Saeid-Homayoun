"""Fail-closed ACK2007 raw-construction admission checks.

The construction registry is the sole machine-readable authority for raw input
construction. Frozen synthetic fixtures are a separate compiler test path.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Iterable, Mapping

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
EXPECTED_SCHEMA_VERSION = 1
EXPECTED_MODEL_ID = "LEMON-SCI-ESM-001"
EXPECTED_SHORT_NAME = "ACK2007"
EXPECTED_SCOPE = "raw_model_input_construction_only"
EXPECTED_DEFAULT_POLICY = "BLOCK"
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
    if registry["schema_version"] != EXPECTED_SCHEMA_VERSION:
        raise ValueError(f"unexpected registry schema_version: {registry['schema_version']!r}")
    if registry["model_id"] != EXPECTED_MODEL_ID:
        raise ValueError(f"unexpected registry model_id: {registry['model_id']!r}")
    if registry["short_name"] != EXPECTED_SHORT_NAME:
        raise ValueError(f"unexpected registry short_name: {registry['short_name']!r}")
    if registry["scope"] != EXPECTED_SCOPE:
        raise ValueError(f"unexpected registry scope: {registry['scope']!r}")
    if registry["default_policy"] != EXPECTED_DEFAULT_POLICY:
        raise ValueError("ACK2007 raw-construction registry must default to BLOCK")
    if not isinstance(registry["notes"], list) or not all(
        isinstance(note, str) and note.strip() for note in registry["notes"]
    ):
        raise ValueError("registry notes must be a list of non-empty strings")

    variables = registry["variables"]
    if not isinstance(variables, dict) or not variables:
        raise ValueError("registry variables must be a non-empty object")

    for name, spec in variables.items():
        if not isinstance(name, str) or not name:
            raise ValueError("registry variable names must be non-empty strings")
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


def execute_raw_construction_request(
    registry: Mapping,
    name: str,
    raw_record: Mapping,
    constructor: Callable,
    proposed_rule: Mapping | None = None,
):
    """End-to-end fail-closed boundary for a single raw-input construction.

    The gate is checked before a constructor or proposed transformation can run.
    Constructor exceptions are deliberately not swallowed.
    """
    require_raw_construction_allowed(registry, [name])
    return constructor(raw_record, proposed_rule)
