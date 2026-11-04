"""A fail-closed, opt-in handoff from NAAIL synthetic Decision-1 pilot into LEMON.

This is NOT an autonomous reviewer or a new approval pathway.
"""
from __future__ import annotations

from lemon_icfr.models import EvidenceItem
from lemon_icfr.orchestrator import LemonOrchestrator

PILOT_GATE = "AWAITING_INDEPENDENT_HUMAN_APPROVAL"

def build_submission(case: dict, triage: dict) -> dict:
    """Convert research triage to a Lemon evidence submission; keep reviewer separate."""
    if case.get("data_class") != "SYNTHETIC" or triage.get("data_class") != "SYNTHETIC":
        raise ValueError("Synthetic-only pilot boundary")
    if triage.get("case_id") != case.get("case_id"):
        raise ValueError("Case IDs differ")
    if triage.get("approved") is not False or triage.get("human_gate") != PILOT_GATE:
        raise ValueError("Cannot import approved or ungated candidate conclusions")
    if triage.get("evidence_status") != "COMPLETE":
        raise ValueError("Unverified evidence; review outside scoring pipeline")
    raw = case.get("evidence", [])
    ids = [e.get("evidence_id") for e in raw]
    if not ids or len(set(ids)) != len(ids) or ids != triage.get("evidence_ids"):
        raise ValueError("Evidence IDs mismatch")
    if any(not str(e.get("source_uri","")).startswith("synthetic://") or not e.get("fact")
           or e.get("contradicts") for e in raw):
        raise ValueError("Missing or contradictory evidence")
    risk = triage.get("model_prediction")
    if risk not in ("HIGH", "MODERATE", "LOW"):
        raise ValueError("No classifiable risk hypothesis")
    evidence = [
        EvidenceItem(
            evidence_id=e["evidence_id"],
            source="NAAIL synthetic fixture",
            provenance=e["source_uri"],
            rights_status="SYNTHETIC_RESEARCH_ONLY",
            content=e["fact"],
            version=triage.get("version"),
        ) for e in raw
    ]
    return {
        "case_id":case["case_id"],
        "question":f"Evaluate evidence independently; provisional AI ICFR triage class={risk}. Do not treat it as a material weakness conclusion.",
        "evidence":evidence,
        "triage_metadata":{
            "provider":triage.get("provider"),
            "candidate_state_sha256":triage.get("candidate_state_sha256"),
            "confidence":triage.get("confidence"),
            "review_queue":triage.get("review_queue"),
        },
    }

def run_independent_lemon_review(
    case: dict, triage: dict, *, independent_provider,
    coso_context_supplied: bool, reproducibility_ref: str
):
    """Caller supplies a separately controlled reviewer; Lemon retains every gate."""
    if independent_provider is None or not callable(getattr(independent_provider,"challenge_claim",None)):
        raise ValueError("Independent review provider required")
    if getattr(independent_provider,"name",None) in (None, "", triage.get("provider")):
        raise ValueError("Reviewer identity cannot equal the decision scorer")
    submission = build_submission(case, triage)
    return LemonOrchestrator().run(
        case_id=submission["case_id"],
        question=submission["question"],
        evidence=submission["evidence"],
        provider=independent_provider,
        coso_context_supplied=coso_context_supplied,
        reproducibility_ref=reproducibility_ref,
    )
