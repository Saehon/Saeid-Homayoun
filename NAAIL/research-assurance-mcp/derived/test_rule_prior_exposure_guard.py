#!/usr/bin/env python3
"""Fail-closed prior-exposure governance check for NAAIL research rules.

Policy:
1. Every registry entry declares prior_exposure.
2. Every referenced commit exists and its recorded timestamp matches Git history.
3. If outcome evidence predates a rule/protocol freeze, prior_exposure must be true.
4. An active FROZEN_PREREGISTERED rule must have prior_exposure=false and no outcome
   artifact dated at or before its freeze.
5. Historical/rejected rules may remain in the registry only when inactive and
   accompanied by an additive correction record.

This test performs no network access and retrieves no SEC data.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[1]
REGISTRY_PATH = PROJECT_ROOT / "derived" / "rule_prior_exposure_registry.json"

REQUIRED = {
    "rule_id",
    "status",
    "active_for_execution",
    "prior_exposure",
    "freeze_commit",
    "freeze_timestamp_utc",
    "earliest_outcome_artifact",
    "policy_disposition",
}


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def git_commit_time(commit: str) -> str:
    return subprocess.check_output(
        ["git", "show", "-s", "--format=%aI", commit],
        cwd=REPO_ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    ).strip()


def assert_commit_timestamp(commit: str, declared: str, label: str) -> datetime:
    actual = git_commit_time(commit)
    actual_dt = parse_time(actual)
    declared_dt = parse_time(declared)
    if actual_dt != declared_dt:
        raise AssertionError(
            f"{label}: declared timestamp {declared} != git author timestamp {actual}"
        )
    return actual_dt


def check_entry(entry: dict[str, Any]) -> list[str]:
    missing = sorted(REQUIRED - set(entry))
    if missing:
        raise AssertionError(f"{entry.get('rule_id','UNKNOWN')}: missing fields {missing}")

    rule_id = entry["rule_id"]
    freeze_dt = assert_commit_timestamp(
        entry["freeze_commit"], entry["freeze_timestamp_utc"], f"{rule_id}/freeze"
    )

    earliest = entry["earliest_outcome_artifact"]
    prior_exposure = entry["prior_exposure"]
    active = entry["active_for_execution"]
    status = entry["status"]

    notes: list[str] = []

    if earliest is not None:
        outcome_dt = assert_commit_timestamp(
            earliest["commit"], earliest["timestamp_utc"], f"{rule_id}/earliest_outcome"
        )
        outcome_before_or_at_freeze = outcome_dt <= freeze_dt

        if outcome_before_or_at_freeze and prior_exposure is not True:
            raise AssertionError(
                f"{rule_id}: outcome artifact predates/equal freeze but prior_exposure is not true"
            )
        if not outcome_before_or_at_freeze and prior_exposure is True:
            notes.append(
                f"{rule_id}: prior_exposure=true even though registered earliest outcome is later; review registry completeness"
            )
    elif prior_exposure is True:
        raise AssertionError(
            f"{rule_id}: prior_exposure=true requires earliest_outcome_artifact"
        )

    if status == "FROZEN_PREREGISTERED" and active:
        if prior_exposure:
            raise AssertionError(
                f"{rule_id}: active preregistered rule cannot have prior_exposure=true"
            )
        if earliest is not None and parse_time(earliest["timestamp_utc"]) <= freeze_dt:
            raise AssertionError(
                f"{rule_id}: active preregistered rule froze after outcome data already existed"
            )

    if status in {"REJECTED_V1_PREREGISTRATION", "HISTORICAL"}:
        if active:
            raise AssertionError(f"{rule_id}: rejected/historical rule must be inactive")
        correction = entry.get("correction_record")
        if not correction:
            raise AssertionError(f"{rule_id}: rejected/historical rule needs correction_record")
        if not (REPO_ROOT / correction).exists():
            raise AssertionError(
                f"{rule_id}: correction_record does not exist: {correction}"
            )

    return notes


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries = registry.get("entries")
    if not isinstance(entries, list) or not entries:
        raise AssertionError("registry.entries must be a non-empty list")

    seen: set[str] = set()
    notes: list[str] = []
    for entry in entries:
        rule_id = entry.get("rule_id")
        if rule_id in seen:
            raise AssertionError(f"duplicate rule_id: {rule_id}")
        seen.add(rule_id)
        notes.extend(check_entry(entry))

    print(
        json.dumps(
            {
                "status": "PASS",
                "entries_checked": len(entries),
                "rule_ids": sorted(seen),
                "notes": notes,
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
