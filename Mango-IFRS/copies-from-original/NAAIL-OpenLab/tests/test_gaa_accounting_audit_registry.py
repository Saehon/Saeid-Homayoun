import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "knowledge" / "accounting_audit_free_evidence_registry.json"


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_gaa_is_not_in_knowledge_core():
    data = load_registry()
    rules = data["boundary_rules"]
    assert rules["gaa_belongs_to_technology_core"] is True
    assert rules["gaa_may_modify_knowledge_rag_core"] is False
    assert rules["evidence_sources_belong_to_knowledge_rag_core"] is True


def test_human_gate_is_required():
    data = load_registry()
    assert data["boundary_rules"]["human_gate_required"] is True
    assert "Human Gate" in data["required_controls"]


def test_required_public_evidence_sources_exist():
    data = load_registry()
    ids = {source["id"] for source in data["sources"]}
    required = {"SEC_EDGAR_XBRL", "SEC_AAER", "PCAOB_INSPECTIONS", "PCAOB_AS_3101"}
    assert required.issubset(ids)


def test_all_sources_have_public_urls_and_states():
    data = load_registry()
    for source in data["sources"]:
        assert source["url"].startswith("https://")
        assert source["adoption_state"].startswith("ADOPT_")
        assert source["primary_uses"]
        assert source["authority_type"]


def test_technology_references_are_not_knowledge_authorities():
    data = load_registry()
    for ref in data["technology_references"]:
        assert ref["knowledge_authority"] is False


def test_benchmark_families_cover_core_accounting_audit_use_cases():
    data = load_registry()
    expected = {
        "revenue_recognition_cutoff",
        "accounting_fraud_misstatement",
        "pcaob_audit_deficiency",
        "cam_as3101_challenge",
        "icfr_deficiency_challenge",
    }
    assert expected.issubset(set(data["benchmark_families"]))
