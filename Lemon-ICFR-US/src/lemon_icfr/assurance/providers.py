"""Validated provider outputs (section 19). Providers are execution layers, not authority."""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Callable, Optional

from .claim import Claim
from .enums import ChallengeOutcome, ReviewOutcome
from .errors import ProviderError, ProviderOutputError


@dataclass(frozen=True)
class ReviewVerdict:
    outcome: ReviewOutcome
    reasoning: str
    evidence_refs: tuple[str, ...]


_REVIEW_KEYS = {"outcome", "reasoning", "evidence_refs", "entity", "period_end"}


def parse_review_verdict(raw: str, claim: Claim) -> ReviewVerdict:
    try:
        obj = json.loads(raw)
    except (TypeError, json.JSONDecodeError) as e:
        raise ProviderOutputError(f"malformed JSON: {e}") from e
    if not isinstance(obj, dict):
        raise ProviderOutputError("verdict must be a JSON object")
    keys = set(obj)
    if keys - _REVIEW_KEYS:
        raise ProviderOutputError(f"unexpected fields: {sorted(keys - _REVIEW_KEYS)}")
    if _REVIEW_KEYS - keys:
        raise ProviderOutputError(f"missing fields: {sorted(_REVIEW_KEYS - keys)}")
    try:
        outcome = ReviewOutcome(obj["outcome"])
    except ValueError as e:
        raise ProviderOutputError(f"invalid outcome {obj['outcome']!r}") from e
    if not isinstance(obj["reasoning"], str) or not obj["reasoning"].strip():
        raise ProviderOutputError("empty reasoning")
    refs = obj["evidence_refs"]
    if not isinstance(refs, list) or not all(isinstance(r, str) for r in refs):
        raise ProviderOutputError("evidence_refs must be a list of strings")
    bad = set(refs) - set(claim.evidence_ids)
    if bad:
        raise ProviderOutputError(f"evidence_refs not cited by claim: {sorted(bad)}")
    if obj["entity"] != claim.entity:
        raise ProviderOutputError("verdict entity does not match claim entity")
    if obj["period_end"] != claim.period_end:
        raise ProviderOutputError("verdict period does not match claim period")
    return ReviewVerdict(outcome, obj["reasoning"], tuple(refs))


@dataclass(frozen=True)
class ProviderChallenge:
    name: str
    outcome: ChallengeOutcome
    detail: str
    evidence_ids: tuple[str, ...]


def parse_challenges(raw: str) -> list[ProviderChallenge]:
    """Meaningless challenges (no detail, no evidence) are downgraded to NOT_TESTABLE."""
    try:
        obj = json.loads(raw)
    except (TypeError, json.JSONDecodeError) as e:
        raise ProviderOutputError(f"malformed JSON: {e}") from e
    if not isinstance(obj, list):
        raise ProviderOutputError("challenges must be a JSON list")
    out = []
    for item in obj:
        if not isinstance(item, dict) or set(item) != {"name", "outcome", "detail", "evidence_ids"}:
            raise ProviderOutputError("challenge must have exactly name/outcome/detail/evidence_ids")
        try:
            oc = ChallengeOutcome(item["outcome"])
        except ValueError as e:
            raise ProviderOutputError(f"invalid challenge outcome {item['outcome']!r}") from e
        detail = str(item["detail"]).strip()
        ids = tuple(item["evidence_ids"]) if isinstance(item["evidence_ids"], list) else ()
        if oc is ChallengeOutcome.SURVIVED and (len(detail) < 20 or not ids):
            oc, detail = ChallengeOutcome.NOT_TESTABLE, f"meaningless provider challenge downgraded: {detail!r}"
        out.append(ProviderChallenge(str(item["name"]), oc, detail, ids))
    return out


class FakeProvider:
    """Deterministic provider for tests. No network, no paid API."""

    def __init__(self, name: str, model: str, respond: Callable[[str], str] | str,
                 fail: Optional[Exception] = None):
        self.name, self.model, self._respond, self._fail = name, model, respond, fail

    def complete(self, prompt: str) -> str:
        if self._fail is not None:
            raise ProviderError(f"provider failure: {self._fail!r}") from self._fail
        return self._respond(prompt) if callable(self._respond) else self._respond
