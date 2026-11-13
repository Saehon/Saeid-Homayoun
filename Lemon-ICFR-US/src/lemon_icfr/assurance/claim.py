from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Proposition:
    predicate: str
    value: str


@dataclass(frozen=True)
class Claim:
    claim_id: str
    text: str
    entity: str
    period_end: str
    assertion: str
    propositions: tuple[Proposition, ...]
    evidence_ids: tuple[str, ...]
    material: bool = True
    causal: bool = False
