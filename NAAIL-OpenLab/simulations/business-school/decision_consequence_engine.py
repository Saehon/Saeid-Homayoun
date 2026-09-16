"""NAAIL Decision–Consequence Engine™ — deterministic education prototype.

This module implements transparent synthetic state transitions for business-school
Digital Twin exercises. The transition magnitudes are pedagogical assumptions,
not empirical causal estimates.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, asdict
from typing import Dict, Mapping, Any


DEFAULT_STATE = {
    "company": {"performance_pressure": 2.0},
    "accounting": {"misstatement_risk": 2.0, "estimate_uncertainty": 2.0},
    "controls": {"deficiency_severity": 2.0},
    "audit": {"audit_risk": 2.0, "evidence_gap": 2.0, "cam_candidate": 1.0},
    "market": {"investor_confidence": 3.0, "volatility": 2.0},
    "regulatory": {"scrutiny": 1.0},
    "esg": {"reporting_credibility": 3.0},
    "education": {"time_cost": 1.0},
}


# Synthetic educational effects. Each delta is applied to a path in the state.
RULES = {
    "REQUEST_MORE_EVIDENCE": {
        "accounting.estimate_uncertainty": -0.5,
        "audit.evidence_gap": -0.8,
        "education.time_cost": +0.5,
    },
    "ACCEPT_MANAGEMENT_ESTIMATE": {
        "accounting.misstatement_risk": +0.6,
        "audit.audit_risk": +0.4,
        "regulatory.scrutiny": +0.2,
    },
    "PROPOSE_ADJUSTMENT": {
        "accounting.misstatement_risk": -0.6,
        "audit.audit_risk": -0.3,
        "company.performance_pressure": +0.2,
        "education.time_cost": +0.2,
    },
    "ESCALATE_CONTROL_DEFICIENCY": {
        "controls.deficiency_severity": -0.5,
        "audit.evidence_gap": -0.2,
        "regulatory.scrutiny": +0.2,
        "education.time_cost": +0.4,
    },
    "DESIGNATE_CAM": {
        "audit.cam_candidate": +1.0,
        "regulatory.scrutiny": -0.1,
        "education.time_cost": +0.3,
    },
    "REJECT_UNSUPPORTED_AI_RECOMMENDATION": {
        "audit.evidence_gap": -0.3,
        "regulatory.scrutiny": -0.1,
        "education.time_cost": +0.2,
    },
    "ACCEPT_UNSUPPORTED_AI_RECOMMENDATION": {
        "audit.evidence_gap": +0.7,
        "accounting.misstatement_risk": +0.3,
        "regulatory.scrutiny": +0.4,
    },
    "STRENGTHEN_ESG_DISCLOSURE": {
        "esg.reporting_credibility": +0.6,
        "market.investor_confidence": +0.2,
        "education.time_cost": +0.2,
    },
}


@dataclass(frozen=True)
class ConsequenceLedgerEntry:
    decision: str
    rationale: str
    rule_type: str
    previous_state: Dict[str, Any]
    new_state: Dict[str, Any]
    deltas: Dict[str, float]
    human_approval_status: str = "PENDING_HUMAN_APPROVAL"


def _get_nested(state: Mapping[str, Any], path: str) -> float:
    section, key = path.split(".", 1)
    return float(state[section][key])


def _set_nested(state: Dict[str, Any], path: str, value: float) -> None:
    section, key = path.split(".", 1)
    state[section][key] = round(max(0.0, min(5.0, value)), 3)


def apply_decision(
    state: Mapping[str, Any],
    decision: str,
    rationale: str,
) -> ConsequenceLedgerEntry:
    """Apply one transparent synthetic decision rule to a Digital Twin state.

    The function never auto-approves the outcome. Human approval remains pending.
    """
    if decision not in RULES:
        raise ValueError(f"Unknown decision: {decision}")
    if not rationale or not rationale.strip():
        raise ValueError("A non-empty rationale is required")

    previous = deepcopy(dict(state))
    new_state = deepcopy(previous)
    deltas = RULES[decision]

    for path, delta in deltas.items():
        current = _get_nested(new_state, path)
        _set_nested(new_state, path, current + delta)

    return ConsequenceLedgerEntry(
        decision=decision,
        rationale=rationale.strip(),
        rule_type="SYNTHETIC_PEDAGOGICAL_TRANSITION",
        previous_state=previous,
        new_state=new_state,
        deltas=dict(deltas),
    )


def to_dict(entry: ConsequenceLedgerEntry) -> Dict[str, Any]:
    """Serialize a consequence ledger entry."""
    return asdict(entry)


if __name__ == "__main__":
    example = apply_decision(
        DEFAULT_STATE,
        "REQUEST_MORE_EVIDENCE",
        "Evidence is insufficient to support the current estimate.",
    )
    print(to_dict(example))
