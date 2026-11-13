from enum import Enum, IntEnum


class _S(str, Enum):
    def __str__(self) -> str:
        return self.value


class SupportClass(_S):
    SUPPORTED = "SUPPORTED"
    PARTIALLY_SUPPORTED = "PARTIALLY_SUPPORTED"
    UNSUPPORTED = "UNSUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class ReviewOutcome(_S):
    PASS = "PASS"
    ESCALATE = "ESCALATE"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"
    FAIL = "FAIL"
    CONTRADICTED = "CONTRADICTED"


_REVIEW_RANK = {ReviewOutcome.PASS: 0, ReviewOutcome.ESCALATE: 1,
                ReviewOutcome.INSUFFICIENT_EVIDENCE: 2, ReviewOutcome.FAIL: 3,
                ReviewOutcome.CONTRADICTED: 4}


def worst(a: "ReviewOutcome", b: "ReviewOutcome") -> "ReviewOutcome":
    """Combine two review outcomes; the more severe always wins (no upgrades)."""
    return a if _REVIEW_RANK[a] >= _REVIEW_RANK[b] else b


class ChallengeOutcome(_S):
    SURVIVED = "SURVIVED"
    REFUTED = "REFUTED"
    NOT_TESTABLE = "NOT_TESTABLE"


class FalsificationOutcome(_S):
    SURVIVED = "SURVIVED"
    REFUTED = "REFUTED"
    INCONCLUSIVE = "INCONCLUSIVE"


class Independence(_S):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class HumanDecision(_S):
    APPROVED = "APPROVED"
    APPROVED_WITH_CONDITIONS = "APPROVED_WITH_CONDITIONS"
    REJECTED = "REJECTED"
    RETURN_FOR_MORE_EVIDENCE = "RETURN_FOR_MORE_EVIDENCE"
    ESCALATED = "ESCALATED"


class ScientificStatus(_S):
    ENGINEERING_PASS = "ENGINEERING_PASS"
    SCIENTIFIC_HOLD = "SCIENTIFIC_HOLD"
    DEVELOPMENT_ONLY = "DEVELOPMENT_ONLY"
    PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"
    VERIFIED = "VERIFIED"
    CONFIRMATORY_PASS = "CONFIRMATORY_PASS"
    FAILED = "FAILED"
    QUARANTINED = "QUARANTINED"


class VariableStatus(_S):
    VERIFIED = "VERIFIED"
    PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"
    PENDING = "PENDING"
    SECONDARY = "SECONDARY"
    UNVERIFIED = "UNVERIFIED"
    QUARANTINED = "QUARANTINED"


class Rights(_S):
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    OPEN_LICENSE = "OPEN_LICENSE"
    LICENSED_REDISTRIBUTABLE = "LICENSED_REDISTRIBUTABLE"
    LICENSED_RESTRICTED = "LICENSED_RESTRICTED"   # usable privately, never published
    UNKNOWN = "UNKNOWN"                           # inadmissible


class SourceTier(IntEnum):
    """Lower number = higher authority. Secondary sources never silently outrank primary."""
    SEC = 1
    PCAOB = 2
    SOX404 = 3
    COSO = 4
    SEC_FILING = 5
    XBRL = 6
    COMPANY_PRIMARY = 7
    LICENSED_DATASET = 8
    SECONDARY = 9


class FinalStatus(_S):
    BLOCKED = "BLOCKED"
    INVALIDATED = "INVALIDATED"
    AWAITING_HUMAN_APPROVAL = "AWAITING_HUMAN_APPROVAL"
    APPROVED = "APPROVED"
    APPROVED_WITH_CONDITIONS = "APPROVED_WITH_CONDITIONS"
    REJECTED = "REJECTED"
    RETURNED_FOR_MORE_EVIDENCE = "RETURNED_FOR_MORE_EVIDENCE"
    ESCALATED = "ESCALATED"
