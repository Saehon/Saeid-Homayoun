import json
from pathlib import Path


REGISTRY = Path(__file__).resolve().parents[1] / "architecture" / "accounting_audit_open_source_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_core_boundary_is_preserved():
    data = load_registry()
    boundary = data["boundary"]
    assert boundary["external_software_belongs_to_technology_or_ingestion_layer"] is True
    assert boundary["external_repo_may_modify_knowledge_rag_core"] is False
    assert boundary["parsed_output_requires_provenance_validation"] is True
    assert boundary["human_gate_required"] is True


def test_projects_are_external_and_non_authoritative():
    data = load_registry()
    projects = data["projects"]
    assert len(projects) >= 6
    for project in projects:
        assert project["license_verified"] is True
        assert project["license"] in {"MIT", "Apache-2.0"}
        assert project["third_party_code_vendored"] is False
        assert project["knowledge_core_authority"] is False
        assert project["repository"].startswith("https://github.com/")


def test_scientific_and_governance_invariants():
    data = load_registry()
    inv = data["invariants"]
    assert inv["external_repo_is_authoritative_accounting_truth"] is False
    assert inv["external_repo_may_rewrite_knowledge_rag_core"] is False
    assert inv["parsed_output_is_authoritative_without_validation"] is False
    assert inv["agent_generated_journal_is_posted_without_gate"] is False
    assert inv["third_party_code_is_naail_owned"] is False
    assert inv["human_gate_required"] is True
