import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAAIL = ROOT / "NAAIL-OpenLab"
REGISTRY = NAAIL / "architecture" / "platform_capability_registry.json"
TECH = NAAIL / "architecture" / "business_school_simulation_technology_registry.json"
PASSPORT = NAAIL / "architecture" / "professional_judgment_passport.schema.json"
HIERARCHY = NAAIL / "architecture" / "MASTER_PLATFORM_HIERARCHY.md"
ENGINE = NAAIL / "simulations" / "business-school" / "decision_consequence_engine.py"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_exactly_two_permanent_cores():
    data = load(REGISTRY)
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert data["invariants"]["permanent_core_count"] == 2


def test_canonical_professional_agents_and_paths_exist():
    required = [
        "agents/kiwi/README.md",
        "agents/pomelo/README.md",
        "agents/vera/README.md",
        "agents/ifrs/README.md",
        "agents/pcaob/README.md",
        "agents/esg/README.md",
        "agents/econova-s/README.md",
    ]
    missing = [p for p in required if not (NAAIL / p).exists()]
    assert not missing, f"Missing professional agent paths: {missing}"


def test_patent_sensitive_public_assets_are_non_enabling():
    schema = load(PASSPORT)
    assert schema["properties"]["status"]["const"] == "PATENT_HOLD_NON_ENABLING"
    engine_text = ENGINE.read_text(encoding="utf-8")
    assert "PUBLIC PATENT-HOLD STUB" in engine_text
    assert "def apply_decision" not in engine_text
    hierarchy = HIERARCHY.read_text(encoding="utf-8")
    assert "PATENT APPLICATION PREPARATION IN PROGRESS" in hierarchy
    assert "exactly two permanent cores" in hierarchy.lower()


def test_technology_registry_does_not_create_authority_or_core():
    data = load(TECH)
    assert data["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert data["invariants"]["permanent_core_count"] == 2
    assert data["invariants"]["new_technology_creates_new_core"] is False
    assert data["invariants"]["external_framework_is_authoritative_professional_truth"] is False
