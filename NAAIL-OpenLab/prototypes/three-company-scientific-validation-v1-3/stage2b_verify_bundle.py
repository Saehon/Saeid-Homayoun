#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir", type=Path)
    args = ap.parse_args()
    d = args.run_dir

    errors = []
    warnings = []

    manifest = d / "run_manifest.json"
    index_file = d / "response_freeze_index.json"
    if not manifest.exists():
        errors.append("run_manifest.json missing")
    if not index_file.exists():
        errors.append("response_freeze_index.json missing")

    m = {}
    index = []
    if manifest.exists():
        m = json.loads(manifest.read_text(encoding="utf-8"))
        if m.get("scoring_opened") is not False:
            errors.append("scoring_opened must be false before Stage 2C")
        if m.get("gold_key_access") != "NOT_AVAILABLE_TO_RUNNER":
            errors.append("gold_key_access is not locked")
        if m.get("task_count") != 21:
            errors.append(f"manifest task_count is {m.get('task_count')}, expected 21")
        sha_file = d / "run_manifest.sha256"
        if not sha_file.exists():
            errors.append("run_manifest.sha256 missing")
        else:
            registered = sha_file.read_text(encoding="utf-8").split()[0].strip()
            actual = sha256(manifest)
            if registered != actual:
                errors.append("run_manifest SHA-256 mismatch")

    if index_file.exists():
        index = json.loads(index_file.read_text(encoding="utf-8"))
        if len(index) != 21:
            errors.append(f"freeze index contains {len(index)} records, expected 21")
        seen = set()
        for rec in index:
            tid = str(rec.get("task_id"))
            if tid in seen:
                errors.append(f"duplicate task in freeze index: {tid}")
            seen.add(tid)
            artifact = d / str(rec.get("response_artifact", ""))
            if not artifact.exists():
                errors.append(f"missing response artifact for task {tid}")
                continue
            actual = sha256(artifact)
            if actual != rec.get("response_sha256"):
                errors.append(f"response SHA-256 mismatch for task {tid}")
            sidecar = d / f"{tid}.sha256"
            if not sidecar.exists():
                errors.append(f"missing SHA sidecar for task {tid}")
            else:
                registered = sidecar.read_text(encoding="utf-8").split()[0].strip()
                if registered != actual:
                    errors.append(f"SHA sidecar mismatch for task {tid}")

    names = [p.name.lower() for p in d.iterdir()] if d.exists() else []
    for name in names:
        if "gold" in name or "rubric" in name or "answer_key" in name:
            errors.append(f"forbidden scoring/gold artifact found in run directory: {name}")

    if m and index_file.exists():
        actual_index_hash = sha256(index_file)
        if m.get("response_freeze_index_sha256") != actual_index_hash:
            errors.append("response_freeze_index SHA-256 mismatch")

    result = {
        "run_dir": str(d),
        "candidate_id": m.get("candidate_id"),
        "model": m.get("model"),
        "run_status": m.get("run_status"),
        "executed_count": m.get("executed_count"),
        "failed_count": m.get("failed_count"),
        "response_records": len(index),
        "scoring_opened": m.get("scoring_opened"),
        "errors": errors,
        "warnings": warnings,
        "freeze_bundle_valid": not errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
