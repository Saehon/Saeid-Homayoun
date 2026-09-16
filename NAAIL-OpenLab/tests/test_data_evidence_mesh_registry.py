import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "NAAIL-OpenLab" / "architecture" / "data_evidence_mesh_registry.json"
MESH_DOC = ROOT / "NAAIL-OpenLab" / "DATA_EVIDENCE_MESH.md"
TWIN_DOC = ROOT / "NAAIL-OpenLab" / "digital-twins" / "audit-accounting" / "README.md"

REQUIRED_SOURCE_IDS = {
    "SEC_EDGAR_XBRL",
    "FRED_ALFRED",
    "FAMA_FRENCH",
    "WORLD_BANK",
    "OWID_CO2",
    "OWID_ENERGY",
    "OPENALEX",
    "OPENSANCTIONS",
    "OPENBB_OPTIONAL",
}


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def test_mesh_files_exist():
    assert REGISTRY.exists()
    assert MESH_DOC.exists()
    assert TWIN_DOC.exists()


def test_mesh_preserves_two_core_architecture():
    registry = load_registry()
    assert registry["permanent_core_count"] == 2
    assert registry["is_permanent_core"] is False
    assert registry["invariants"]["data_evidence_mesh_is_core"] is False
    assert registry["invariants"]["technology_core_may_rewrite_knowledge_core"] is False


def test_required_sources_are_registered():
    registry = load_registry()
    source_ids = {source["id"] for source in registry["sources"]}
    assert REQUIRED_SOURCE_IDS.issubset(source_ids)


def test_large_dataset_storage_is_prohibited():
    registry = load_registry()
    assert registry["storage_policy"]["store_large_third_party_datasets_in_github"] is False
    assert registry["storage_policy"]["secrets_in_repository"] is False
    assert registry["invariants"]["large_third_party_dataset_should_be_committed_to_github"] is False


def test_provenance_and_versioning_are_required():
    registry = load_registry()
    required = set(registry["required_evidence_passport_fields"])
    for field in {
        "source_id",
        "source_url_or_endpoint",
        "retrieved_at_utc",
        "source_version_or_period",
        "query_or_request_parameters",
        "raw_hash_or_response_hash",
        "transformation_chain",
        "license_or_terms_status",
        "validation_status",
        "human_reviewer",
    }:
        assert field in required


def test_sensitive_boundaries_fail_closed():
    registry = load_registry()
    inv = registry["invariants"]
    assert inv["connector_name_implies_execution"] is False
    assert inv["api_response_is_authoritative_interpretation"] is False
    assert inv["public_access_equals_unrestricted_redistribution"] is False
    assert inv["openbb_provider_equals_original_source"] is False
    assert inv["opensanctions_match_equals_legal_determination"] is False
    assert inv["openalex_metadata_proves_research_claim"] is False
    assert inv["human_gate_required"] is True
