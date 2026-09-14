#!/usr/bin/env python3
"""Validate the NAAIL FT50/AJG 4* external benchmark registry.

This script validates metadata only. It does not clone, download, or execute
third-party repositories. External code/data execution requires rights checks,
commit pinning, an isolated environment, and the NAAIL Human Gate.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from urllib.parse import urlparse

REQUIRED_FIELDS = {
    "benchmark_id",
    "journal",
    "ft50",
    "ajg_band",
    "title",
    "repository",
    "domain",
    "languages",
    "tests",
    "license_status",
    "source_commit",
}


def is_github_repo_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and parsed.netloc == "github.com" and len(parsed.path.strip("/").split("/")) >= 2


def validate(registry: dict, strict_pins: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if registry.get("third_party_code_copied_into_naail_core") is not False:
        errors.append("Registry must keep third_party_code_copied_into_naail_core=false by default.")
    if registry.get("human_gate_required") is not True:
        errors.append("human_gate_required must be true.")

    items = registry.get("benchmarks")
    if not isinstance(items, list) or not items:
        errors.append("benchmarks must be a non-empty list.")
        return errors, warnings

    seen: set[str] = set()
    for idx, item in enumerate(items, start=1):
        prefix = f"benchmark[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix}: item must be an object.")
            continue

        missing = sorted(REQUIRED_FIELDS - item.keys())
        if missing:
            errors.append(f"{prefix}: missing fields: {', '.join(missing)}")

        bid = item.get("benchmark_id")
        if bid in seen:
            errors.append(f"{prefix}: duplicate benchmark_id {bid!r}.")
        elif isinstance(bid, str):
            seen.add(bid)

        repo = item.get("repository")
        if not isinstance(repo, str) or not is_github_repo_url(repo):
            errors.append(f"{prefix}: repository must be an https://github.com/<owner>/<repo> URL.")

        tests = item.get("tests")
        if not isinstance(tests, list) or not tests:
            errors.append(f"{prefix}: tests must be a non-empty list.")

        domains = item.get("domain")
        if not isinstance(domains, list) or not domains:
            errors.append(f"{prefix}: domain must be a non-empty list.")

        commit = item.get("source_commit")
        if commit is None:
            message = f"{prefix}: source_commit is not pinned; pin an exact SHA before execution."
            if strict_pins:
                errors.append(message)
            else:
                warnings.append(message)
        elif not isinstance(commit, str) or len(commit) < 7:
            errors.append(f"{prefix}: source_commit must be a Git commit SHA or null before pinning.")

        if item.get("ft50") is not True:
            warnings.append(f"{prefix}: ft50 is not true; confirm inclusion criteria.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "registry",
        nargs="?",
        default=str(pathlib.Path(__file__).with_name("registry.json")),
        help="Path to registry.json",
    )
    parser.add_argument(
        "--strict-pins",
        action="store_true",
        help="Fail validation when an external benchmark has not yet been pinned to a commit SHA.",
    )
    args = parser.parse_args()

    path = pathlib.Path(args.registry)
    try:
        registry = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read registry: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate(registry, strict_pins=args.strict_pins)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    total = len(registry.get("benchmarks", []))
    print(f"Validated {total} benchmark record(s): {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
