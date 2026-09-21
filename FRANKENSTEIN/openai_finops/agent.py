from __future__ import annotations

import asyncio
import json
from pathlib import Path

from agents import Runner
from agents.decorators import tool

from .analytics import analyze_transactions
from .governance import (
    enforce_challenge_evidence,
    enforce_leader_evidence,
    enforce_specialist_evidence,
    valid_finding_ids,
)
from .schemas import (
    FrankensteinAuditReport,
    HumanGate,
    RiskDomain,
    RunMetadata,
    SpecialistAssessment,
)
from .specialists import (
    SPECIALIST_SPECS,
    build_specialist_agent,
    challenge_agent,
    leader_agent,
)


PACKAGE_ROOT = Path(__file__).resolve().parent
ALL_DOMAINS: tuple[RiskDomain, ...] = tuple(SPECIALIST_SPECS.keys())


def _resolve_repo_local_path(csv_path: str) -> Path:
    candidate = Path(csv_path)
    if not candidate.is_absolute():
        candidate = (PACKAGE_ROOT / candidate).resolve()
    else:
        candidate = candidate.resolve()

    allowed_root = PACKAGE_ROOT.resolve()
    if allowed_root not in candidate.parents and candidate != allowed_root:
        raise ValueError(
            "For this public research prototype, data files must be inside "
            "openai_finops/ to reduce accidental access to unrelated local files."
        )
    return candidate


def resolve_domains(domains: list[str] | None) -> list[RiskDomain]:
    if not domains:
        return list(ALL_DOMAINS)

    unknown = sorted(set(domains).difference(ALL_DOMAINS))
    if unknown:
        raise ValueError(
            f"Unknown audit domains: {unknown}. Valid domains: {list(ALL_DOMAINS)}"
        )
    return [domain for domain in ALL_DOMAINS if domain in domains]


@tool
def run_transaction_tests(csv_path: str) -> str:
    """Run deterministic finance and operations audit tests on a repo-local CSV file.

    Args:
        csv_path: Path relative to openai_finops/, for example
            sample_data/transactions.csv.
    """
    path = _resolve_repo_local_path(csv_path)
    result = analyze_transactions(path)
    return json.dumps(result.model_dump(), indent=2)


def _domain_evidence_packet(domain: RiskDomain, deterministic_result) -> dict:
    relevant = [
        finding.model_dump()
        for finding in deterministic_result.findings
        if domain in finding.domains
    ]
    return {
        "domain": domain,
        "source_sha256": deterministic_result.source_sha256,
        "row_count": deterministic_result.row_count,
        "deterministic_risk_score": deterministic_result.risk_score,
        "relevant_findings": relevant,
        "global_limitations": deterministic_result.limitations,
    }


async def _run_specialist(
    domain: RiskDomain,
    objective: str,
    deterministic_result,
) -> SpecialistAssessment:
    agent = build_specialist_agent(domain)
    packet = _domain_evidence_packet(domain, deterministic_result)
    prompt = (
        f"Audit objective: {objective}\n"
        "Assess only your assigned domain using this deterministic evidence packet. "
        "If the packet lacks domain-specific evidence, state that clearly and identify the records needed.\n\n"
        f"{json.dumps(packet, indent=2)}"
    )
    result = await Runner.run(agent, prompt)
    assessment: SpecialistAssessment = result.final_output

    expected_name = SPECIALIST_SPECS[domain][0]
    assessment.domain = domain
    assessment.specialist_name = expected_name
    return assessment


async def run_frankenstein_audit(
    objective: str,
    csv_path: str,
    domains: list[str] | None = None,
) -> FrankensteinAuditReport:
    """Run the full deterministic -> specialist -> challenge -> leader -> human-gate pipeline."""
    path = _resolve_repo_local_path(csv_path)
    deterministic = analyze_transactions(path)
    active_domains = resolve_domains(domains)
    valid_ids = valid_finding_ids(deterministic.findings)

    specialist_tasks = [
        _run_specialist(domain, objective, deterministic)
        for domain in active_domains
    ]
    specialist_assessments = list(await asyncio.gather(*specialist_tasks))
    specialist_assessments = [
        enforce_specialist_evidence(assessment, valid_ids)
        for assessment in specialist_assessments
    ]

    challenge_payload = {
        "objective": objective,
        "deterministic_findings": [
            finding.model_dump() for finding in deterministic.findings
        ],
        "specialist_assessments": [
            assessment.model_dump() for assessment in specialist_assessments
        ],
        "limitations": deterministic.limitations,
    }
    challenge_result = await Runner.run(
        challenge_agent,
        "Independently challenge this audit package before executive synthesis:\n\n"
        + json.dumps(challenge_payload, indent=2),
    )
    challenge = enforce_challenge_evidence(challenge_result.final_output, valid_ids)

    leader_payload = {
        "objective": objective,
        "deterministic_risk_score": deterministic.risk_score,
        "deterministic_findings": [
            finding.model_dump() for finding in deterministic.findings
        ],
        "specialist_assessments": [
            assessment.model_dump() for assessment in specialist_assessments
        ],
        "challenge_review": challenge.model_dump(),
        "limitations": deterministic.limitations,
    }
    leader_result = await Runner.run(
        leader_agent,
        "Synthesize this evidence-governed audit package for qualified human review:\n\n"
        + json.dumps(leader_payload, indent=2),
    )
    synthesis = enforce_leader_evidence(leader_result.final_output, valid_ids)

    gate_conditions = [
        "A qualified human reviewer must approve or reject every material conclusion.",
        "Corroborate flagged transactions with source documents and relevant system/workflow evidence.",
        "Calibrate thresholds and materiality to the audited entity before professional use.",
    ]
    if challenge.challenged_claims:
        gate_conditions.append(
            "Resolve the independent challenger's disputed claims before escalation."
        )
    if challenge.release_recommendation != "proceed_to_human_review":
        gate_conditions.append(
            "Do not promote conclusions until the challenge review is revised or additional evidence is obtained."
        )

    combined_limitations = list(
        dict.fromkeys(deterministic.limitations + synthesis.limitations)
    )

    return FrankensteinAuditReport(
        objective=objective,
        run_metadata=RunMetadata(
            source_file=str(path),
            source_sha256=deterministic.source_sha256,
            row_count=deterministic.row_count,
            total_absolute_value=deterministic.total_absolute_value,
            deterministic_risk_score=deterministic.risk_score,
            active_domains=active_domains,
        ),
        deterministic_findings=deterministic.findings,
        specialist_assessments=specialist_assessments,
        challenge_review=challenge,
        executive_summary=synthesis.executive_summary,
        cross_domain_risks=synthesis.cross_domain_risks,
        evidence_references=synthesis.evidence_references,
        priority_actions=synthesis.priority_actions,
        unresolved_uncertainties=synthesis.unresolved_uncertainties,
        limitations=combined_limitations,
        human_gate=HumanGate(conditions=gate_conditions),
    )


async def run_audit(
    objective: str,
    csv_path: str,
    domains: list[str] | None = None,
) -> FrankensteinAuditReport:
    """Backward-compatible alias for the Frankenstein orchestration pipeline."""
    return await run_frankenstein_audit(objective, csv_path, domains)
