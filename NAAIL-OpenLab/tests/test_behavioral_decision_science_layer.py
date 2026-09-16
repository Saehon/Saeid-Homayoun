from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_behavioral_layer_preserves_two_core_architecture():
    registry = json.loads((ROOT / "architecture" / "platform_capability_registry.json").read_text(encoding="utf-8"))
    assert registry["platform"]["architecture"] == "V2026.3 Multi-Agent Digital Twin"
    assert registry["platform"]["permanent_core_count"] == 2
    assert registry["platform"]["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert registry["invariants"]["behavioral_decision_science_layer_is_core"] is False


def test_behavioral_layer_is_registered_non_enabling():
    registry = json.loads((ROOT / "architecture" / "platform_capability_registry.json").read_text(encoding="utf-8"))
    cap = next(c for c in registry["capabilities"] if c["id"] == "behavioral_decision_science_human_ai")
    assert cap["status"] == "PATENT_HOLD_NON_ENABLING"
    assert cap["path"] == "NAAIL-OpenLab/BEHAVIORAL_DECISION_SCIENCE_HUMAN_AI_LAYER.md"


def test_behavioral_proxies_are_not_personality_diagnosis():
    registry = json.loads((ROOT / "architecture" / "platform_capability_registry.json").read_text(encoding="utf-8"))
    assert registry["invariants"]["behavioral_proxies_are_personality_diagnosis"] is False


def test_validated_checkpoint_is_unchanged():
    registry = json.loads((ROOT / "architecture" / "platform_capability_registry.json").read_text(encoding="utf-8"))
    assert registry["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"
    assert registry["invariants"]["validated_checkpoint_changed_by_behavioral_layer"] is False
