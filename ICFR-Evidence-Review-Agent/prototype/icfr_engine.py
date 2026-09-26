from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class ControlInput:
    control_id: str
    objective: str
    required_evidence: list[str]
    evidence_text: str
    period: str = ""


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def review_control(control: ControlInput) -> dict:
    evidence = control.evidence_text.strip()
    evidence_lower = evidence.lower()

    matched = [
        item for item in control.required_evidence
        if item.strip() and item.lower() in evidence_lower
    ]
    missing = [item for item in control.required_evidence if item not in matched]

    total = len(control.required_evidence)
    coverage = 1.0 if total == 0 else len(matched) / total

    if not evidence:
        status = "NO_EVIDENCE"
        risk = "HIGH"
    elif coverage == 1.0:
        status = "READY_FOR_HUMAN_REVIEW"
        risk = "LOW"
    elif coverage >= 0.5:
        status = "EVIDENCE_GAPS"
        risk = "MEDIUM"
    else:
        status = "MATERIAL_EVIDENCE_GAPS"
        risk = "HIGH"

    primary = {
        "status": status,
        "risk_triage": risk,
        "coverage": round(coverage, 4),
        "matched_requirements": matched,
        "missing_requirements": missing,
        "limitations": [
            "Keyword coverage is a deterministic prototype check, not a professional sufficiency conclusion."
        ],
    }

    challenge_flags = []
    if primary["status"] == "READY_FOR_HUMAN_REVIEW" and not evidence:
        challenge_flags.append("Primary status inconsistent with empty evidence.")
    if primary["coverage"] < 1.0:
        challenge_flags.append("At least one required evidence element is not explicitly matched.")
    if len(evidence) < 40 and evidence:
        challenge_flags.append("Evidence text is unusually short and should be inspected manually.")

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    passport = {
        "control_id": control.control_id,
        "period": control.period,
        "evidence_sha256": _sha256(evidence),
        "reviewed_at_utc": now,
        "engine": "icfr-evidence-review-agent-deterministic-v0",
        "source_type": "user_supplied_text",
        "ai_model_used": False,
        "human_gate": {
            "required": True,
            "approved": False,
            "decision": "PENDING",
        },
    }

    return {
        "input": asdict(control),
        "primary_review": primary,
        "independent_challenge": {
            "flags": challenge_flags,
            "requires_escalation": bool(challenge_flags),
        },
        "evidence_passport": passport,
        "final_professional_conclusion": None,
    }


def to_json(result: dict) -> str:
    return json.dumps(result, indent=2, ensure_ascii=False)
