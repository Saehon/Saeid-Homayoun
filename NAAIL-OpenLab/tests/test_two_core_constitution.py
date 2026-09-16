from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONSTITUTION = ROOT / "TWO_CORE_CONSTITUTION.md"
REGISTRY = ROOT / "architecture" / "platform_capability_registry.json"
HIERARCHY = ROOT / "architecture" / "MASTER_PLATFORM_HIERARCHY.md"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_constitution_exists_and_is_frozen():
    text = CONSTITUTION.read_text(encoding="utf-8")
    assert "Constitutional status:** FROZEN" in text
    assert "Stable Knowledge Core™" in text
    assert "Replaceable Technology Core™" in text
    assert "No third permanent core" in text


def test_registry_has_exactly_two_permanent_cores():
    data = load_registry()
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == [
        "Stable Knowledge Core™",
        "Replaceable Technology Core™",
    ]
    assert data["invariants"]["two_core_constitution_frozen"] is True
    assert data["invariants"]["third_permanent_core_allowed"] is False


def test_modular_layers_are_not_cores():
    inv = load_registry()["invariants"]
    layer_flags = [
        "data_evidence_mesh_is_core",
        "ft50_ajg_evidence_graph_is_core",
        "nobel_theory_engine_is_core",
        "behavioral_decision_science_layer_is_core",
        "innovation_entrepreneurship_layer_is_core",
        "business_school_simulation_layer_is_core",
        "knowledge_rag_graphrag_kag_layer_is_core",
        "professional_education_question_bank_layer_is_core",
        "decision_consequence_engine_is_core",
        "professional_judgment_passport_is_core",
        "cccmp_is_core",
    ]
    assert all(inv[name] is False for name in layer_flags)


def test_future_change_types_cannot_create_new_core():
    inv = load_registry()["invariants"]
    for name in [
        "new_domain_creates_new_core",
        "new_dataset_creates_new_core",
        "new_model_creates_new_core",
        "new_vendor_creates_new_core",
        "new_github_technology_creates_new_core",
        "supporting_layer_may_become_third_core",
        "specialist_programme_may_become_third_core",
    ]:
        assert inv[name] is False


def test_scientific_meaning_is_not_silently_rewritten_by_technology():
    inv = load_registry()["invariants"]
    assert inv["technology_change_redefines_scientific_meaning"] is False
    assert inv["technology_core_may_silently_rewrite_knowledge_core"] is False


def test_governance_and_validation_boundary():
    data = load_registry()
    inv = data["invariants"]
    assert inv["source_license_gate_required"] is True
    assert inv["provenance_required"] is True
    assert inv["reproducibility_required"] is True
    assert inv["human_gate_required"] is True
    assert inv["validated_checkpoint_changed_by_two_core_constitution"] is False
    assert data["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"


def test_hierarchy_points_to_constitution():
    text = HIERARCHY.read_text(encoding="utf-8")
    assert "Two-Core Constitution" in text
    assert "permanently preserves exactly two cores" in text
