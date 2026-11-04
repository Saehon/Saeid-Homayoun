"""Genuine independent review (P0-1). Replaces the boolean "a hypothesis exists" reviewer gate."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .claim import Claim
from .enums import Independence, ReviewOutcome, SupportClass, worst
from .errors import ProviderError, ProviderOutputError
from .independence import AgentRun, assess_independence
from .providers import FakeProvider, parse_review_verdict
from .support import SupportResult


@dataclass(frozen=True)
class Alternative:
    description: str
    rebuttal_evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Hypothesis:
    hypothesis_id: str
    claim: Claim
    generator: AgentRun
    assumptions: tuple[str, ...] = ()
    alternatives: tuple[Alternative, ...] = ()
    limitations: tuple[str, ...] = ()
    identification_strategy: str = ""     # required for causal claims


@dataclass(frozen=True)
class ReproRef:
    code_version: str
    repo_commit: str
    data_version: str
    config_hash: str
    environment: str
    model_provider: str
    model_version: str
    prompt_version: str
    seed: Optional[int] = None

    def missing(self) -> list[str]:
        return [k for k, v in self.__dict__.items() if k != "seed" and not v]


@dataclass(frozen=True)
class ReviewResult:
    outcome: ReviewOutcome
    reasons: tuple[str, ...]
    reviewer: AgentRun
    independence: Independence
    provider_outcome: Optional[str] = None


_SUPPORT_MAP = {
    SupportClass.SUPPORTED: ReviewOutcome.PASS,
    SupportClass.PARTIALLY_SUPPORTED: ReviewOutcome.ESCALATE,
    SupportClass.UNSUPPORTED: ReviewOutcome.FAIL,
    SupportClass.INSUFFICIENT_EVIDENCE: ReviewOutcome.INSUFFICIENT_EVIDENCE,
    SupportClass.CONTRADICTED: ReviewOutcome.CONTRADICTED,
}


class Reviewer:
    def __init__(self, run: AgentRun, provider: Optional[FakeProvider] = None):
        if run.role != "reviewer":
            raise ValueError("Reviewer requires an AgentRun with role='reviewer'")
        self.run, self.provider = run, provider

    def review(self, hyp: Hypothesis, support: SupportResult, scope_issues: list[str],
               repro: Optional[ReproRef]) -> ReviewResult:
        indep = assess_independence(hyp.generator, self.run)   # raises on self-review
        claim, reasons = hyp.claim, []
        outcome = _SUPPORT_MAP[support.classification]
        reasons.append(f"evidence support: {support.classification}")
        if support.conflicts:
            outcome = worst(outcome, ReviewOutcome.ESCALATE)
            reasons += [f"source conflict: {c}" for c in support.conflicts]
        if scope_issues:
            outcome = worst(outcome, ReviewOutcome.FAIL)
            reasons += [f"ICFR/COSO grounding: {i}" for i in scope_issues]
        if repro is None or repro.missing():
            outcome = worst(outcome, ReviewOutcome.FAIL)
            reasons.append(f"reproducibility reference incomplete: {repro.missing() if repro else 'absent'}")
        if claim.material and not hyp.alternatives:
            outcome = worst(outcome, ReviewOutcome.ESCALATE)
            reasons.append("material claim with no alternative explanations considered")
        if claim.causal and not hyp.identification_strategy:
            outcome = worst(outcome, ReviewOutcome.ESCALATE)
            reasons.append("causal claim without identification strategy")
        if not hyp.limitations:
            reasons.append("note: no limitations stated")

        provider_outcome = None
        if self.provider is not None:
            try:
                verdict = parse_review_verdict(self.provider.complete(self._prompt(hyp, support)), claim)
                provider_outcome = verdict.outcome.value
                outcome = worst(outcome, verdict.outcome)          # provider can only downgrade
                reasons.append(f"provider verdict: {verdict.outcome}: {verdict.reasoning}")
            except (ProviderOutputError, ProviderError) as e:
                provider_outcome = "PROVIDER_FAILURE"
                outcome = worst(outcome, ReviewOutcome.ESCALATE)
                reasons.append(f"provider failure, fail closed: {e}")
        return ReviewResult(outcome, tuple(reasons), self.run, indep, provider_outcome)

    @staticmethod
    def _prompt(hyp: Hypothesis, support: SupportResult) -> str:
        return f"Review claim {hyp.claim.claim_id}: {hyp.claim.text}. Support: {support.classification}."
