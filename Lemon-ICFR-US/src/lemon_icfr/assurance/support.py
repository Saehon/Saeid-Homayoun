"""Evidence-ID is not evidence support (P0-4).

Deterministic support determination over structured facts. A semantic (LLM) judge
may be layered on top later, but it may only downgrade, never upgrade.
"""
from __future__ import annotations

from dataclasses import dataclass

from .claim import Claim
from .enums import SupportClass
from .evidence import EvidenceStore


@dataclass(frozen=True)
class EvidenceFinding:
    evidence_id: str
    status: str            # ADMISSIBLE | MISSING | INADMISSIBLE
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class PropositionResult:
    predicate: str
    classification: SupportClass
    supporting: tuple[str, ...]
    contradicting: tuple[str, ...]
    note: str = ""


@dataclass(frozen=True)
class SupportResult:
    classification: SupportClass
    propositions: tuple[PropositionResult, ...]
    findings: tuple[EvidenceFinding, ...]
    conflicts: tuple[str, ...]     # recorded, never silent
    notes: tuple[str, ...]


def assess_support(claim: Claim, store: EvidenceStore) -> SupportResult:
    findings, usable, notes = [], [], []
    if not claim.evidence_ids:
        return SupportResult(SupportClass.INSUFFICIENT_EVIDENCE, (), (), (), ("claim cites no evidence",))

    for eid in claim.evidence_ids:
        ev = store.get(eid)
        if ev is None:
            findings.append(EvidenceFinding(eid, "MISSING", ("evidence id not found in store",)))
            continue
        issues = ev.admissibility_issues()
        if issues:
            findings.append(EvidenceFinding(eid, "INADMISSIBLE", tuple(issues)))
            continue
        findings.append(EvidenceFinding(eid, "ADMISSIBLE"))
        usable.append(ev)

    missing = [f.evidence_id for f in findings if f.status == "MISSING"]
    if missing and claim.material:
        return SupportResult(SupportClass.UNSUPPORTED, (), tuple(findings), (),
                             (f"material claim cites non-existent evidence: {missing}",))
    if not usable:
        return SupportResult(SupportClass.INSUFFICIENT_EVIDENCE, (), tuple(findings), (),
                             ("no admissible evidence",))

    prop_results, conflicts = [], []
    for prop in claim.propositions:
        sup, con, wrong_scope = [], [], []
        for ev in usable:
            for f in ev.facts:
                if f.predicate != prop.predicate:
                    continue
                if f.entity != claim.entity or f.period_end != claim.period_end:
                    wrong_scope.append(f"{ev.evidence_id}:{f.entity}/{f.period_end}")
                    continue
                (sup if f.value == prop.value else con).append(ev)
        if not sup and not con:
            note = f"facts exist only for other entity/period: {wrong_scope}" if wrong_scope else "no relevant fact"
            prop_results.append(PropositionResult(prop.predicate, SupportClass.UNSUPPORTED, (), (), note))
            continue
        best_sup = min((e.tier for e in sup), default=99)
        best_con = min((e.tier for e in con), default=99)
        if con and best_con <= best_sup:
            cls = SupportClass.CONTRADICTED
            note = "contradicted by equal-or-higher-authority evidence"
        else:
            cls = SupportClass.SUPPORTED
            note = ""
            if con:
                msg = (f"{prop.predicate}: lower-authority source(s) {[e.evidence_id for e in con]} contradict "
                       f"higher-authority support; primary evidence prevails, conflict recorded")
                conflicts.append(msg)
                note = msg
        prop_results.append(PropositionResult(prop.predicate, cls,
                                              tuple(e.evidence_id for e in sup),
                                              tuple(e.evidence_id for e in con), note))

    classes = [p.classification for p in prop_results]
    if not classes:
        overall = SupportClass.INSUFFICIENT_EVIDENCE
        notes.append("claim has no propositions")
    elif SupportClass.CONTRADICTED in classes:
        overall = SupportClass.CONTRADICTED
    elif all(c is SupportClass.SUPPORTED for c in classes):
        overall = SupportClass.SUPPORTED
    elif SupportClass.SUPPORTED in classes:
        overall = SupportClass.PARTIALLY_SUPPORTED
    else:
        overall = SupportClass.UNSUPPORTED
    if any(f.status != "ADMISSIBLE" for f in findings) and overall is SupportClass.SUPPORTED:
        overall = SupportClass.PARTIALLY_SUPPORTED
        notes.append("some cited evidence inadmissible or missing")
    return SupportResult(overall, tuple(prop_results), tuple(findings), tuple(conflicts), tuple(notes))
