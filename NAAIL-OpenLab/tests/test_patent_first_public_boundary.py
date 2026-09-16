import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAAIL = ROOT / "NAAIL-OpenLab"


def test_private_patent_directory_is_not_in_public_tree():
    assert not (NAAIL / "private" / "patent").exists()


def test_public_patent_notice_uses_pre_filing_status():
    text = (NAAIL / "PATENT_NOTICE.md").read_text(encoding="utf-8")
    assert "PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS" in text
    assert "No NAAIL OpenLab™ patent application is represented" in text


def test_sensitive_public_assets_are_non_enabling():
    engine = (NAAIL / "simulations" / "business-school" / "decision_consequence_engine.py").read_text(encoding="utf-8")
    assert "PUBLIC PATENT-HOLD STUB" in engine
    assert "def apply_decision" not in engine

    passport = json.loads((NAAIL / "architecture" / "professional_judgment_passport.schema.json").read_text(encoding="utf-8"))
    assert passport["properties"]["status"]["const"] == "PATENT_HOLD_NON_ENABLING"

    mesh = json.loads((NAAIL / "architecture" / "data_evidence_mesh_registry.json").read_text(encoding="utf-8"))
    assert mesh["status"] == "PATENT_HOLD_NON_ENABLING"


def test_public_license_reserves_patent_and_commercial_rights():
    text = (NAAIL / "LICENSE").read_text(encoding="utf-8")
    assert "academic research" in text
    assert "non-commercial evaluation" in text
    assert "COMMERCIAL USE PROHIBITED" in text
    assert "NO PATENT OR OTHER IMPLIED IP LICENSE" in text
