import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "NAAIL-OpenLab" / "simulations" / "business-school" / "decision_consequence_engine.py"


def load_engine():
    module_name = "decision_consequence_engine"
    spec = importlib.util.spec_from_file_location(module_name, ENGINE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_engine_file_exists():
    assert ENGINE.exists()


def test_request_more_evidence_reduces_evidence_gap_and_never_auto_approves():
    m = load_engine()
    entry = m.apply_decision(
        m.DEFAULT_STATE,
        "REQUEST_MORE_EVIDENCE",
        "Current evidence is insufficient.",
    )
    assert entry.new_state["audit"]["evidence_gap"] < entry.previous_state["audit"]["evidence_gap"]
    assert entry.human_approval_status == "PENDING_HUMAN_APPROVAL"
    assert entry.rule_type == "SYNTHETIC_PEDAGOGICAL_TRANSITION"


def test_unsupported_ai_acceptance_increases_evidence_risk():
    m = load_engine()
    entry = m.apply_decision(
        m.DEFAULT_STATE,
        "ACCEPT_UNSUPPORTED_AI_RECOMMENDATION",
        "Intentional negative-path test.",
    )
    assert entry.new_state["audit"]["evidence_gap"] > entry.previous_state["audit"]["evidence_gap"]
    assert entry.new_state["regulatory"]["scrutiny"] > entry.previous_state["regulatory"]["scrutiny"]


def test_engine_is_deterministic_for_same_input():
    m = load_engine()
    a = m.to_dict(m.apply_decision(m.DEFAULT_STATE, "PROPOSE_ADJUSTMENT", "Same rationale"))
    b = m.to_dict(m.apply_decision(m.DEFAULT_STATE, "PROPOSE_ADJUSTMENT", "Same rationale"))
    assert a == b


def test_unknown_decision_fails_closed():
    m = load_engine()
    try:
        m.apply_decision(m.DEFAULT_STATE, "INVENTED_DECISION", "test")
    except ValueError:
        pass
    else:
        raise AssertionError("Unknown decisions must fail closed")
