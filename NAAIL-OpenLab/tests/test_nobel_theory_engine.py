from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "platform_capability_registry.json"
ENGINE = ROOT / "NOBEL_THEORY_TO_EVIDENCE_AI_EXPERIMENT_ENGINE.md"
HIERARCHY = ROOT / "architecture" / "MASTER_PLATFORM_HIERARCHY.md"


def test_nobel_engine_files_exist():
    assert ENGINE.exists()
    assert REGISTRY.exists()
    assert HIERARCHY.exists()


def test_exactly_two_permanent_cores_and_engine_not_core():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["platform"]["permanent_core_count"] == 2
    assert len(data["platform"]["permanent_cores"]) == 2
    assert data["invariants"]["nobel_theory_engine_is_core"] is False
    assert data["invariants"]["nobel_theory_engine_is_cccmp_specific"] is False


def test_scientific_safeguards_are_locked():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    inv = data["invariants"]
    assert inv["theory_name_equals_valid_measurement"] is False
    assert inv["behavioral_proxies_are_personality_diagnosis"] is False
    assert inv["predictive_accuracy_is_causality"] is False
    assert inv["github_repo_is_authoritative_data"] is False
    assert inv["registry_entry_equals_dependency_installed"] is False
    assert inv["current_ft50_ajg_verification_required_when_used"] is True
    assert inv["source_license_gate_required"] is True
    assert inv["human_gate_required"] is True


def test_public_engine_remains_non_enabling():
    text = ENGINE.read_text(encoding="utf-8")
    assert "PATENT_HOLD_NON_ENABLING" in text
    assert "not a third core" in text.lower()
    assert "not a cccmp-specific module" in text.lower()
    assert "psychological diagnoses" in text


def test_validated_checkpoint_is_unchanged():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"
