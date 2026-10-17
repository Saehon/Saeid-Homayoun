#!/usr/bin/env python3
"""Fail-closed prior-exposure governance check for NAAIL rule/protocol artifacts.

Controls:
1. Validate the registry against its JSON Schema using jsonschema.
2. Discover every JSON artifact under derived/ that declares rule_id or protocol_id;
   each must have exactly one registry entry.
3. Read the registered rule/protocol at its freeze commit.
4. If its source_csv already exists at the freeze commit, prior_exposure must be true.
5. Use git merge-base --is-ancestor for historical ordering; do not infer ordering
   from author/committer dates.
6. Rejected/historical preregistration artifacts must remain inactive.

This check performs no SEC/network data retrieval.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[1]
DERIVED_ROOT = PROJECT_ROOT / "derived"
REGISTRY_PATH = DERIVED_ROOT / "rule_prior_exposure_registry.json"
SCHEMA_PATH = DERIVED_ROOT / "rule_prior_exposure_registry.schema.json"


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def commit_exists(commit: str) -> bool:
    return git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode == 0


def path_exists_at(commit: str, path: str) -> bool:
    return git("cat-file", "-e", f"{commit}:{path}", check=False).returncode == 0


def read_json_at(commit: str, path: str) -> dict[str, Any]:
    proc = git("show", f"{commit}:{path}")
    return json.loads(proc.stdout)


def is_ancestor(older: str, newer: str) -> bool:
    return git("merge-base", "--is-ancestor", older, newer, check=False).returncode == 0


def normalize_source_path(value: str) -> str:
    value = value.lstrip("/")
    project_prefix = "NAAIL/research-assurance-mcp/"
    if value.startswith(project_prefix):
        return value
    return project_prefix + value


def discover_governed_files() -> dict[str, str]:
    found: dict[str, str] = {}
    for path in DERIVED_ROOT.rglob("*.json"):
        rel = path.relative_to(REPO_ROOT).as_posix()
        if path.name in {
            "rule_prior_exposure_registry.json",
            "rule_prior_exposure_registry.schema.json",
        }:
            continue
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        if isinstance(obj.get("rule_id"), str):
            found[rel] = obj["rule_id"]
        elif isinstance(obj.get("protocol_id"), str):
            found[rel] = obj["protocol_id"]
    return found


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(registry), key=lambda err: list(err.path))
    if errors:
        formatted = [
            {
                "path": list(err.path),
                "message": err.message,
            }
            for err in errors
        ]
        raise AssertionError(f"registry schema validation failed: {formatted}")

    entries = registry["entries"]
    by_path: dict[str, dict[str, Any]] = {}
    by_id: dict[str, dict[str, Any]] = {}
    for entry in entries:
        path = entry["artifact_path"]
        artifact_id = entry["artifact_id"]
        if path in by_path:
            raise AssertionError(f"duplicate registry artifact_path: {path}")
        if artifact_id in by_id:
            raise AssertionError(f"duplicate registry artifact_id: {artifact_id}")
        by_path[path] = entry
        by_id[artifact_id] = entry

    discovered = discover_governed_files()
    missing_registry = sorted(set(discovered) - set(by_path))
    if missing_registry:
        raise AssertionError(
            f"governed rule/protocol files missing registry entries: {missing_registry}"
        )

    mismatched_ids = [
        (path, discovered[path], by_path[path]["artifact_id"])
        for path in sorted(discovered)
        if by_path[path]["artifact_id"] != discovered[path]
    ]
    if mismatched_ids:
        raise AssertionError(f"registry artifact IDs do not match files: {mismatched_ids}")

    results: list[dict[str, Any]] = []

    for entry in entries:
        artifact_path = entry["artifact_path"]
        artifact_id = entry["artifact_id"]
        freeze = entry["freeze_commit"]

        if not commit_exists(freeze):
            raise AssertionError(f"{artifact_id}: freeze commit unavailable: {freeze}")
        if not path_exists_at(freeze, artifact_path):
            raise AssertionError(
                f"{artifact_id}: artifact not present at freeze commit: {artifact_path}"
            )

        frozen_obj = read_json_at(freeze, artifact_path)
        embedded_id = frozen_obj.get("rule_id") or frozen_obj.get("protocol_id")
        if embedded_id != artifact_id:
            raise AssertionError(
                f"{artifact_id}: frozen artifact ID mismatch: {embedded_id!r}"
            )

        source_csv = entry.get("source_csv")
        frozen_source_exists = False
        if source_csv:
            normalized_source = normalize_source_path(source_csv)
            frozen_source_exists = path_exists_at(freeze, normalized_source)

            embedded_source = frozen_obj.get("source_csv")
            if embedded_source:
                embedded_source = normalize_source_path(str(embedded_source))
                if embedded_source != normalized_source:
                    raise AssertionError(
                        f"{artifact_id}: registry source_csv differs from frozen artifact"
                    )

            if frozen_source_exists and entry["prior_exposure"] is not True:
                raise AssertionError(
                    f"{artifact_id}: source_csv existed at freeze commit; "
                    "prior_exposure must be true"
                )

        earliest = entry.get("earliest_outcome_artifact")
        earliest_is_ancestor = None
        if earliest:
            outcome_commit = earliest["commit"]
            if not commit_exists(outcome_commit):
                raise AssertionError(
                    f"{artifact_id}: earliest outcome commit unavailable: {outcome_commit}"
                )
            if not path_exists_at(outcome_commit, earliest["path"]):
                raise AssertionError(
                    f"{artifact_id}: earliest outcome path missing at declared commit"
                )
            earliest_is_ancestor = is_ancestor(outcome_commit, freeze)
            if earliest_is_ancestor and entry["prior_exposure"] is not True:
                raise AssertionError(
                    f"{artifact_id}: outcome commit is an ancestor of freeze; "
                    "prior_exposure must be true"
                )

        if entry["status"] in {"REJECTED_V1_PREREGISTRATION", "HISTORICAL"}:
            if entry["active_for_execution"]:
                raise AssertionError(
                    f"{artifact_id}: rejected/historical artifact must be inactive"
                )
            correction = entry.get("correction_record")
            if not correction:
                raise AssertionError(
                    f"{artifact_id}: rejected/historical artifact needs correction_record"
                )

        if (
            entry["status"] == "FROZEN_PREREGISTERED"
            and entry["active_for_execution"]
            and entry["prior_exposure"]
        ):
            raise AssertionError(
                f"{artifact_id}: active preregistered artifact cannot declare prior exposure"
            )

        results.append(
            {
                "artifact_id": artifact_id,
                "artifact_path": artifact_path,
                "freeze_commit": freeze,
                "source_csv_exists_at_freeze": frozen_source_exists,
                "earliest_outcome_is_ancestor_of_freeze": earliest_is_ancestor,
                "prior_exposure": entry["prior_exposure"],
                "active_for_execution": entry["active_for_execution"],
            }
        )

    print(
        json.dumps(
            {
                "status": "PASS",
                "schema_validation": "PASS",
                "governed_files_discovered_in_worktree": discovered,
                "registry_entries_checked": len(entries),
                "results": results,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"PRIOR_EXPOSURE_GUARD_FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
