from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Literal

Sufficiency = Literal["SUFFICIENT", "PARTIAL", "INSUFFICIENT", "UNKNOWN"]
Risk = Literal["LOW", "MEDIUM", "HIGH"]

@dataclass
class AIReview:
    provider: str
    model: str
    evidence_sufficiency: Sufficiency
    risk_triage: Risk
    supported_findings: list[str] = field(default_factory=list)
    potential_exceptions: list[str] = field(default_factory=list)
    evidence_basis: list[str] = field(default_factory=list)
    uncertainty: list[str] = field(default_factory=list)
    recommended_human_action: str = "REVIEW"
    can_approve: bool = False
    final_professional_conclusion: None = None

    def to_dict(self) -> dict:
        data = asdict(self)
        data["can_approve"] = False
        data["final_professional_conclusion"] = None
        return data

ALLOWED_SUFFICIENCY = {"SUFFICIENT", "PARTIAL", "INSUFFICIENT", "UNKNOWN"}
ALLOWED_RISK = {"LOW", "MEDIUM", "HIGH"}

def validate_ai_review(review: AIReview, evidence_text: str) -> dict:
    issues: list[str] = []
    if review.evidence_sufficiency not in ALLOWED_SUFFICIENCY:
        issues.append("Invalid evidence_sufficiency value.")
    if review.risk_triage not in ALLOWED_RISK:
        issues.append("Invalid risk_triage value.")

    evidence_lower = evidence_text.lower()
    unsupported_basis = [
        basis for basis in review.evidence_basis
        if basis.strip() and basis.lower() not in evidence_lower
    ]
    if unsupported_basis:
        issues.append("One or more evidence_basis items are not present in supplied evidence.")
    if review.can_approve:
        issues.append("AI provider attempted to claim approval authority.")

    return {
        "valid": not issues,
        "issues": issues,
        "unsupported_evidence_basis": unsupported_basis,
        "normalized_review": review.to_dict(),
    }
