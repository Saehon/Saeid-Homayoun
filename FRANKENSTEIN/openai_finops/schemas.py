from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field


Severity = Literal["low", "medium", "high", "critical"]
RiskDomain = Literal[
    "finance_controls",
    "forensic",
    "treasury",
    "revenue",
    "procurement_ap",
    "payroll",
    "tax",
    "fpna",
    "icfr",
    "ai_data_governance",
    "operations_risk",
]


class AuditFinding(BaseModel):
    finding_id: str
    rule_id: str
    severity: Severity
    title: str
    transaction_ids: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    rationale: str
    domains: list[RiskDomain] = Field(default_factory=list)
    control_objectives: list[str] = Field(default_factory=list)


class DeterministicAuditResult(BaseModel):
    source_file: str
    source_sha256: str
    row_count: int
    total_absolute_value: float
    risk_score: int
    findings: list[AuditFinding] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class SpecialistAssessment(BaseModel):
    specialist_name: str
    domain: RiskDomain
    conclusion: str
    material_risks: list[str] = Field(default_factory=list)
    evidence_references: list[str] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class ChallengeReview(BaseModel):
    supported_evidence_ids: list[str] = Field(default_factory=list)
    challenged_claims: list[str] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    unresolved_uncertainties: list[str] = Field(default_factory=list)
    release_recommendation: Literal[
        "proceed_to_human_review",
        "revise",
        "insufficient_evidence",
    ]


class LeaderSynthesis(BaseModel):
    executive_summary: str
    cross_domain_risks: list[str] = Field(default_factory=list)
    priority_actions: list[str] = Field(default_factory=list)
    evidence_references: list[str] = Field(default_factory=list)
    unresolved_uncertainties: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class HumanGate(BaseModel):
    required: bool = True
    status: Literal["pending_human_review"] = "pending_human_review"
    reviewer_role: str = "Qualified internal-audit / accounting professional"
    conditions: list[str] = Field(default_factory=list)


class RunMetadata(BaseModel):
    source_file: str
    source_sha256: str
    row_count: int
    total_absolute_value: float
    deterministic_risk_score: int
    active_domains: list[RiskDomain] = Field(default_factory=list)


class FrankensteinAuditReport(BaseModel):
    system_name: str = "FRANKENSTEIN Finance & Operations Audit System"
    architecture_version: str = "0.2.0"
    objective: str
    run_metadata: RunMetadata
    deterministic_findings: list[AuditFinding] = Field(default_factory=list)
    specialist_assessments: list[SpecialistAssessment] = Field(default_factory=list)
    challenge_review: ChallengeReview
    executive_summary: str
    cross_domain_risks: list[str] = Field(default_factory=list)
    evidence_references: list[str] = Field(default_factory=list)
    priority_actions: list[str] = Field(default_factory=list)
    unresolved_uncertainties: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    human_gate: HumanGate
