from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def canonical_payload(record: dict) -> str:
    payload = {k: v for k, v in record.items() if k != "content_sha256"}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def compute_hash(record: dict) -> str:
    return hashlib.sha256(canonical_payload(record).encode("utf-8")).hexdigest()


def validate_basic(record: dict) -> list[str]:
    errors: list[str] = []
    required = [
        "task_id", "run_id", "sender", "receiver", "claim", "evidence", "method",
        "assumptions", "confidence", "contradictions", "failure_status", "provenance",
        "required_next_action", "content_sha256",
    ]
    for key in required:
        if key not in record:
            errors.append(f"missing required field: {key}")

    confidence = record.get("confidence")
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
        errors.append("confidence must be a number between 0 and 1")

    failure = record.get("failure_status", {})
    if not isinstance(failure, dict) or not isinstance(failure.get("failed"), bool) or not isinstance(failure.get("reasons"), list):
        errors.append("failure_status must contain boolean failed and list reasons")

    provenance = record.get("provenance", {})
    for key in ("model_or_tool", "version", "timestamp_utc"):
        if not isinstance(provenance, dict) or not provenance.get(key):
            errors.append(f"provenance missing required field: {key}")

    expected = record.get("content_sha256")
    actual = compute_hash(record)
    if expected != actual:
        errors.append(f"content_sha256 mismatch: expected {expected}, computed {actual}")

    if record.get("sender") == record.get("receiver"):
        errors.append("sender and receiver must be different roles")

    return errors


def validate_schema(record: dict, schema: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []

    validator = jsonschema.Draft202012Validator(schema)
    return [f"schema: {e.message}" for e in sorted(validator.iter_errors(record), key=lambda e: list(e.path))]


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate an ECONOVA-S AI-to-AI scientific handoff.")
    ap.add_argument("handoff", nargs="?", default="automation/sample_handoff.json")
    ap.add_argument("--schema", default="automation/ai_handoff.schema.json")
    args = ap.parse_args()

    record = json.loads(Path(args.handoff).read_text(encoding="utf-8"))
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))

    errors = validate_basic(record) + validate_schema(record, schema)
    if errors:
        print("AI-to-AI handoff validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AI-to-AI handoff validation PASSED")
    print(f"task_id={record['task_id']}")
    print(f"sender={record['sender']} -> receiver={record['receiver']}")
    print(f"content_sha256={record['content_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
