"""Canonical Evidence Passport (section 18). Fails closed on missing material fields."""
from __future__ import annotations

import dataclasses
import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

from .enums import FinalStatus, HumanDecision
from .evidence import EvidenceStore
from .falsify import FalsificationResult
from .grounding import ICFRScope
from .human_gate import HumanDisposition
from .review import Hypothesis, ReproRef, ReviewResult
from .support import SupportResult
from .twin import TwinResult

SCHEMA_VERSION = "lemon.passport/1.0"


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    source: str
    source_type: str
    tier: int
    provenance: str
    rights: str
    version: str
    sha256: str
    retrieved_at: str


def _jsonable(o: Any) -> Any:
    if isinstance(o, Enum):
        return o.value
    if dataclasses.is_dataclass(o):
        return {f.name: _jsonable(getattr(o, f.name)) for f in dataclasses.fields(o)
                if f.name != "content"}
    if isinstance(o, (list, tuple)):
        return [_jsonable(x) for x in o]
    if isinstance(o, dict):
        return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, bytes):
        return hashlib.sha256(o).hexdigest()
    return o


@dataclass(frozen=True)
class EvidencePassport:
    passport_id: str
    case_id: str
    created_at: str
    entity: str
    period_end: str
    question: str
    evidence: tuple[EvidenceRecord, ...]
    scope: ICFRScope
    hypothesis: Hypothesis
    support: SupportResult
    review: Optional[ReviewResult]
    falsification: Optional[FalsificationResult]
    repro: Optional[ReproRef]
    twin: tuple[TwinResult, ...] = ()
    human: Optional[HumanDisposition] = None
    schema_version: str = field(default=SCHEMA_VERSION)

    @staticmethod
    def records_from(store: EvidenceStore, ids) -> tuple[EvidenceRecord, ...]:
        out = []
        for i in ids:
            e = store.get(i)
            if e is not None:
                out.append(EvidenceRecord(e.evidence_id, e.source, e.source_type, int(e.tier), e.provenance,
                                          e.rights.value, e.version, e.sha256, e.retrieved_at))
        return tuple(out)

    def missing_material_fields(self) -> list[str]:
        m = [n for n in ("passport_id", "case_id", "created_at", "entity", "period_end", "question")
             if not getattr(self, n)]
        if not self.evidence:
            m.append("evidence")
        for n in ("review", "falsification", "repro"):
            if getattr(self, n) is None:
                m.append(n)
        if self.repro is not None and self.repro.missing():
            m.append(f"repro.{self.repro.missing()}")
        return m

    def to_dict(self, include_human: bool = True) -> dict:
        d = _jsonable(self)
        if not include_human:
            d.pop("human", None)
        return d

    def content_hash(self) -> str:
        """Hash of everything except the human disposition: what the human signs."""
        b = json.dumps(self.to_dict(include_human=False), sort_keys=True, separators=(",", ":")).encode()
        return hashlib.sha256(b).hexdigest()

    def to_json(self) -> str:
        d = self.to_dict()
        d["content_hash"] = self.content_hash()
        d["final_status"] = self.final_status().value
        return json.dumps(d, sort_keys=True, indent=2)

    def final_status(self, store: Optional[EvidenceStore] = None) -> FinalStatus:
        if self.missing_material_fields():
            return FinalStatus.BLOCKED
        if store is not None:
            for rec in self.evidence:
                e = store.get(rec.evidence_id)
                if e is None or e.sha256 != rec.sha256 or e.admissibility_issues():
                    return FinalStatus.INVALIDATED
        if self.human is None:
            return FinalStatus.AWAITING_HUMAN_APPROVAL
        if self.human.passport_hash != self.content_hash():
            return FinalStatus.INVALIDATED
        return {
            HumanDecision.APPROVED: FinalStatus.APPROVED,
            HumanDecision.APPROVED_WITH_CONDITIONS: FinalStatus.APPROVED_WITH_CONDITIONS,
            HumanDecision.REJECTED: FinalStatus.REJECTED,
            HumanDecision.RETURN_FOR_MORE_EVIDENCE: FinalStatus.RETURNED_FOR_MORE_EVIDENCE,
            HumanDecision.ESCALATED: FinalStatus.ESCALATED,
        }[self.human.decision]
