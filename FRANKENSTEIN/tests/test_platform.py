from frankenstein.agents import AGENTS
from frankenstein.orchestrator import DEFAULT_SAMPLE, run


def test_required_specialists_exist():
    domains = {a.domain for a in AGENTS}
    assert {
        "finance_controls", "internal_audit", "ifrs_reporting", "icfr", "forensic",
        "esg_assurance", "cost_finops", "operations_risk", "ai_data_governance",
    }.issubset(domains)


def test_offline_evidence_and_human_gate():
    report = run("Test controlled orchestration.", DEFAULT_SAMPLE, use_claude=False)
    assert report.deterministic_risk_score > 0
    assert report.human_review_required is True
    assert len(report.specialist_assessments) == len(AGENTS)
    assert any("DUPLICATE_ID" in x for x in report.evidence_references)
    assert any("SOD_CONFLICT" in x for x in report.evidence_references)
