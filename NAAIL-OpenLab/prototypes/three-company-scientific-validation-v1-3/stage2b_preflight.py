#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path

CANDIDATES = {
    "C01": ("OpenAI", "gpt-6-astra", "OPENAI_API_KEY", "openai"),
    "C02": ("Google", "gemini-3.8-flash", "GEMINI_API_KEY", "google-genai"),
    "C03": ("Anthropic", "claude-fable-5", "ANTHROPIC_API_KEY", "anthropic"),
}

FORBIDDEN_KEYS = {
    "answer", "answers", "gold", "gold_key", "gold_answer",
    "expected_answer", "reference_answer", "rubric", "scoring_rubric", "score_key"
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pkg_version(name: str):
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def validate_tasks(path: Path):
    tasks = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        obj = json.loads(line)
        if not obj.get("task_id") or not obj.get("prompt"):
            raise ValueError(f"Line {n}: task_id and prompt are required")
        leaked = FORBIDDEN_KEYS.intersection({str(k).lower() for k in obj})
        if leaked:
            raise ValueError(f"Line {n}: forbidden blind-evaluation fields: {sorted(leaked)}")
        tasks.append(obj)
    ids = [str(t["task_id"]) for t in tasks]
    if len(tasks) != 21:
        raise ValueError(f"Expected 21 tasks, found {len(tasks)}")
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task IDs found")
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", choices=sorted(CANDIDATES), required=True)
    ap.add_argument("--tasks", type=Path, required=True)
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--expected-tasks-sha256")
    ap.add_argument("--expected-evidence-sha256")
    ap.add_argument("--require-key", action="store_true")
    args = ap.parse_args()

    provider, model, env_name, package = CANDIDATES[args.candidate]
    errors = []
    warnings = []

    for label, path in (("tasks", args.tasks), ("evidence", args.evidence)):
        if not path.exists() or not path.is_file():
            errors.append(f"{label} file missing: {path}")
        if "gold_key" in str(path).lower() or "gold-key" in str(path).lower():
            errors.append(f"{label} path appears to reference a gold-key artifact")

    task_ids = []
    tasks_hash = evidence_hash = None
    if args.tasks.exists():
        try:
            task_ids = validate_tasks(args.tasks)
            tasks_hash = sha256(args.tasks)
        except Exception as e:
            errors.append(f"task packet validation failed: {e}")
    if args.evidence.exists():
        evidence_hash = sha256(args.evidence)

    if args.expected_tasks_sha256 and tasks_hash != args.expected_tasks_sha256.lower():
        errors.append("task packet SHA-256 mismatch")
    if args.expected_evidence_sha256 and evidence_hash != args.expected_evidence_sha256.lower():
        errors.append("evidence packet SHA-256 mismatch")

    if args.require_key and not os.getenv(env_name):
        errors.append(f"missing environment variable {env_name}")
    elif not os.getenv(env_name):
        warnings.append(f"{env_name} not set; dry-run only")

    if args.output_dir.exists():
        warnings.append("output directory already exists; runner creates a new timestamped subdirectory")
    for parent in [args.output_dir.resolve(), *args.output_dir.resolve().parents]:
        if (parent / ".git").exists():
            errors.append("output directory is inside a Git worktree; use a private path outside the repo")
            break

    version = pkg_version(package)
    if version is None:
        warnings.append(f"SDK package not installed: {package}")

    result = {
        "candidate_id": args.candidate,
        "provider": provider,
        "model": model,
        "task_count": len(task_ids),
        "tasks_sha256": tasks_hash,
        "evidence_sha256": evidence_hash,
        "sdk_package": package,
        "sdk_version": version,
        "api_key_env": env_name,
        "api_key_present": bool(os.getenv(env_name)),
        "gold_key_access": "NOT_CHECKED_OR_LOADED",
        "scoring_opened": False,
        "errors": errors,
        "warnings": warnings,
        "ready_for_live_run": not errors and (bool(os.getenv(env_name)) if args.require_key else True),
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
