from ifrs_value_os import DecisionCase, IFRSValueOrchestrator, RiskLevel


def test_high_risk_case_is_challenged_and_human_gated():
    case = DecisionCase(
        case_id="IFRS15-001",
        standard="IFRS15",
        question="Determine the defensible recognition pattern for a complex revenue arrangement.",
        risk=RiskLevel.HIGH,
    )

    result = IFRSValueOrchestrator().run(case)

    assert result.requires_human_approval is True
    assert len(result.hypotheses) >= 2
    assert all(h.challenges for h in result.hypotheses)
    assert result.selected_hypothesis is not None
    assert "adversarial:challenged_all" in result.audit_trail
