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


def test_gate_cannot_be_true_without_required_artifact():
    record = copy.deepcopy(BASE)
    record["gates"]["chain_of_evidence"] = True
    record["artifacts"]["chain_of_evidence"] = None
    errors = validator.validate_governance(record)
    assert any("chain_of_evidence" in e and "artifact" in e for e in errors)


def test_discovery_requires_frozen_protocol_and_holdout_isolation():
    record = copy.deepcopy(BASE)
    record["discovery_claim_allowed"] = True
    record["study_stage"] = "approved"
    record["integrity"]["protocol_frozen"] = False
    record["integrity"]["holdout_isolated"] = False
    errors = validator.validate_governance(record)
    assert any("protocol_frozen" in e for e in errors)
    assert any("holdout_isolated" in e for e in errors)


def test_role_only_ai_review_is_insufficient_for_discovery():
    record = copy.deepcopy(BASE)
    record["discovery_claim_allowed"] = True
    record["study_stage"] = "approved"
    record["integrity"]["ai_review_independence_level"] = "role_only"
    errors = validator.validate_governance(record)
    assert any("role-only" in e for e in errors)


def test_human_decision_must_explicitly_authorize_scientific_claim():
    record = copy.deepcopy(BASE)
    record["discovery_claim_allowed"] = True
    record["study_stage"] = "approved"
    record["human_gate"]["approved"] = True
    record["human_gate"]["reviewer"] = "Independent reviewer"
    record["human_gate"]["decision_date"] = "2026-09-14"
    record["human_gate"]["decision"] = "PROCEED"
    record["human_gate"]["independence_statement"] = "Reviewer did not generate the candidate result."
    errors = validator.validate_governance(record)
    assert any("does not authorize" in e for e in errors)


def test_nonexistent_local_artifact_does_not_resolve():
    assert validator._artifact_is_resolvable("discovery/definitely_missing_artifact.json") is False
