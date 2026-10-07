from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(slots=True)
class EvidenceItem:
    evidence_id: str
    source_type: str
    reference: str
    content_hash: str | None = None


@dataclass(slots=True)
class DecisionCase:
    case_id: str
    standard: str
    question: str
    risk: RiskLevel = RiskLevel.MEDIUM
    materiality: float | None = None
    evidence: list[EvidenceItem] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Hypothesis:
    hypothesis_id: str
    statement: str
    support: list[str] = field(default_factory=list)
    challenges: list[str] = field(default_factory=list)
    score: float = 0.0


@dataclass(slots=True)
class DecisionResult:
    case_id: str
    selected_hypothesis: Hypothesis | None
    hypotheses: list[Hypothesis]
    requires_human_approval: bool
    audit_trail: list[str] = field(default_factory=list)
