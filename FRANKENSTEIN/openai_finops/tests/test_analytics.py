from pathlib import Path

from openai_finops.analytics import analyze_transactions


SAMPLE = (
    Path(__file__).resolve().parents[1]
    / "sample_data"
    / "transactions.csv"
)


def test_sample_data_detects_expected_control_signals():
    result = analyze_transactions(SAMPLE)
    rules = {finding.rule_id for finding in result.findings}

    assert result.row_count == 12
    assert len(result.source_sha256) == 64
    assert "DUPLICATE_ID" in rules
    assert "MISSING_APPROVER" in rules
    assert "SOD_CONFLICT" in rules
    assert "WEEKEND_POSTING" in rules
    assert "OUT_OF_HOURS" in rules
    assert "ROBUST_AMOUNT_OUTLIER" in rules
    assert "LARGE_ROUND_AMOUNT" in rules
    assert result.risk_score > 0


def test_every_finding_has_traceable_evidence_and_domain_routing():
    result = analyze_transactions(SAMPLE)
    for finding in result.findings:
        assert finding.finding_id.startswith("F-")
        assert finding.evidence
        assert finding.rationale
        assert finding.domains
        assert finding.control_objectives


def test_segregation_of_duties_routes_to_icfr_and_forensic():
    result = analyze_transactions(SAMPLE)
    sod = next(f for f in result.findings if f.rule_id == "SOD_CONFLICT")

    assert "icfr" in sod.domains
    assert "forensic" in sod.domains
    assert "finance_controls" in sod.domains
