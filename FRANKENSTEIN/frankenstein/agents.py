from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentSpec:
    name: str
    domain: str
    mandate: str


AGENTS: tuple[AgentSpec, ...] = (
    AgentSpec("Finance Controls Agent", "finance_controls", "Assess authorization, segregation of duties, reconciliations, transaction integrity and financial-process control evidence."),
    AgentSpec("Internal Audit Agent", "internal_audit", "Assess risk, control design, operating-effectiveness evidence, root causes, remediation and residual risk."),
    AgentSpec("IFRS Reporting Agent", "ifrs_reporting", "Assess financial-reporting judgments and evidence needs without inventing standards or asserting compliance."),
    AgentSpec("ICFR Agent", "icfr", "Assess financial-reporting control objectives, evidence gaps, deficiency indicators and remediation without independently declaring a material weakness."),
    AgentSpec("Forensic Agent", "forensic", "Assess unusual transactions, duplicates, anomalous timing and possible circumvention indicators without alleging misconduct."),
    AgentSpec("ESG & Sustainability Assurance Agent", "esg_assurance", "Assess sustainability-data provenance, consistency, estimation risk, controls and assurance readiness."),
    AgentSpec("Cost & AI FinOps Agent", "cost_finops", "Assess activity, time, model/token cost and cost-to-evidence trade-offs without allowing cost minimization to override assurance quality."),
    AgentSpec("Operations Risk Agent", "operations_risk", "Assess process resilience, accountability, scalability, workflow dependencies and operational bottlenecks."),
    AgentSpec("AI & Data Governance Agent", "ai_data_governance", "Assess data lineage, access, agent/model actions, logging, privacy, change management, reproducibility and human oversight."),
)

LEADER_NAME = "FRANKENSTEIN Audit & Assurance Leader"
