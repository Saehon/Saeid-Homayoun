"""P03 — Entity-level scope mode (ORQ-012).

For public-company POCs: control-level details (controls, tests, populations) are not
published. They are recorded as NOT_PUBLICLY_OBSERVABLE, never invented. Any claim
whose predicate is control-level returns INSUFFICIENT_EVIDENCE under entity scope.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Optional, Sequence

from .adapter import AdapterError, GateDecision, legacy_to_hypothesis
from .claim import Claim
from .enums import FalsificationOutcome, ReviewOutcome, SupportClass
from .evidence import EvidenceStore
from .falsify import Falsifier
from .grounding import COSO_PRINCIPLES
from .independence import AgentRun
from .passport import EvidencePassport
from .review import ReproRef, Reviewer
from .support import SupportResult, assess_support

NOT_PUBLICLY_OBSERVABLE = "NOT_PUBLICLY_OBSERVABLE"
ENTITY_ASSERTION = "entity_level_icfr"
CONTROL_LEVEL_PREDICATES = frozenset({
    "control_design_effective", "control_operating_effective", "control_exception_rate",
    "test_population_size", "control_owner", "control_frequency"})


@dataclass(frozen=True)
class EntityScope:
    entity: str
    period_end: str
    authority_refs: tuple[str, ...]
    coso_component: str = ""
    coso_principle: int = 0
    level: str = "ENTITY"
    assertion: str = ENTITY_ASSERTION          # read by the falsifier
    process: str = NOT_PUBLICLY_OBSERVABLE
    account: str = NOT_PUBLICLY_OBSERVABLE
    control: str = NOT_PUBLICLY_OBSERVABLE
    test: None = None                          # no operating-effectiveness test is observable


def validate_entity_scope(s: EntityScope) -> list[str]:
    issues = []
    if not s.entity:
        issues.append("missing entity")
    if not s.period_end:
        issues.append("missing period_end")
    if not s.authority_refs:
        issues.append("missing authority_refs")
    if s.coso_component:
        rng = COSO_PRINCIPLES.get(s.coso_component)
        if rng is None:
            issues.append(f"unknown COSO component {s.coso_component!r}")
        elif s.coso_principle not in rng:
            issues.append(f"COSO principle {s.coso_principle} not in {s.coso_component}")
    for name in ("process", "account", "control"):
        if getattr(s, name) != NOT_PUBLICLY_OBSERVABLE:
            issues.append(f"entity scope must not carry invented {name} details")
    return issues


def entity_level_support(claim: Claim, store: EvidenceStore) -> SupportResult:
    ctl = [p.predicate for p in claim.propositions if p.predicate in CONTROL_LEVEL_PREDICATES]
    if ctl:
        return SupportResult(SupportClass.INSUFFICIENT_EVIDENCE, (), (), (),
                             (f"control-level predicates {ctl} are {NOT_PUBLICLY_OBSERVABLE} under entity scope",))
    return assess_support(claim, store)


def assure_entity_case(*, case_id: str, question: str, created_at: str, hypotheses: Sequence[Mapping],
                       store: EvidenceStore, scope: EntityScope, repro: Optional[ReproRef], generator: AgentRun,
                       reviewer: Reviewer, falsifier: Falsifier,
                       replay: Optional[Callable[[], str]] = None) -> GateDecision:
    sel = [h for h in hypotheses if isinstance(h, Mapping) and h.get("selected") is True]
    if len(sel) != 1:
        return GateDecision(False, False, False, None, (f"fail closed: exactly one selected hypothesis required, found {len(sel)}",))
    try:
        hyp = legacy_to_hypothesis(sel[0], [h for h in hypotheses if h is not sel[0]], generator)
    except AdapterError as e:
        return GateDecision(False, False, False, None, (f"fail closed: {e}",))
    sup = entity_level_support(hyp.claim, store)
    rv = reviewer.review(hyp, sup, validate_entity_scope(scope), repro)
    fz = falsifier.falsify(hyp, scope, sup, replay=replay)
    pp = EvidencePassport(f"PP-{case_id}", case_id, created_at, hyp.claim.entity, hyp.claim.period_end, question,
                          EvidencePassport.records_from(store, hyp.claim.evidence_ids), scope, hyp, sup, rv, fz, repro)
    reasons = tuple(rv.reasons) + tuple(f"falsification:{c.name}:{c.outcome}: {c.detail}"
                                        for c in fz.challenges if c.outcome.value != "SURVIVED")
    return GateDecision(sup.classification is SupportClass.SUPPORTED, rv.outcome is ReviewOutcome.PASS,
                        fz.outcome is FalsificationOutcome.SURVIVED, pp, reasons)
