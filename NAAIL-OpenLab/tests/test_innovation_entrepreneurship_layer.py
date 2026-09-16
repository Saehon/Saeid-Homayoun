from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "platform_capability_registry.json"
LAYER = ROOT / "INNOVATION_ENTREPRENEURSHIP_EVIDENCE_LAYER.md"
HIERARCHY = ROOT / "architecture" / "MASTER_PLATFORM_HIERARCHY.md"
OVERVIEW = ROOT / "PUBLIC_PLATFORM_OVERVIEW.md"


def test_public_layer_assets_exist():
    assert LAYER.exists()
    assert REGISTRY.exists()
    assert HIERARCHY.exists()
    assert OVERVIEW.exists()


def test_two_core_invariant_and_layer_role():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["platform"]["permanent_core_count"] == 2
    assert len(data["platform"]["permanent_cores"]) == 2
    inv = data["invariants"]
    assert inv["innovation_entrepreneurship_layer_is_core"] is False
    assert inv["innovation_entrepreneurship_layer_is_cccmp_specific"] is False
    assert inv["innovation_entrepreneurship_layer_serves_all_naail_engines"] is True


def test_research_safeguards_are_locked():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    inv = data["invariants"]
    assert inv["entrepreneurial_opportunity_score_is_deterministic_recommendation"] is False
    assert inv["behavioral_proxies_are_personality_diagnosis"] is False
    assert inv["github_repo_is_authoritative_data"] is False
    assert inv["public_access_equals_unrestricted_redistribution"] is False
    assert inv["source_license_gate_required"] is True
    assert inv["current_ft50_ajg_verification_required_when_used"] is True
    assert inv["human_gate_required"] is True


def test_public_layer_remains_non_enabling():
    text = LAYER.read_text(encoding="utf-8")
    assert "PATENT_HOLD_NON_ENABLING" in text
    assert "not a core" in text.lower()
    assert "not a deterministic recommendation" in text.lower()
    assert "psychological diagnoses" in text.lower()
    assert "detailed machine-readable" in text.lower()


def test_validated_checkpoint_is_unchanged():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"
    assert data["invariants"]["validated_checkpoint_changed_by_innovation_layer"] is False
