import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "architecture" / "core_boundary_policy.json"


def load_policy():
    with POLICY.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_frozen_core_flags():
    policy = load_policy()
    rules = policy["rules"]

    assert policy["status"] == "FROZEN_ARCHITECTURAL_INVARIANT"
    assert rules["knowledge_rag_core_frozen"] is True
    assert rules["technology_core_separate"] is True
    assert rules["provider_release_may_rewrite_knowledge_core"] is False
    assert rules["technology_upgrade_may_rewrite_rag_semantics"] is False
    assert rules["technology_upgrade_may_rewrite_graph_ontology"] is False
    assert rules["technology_upgrade_may_rewrite_evidence_hierarchy"] is False
    assert rules["technology_upgrade_may_rewrite_causal_dag"] is False
    assert rules["technology_upgrade_may_bypass_human_gate"] is False


def test_no_component_overlap_between_cores():
    policy = load_policy()
    knowledge = set(policy["knowledge_rag_core"])
    technology = set(policy["technology_core"])

    overlap = knowledge.intersection(technology)
    assert not overlap, f"Knowledge/RAG Core and Technology Core overlap: {sorted(overlap)}"


def test_canonical_document_exists():
    policy = load_policy()
    canonical = (POLICY.parent / policy["canonical_document"]).resolve()
    assert canonical.exists(), f"Canonical invariant document missing: {canonical}"


def test_required_knowledge_rag_items_are_frozen():
    policy = load_policy()
    knowledge = set(policy["knowledge_rag_core"])
    required = {
        "knowledge_graph_ontology",
        "graphrag_semantics",
        "rag_corpus_governance",
        "retrieval_meaning_and_citation_contract",
        "evidence_hierarchy",
        "causal_dags",
        "human_gate_rules",
    }
    missing = required - knowledge
    assert not missing, f"Required frozen Knowledge/RAG Core items missing: {sorted(missing)}"
