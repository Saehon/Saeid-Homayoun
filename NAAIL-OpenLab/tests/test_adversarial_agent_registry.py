import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "adversarial_agent_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_registry_is_technology_core_only():
    data = load_registry()
    boundary = data["core_boundary"]
    assert boundary["technology_core_only"] is True
    assert boundary["may_modify_knowledge_rag_core"] is False
    assert boundary["human_gate_required"] is True
    assert boundary["knowledge_rag_core_version"] == "KRG2026.3"


def test_required_adversarial_roles_exist():
    data = load_registry()
    required = {
        "proposer",
        "critic",
        "defender",
        "falsifier",
        "replicator",
        "evidence_auditor",
        "judge",
    }
    assert required.issubset(set(data["roles"]))


def test_no_third_party_code_is_claimed_as_vendored():
    data = load_registry()
    for project in data["projects"]:
        assert project["third_party_code_vendored"] is False


def test_runtime_claims_are_not_fabricated():
    data = load_registry()
    for project in data["projects"]:
        assert project["runtime_executed"] is False


def test_scientific_invariants_are_preserved():
    inv = load_registry()["scientific_invariants"]
    assert inv["agent_consensus_is_truth"] is False
    assert inv["majority_vote_is_truth"] is False
    assert inv["statistical_significance_is_discovery"] is False
    assert inv["predictive_accuracy_is_causality"] is False
    assert inv["adversarial_agent_may_modify_knowledge_rag_core"] is False
    assert inv["red_team_tool_may_modify_knowledge_rag_core"] is False
    assert inv["human_gate_required"] is True


def test_each_project_has_required_promotion_gates():
    data = load_registry()
    required_gates = {
        "license_and_terms_review",
        "dependency_security_review",
        "synthetic_sandbox_execution",
        "frozen_benchmark_evaluation",
        "human_architecture_gate",
    }
    assert required_gates.issubset(set(data["promotion_gates"]))
    assert len(data["projects"]) >= 7
