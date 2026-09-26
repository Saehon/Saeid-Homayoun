from __future__ import annotations

from dataclasses import asdict

from agent_contract import AIReview, validate_ai_review
from icfr_engine import ControlInput, review_control
from providers import ReviewProvider

def _disagreement(primary: AIReview, challenger: AIReview) -> bool:
    return (
        primary.evidence_sufficiency != challenger.evidence_sufficiency
        or primary.risk_triage != challenger.risk_triage
    )

def orchestrate_review(
    control: ControlInput,
    *,
    primary_provider: ReviewProvider | None = None,
    challenger_provider: ReviewProvider | None = None,
) -> dict:
    deterministic = review_control(control)
    result = {
        "control": asdict(control),
        "deterministic": deterministic,
        "primary_ai": None,
        "challenger_ai": None,
        "cross_model": {
            "disagreement": False,
            "requires_escalation": deterministic["independent_challenge"]["requires_escalation"],
        },
        "human_gate": {"required": True, "approved": False, "decision": "PENDING"},
        "final_professional_conclusion": None,
    }

    if primary_provider is None:
        return result

    primary = primary_provider.review(
        control=asdict(control), deterministic_result=deterministic
    )
    primary_validation = validate_ai_review(primary, control.evidence_text)
    result["primary_ai"] = primary_validation
    if not primary_validation["valid"]:
        result["cross_model"]["requires_escalation"] = True

    if challenger_provider is not None:
        challenger = challenger_provider.review(
            control=asdict(control), deterministic_result=deterministic
        )
        challenger_validation = validate_ai_review(challenger, control.evidence_text)
        result["challenger_ai"] = challenger_validation
        disagreement = _disagreement(primary, challenger)
        result["cross_model"]["disagreement"] = disagreement
        if disagreement or not challenger_validation["valid"]:
            result["cross_model"]["requires_escalation"] = True

    result["human_gate"] = {"required": True, "approved": False, "decision": "PENDING"}
    result["final_professional_conclusion"] = None
    return result
