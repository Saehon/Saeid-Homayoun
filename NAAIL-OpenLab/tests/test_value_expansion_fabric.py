import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "NAAIL-OpenLab"
REGISTRY = ROOT / "architecture" / "platform_capability_registry.json"
FABRIC = ROOT / "VALUE_EXPANSION_FABRIC.md"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_value_expansion_fabric_is_registered_and_publicly_non_enabling():
    data = load_registry()
    by_id = {item["id"]: item for item in data["capabilities"]}
    item = by_id["value_expansion_fabric"]
    assert item["status"] == "PATENT_HOLD_NON_ENABLING"
    assert FABRIC.exists()
    assert "does **not** create a third core" in FABRIC.read_text(encoding="utf-8")


def test_value_expansion_does_not_change_fixed_architecture():
    data = load_registry()
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    inv = data["invariants"]
    assert inv["value_expansion_fabric_is_core"] is False
    assert inv["canonical_agent_set_changed_by_value_expansion"] is False
    assert inv["validated_checkpoint_changed_by_value_expansion"] is False


def test_third_party_and_execution_boundaries_fail_closed():
    data = load_registry()
    inv = data["invariants"]
    assert inv["public_access_equals_unrestricted_redistribution"] is False
    assert inv["third_party_rights_are_overridden_by_naail"] is False
    assert inv["registry_entry_equals_dependency_installed"] is False
    assert inv["new_enabling_patent_sensitive_details_public_before_filing_review"] is False
    assert inv["human_gate_required"] is True


def test_validated_public_checkpoint_remains_prototype_003():
    data = load_registry()
    executed = [x for x in data["capabilities"] if x["status"] == "EXECUTED_VALIDATED"]
    assert len(executed) == 1
    assert executed[0]["id"] == "prototype_003"
