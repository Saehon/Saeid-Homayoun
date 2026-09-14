import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASE_REGISTRY = ROOT / "architecture" / "google_science_phase_registry.json"
TWIN_REGISTRY = ROOT / "architecture" / "digital_twin_science_link_registry.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_phase_registry_invariants():
    data = load(PHASE_REGISTRY)
    assert data["knowledge_rag_core"] == "KRG2026.3"
    assert data["external_system_names_imply_execution"] is False
    assert data["technology_core_may_rewrite_knowledge_core"] is False
    assert data["human_gate_required"] is True
    phases = {p["phase_id"]: p for p in data["phases"]}
    for required in ["P00", "P01", "P03", "P05", "P06", "P10", "P11"]:
        assert required in phases
    assert phases["P11"]["status"] == "NAAIL_ONLY_AUTHORITY"


def test_no_pvalue_optimization_gate():
    data = load(PHASE_REGISTRY)
    phase = next(p for p in data["phases"] if p["phase_id"] == "P05")
    assert "no_pvalue_optimization" in phase["naail_gate"]
    assert "frozen_fitness_function" in phase["naail_gate"]


def test_digital_twins_link_to_local_repo_paths():
    data = load(TWIN_REGISTRY)
    phase_ids = {p["phase_id"] for p in load(PHASE_REGISTRY)["phases"]}
    assert data["invariants"]["all_paths_must_be_repository_local"] is True
    assert data["invariants"]["human_gate_required"] is True
    for twin in data["digital_twins"]:
        assert twin["github_paths"]
        for repo_path in twin["github_paths"]:
            assert repo_path.startswith("NAAIL-OpenLab/")
        assert set(twin["science_phases"]).issubset(phase_ids)
        assert "P11" in twin["science_phases"]


def test_external_systems_do_not_become_authority():
    phase_data = load(PHASE_REGISTRY)
    twin_data = load(TWIN_REGISTRY)
    assert phase_data["default_external_execution_status"] == "NOT_EXECUTED"
    assert twin_data["invariants"]["external_system_name_implies_execution"] is False
    assert twin_data["invariants"]["technology_core_may_rewrite_knowledge_core"] is False
    assert twin_data["invariants"]["digital_twin_output_is_authoritative_without_validation"] is False
