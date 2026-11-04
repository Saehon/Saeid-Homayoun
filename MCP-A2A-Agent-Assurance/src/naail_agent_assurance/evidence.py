"""Minimal, dependency-free Evidence Passport validation."""

from __future__ import annotations

import hashlib
import json
from typing import Any

ALLOWED_STATES = {"VERIFIED", "REPLICATED", "INFERRED", "UNRESOLVED", "FALSIFIED", "DRAFT"}
APPROVAL_STATES = {"pending", "approved", "rejected", "not_required"}


def _canonical_payload(passport: dict[str, Any]) -> bytes:
    payload = dict(passport)
    payload.pop("content_sha256", None)
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def compute_content_hash(passport: dict[str, Any]) -> str:
    """Return SHA-256 over the canonical passport excluding content_sha256."""
    return hashlib.sha256(_canonical_payload(passport)).hexdigest()


def validate_passport(passport: dict[str, Any], *, verify_hash: bool = True) -> list[str]:
    """Return validation errors. An empty list means the minimum contract passes."""
    errors: list[str] = []
    required = {
        "schema_version", "passport_id", "created_at", "task", "generator",
        "sources", "claims", "calculations", "reviews", "conflicts",
        "human_approval", "final_status", "content_sha256",
    }
    missing = sorted(required - set(passport))
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
        return errors

    if passport["schema_version"] != "0.1":
        errors.append("schema_version must be 0.1")
    if not isinstance(passport["passport_id"], str) or not passport["passport_id"].strip():
        errors.append("passport_id must be a non-empty string")

    task = passport.get("task")
    if not isinstance(task, dict) or not all(task.get(k) for k in ("task_id", "description", "risk_level")):
        errors.append("task must contain task_id, description and risk_level")
    elif task["risk_level"] not in {"low", "medium", "high", "critical"}:
        errors.append("task.risk_level is invalid")

    generator = passport.get("generator")
    if not isinstance(generator, dict) or not all(generator.get(k) for k in ("agent_id", "provider", "model", "version")):
        errors.append("generator must contain agent_id, provider, model and version")

    sources = passport.get("sources")
    if not isinstance(sources, list):
        errors.append("sources must be a list")
        sources = []
    source_ids = set()
    for i, source in enumerate(sources):
        if not isinstance(source, dict) or not all(source.get(k) for k in ("source_id", "uri", "retrieved_at")):
            errors.append(f"sources[{i}] must contain source_id, uri and retrieved_at")
        else:
            source_ids.add(source["source_id"])

    claims = passport.get("claims")
    if not isinstance(claims, list):
        errors.append("claims must be a list")
        claims = []
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"claims[{i}] must be an object")
            continue
        if claim.get("status") not in ALLOWED_STATES:
            errors.append(f"claims[{i}].status is invalid")
        refs = claim.get("evidence_refs")
        if not isinstance(refs, list):
            errors.append(f"claims[{i}].evidence_refs must be a list")
        else:
            unknown = sorted(set(refs) - source_ids)
            if unknown:
                errors.append(f"claims[{i}] references unknown evidence: {', '.join(unknown)}")

    if passport.get("final_status") not in ALLOWED_STATES:
        errors.append("final_status is invalid")

    approval = passport.get("human_approval")
    if not isinstance(approval, dict) or not isinstance(approval.get("required"), bool):
        errors.append("human_approval.required must be boolean")
    elif approval.get("status") not in APPROVAL_STATES:
        errors.append("human_approval.status is invalid")
    elif approval["required"] and approval["status"] == "not_required":
        errors.append("human approval cannot be not_required when required=true")

    digest = passport.get("content_sha256")
    if not isinstance(digest, str) or len(digest) != 64:
        errors.append("content_sha256 must be a 64-character SHA-256 hex digest")
    elif verify_hash and digest != compute_content_hash(passport):
        errors.append("content_sha256 does not match canonical passport content")

    return errors
