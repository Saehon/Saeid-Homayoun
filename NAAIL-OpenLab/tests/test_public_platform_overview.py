from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
REGISTRY = ROOT / "architecture" / "platform_capability_registry.json"
OVERVIEW = ROOT / "PUBLIC_PLATFORM_OVERVIEW.md"
NAAIL_README = ROOT / "README.md"
ROOT_README = REPO_ROOT / "README.md"


def test_public_overview_and_landing_pages_exist():
    assert OVERVIEW.exists()
    assert NAAIL_README.exists()
    assert ROOT_README.exists()
    assert REGISTRY.exists()


def test_registry_v2_preserves_two_core_architecture():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["schema_version"] == "2.5"
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == [
        "Stable Knowledge Core™",
        "Replaceable Technology Core™",
    ]
    inv = data["invariants"]
    assert inv["public_platform_overview_is_non_enabling"] is True
    assert inv["nobel_theory_engine_is_core"] is False
    assert inv["nobel_theory_engine_is_cccmp_specific"] is False
    assert inv["nobel_theory_engine_serves_all_naail_domains"] is True
    assert inv["cccmp_is_core"] is False


def test_public_overview_keeps_patent_and_scientific_boundaries():
    text = OVERVIEW.read_text(encoding="utf-8")
    assert "high-level and non-enabling" in text
    assert "exactly two permanent cores" in text
    assert "NAAIL Nobel Theory-to-Evidence & AI Experiment Engine™" in text
    assert "No third permanent core is permitted." in text
    assert "CCCMP™ → specialist programme" in text
    assert "Behavioral Decision Science & Human–AI Experimentation Layer™" in text
    assert "Public access does not imply unrestricted redistribution." in text
    assert "PATENT APPLICATION PREPARATION IN PROGRESS" in text


def test_public_landing_pages_show_current_architecture():
    for path in (NAAIL_README, ROOT_README):
        text = path.read_text(encoding="utf-8")
        assert "NAAIL OpenLab™" in text
        assert "Stable Knowledge Core™" in text
        assert "Replaceable Technology Core™" in text
        assert "Prototype 003" in text

    root_text = ROOT_README.read_text(encoding="utf-8")
    assert "PUBLIC_PLATFORM_OVERVIEW.md" in root_text


def test_validated_checkpoint_remains_prototype_003():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["platform"]["validated_executable_checkpoint"] == "v0.2.3 / Audit Workspace V0.4 / Prototype 003"
