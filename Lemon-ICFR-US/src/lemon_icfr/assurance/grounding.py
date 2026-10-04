"""Structured ICFR/COSO grounding (P0-5). Replaces the Boolean COSO-context flag."""
from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Optional

ASSERTIONS = frozenset({"existence_occurrence", "completeness", "accuracy_valuation", "cutoff",
                        "classification", "rights_obligations", "presentation_disclosure"})

# COSO 2013: 5 components, 17 principles.
COSO_PRINCIPLES = {
    "control_environment": range(1, 6),
    "risk_assessment": range(6, 10),
    "control_activities": range(10, 13),
    "information_communication": range(13, 16),
    "monitoring": range(16, 18),
}
CONTROL_TYPES = frozenset({"preventive", "detective"})


@dataclass(frozen=True)
class Risk:
    risk_id: str
    description: str
    assertion: str


@dataclass(frozen=True)
class Control:
    control_id: str
    objective: str
    addresses_assertions: tuple[str, ...]
    control_type: str
    frequency: str
    owner: str
    coso_component: str
    coso_principle: int
    key: bool = True


@dataclass(frozen=True)
class TestProcedure:
    __test__ = False   # not a pytest test class (fixes PytestCollectionWarning)
    test_id: str
    control_id: str
    population_source: str
    population_size: Optional[int]
    sampling_rule: str
    evidence_ids: tuple[str, ...]
    exceptions: int = 0


@dataclass(frozen=True)
class ICFRScope:
    """ENTITY → PROCESS → ACCOUNT → ASSERTION → RISK → CONTROL → TEST → EVIDENCE → EXCEPTION."""
    entity: str
    period_end: str
    process: str
    subprocess: str
    account: str
    fsli: str
    assertion: str
    risk: Risk
    control: Control
    test: Optional[TestProcedure]
    authority_refs: tuple[str, ...]      # SEC / PCAOB grounding references


def validate_scope(scope: ICFRScope) -> list[str]:
    issues = []
    for f in fields(scope):
        v = getattr(scope, f.name)
        if f.name == "test":
            continue
        if v in ("", None, ()):
            issues.append(f"missing {f.name}")
    if scope.assertion not in ASSERTIONS:
        issues.append(f"unknown assertion {scope.assertion!r}")
    if scope.risk.assertion != scope.assertion:
        issues.append("risk assertion does not match scope assertion")
    c = scope.control
    if scope.assertion not in c.addresses_assertions:
        issues.append("control does not address the scoped assertion")
    if c.control_type not in CONTROL_TYPES:
        issues.append(f"unknown control type {c.control_type!r}")
    if not c.owner or not c.frequency or not c.objective:
        issues.append("control missing owner/frequency/objective")
    rng = COSO_PRINCIPLES.get(c.coso_component)
    if rng is None:
        issues.append(f"unknown COSO component {c.coso_component!r}")
    elif c.coso_principle not in rng:
        issues.append(f"COSO principle {c.coso_principle} not in component {c.coso_component}")
    if scope.test is not None and scope.test.control_id != c.control_id:
        issues.append("test procedure does not test the scoped control")
    return issues
