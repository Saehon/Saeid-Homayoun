import json
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[1] / "architecture" / "esg_sustainability_open_source_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_core_boundary_is_preserved():
    data = load_registry()
    assert data["knowledge_rag_core_version"] == "KRG2026.3"
    assert data["core_boundary"]["may_modify_knowledge_rag_core"] is False
    assert data["core_boundary"]["human_gate_required"] is True


def test_no_external_project_is_vendored_by_default():
    data = load_registry()
    for project in data["projects"]:
        assert project["code_vendored"] is False
        assert project["runtime_executed"] is False


def test_unverified_license_projects_are_not_promoted_as_reusable_code():
    data = load_registry()
    for project in data["projects"]:
        if not project["license_verified"]:
            assert project["state"] in {
                "REFERENCE_LICENSE_REVIEW",
                "REFERENCE_DATA_RIGHTS_REVIEW",
                "ADOPT_DATA_REFERENCE_WITH_SOURCE_RIGHTS",
                "ADOPT_REFERENCE_RUNTIME_GATED",
                "SANDBOX_REFERENCE",
                "ADOPT_RESEARCH_DATA_REFERENCE",
            }


def test_standards_text_not_republished_by_default():
    data = load_registry()
    for source in data["standards_sources"]:
        if "public_replication_of_full_text_allowed_by_default" in source:
            assert source["public_replication_of_full_text_allowed_by_default"] is False


def test_scientific_invariants():
    data = load_registry()
    inv = data["invariants"]
    assert inv["public_access_equals_public_domain"] is False
    assert inv["software_license_equals_data_license"] is False
    assert inv["third_party_esg_score_equals_ground_truth"] is False
    assert inv["sdg_mapping_equals_causal_impact"] is False
    assert inv["climate_scenario_equals_forecast"] is False
    assert inv["external_repo_may_modify_knowledge_rag_core"] is False
    assert inv["human_gate_required"] is True
