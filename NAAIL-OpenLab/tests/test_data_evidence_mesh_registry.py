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
    "OWID_CO2_ENERGY",
    "OPENALEX",
    "OPENSANCTIONS",
    "OPENBB_OPTIONAL",
}


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_mesh_public_files_exist():
    assert REGISTRY.exists()
    assert MESH_DOC.exists()
    assert TWIN_DOC.exists()


def test_mesh_public_registry_is_patent_hold_and_not_core():
    registry = load_registry()
    assert registry["status"] == "PATENT_HOLD_NON_ENABLING"
    assert registry["permanent_core_count"] == 2
    assert registry["is_permanent_core"] is False
    assert registry["patent_hold"]["implementation_details_private_pending_filing_review"] is True
    assert registry["patent_hold"]["detailed_provenance_schema_public"] is False
    assert registry["patent_hold"]["routing_algorithm_public"] is False


def test_required_public_source_families_are_named_without_enabling_contracts():
    registry = load_registry()
    source_ids = {source["id"] for source in registry["public_source_families"]}
    assert REQUIRED_SOURCE_IDS.issubset(source_ids)
    assert registry["storage_policy"]["store_large_third_party_datasets_in_github"] is False
    assert registry["storage_policy"]["store_credentials_in_repository"] is False
    assert registry["storage_policy"]["preserve_third_party_rights"] is True
