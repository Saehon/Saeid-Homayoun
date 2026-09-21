from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

Severity = Literal["low", "medium", "high", "critical"]


class AuditFinding(BaseModel):
    finding_id: str
    rule_id: str
    severity: Severity
    title: str
    transaction_ids: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    rationale: str


class DeterministicAuditResult(BaseModel):
    source_file: str
    row_count: int
    total_absolute_value: float
    risk_score: int
    findings: list[AuditFinding] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class SpecialistAssessment(BaseModel):
    agent_name: str
    domain: str
    risk_summary: str
    key_risks: list[str] = Field(default_factory=list)
    evidence_references: list[str] = Field(default_factory=list)
    tests_requested: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class FrankensteinReport(BaseModel):
    executive_summary: str
    audit_objective: str
    deterministic_risk_score: int
    specialist_assessments: list[SpecialistAssessment] = Field(default_factory=list)
    cross_domain_risks: list[str] = Field(default_factory=list)
    evidence_references: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    human_review_required: bool = True
