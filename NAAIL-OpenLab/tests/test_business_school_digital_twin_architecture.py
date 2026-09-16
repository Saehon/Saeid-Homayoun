import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAAIL = ROOT / "NAAIL-OpenLab"
REGISTRY = NAAIL / "architecture" / "platform_capability_registry.json"
TECH = NAAIL / "architecture" / "business_school_simulation_technology_registry.json"
PASSPORT = NAAIL / "architecture" / "professional_judgment_passport.schema.json"
HIERARCHY = NAAIL / "architecture" / "MASTER_PLATFORM_HIERARCHY.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_exactly_two_permanent_cores():
    data = load(REGISTRY)
    assert data["platform"]["permanent_core_count"] == 2
    assert data["platform"]["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert data["invariants"]["permanent_core_count"] == 2
    assert data["invariants"]["business_school_simulation_layer_is_core"] is False
    assert data["invariants"]["decision_consequence_engine_is_core"] is False
    assert data["invariants"]["professional_judgment_passport_is_core"] is False


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


def test_business_school_layer_and_first_prototype_exist():
    paths = [
        NAAIL / "BUSINESS_SCHOOL_SIMULATION_DIGITAL_TWIN_LAYER.md",
        NAAIL / "digital-twins" / "audit-accounting" / "README.md",
        NAAIL / "simulations" / "business-school" / "decision_consequence_engine.py",
        PASSPORT,
        TECH,
    ]
    assert all(p.exists() for p in paths)


def test_technology_registry_does_not_create_authority_or_core():
    data = load(TECH)
    assert data["permanent_cores"] == ["Knowledge Core™", "Technology Core™"]
    assert data["invariants"]["permanent_core_count"] == 2
    assert data["invariants"]["new_technology_creates_new_core"] is False
    assert data["invariants"]["external_framework_is_authoritative_professional_truth"] is False
    assert data["invariants"]["framework_name_implies_executed"] is False
    names = {x["name"] for x in data["technologies"]}
    expected = {"Mesa", "AgentTorch", "SimPy", "OpenAI Agents SDK", "Microsoft Agent Framework", "HARK", "ABIDES", "FinRL", "RD-Agent"}
    assert expected.issubset(names)


def test_professional_judgment_passport_has_required_dimensions_and_human_gate():
    schema = load(PASSPORT)
    required_dims = set(schema["properties"]["dimensions"]["required"])
    assert required_dims == {"EQ", "PS", "RI", "AJ", "AUJ", "CKR", "AIV", "ETH", "HOR"}
    assert schema["properties"]["employment_use_prohibited_without_validation_and_consent"]["const"] is True
    assert schema["properties"]["external_certification_claimed"]["const"] is False
    decisions = schema["properties"]["human_gate"]["properties"]["decision"]["enum"]
    assert set(decisions) == {"APPROVE", "MODIFY", "REJECT", "REQUEST_MORE_EVIDENCE", "ESCALATE"}


def test_hierarchy_states_fixed_two_core_rule():
    text = HIERARCHY.read_text(encoding="utf-8")
    assert "exactly two permanent cores" in text.lower()
    assert "Business School Simulation & Digital Twin Layer" in text
    assert "Decision–Consequence Engine" in text
    assert "Professional Judgment Passport" in text
