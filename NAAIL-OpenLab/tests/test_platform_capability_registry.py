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
    "PATENT_HOLD_NON_ENABLING",
}


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_registry_exists_and_brand_is_canonical():
    data = load_registry()
    platform = data["platform"]
    assert platform["master_brand"] == "NAAIL OpenLab™"
    assert platform["lab_name"] == EXPECTED_BRAND
    assert platform["descriptor"] == EXPECTED_DESCRIPTOR
    assert platform["permanent_core_count"] == 2
    assert platform["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert "PATENT APPLICATION PREPARATION IN PROGRESS" in platform["public_ip_status"]


def test_status_vocabulary_is_closed_and_used_consistently():
    data = load_registry()
    assert set(data["status_vocabulary"]) == ALLOWED_STATUSES
    assert data["capabilities"]
    assert all(item["status"] in ALLOWED_STATUSES for item in data["capabilities"])
    ids = [item["id"] for item in data["capabilities"]]
    assert len(ids) == len(set(ids))


def test_all_registered_paths_exist():
    missing = []
    for item in load_registry()["capabilities"]:
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


def test_patent_sensitive_capabilities_are_currently_non_enabling():
    by_id = {item["id"]: item for item in load_registry()["capabilities"]}
    for cap_id in {
        "master_hierarchy",
        "data_evidence_mesh",
        "business_school_simulation_layer",
        "decision_consequence_engine",
        "professional_judgment_passport",
        "audit_accounting_dynamic_twin",
        "vera",
    }:
        assert by_id[cap_id]["status"] == "PATENT_HOLD_NON_ENABLING"


def test_patent_first_invariants():
    inv = load_registry()["invariants"]
    assert inv["permanent_core_count"] == 2
    assert inv["technology_core_may_rewrite_knowledge_core"] is False
    assert inv["new_enabling_patent_sensitive_details_public_before_filing_review"] is False
    assert inv["patent_pending_claimed_before_confirmed_filing"] is False
    assert inv["human_gate_required"] is True
