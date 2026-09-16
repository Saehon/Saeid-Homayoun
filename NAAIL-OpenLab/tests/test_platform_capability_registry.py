import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "NAAIL-OpenLab" / "architecture" / "platform_capability_registry.json"

EXPECTED_BRAND = "Next-Generation Accounting, Audit & Assurance Intelligence Lab"
EXPECTED_DESCRIPTOR = (
    "A Global Evidence-Governed Multi-Agent Digital Twin Platform for Accounting, "
    "Audit, Finance, Sustainability and Scientific Discovery"
)
ALLOWED_STATUSES = {
    "EXECUTED_VALIDATED",
    "IMPLEMENTED_EXECUTION_GATED",
    "ARCHITECTURE_ADOPTED",
    "REGISTRY_ADOPTED",
    "RESEARCH_PROTOTYPE",
    "PUBLIC_EDUCATION_DESIGN",
    "REFERENCE_ONLY",
}


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_registry_exists_and_brand_is_canonical():
    assert REGISTRY.exists()
    data = load_registry()
    platform = data["platform"]
    assert platform["master_brand"] == "NAAIL OpenLab™"
    assert platform["lab_name"] == EXPECTED_BRAND
    assert platform["descriptor"] == EXPECTED_DESCRIPTOR
    assert platform["knowledge_rag_core"] == "KRG2026.3"


def test_status_vocabulary_is_closed_and_used_consistently():
    data = load_registry()
    assert set(data["status_vocabulary"]) == ALLOWED_STATUSES
    capabilities = data["capabilities"]
    assert capabilities
    assert all(item["status"] in ALLOWED_STATUSES for item in capabilities)
    ids = [item["id"] for item in capabilities]
    assert len(ids) == len(set(ids)), "Capability IDs must be unique"


def test_all_registered_paths_exist():
    data = load_registry()
    missing = []
    for item in data["capabilities"]:
        path = ROOT / item["path"]
        if not path.exists():
            missing.append(item["path"])
    assert not missing, f"Registered capability paths missing: {missing}"


def test_execution_claim_is_narrow():
    data = load_registry()
    executed = [c for c in data["capabilities"] if c["status"] == "EXECUTED_VALIDATED"]
    assert len(executed) == 1
    assert executed[0]["id"] == "prototype_003"
    assert "synthetic" in executed[0].get("scope", "").lower()


def test_permanent_invariants():
    inv = load_registry()["invariants"]
    assert inv["architecture_documented_equals_runtime_executed"] is False
    assert inv["registry_entry_equals_dependency_installed"] is False
    assert inv["provider_name_equals_provider_run"] is False
    assert inv["external_repo_is_authoritative_truth"] is False
    assert inv["technology_core_may_rewrite_knowledge_core"] is False
    assert inv["agent_consensus_is_scientific_truth"] is False
    assert inv["optimize_for_p_value"] is False
    assert inv["human_gate_required"] is True
