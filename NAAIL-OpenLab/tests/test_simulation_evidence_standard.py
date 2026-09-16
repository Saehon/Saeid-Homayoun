import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "NAAIL-OpenLab" / "architecture" / "simulation_evidence_card.schema.json"
EXAMPLE = ROOT / "NAAIL-OpenLab" / "docs" / "education" / "simulation_evidence_card.example.json"
STANDARD = ROOT / "NAAIL-OpenLab" / "docs" / "education" / "SIMULATION_EVIDENCE_STANDARD.md"
PLATFORM = ROOT / "NAAIL-OpenLab" / "GLOBAL_AI_BUSINESS_EDUCATION_PLATFORM.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_required_files_exist():
    for path in (SCHEMA, EXAMPLE, STANDARD, PLATFORM):
        assert path.exists(), f"Missing required education-governance asset: {path}"


def test_schema_and_example_identity():
    schema = load(SCHEMA)
    card = load(EXAMPLE)
    assert schema["title"] == "NAAIL Simulation Research Evidence Card"
    assert card["schema_version"] == "1.0"
    required = set(schema["required"])
    assert required.issubset(card.keys())


def test_human_gate_and_high_stakes_invariants():
    card = load(EXAMPLE)
    assert card["ai_condition"]["human_gate_bypass_allowed"] is False
    assert card["human_gate"]["model_self_approval_allowed"] is False
    assert card["assessment"]["high_stakes_use_allowed"] is False
    assert card["human_gate"]["status"] == "PENDING_HUMAN_APPROVAL"


def test_no_fake_top_journal_claim_in_template():
    card = load(EXAMPLE)
    research = card["research_grounding"]
    assert research["state"] == "EVIDENCE_GAP_DECLARED"
    assert research["anchors"] == []
    assert "Before promotion" in research["evidence_gap_note"]


def test_professional_alignment_is_not_certification():
    card = load(EXAMPLE)
    assert card["professional_competencies"]
    assert all(item["alignment_only"] is True for item in card["professional_competencies"])


def test_sustainability_value_has_four_dimensions():
    card = load(EXAMPLE)
    assert set(card["sustainability_value"]) == {"people", "planet", "society", "sustainable_profit"}


def test_platform_contract_contains_core_boundaries():
    text = PLATFORM.read_text(encoding="utf-8")
    for phrase in (
        "simulation_may_invent_top_journal_support = false",
        "professional_body_alignment_equals_certification = false",
        "research_overrides_authoritative_standard = false",
        "Human Gate™",
        "People × Planet × Society × Sustainable Profit™",
    ):
        assert phrase in text
