from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Optional

from .enums import Rights, SourceTier


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


@dataclass(frozen=True)
class Fact:
    """A structured statement an evidence item makes (entity, period, predicate, value)."""
    entity: str
    period_end: str
    predicate: str
    value: str


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source: str
    source_type: str
    tier: SourceTier
    provenance: str
    rights: Rights
    version: str
    sha256: str
    retrieved_at: str
    content: bytes = field(repr=False)
    facts: tuple[Fact, ...] = ()

    def admissibility_issues(self) -> list[str]:
        issues = []
        if not self.provenance.strip():
            issues.append("missing provenance")
        if self.rights is Rights.UNKNOWN:
            issues.append("rights/licence unknown")
        if sha256(self.content) != self.sha256:
            issues.append("checksum mismatch")
        if not self.retrieved_at:
            issues.append("missing retrieval timestamp")
        return issues


def make_evidence(evidence_id: str, *, content: bytes, facts=(), source="", source_type="filing",
                  tier=SourceTier.SEC_FILING, provenance="", rights=Rights.PUBLIC_DOMAIN,
                  version="1", retrieved_at="2026-10-04T00:00:00Z") -> EvidenceItem:
    return EvidenceItem(evidence_id, source, source_type, tier, provenance, rights, version,
                        sha256(content), retrieved_at, content, tuple(facts))


class EvidenceStore:
    def __init__(self) -> None:
        self._items: dict[str, EvidenceItem] = {}

    def add(self, item: EvidenceItem) -> None:
        if item.evidence_id in self._items:
            raise ValueError(f"duplicate evidence_id {item.evidence_id}")
        self._items[item.evidence_id] = item

    def get(self, evidence_id: str) -> Optional[EvidenceItem]:
        return self._items.get(evidence_id)

    def remove(self, evidence_id: str) -> None:
        self._items.pop(evidence_id, None)

    def replace(self, item: EvidenceItem) -> None:
        self._items[item.evidence_id] = item

    def all(self) -> list[EvidenceItem]:
        return list(self._items.values())
