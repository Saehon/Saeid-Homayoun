import json
from pathlib import Path


REGISTRY = Path(__file__).resolve().parents[1] / "architecture" / "free_data_source_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_registry_identity_and_core_boundary():
    data = load_registry()
    assert data["registry_id"] == "NAAIL-FREE-DATA-FABRIC-2026.09"
    assert data["knowledge_rag_core_version"] == "KRG2026.3"
    boundary = data["boundary"]
    assert boundary["free_access_means_authoritative"] is False
    assert boundary["free_access_means_unrestricted_redistribution"] is False
    assert boundary["parser_output_is_authoritative"] is False
    assert boundary["technology_tool_may_modify_knowledge_rag_core"] is False
    assert boundary["provenance_required"] is True
    assert boundary["rights_review_required"] is True
    assert boundary["human_gate_required"] is True


def test_required_high_priority_sources_present():
    data = load_registry()
    ids = {source["id"] for source in data["sources"]}
    required = {
        "SEC_FIN_STATEMENTS",
        "SEC_FIN_NOTES",
        "SEC_AAER",
        "PCAOB_AUDITORSEARCH",
        "PCAOB_INSPECTIONS",
        "XBRL_FILINGS_ORG",
        "GLEIF",
        "SCB",
        "RIKSBANK",
        "BRREG",
        "WORLD_BANK",
        "CLIMATE_TRACE",
        "OPENALEX",
        "CROSSREF",
        "FAMA_FRENCH",
        "DAMODARAN",
        "FRED",
        "STANFORD_ROCK_CENTER",
    }
    assert required.issubset(ids)


def test_every_source_has_rights_and_provenance_fields():
    data = load_registry()
    for source in data["sources"]:
        assert source["url"].startswith("https://")
        assert source["rights_status"]
        assert source["redistribution_policy"]
        assert source["authority_type"]
        assert source["adoption_state"]
        assert source["primary_agents"]
        assert source["knowledge_authority"]


def test_admission_pipeline_is_governed():
    data = load_registry()
    states = data["admission_states"]
    assert states[0] == "DISCOVERED"
    assert "RIGHTS_REVIEWED" in states
    assert "PROVENANCE_VERIFIED" in states
    assert "VALIDATED" in states
    assert "ADMITTED_TO_KNOWLEDGE_RAG_CORE" in states
    assert states[-1] == "VERSIONED_OR_RETIRED"


def test_evidence_passport_minimum_fields():
    data = load_registry()
    fields = set(data["required_evidence_passport_fields"])
    required = {
        "source_id",
        "source_url",
        "retrieval_timestamp",
        "source_version_or_period",
        "raw_hash",
        "transformation_chain",
        "license_or_terms_status",
        "redistribution_status",
        "knowledge_core_admission_status",
        "validation_status",
        "human_reviewer",
    }
    assert required.issubset(fields)
