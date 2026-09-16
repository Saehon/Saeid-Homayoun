from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def load_registry():
    return json.loads((ROOT / "architecture" / "platform_capability_registry.json").read_text(encoding="utf-8"))


def test_cccmp_preserves_two_core_architecture():
    registry = load_registry()
    assert registry["platform"]["permanent_core_count"] == 2
    assert registry["platform"]["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert registry["invariants"]["cccmp_is_core"] is False


def test_cccmp_public_files_are_registered():
    registry = load_registry()
    by_id = {item["id"]: item for item in registry["capabilities"]}
    assert by_id["cccmp_programme"]["status"] == "PATENT_HOLD_NON_ENABLING"
    assert by_id["cccmp_research_governance"]["status"] == "ARCHITECTURE_ADOPTED"
    for capability_id in ("cccmp_programme", "cccmp_research_governance"):
        path = by_id[capability_id]["path"].replace("NAAIL-OpenLab/", "")
        assert (ROOT / path).exists(), path


def test_cccmp_rights_and_causality_boundaries():
    registry = load_registry()
    inv = registry["invariants"]
    assert inv["cccmp_industry_use_publicly_licensed"] is False
    assert inv["cccmp_third_party_rights_overridden"] is False
    assert inv["cccmp_simulation_equals_real_world_causality"] is False
    assert inv["public_access_equals_unrestricted_redistribution"] is False


def test_cccmp_does_not_change_validated_checkpoint():
    registry = load_registry()
    assert registry["invariants"]["cccmp_changes_validated_checkpoint"] is False
    assert registry["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"


def test_public_cccmp_page_is_non_enabling_and_patent_first():
    text = (ROOT / "CCCMP_PROJECT_COST_CONTRACT_CLAIMS_PROGRAMME.md").read_text(encoding="utf-8")
    assert "PATENT APPLICATION PREPARATION IN PROGRESS" in text
    assert "not a third" in text.lower()
    assert "private under patent hold" in text.lower()
    assert "Free to view does not mean free to copy or redistribute." in text
