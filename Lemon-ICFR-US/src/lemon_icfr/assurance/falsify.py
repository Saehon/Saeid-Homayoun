"""Independent falsification (P0-2). Replaces the boolean "a challenge exists" falsification gate.

The falsifier tries to destroy the hypothesis. A required challenge that cannot be
run makes the result INCONCLUSIVE, never SURVIVED.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from .enums import ChallengeOutcome as C, FalsificationOutcome, Independence, SourceTier, SupportClass
from .errors import ProviderError, ProviderOutputError
from .evidence import EvidenceStore
from .grounding import ICFRScope
from .independence import AgentRun, assess_independence
from .providers import FakeProvider, parse_challenges
from .review import Hypothesis
from .support import SupportResult

REQUIRED = ("contradictory_evidence", "unsupported_inference", "entity_match", "period_match",
            "assertion_match", "provenance_rights", "source_hierarchy", "alternative_explanations",
            "causal_ambiguity", "population_evidence", "materiality", "benchmark_leakage", "reproduction")


@dataclass(frozen=True)
class ChallengeResult:
    name: str
    outcome: C
    detail: str


@dataclass(frozen=True)
class FalsificationResult:
    outcome: FalsificationOutcome
    challenges: tuple[ChallengeResult, ...]
    falsifier: AgentRun
    independence: Independence


class Falsifier:
    def __init__(self, run: AgentRun, store: EvidenceStore, provider: Optional[FakeProvider] = None):
        if run.role != "falsifier":
            raise ValueError("Falsifier requires an AgentRun with role='falsifier'")
        self.run, self.store, self.provider = run, store, provider

    def falsify(self, hyp: Hypothesis, scope: ICFRScope, support: SupportResult, *,
                replay: Optional[Callable[[], str]] = None,
                case_is_development: Optional[bool] = None,
                used_as_confirmatory: bool = False) -> FalsificationResult:
        indep = assess_independence(hyp.generator, self.run)
        claim, r = hyp.claim, []
        add = lambda n, o, d="": r.append(ChallengeResult(n, o, d))

        # 1. contradictory authoritative evidence, including evidence the claim OMITTED
        cited = set(claim.evidence_ids)
        sup_tier = min((self.store.get(e).tier for p in support.propositions for e in p.supporting
                        if self.store.get(e)), default=SourceTier.SECONDARY + 1)
        omitted = []
        for ev in self.store.all():
            if ev.evidence_id in cited or ev.admissibility_issues():
                continue
            for f in ev.facts:
                for p in claim.propositions:
                    if (f.entity, f.period_end, f.predicate) == (claim.entity, claim.period_end, p.predicate) \
                            and f.value != p.value and ev.tier <= sup_tier:
                        omitted.append(ev.evidence_id)
        if support.classification is SupportClass.CONTRADICTED:
            add("contradictory_evidence", C.REFUTED, "cited evidence contradicts the claim")
        elif omitted:
            add("contradictory_evidence", C.REFUTED, f"uncited equal/higher-authority evidence contradicts: {sorted(set(omitted))}")
        else:
            add("contradictory_evidence", C.SURVIVED, "no contradicting admissible evidence found in store")

        # 2. unsupported inference
        if support.classification in (SupportClass.UNSUPPORTED, SupportClass.INSUFFICIENT_EVIDENCE):
            add("unsupported_inference", C.REFUTED, f"support={support.classification}")
        else:
            add("unsupported_inference", C.SURVIVED)

        add("entity_match", C.REFUTED if scope.entity != claim.entity else C.SURVIVED, f"{scope.entity} vs {claim.entity}")
        add("period_match", C.REFUTED if scope.period_end != claim.period_end else C.SURVIVED, f"{scope.period_end} vs {claim.period_end}")
        add("assertion_match", C.REFUTED if scope.assertion != claim.assertion else C.SURVIVED, f"{scope.assertion} vs {claim.assertion}")

        bad = [f for f in support.findings if f.status != "ADMISSIBLE"]
        add("provenance_rights", C.REFUTED if bad else C.SURVIVED,
            "; ".join(f"{f.evidence_id}:{f.status}:{','.join(f.issues)}" for f in bad))

        tiers = [self.store.get(e).tier for p in support.propositions for e in p.supporting if self.store.get(e)]
        if claim.material and tiers and min(tiers) >= SourceTier.SECONDARY:
            add("source_hierarchy", C.REFUTED, "material claim rests only on secondary sources")
        else:
            add("source_hierarchy", C.SURVIVED, "; ".join(support.conflicts) or "no hierarchy conflict")

        unrebutted = [a.description for a in hyp.alternatives
                      if not any(self.store.get(e) and not self.store.get(e).admissibility_issues()
                                 for e in a.rebuttal_evidence_ids)]
        if claim.material and not hyp.alternatives:
            add("alternative_explanations", C.NOT_TESTABLE, "no alternatives supplied to test")
        elif unrebutted:
            add("alternative_explanations", C.NOT_TESTABLE, f"alternatives not rebutted by evidence: {unrebutted}")
        else:
            add("alternative_explanations", C.SURVIVED)

        if claim.causal and not hyp.identification_strategy:
            add("causal_ambiguity", C.NOT_TESTABLE, "causal claim without identification strategy")
        else:
            add("causal_ambiguity", C.SURVIVED, "non-causal claim" if not claim.causal else hyp.identification_strategy)

        t = scope.test
        if t is None:
            add("population_evidence", C.SURVIVED, "not applicable: no operating-effectiveness test in scope")
        elif not t.population_source or t.population_size is None or not t.sampling_rule:
            add("population_evidence", C.REFUTED, "operating-effectiveness test lacks population/sampling evidence")
        else:
            add("population_evidence", C.SURVIVED)

        add("materiality", C.REFUTED if claim.material and support.classification is SupportClass.PARTIALLY_SUPPORTED
            else C.SURVIVED, "material claim only partially supported" if claim.material else "")

        if case_is_development is None:
            add("benchmark_leakage", C.SURVIVED, "not a benchmark evaluation")
        elif case_is_development and used_as_confirmatory:
            add("benchmark_leakage", C.REFUTED, "development case used as confirmatory evidence")
        else:
            add("benchmark_leakage", C.SURVIVED)

        if replay is None:
            add("reproduction", C.NOT_TESTABLE, "no replay function supplied")
        else:
            a, b = replay(), replay()
            add("reproduction", C.SURVIVED if a == b else C.REFUTED, f"replay hashes {a[:12]} / {b[:12]}")

        if self.provider is not None:
            # A configured provider is a REQUIRED challenger: failure, an empty list, or any
            # meaningless (downgraded) challenge makes the result INCONCLUSIVE, never SURVIVED.
            provider_ok = True
            try:
                pcs = parse_challenges(self.provider.complete(claim.text))
                if not pcs:
                    provider_ok = False
                    add("provider", C.NOT_TESTABLE, "provider returned no challenges")
                for pc in pcs:
                    add(f"provider:{pc.name}", pc.outcome, pc.detail)
                    if pc.outcome is C.NOT_TESTABLE:
                        provider_ok = False
            except (ProviderOutputError, ProviderError) as e:
                provider_ok = False
                add("provider", C.NOT_TESTABLE, f"provider failure: {e}")
            if not provider_ok:
                add("provider_required", C.NOT_TESTABLE, "configured provider produced no usable challenge")

        outs = {c.name: c.outcome for c in r}
        if C.REFUTED in outs.values():
            outcome = FalsificationOutcome.REFUTED
        elif any(outs.get(n) is C.NOT_TESTABLE for n in REQUIRED) or "provider_required" in outs:
            outcome = FalsificationOutcome.INCONCLUSIVE
        else:
            outcome = FalsificationOutcome.SURVIVED
        return FalsificationResult(outcome, tuple(r), self.run, indep)
