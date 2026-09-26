from __future__ import annotations

from typing import Protocol

from lemon_icfr.models import EvidenceItem, Finding


class ModelProvider(Protocol):
    """Replaceable model-provider contract used by Lemon."""

    name: str

    def generate_hypotheses(
        self, case_id: str, evidence: list[EvidenceItem], question: str
    ) -> list[Finding]:
        ...

    def challenge_claim(
        self, case_id: str, evidence: list[EvidenceItem], finding: Finding
    ) -> Finding:
        ...

    def lineage(self) -> str:
        ...
