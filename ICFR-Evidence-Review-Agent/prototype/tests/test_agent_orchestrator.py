import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent_contract import AIReview
from agent_orchestrator import orchestrate_review
from icfr_engine import ControlInput
from providers import StaticReviewProvider

def _control():
    return ControlInput(
        control_id="REV-01",
        objective="Monthly revenue reconciliation is independently reviewed.",
        required_evidence=["reconciliation", "reviewer sign-off", "period"],
        evidence_text="Monthly revenue reconciliation for period FY2026. Reviewer sign-off completed.",
        period="FY2026",
    )

def test_ai_can_never_approve():
    primary = StaticReviewProvider(
        AIReview(
            provider="test",
            model="test-primary",
            evidence_sufficiency="SUFFICIENT",
            risk_triage="LOW",
            evidence_basis=["revenue reconciliation"],
            can_approve=True,
        )
    )
    result = orchestrate_review(_control(), primary_provider=primary)

    assert result["human_gate"]["approved"] is False
    assert result["human_gate"]["decision"] == "PENDING"
    assert result["final_professional_conclusion"] is None
    assert result["primary_ai"]["normalized_review"]["can_approve"] is False
    assert result["cross_model"]["requires_escalation"] is True

def test_unsupported_evidence_basis_is_flagged():
    primary = StaticReviewProvider(
        AIReview(
            provider="test",
            model="test-primary",
            evidence_sufficiency="PARTIAL",
            risk_triage="MEDIUM",
            evidence_basis=["CFO signed the exception"],
        )
    )
    result = orchestrate_review(_control(), primary_provider=primary)

    assert result["primary_ai"]["valid"] is False
    assert result["primary_ai"]["unsupported_evidence_basis"]
    assert result["cross_model"]["requires_escalation"] is True

def test_cross_model_disagreement_escalates():
    primary = StaticReviewProvider(
        AIReview(
            provider="provider-a",
            model="model-a",
            evidence_sufficiency="SUFFICIENT",
            risk_triage="LOW",
            evidence_basis=["reviewer sign-off"],
        )
    )
    challenger = StaticReviewProvider(
        AIReview(
            provider="provider-b",
            model="model-b",
            evidence_sufficiency="PARTIAL",
            risk_triage="MEDIUM",
            evidence_basis=["reviewer sign-off"],
        )
    )
    result = orchestrate_review(
        _control(),
        primary_provider=primary,
        challenger_provider=challenger,
    )

    assert result["cross_model"]["disagreement"] is True
    assert result["cross_model"]["requires_escalation"] is True
