from __future__ import annotations

import hashlib
import json
import re
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


_PERIOD_PATTERN = re.compile(
    r"\\b(?:q[1-4]\\s*fy?\\s*20\\d{2}|fy\\s*20\\d{2}|20\\d{2}[-/](?:0?[1-9]|1[0-2]))\\b",
    re.IGNORECASE,
)

_PROMPT_INJECTION_MARKERS = (
    "ignore previous instructions",
    "ignore all previous instructions",
    "system prompt",
    "developer message",
    "you are chatgpt",
    "override the instructions",
    "do not follow the instructions",
    "assistant:",
)

_STALE_MARKERS = (
    "stale evidence",
    "outdated",
    "expired",
    "superseded",
    "prior-year evidence",
    "previous-period evidence",
)

_CONCLUSION_MARKERS = (
    "control is effective",
    "no exception exists",
    "evidence is sufficient",
    "automatically approve",
)


def _normalized_nonempty_lines(text: str) -> list[str]:
    return [
        " ".join(line.lower().split())
        for line in text.splitlines()
        if len(" ".join(line.split())) >= 20
    ]


def _detect_duplicate_evidence(text: str) -> bool:
    lines = _normalized_nonempty_lines(text)
    return len(lines) != len(set(lines))


def _detect_period_mismatch(control_period: str, evidence_text: str) -> bool:
    expected = " ".join(control_period.lower().split())
    if not expected:
        return False
    normalized_evidence = " ".join(evidence_text.lower().split())
    if expected in normalized_evidence:
        return False
    return bool(_PERIOD_PATTERN.search(evidence_text))


def _detect_conflict(evidence_lower: str) -> bool:
    conflict_pairs = (
        ("approved", "not approved"),
        ("completed", "not completed"),
        ("reviewed", "not reviewed"),
        ("sign-off completed", "sign-off missing"),
        ("reconciled", "not reconciled"),
    )
    return any(left in evidence_lower and right in evidence_lower for left, right in conflict_pairs)


def _deterministic_flags(control: ControlInput, evidence: str) -> list[str]:
    if not evidence:
        return []

    evidence_lower = evidence.lower()
    flags: list[str] = []

    if any(marker in evidence_lower for marker in _PROMPT_INJECTION_MARKERS):
        flags.append("PROMPT_INJECTION")
    if _detect_period_mismatch(control.period, evidence):
        flags.append("PERIOD_MISMATCH")
    if any(marker in evidence_lower for marker in _STALE_MARKERS):
        flags.append("STALE_EVIDENCE")
    if _detect_conflict(evidence_lower):
        flags.append("CONFLICTING_EVIDENCE")
    if _detect_duplicate_evidence(evidence):
        flags.append("DUPLICATE_EVIDENCE")
    if any(marker in evidence_lower for marker in _CONCLUSION_MARKERS):
        flags.append("UNSUPPORTED_CONCLUSION_LANGUAGE")

    return flags


def review_control(control: ControlInput) -> dict:
    evidence = control.evidence_text.strip()
    evidence_lower = evidence.lower()

    matched = [
        item
        for item in control.required_evidence
        if item.strip() and item.lower() in evidence_lower
    ]
    missing = [item for item in control.required_evidence if item not in matched]

    total = len(control.required_evidence)
    coverage = 1.0 if total == 0 else len(matched) / total
    deterministic_flags = _deterministic_flags(control, evidence)

    high_risk_flags = {
        "PROMPT_INJECTION",
        "PERIOD_MISMATCH",
        "STALE_EVIDENCE",
        "CONFLICTING_EVIDENCE",
        "UNSUPPORTED_CONCLUSION_LANGUAGE",
    }

    if not evidence:
        status = "NO_EVIDENCE"
        risk = "HIGH"
    elif deterministic_flags:
        status = "EXCEPTION_REVIEW_REQUIRED"
        risk = "HIGH" if high_risk_flags.intersection(deterministic_flags) else "MEDIUM"
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
        "deterministic_flags": deterministic_flags,
        "limitations": [
            "Deterministic checks are triage signals, not a professional sufficiency conclusion.",
            "Keyword coverage does not establish authenticity, operating effectiveness, or management/auditor sign-off.",
        ],
    }

    challenge_flags = []
    if primary["status"] == "READY_FOR_HUMAN_REVIEW" and not evidence:
        challenge_flags.append("Primary status inconsistent with empty evidence.")
    if primary["coverage"] < 1.0:
        challenge_flags.append("At least one required evidence element is not explicitly matched.")
    if len(evidence) < 40 and evidence:
        challenge_flags.append("Evidence text is unusually short and should be inspected manually.")
    challenge_flags.extend(
        f"Deterministic signal: {flag}" for flag in deterministic_flags
    )

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    passport = {
        "control_id": control.control_id,
        "period": control.period,
        "evidence_sha256": _sha256(evidence),
        "reviewed_at_utc": now,
        "engine": "icfr-evidence-review-agent-deterministic-v1",
        "source_type": "user_supplied_text",
        "deterministic_flags": deterministic_flags,
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
