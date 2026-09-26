from icfr_engine import ControlInput, review_control


def test_complete_evidence_requires_human_gate():
    result = review_control(
        ControlInput(
            control_id="C1",
            objective="Monthly reconciliation is reviewed.",
            required_evidence=["reconciliation", "reviewer sign-off"],
            evidence_text="Revenue reconciliation with reviewer sign-off.",
            period="FY2026",
        )
    )
    assert result["primary_review"]["coverage"] == 1.0
    assert result["primary_review"]["status"] == "READY_FOR_HUMAN_REVIEW"
    assert result["evidence_passport"]["human_gate"]["approved"] is False
    assert result["final_professional_conclusion"] is None


def test_missing_evidence_is_flagged():
    result = review_control(
        ControlInput(
            control_id="C2",
            objective="Evidence test",
            required_evidence=["reconciliation", "reviewer sign-off", "period"],
            evidence_text="Revenue reconciliation only.",
        )
    )
    assert result["primary_review"]["coverage"] < 1.0
    assert result["primary_review"]["missing_requirements"]
    assert result["independent_challenge"]["requires_escalation"] is True


def test_empty_evidence_is_high_risk():
    result = review_control(
        ControlInput(
            control_id="C3",
            objective="Evidence test",
            required_evidence=["approval"],
            evidence_text="",
        )
    )
    assert result["primary_review"]["status"] == "NO_EVIDENCE"
    assert result["primary_review"]["risk_triage"] == "HIGH"
