import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "finance_open_source_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_frozen_core_boundary():
    data = load_registry()
    assert data["knowledge_rag_core_version"] == "KRG2026.3"
    boundary = data["boundary"]
    assert boundary["finance_tool_may_modify_knowledge_rag_core"] is False
    assert boundary["human_gate_required"] is True


def test_data_rights_are_separate_from_software_license():
    data = load_registry()
    boundary = data["boundary"]
    assert boundary["software_license_equals_data_license"] is False
    assert boundary["free_access_equals_free_redistribution"] is False


def test_no_vendor_rating_claims():
    data = load_registry()
    assert data["boundary"]["research_score_equals_external_credit_rating"] is False
    claims = set(data["prohibited_claims"])
    assert "naail_is_bloomberg" in claims
    assert "naail_is_sp_global" in claims
    assert "naail_scores_are_sp_moodys_or_fitch_ratings" in claims


def test_no_third_party_code_claimed_vendored_or_executed():
    data = load_registry()
    for project in data["projects"]:
        assert project["third_party_code_vendored"] is False
        assert project["runtime_executed"] is False


def test_openbb_is_isolated_for_agpl():
    data = load_registry()
    openbb = next(p for p in data["projects"] if p["name"] == "OpenBB")
    assert openbb["license"] == "AGPL-3.0"
    assert openbb["state"] == "REFERENCE_ISOLATED_AGPL"


def test_expected_finance_projects_present():
    data = load_registry()
    names = {p["name"] for p in data["projects"]}
    required = {
        "OpenBB",
        "FinanceToolkit",
        "FinanceDatabase",
        "yfinance",
        "QuantLib",
        "FinRL",
        "PyPortfolioOpt",
        "Riskfolio-Lib",
    }
    assert required.issubset(names)


def test_promotion_gates_include_rights_and_oos():
    gates = set(load_registry()["promotion_gates"])
    assert "software_license_review" in gates
    assert "separate_data_terms_review" in gates
    assert "out_of_sample_validation" in gates
    assert "knowledge_rag_core_boundary_test" in gates
    assert "human_architecture_gate" in gates
