from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "validate_study_manifest.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)

BASE = json.loads((ROOT / "sample_study_manifest.json").read_text(encoding="utf-8"))


def test_current_manifest_is_valid_but_not_discovery_approved():
    assert BASE["discovery_claim_allowed"] is False
    assert validator.validate_governance(BASE) == []


def test_human_gate_cannot_be_bypassed():
    record = copy.deepcopy(BASE)
    record["discovery_claim_allowed"] = True
    errors = validator.validate_governance(record)
    assert any("Human Gate" in e for e in errors)
    assert any("mandatory gate" in e for e in errors)


def test_causal_label_requires_identification():
    record = copy.deepcopy(BASE)
    record["evidence_class"] = "causal"
    record["gates"]["identification"] = False
    errors = validator.validate_governance(record)
    assert any("causal" in e and "identification" in e for e in errors)


def test_chain_of_evidence_gate_requires_artifact():
    record = copy.deepcopy(BASE)
    record["gates"]["chain_of_evidence"] = True
    record["artifacts"]["chain_of_evidence"] = None
    errors = validator.validate_governance(record)
    assert any("chain_of_evidence" in e for e in errors)
