from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source: str
    provenance: str
    rights_status: str
    content: str
    version: str | None = None
    evidence_class: str = "real"
    chronology_status: str = "known"


@dataclass
class Finding:
    agent: str
    claim: str
    evidence_refs: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    alternative_explanations: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    model_tool_version: str = "deterministic-core"
    requires_human_review: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class GateResult:
    gate: str
    passed: bool
    notes: list[str] = field(default_factory=list)


@dataclass
class LemonCaseResult:
    case_id: str
    findings: list[Finding]
    gates: list[GateResult]
    contradictions: list[str]
    status: str
    human_disposition: str | None = None
