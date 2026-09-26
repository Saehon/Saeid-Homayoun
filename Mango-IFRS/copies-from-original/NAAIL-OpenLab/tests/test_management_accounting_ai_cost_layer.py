import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAAIL = ROOT / "NAAIL-OpenLab"
REGISTRY = NAAIL / "architecture" / "platform_capability_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_two_core_constitution_remains_frozen():
    data = load_registry()
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == [
        "Stable Knowledge Core™",
        "Replaceable Technology Core™",
    ]
    assert data["invariants"]["two_core_constitution_frozen"] is True
    assert data["invariants"]["third_permanent_core_allowed"] is False


def test_management_accounting_layers_are_registered_and_not_cores():
    data = load_registry()
    by_id = {item["id"]: item for item in data["capabilities"]}
    expected = {
        "management_accounting_ai_cost_intelligence_layer": "NAAIL-OpenLab/MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md",
        "open_model_benchmark_cost_intelligence_layer": "NAAIL-OpenLab/OPEN_MODEL_BENCHMARK_COST_INTELLIGENCE_LAYER.md",
        "visualization_decision_intelligence_layer": "NAAIL-OpenLab/VISUALIZATION_DECISION_INTELLIGENCE_LAYER.md",
    }
    for cap_id, path in expected.items():
        assert cap_id in by_id
        assert by_id[cap_id]["path"] == path
        assert by_id[cap_id]["core"] is False
        assert (ROOT / path).exists()


def test_no_management_accounting_subdomain_becomes_a_core():
    inv = load_registry()["invariants"]
    for key in {
        "management_accounting_ai_cost_layer_is_core",
        "open_model_benchmark_cost_layer_is_core",
        "visualization_decision_intelligence_layer_is_core",
        "bsc_is_new_core",
        "abc_is_new_core",
        "tdabc_is_new_core",
        "ai_finops_is_new_core",
    }:
        assert inv[key] is False


def test_cost_optimization_cannot_override_scientific_governance():
    inv = load_registry()["invariants"]
    assert inv["cost_minimization_overrides_quality_evidence_or_governance"] is False
    assert inv["benchmark_rank_equals_truth"] is False
    assert inv["current_model_price_without_timestamped_provenance_allowed"] is False
    assert inv["source_license_gate_required"] is True
    assert inv["provenance_required"] is True
    assert inv["human_gate_required"] is True


def test_validated_checkpoint_is_unchanged():
    data = load_registry()
    assert data["platform"]["validated_executable_checkpoint"] == (
        "v0.2.3 / Audit Workspace V0.4 / Prototype 003"
    )
    assert data["invariants"]["validated_checkpoint_changed_by_management_accounting_layer"] is False


def test_public_management_accounting_doc_keeps_attribution_boundary():
    text = (NAAIL / "MANAGEMENT_ACCOUNTING_AI_COST_INTELLIGENCE_LAYER.md").read_text(encoding="utf-8")
    assert "NAAIL-developed extension inspired by ABC/TDABC" in text
    assert "not represented as original Kaplan" in text
    assert "minimum defensible ai cost" in text.lower()
