"""P17 — Read-only Evidence Passport export for MCP / A2A consumers (schema lemon.passport/1.0).

There is deliberately NO import path: external agents can read passports but can never
set a gate, a status or a human disposition.
"""
from __future__ import annotations

import json
from typing import Any

from .passport import EvidencePassport

SCHEMA_ID = "lemon.passport/1.0"
REQUIRED = {
    "schema_version": str, "passport_id": str, "case_id": str, "created_at": str, "entity": str,
    "period_end": str, "question": str, "evidence": list, "scope": dict, "hypothesis": dict, "support": dict,
    "review": dict, "falsification": dict, "repro": dict, "content_hash": str, "final_status": str,
}
FINAL_STATUSES = {"BLOCKED", "INVALIDATED", "AWAITING_HUMAN_APPROVAL", "APPROVED", "APPROVED_WITH_CONDITIONS",
                  "REJECTED", "RETURNED_FOR_MORE_EVIDENCE", "ESCALATED"}
EVIDENCE_KEYS = {"evidence_id", "source", "source_type", "tier", "provenance", "rights", "version", "sha256",
                 "retrieved_at"}


def export_passport(pp: EvidencePassport) -> str:
    """Returns an immutable JSON string. Consumers get a copy, never the live object."""
    return pp.to_json()


def validate_passport_json(doc: Any) -> list[str]:
    errs = []
    if not isinstance(doc, dict):
        return ["passport must be a JSON object"]
    for k, t in REQUIRED.items():
        if k not in doc:
            errs.append(f"missing {k}")
        elif not isinstance(doc[k], t):
            errs.append(f"{k} must be {t.__name__}")
    if doc.get("schema_version") not in (None, SCHEMA_ID) and "schema_version" in doc:
        errs.append(f"schema_version must be {SCHEMA_ID}")
    if "final_status" in doc and doc["final_status"] not in FINAL_STATUSES:
        errs.append("invalid final_status")
    for i, ev in enumerate(doc.get("evidence", []) or []):
        if not isinstance(ev, dict) or set(ev) != EVIDENCE_KEYS:
            errs.append(f"evidence[{i}] has wrong keys")
    if isinstance(doc.get("review"), dict) and "independence" not in doc["review"]:
        errs.append("review.independence missing")
    return errs


def parse_exported(s: str) -> dict:
    d = json.loads(s)
    errs = validate_passport_json(d)
    if errs:
        raise ValueError(f"invalid passport export: {errs}")
    return d
