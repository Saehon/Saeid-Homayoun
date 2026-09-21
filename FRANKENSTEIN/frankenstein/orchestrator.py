from __future__ import annotations

import os
from pathlib import Path

from .agents import AGENTS
from .analytics import analyze_transactions
from .claude_client import ClaudeClient
from .schemas import FrankensteinReport, SpecialistAssessment

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SAMPLE = PACKAGE_ROOT / "sample_data" / "transactions.csv"


def _offline_specialists(evidence: dict) -> list[SpecialistAssessment]:
    refs = [f"{f['finding_id']}:{f['rule_id']}" for f in evidence.get("findings", [])]
    titles = [f["title"] for f in evidence.get("findings", [])]
    return [
        SpecialistAssessment(
            agent_name=spec.name,
            domain=spec.domain,
            risk_summary=(
                f"Deterministic testing produced {len(refs)} risk indicators. "
                "Claude synthesis was not called because offline mode was selected or ANTHROPIC_API_KEY is absent."
            ),
            key_risks=titles,
            evidence_references=refs,
            tests_requested=["Obtain corroborating source documents, workflow logs, control-owner evidence and relevant authoritative support."],
            recommended_actions=["Review deterministic indicators and calibrate tests to entity-specific materiality, process design and jurisdiction."],
            limitations=["Offline mode provides deterministic evidence and specialist scaffolding only."],
        ) for spec in AGENTS
    ]


def run(objective: str, csv_path: str | Path = DEFAULT_SAMPLE, use_claude: bool = True) -> FrankensteinReport:
    deterministic = analyze_transactions(csv_path)
    evidence = deterministic.model_dump()
    refs = [f"{f.finding_id}:{f.rule_id}" for f in deterministic.findings]

    if not use_claude or not os.getenv("ANTHROPIC_API_KEY"):
        specialists = _offline_specialists(evidence)
        return FrankensteinReport(
            executive_summary=(
                f"Deterministic testing identified {len(deterministic.findings)} risk indicators "
                f"with an illustrative risk score of {deterministic.risk_score}/100. Claude synthesis was not executed."
            ),
            audit_objective=objective,
            deterministic_risk_score=deterministic.risk_score,
            specialist_assessments=specialists,
            cross_domain_risks=[f.title for f in deterministic.findings],
            evidence_references=refs,
            recommended_actions=[
                "Corroborate high-severity indicators with source documents and workflow evidence.",
                "Calibrate thresholds to the entity, process, materiality and jurisdiction.",
                "Require qualified human approval before any professional conclusion or remediation decision.",
            ],
            limitations=deterministic.limitations + ["Claude synthesis unavailable or disabled."],
            human_review_required=True,
        )

    client = ClaudeClient()
    specialists = [client.specialist(spec, objective, evidence) for spec in AGENTS]
    return client.leader(objective, deterministic.risk_score, specialists, refs, deterministic.limitations)
