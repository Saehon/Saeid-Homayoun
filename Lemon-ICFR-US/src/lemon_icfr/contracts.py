from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json


@dataclass
class AgentHandoff:
    """Mother-inherited machine-readable AI-to-AI handoff contract."""

    task_id: str
    run_id: str
    sender: str
    receiver: str
    claim: str
    evidence_refs: list[str] = field(default_factory=list)
    method: str = ""
    assumptions: list[str] = field(default_factory=list)
    confidence: float | None = None
    contradictions: list[str] = field(default_factory=list)
    failure_status: str | None = None
    provenance: str = ""
    parent_hash: str | None = None
    independence_class: str = "role-separated"
    risk_flags: list[str] = field(default_factory=list)
    required_next_action: str = "human_review"

    def canonical_payload(self) -> dict:
        return asdict(self)

    def content_sha256(self) -> str:
        payload = json.dumps(
            self.canonical_payload(), sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class VariableDNA:
    """Reproducible definition of a material variable/construct used by Lemon."""

    name: str
    definition: str
    source: str
    construction_rule: str
    chronology_rule: str
    version: str


@dataclass(frozen=True)
class ChainOfEvidenceEntry:
    claim_id: str
    evidence_ref: str
    transformation_ref: str | None
    test_ref: str | None
    result_ref: str | None
    falsification_ref: str | None
    replication_ref: str | None
    human_decision_ref: str | None
