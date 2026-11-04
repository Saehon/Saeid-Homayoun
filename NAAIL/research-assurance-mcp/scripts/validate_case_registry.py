#!/usr/bin/env python3
"""Validate the constrained NAAIL case registry without external packages."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from urllib.parse import unquote


DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$")
TOP_LEVEL_KEYS = {"schema_version", "normalization", "cases"}
CASE_KEYS = {"case_id", "doi", "title", "registry_status", "source_record"}
REQUIRED_CASE_KEYS = CASE_KEYS


class RegistryError(ValueError):
    pass


def parse_scalar(raw: str, line_number: int) -> str:
    raw = raw.strip()
    if not raw:
        raise RegistryError(f"line {line_number}: empty scalar")
    if raw.startswith(('"', "'")):
        try:
            value = ast.literal_eval(raw)
        except (SyntaxError, ValueError) as exc:
            raise RegistryError(f"line {line_number}: invalid quoted scalar") from exc
        if not isinstance(value, str):
            raise RegistryError(f"line {line_number}: scalar must be a string")
        return value
    return raw


def parse_registry(path: Path) -> dict:
    top: dict[str, object] = {}
    cases: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith("  - "):
            if current is not None:
                cases.append(current)
            current = {}
            payload = raw_line[4:]
            if ":" not in payload:
                raise RegistryError(f"line {line_number}: malformed case entry")
            key, value = payload.split(":", 1)
            if key not in CASE_KEYS:
                raise RegistryError(f"line {line_number}: unexpected case key {key!r}")
            current[key] = parse_scalar(value, line_number)
            continue
        if raw_line.startswith("    "):
            if current is None or ":" not in raw_line:
                raise RegistryError(f"line {line_number}: case field outside a case entry")
            key, value = raw_line.strip().split(":", 1)
            if key not in CASE_KEYS:
                raise RegistryError(f"line {line_number}: unexpected case key {key!r}")
            if key in current:
                raise RegistryError(f"line {line_number}: duplicate field {key!r}")
            current[key] = parse_scalar(value, line_number)
            continue
        if raw_line.startswith(" ") or ":" not in raw_line:
            raise RegistryError(f"line {line_number}: unsupported YAML structure")
        key, value = raw_line.split(":", 1)
        if key not in TOP_LEVEL_KEYS:
            raise RegistryError(f"line {line_number}: unexpected top-level key {key!r}")
        if key in top:
            raise RegistryError(f"line {line_number}: duplicate top-level key {key!r}")
        top[key] = [] if key == "cases" else parse_scalar(value, line_number)

    if current is not None:
        cases.append(current)
    top["cases"] = cases
    return top


def normalize_doi(raw: str) -> str:
    value = unquote(raw).strip().lower()
    prefixes = (
        "https://doi.org/",
        "http://doi.org/",
        "https://dx.doi.org/",
        "http://dx.doi.org/",
        "doi:",
    )
    for prefix in prefixes:
        if value.startswith(prefix):
            value = value[len(prefix) :].strip()
            break
    if any(char.isspace() for char in value):
        raise RegistryError(f"DOI contains internal whitespace: {raw!r}")
    if not DOI_PATTERN.fullmatch(value):
        raise RegistryError(f"invalid DOI syntax: {raw!r}")
    return value


def validate_registry(path: Path) -> dict:
    registry = parse_registry(path)
    if registry.get("schema_version") != "1.0":
        raise RegistryError("schema_version must be '1.0'")
    cases = registry.get("cases")
    if not isinstance(cases, list) or not cases:
        raise RegistryError("registry must contain at least one case")

    seen_ids: dict[str, int] = {}
    seen_dois: dict[str, str] = {}
    for index, case in enumerate(cases, 1):
        missing = REQUIRED_CASE_KEYS - set(case)
        extra = set(case) - CASE_KEYS
        if missing or extra:
            raise RegistryError(
                f"case {index}: missing={sorted(missing)} unexpected={sorted(extra)}"
            )
        case_id = case["case_id"].strip().upper()
        if not re.fullmatch(r"CASE-\d{3}", case_id):
            raise RegistryError(f"case {index}: invalid case_id {case['case_id']!r}")
        if case_id in seen_ids:
            raise RegistryError(f"duplicate case_id {case_id}")
        seen_ids[case_id] = index

        normalized = normalize_doi(case["doi"])
        if normalized in seen_dois:
            raise RegistryError(
                f"duplicate normalized DOI {normalized}: {seen_dois[normalized]} and {case_id}"
            )
        seen_dois[normalized] = case_id
        case["case_id"] = case_id
        case["normalized_doi"] = normalized
    return registry


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} REGISTRY.yaml", file=sys.stderr)
        return 2
    try:
        registry = validate_registry(Path(argv[1]))
    except (OSError, RegistryError) as exc:
        print(f"CASE_REGISTRY_INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"CASE_REGISTRY_VALID: {len(registry['cases'])} unique case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
