"""R2 adapter (ORQ-007): the legacy orchestrator's gate booleans are DERIVED from real
assessments instead of `bool(hypotheses)` / `bool(challenges)`.

Design decisions (proposed, for independent review):
- Exactly ONE legacy hypothesis must be marked `selected: True`. Competing hypotheses are
  not "also passing"; they become Alternatives that the falsifier must see rebutted.
- Legacy hypotheses without structured fields fail closed. No field is guessed.
- True gates never mean approval: the passport still ends at AWAITING_HUMAN_APPROVAL.
- Misconfiguration (e.g. reviewer == generator) raises loudly; it is not converted to False.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Optional, Sequence

from .claim import Claim, Proposition
from .enums import FalsificationOutcome, ReviewOutcome, SupportClass
from .errors import LemonError
from .evidence import EvidenceStore
from .falsify import Falsifier
from .grounding import ICFRScope, validate_scope
from .independence import AgentRun
from .passport import EvidencePassport
from .review import Alternative, Hypothesis, ReproRef, Reviewer
from .support import assess_support


class AdapterError(LemonError):
    """A legacy hypothesis cannot be converted without guessing."""


REQUIRED = ("hypothesis_id", "selected", "claim_text", "entity", "period_end", "assertion",
            "propositions", "evidence_ids")


def _req(d: Mapping, k: str):
    if k not in d or d[k] is None or d[k] == "":
        raise AdapterError(f"legacy hypothesis lacks structured field {k!r}")
    return d[k]


def _strs(v, name: str) -> tuple[str, ...]:
    if not isinstance(v, (list, tuple)) or not all(isinstance(x, str) and x for x in v):
        raise AdapterError(f"{name} must be a list of non-empty strings")
    return tuple(v)


def legacy_to_hypothesis(selected: Mapping, competitors: Sequence[Mapping], generator: AgentRun) -> Hypothesis:
    for k in REQUIRED:
        _req(selected, k)
    props = selected["propositions"]
    if not isinstance(props, (list, tuple)) or not props:
        raise AdapterError("propositions must be a non-empty list")
    ps = []
    for p in props:
        if not isinstance(p, Mapping) or set(p) != {"predicate", "value"}:
            raise AdapterError("each proposition must have exactly 'predicate' and 'value'")
        ps.append(Proposition(str(p["predicate"]), str(p["value"])))
    material = selected.get("material", True)          # default is the conservative choice
    causal = selected.get("causal", False)
    if not isinstance(material, bool) or not isinstance(causal, bool):
        raise AdapterError("material/causal must be booleans")
    claim = Claim(str(selected["hypothesis_id"]), str(selected["claim_text"]), str(selected["entity"]),
                  str(selected["period_end"]), str(selected["assertion"]), tuple(ps),
                  _strs(selected["evidence_ids"], "evidence_ids"), material, causal)
    alts = []
    for c in competitors:
        if not isinstance(c, Mapping):
            raise AdapterError("competing hypothesis must be a mapping")
        alts.append(Alternative(str(_req(c, "claim_text")),
                                _strs(c.get("rebuttal_evidence_ids", []), "rebuttal_evidence_ids")))
    return Hypothesis(claim.claim_id, claim, generator,
                      _strs(selected.get("assumptions", []), "assumptions"), tuple(alts),
                      _strs(selected.get("limitations", []), "limitations"),
                      str(selected.get("identification_strategy", "")))


@dataclass(frozen=True)
class GateDecision:
    support_ok: bool
    reviewer_ok: bool
    falsification_ok: bool
    passport: Optional[EvidencePassport]
    reasons: tuple[str, ...]


def _closed(reason: str) -> GateDecision:
    return GateDecision(False, False, False, None, (f"fail closed: {reason}",))


def assure_case(*, case_id: str, question: str, created_at: str, legacy_hypotheses: Sequence[Mapping],
                store: EvidenceStore, scope: ICFRScope, repro: Optional[ReproRef], generator: AgentRun,
                reviewer: Reviewer, falsifier: Falsifier,
                replay: Optional[Callable[[], str]] = None) -> GateDecision:
    if not legacy_hypotheses:
        return _closed("no hypotheses")
    selected = [h for h in legacy_hypotheses if isinstance(h, Mapping) and h.get("selected") is True]
    if len(selected) != 1:
        return _closed(f"exactly one selected hypothesis required, found {len(selected)}")
    competitors = [h for h in legacy_hypotheses if h is not selected[0]]
    try:
        hyp = legacy_to_hypothesis(selected[0], competitors, generator)
    except AdapterError as e:
        return _closed(str(e))
    sup = assess_support(hyp.claim, store)
    rv = reviewer.review(hyp, sup, validate_scope(scope), repro)
    fz = falsifier.falsify(hyp, scope, sup, replay=replay)
    pp = EvidencePassport(f"PP-{case_id}", case_id, created_at, hyp.claim.entity, hyp.claim.period_end,
                          question, EvidencePassport.records_from(store, hyp.claim.evidence_ids),
                          scope, hyp, sup, rv, fz, repro)
    reasons = tuple(rv.reasons) + tuple(f"falsification:{c.name}:{c.outcome}: {c.detail}"
                                        for c in fz.challenges if c.outcome.value != "SURVIVED")
    return GateDecision(sup.classification is SupportClass.SUPPORTED,
                        rv.outcome is ReviewOutcome.PASS,
                        fz.outcome is FalsificationOutcome.SURVIVED, pp, reasons)
