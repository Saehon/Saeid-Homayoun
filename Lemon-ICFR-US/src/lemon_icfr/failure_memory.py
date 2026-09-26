from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FailureRecord:
    run_id: str
    stage: str
    reason: str
    rejected_claim: str | None = None
    contradictions: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    model_tool_version: str | None = None


@dataclass
class FailureMemory:
    """In-memory fail-preserving record; persistence is delegated to governed storage."""

    records: list[FailureRecord] = field(default_factory=list)

    def remember(self, record: FailureRecord) -> None:
        self.records.append(record)

    def by_stage(self, stage: str) -> list[FailureRecord]:
        return [r for r in self.records if r.stage == stage]
