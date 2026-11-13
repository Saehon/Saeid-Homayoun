"""Human Approval Gate (section 17). AI cannot populate an authorised human decision.

The signing key lives with the human approval UI (out of band). The AI pipeline only
holds a verifier. A disposition without a valid signature from a registered human,
bound to the exact passport hash, is rejected.
"""
from __future__ import annotations

import hashlib
import hmac
import json
from dataclasses import asdict, dataclass, replace

from .enums import FalsificationOutcome, HumanDecision, ReviewOutcome
from .errors import SelfApprovalError


@dataclass(frozen=True)
class HumanDisposition:
    reviewer_id: str
    reviewer_role: str
    decision: HumanDecision
    timestamp: str
    comments: str
    findings_reviewed: tuple[str, ...]
    evidence_reviewed: tuple[str, ...]
    override_reason: str
    conditions: tuple[str, ...]
    passport_hash: str
    signature: str = ""

    def payload(self) -> bytes:
        d = asdict(self)
        d.pop("signature")
        d["decision"] = self.decision.value
        return json.dumps(d, sort_keys=True, separators=(",", ":")).encode()


def sign_disposition(d: HumanDisposition, key: bytes) -> HumanDisposition:
    """Called ONLY by the human approval UI, never by the agent pipeline."""
    return replace(d, signature=hmac.new(key, d.payload(), hashlib.sha256).hexdigest())


class HumanRegistry:
    def __init__(self, humans: dict[str, str], agent_ids: set[str]):
        overlap = set(humans) & set(agent_ids)
        if overlap:
            raise ValueError(f"ids registered as both human and agent: {overlap}")
        self.humans, self.agent_ids = dict(humans), set(agent_ids)


class HumanGate:
    def __init__(self, registry: HumanRegistry, verify_key: bytes):
        self.registry, self._key = registry, verify_key

    def accept(self, d: HumanDisposition, *, passport_hash: str, review: ReviewOutcome,
               falsification: FalsificationOutcome) -> HumanDisposition:
        if d.reviewer_id in self.registry.agent_ids:
            raise SelfApprovalError("an AI agent identity cannot record a human disposition")
        if d.reviewer_id not in self.registry.humans:
            raise SelfApprovalError(f"reviewer {d.reviewer_id!r} is not a registered human approver")
        if self.registry.humans[d.reviewer_id] != d.reviewer_role:
            raise SelfApprovalError("reviewer role does not match registry")
        expected = hmac.new(self._key, d.payload(), hashlib.sha256).hexdigest()
        if not d.signature or not hmac.compare_digest(expected, d.signature):
            raise SelfApprovalError("missing or invalid human signature")
        if d.passport_hash != passport_hash:
            raise SelfApprovalError("disposition is bound to a different passport version")
        if d.decision in (HumanDecision.APPROVED, HumanDecision.APPROVED_WITH_CONDITIONS):
            if not d.findings_reviewed or not d.evidence_reviewed:
                raise SelfApprovalError("approval requires listing findings and evidence reviewed")
            if (review is not ReviewOutcome.PASS or falsification is not FalsificationOutcome.SURVIVED) \
                    and not d.override_reason.strip():
                raise SelfApprovalError("approving over a non-PASS review/falsification requires override_reason")
            if d.decision is HumanDecision.APPROVED_WITH_CONDITIONS and not d.conditions:
                raise SelfApprovalError("APPROVED_WITH_CONDITIONS requires conditions")
        return d
