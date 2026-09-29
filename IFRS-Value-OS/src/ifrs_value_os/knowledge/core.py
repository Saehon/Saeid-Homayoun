from __future__ import annotations

from dataclasses import dataclass

from ifrs_value_os.contracts import DecisionCase


@dataclass(slots=True)
class KnowledgeBundle:
    standard: str
    evidence_ids: list[str]
    retrieved_context: list[str]


class KnowledgeCore:
    """Retrieval boundary for standards metadata, evidence and enterprise context.

    Licensed IFRS text must be supplied through an authorized source at runtime.
    """

    def retrieve(self, case: DecisionCase) -> KnowledgeBundle:
        return KnowledgeBundle(
            standard=case.standard,
            evidence_ids=[e.evidence_id for e in case.evidence],
            retrieved_context=[case.question],
        )
