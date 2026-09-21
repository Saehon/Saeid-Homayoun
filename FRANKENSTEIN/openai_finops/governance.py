from __future__ import annotations

from collections.abc import Iterable

from .schemas import ChallengeReview, LeaderSynthesis, SpecialistAssessment


def valid_finding_ids(findings: Iterable) -> set[str]:
    return {finding.finding_id for finding in findings}


def sanitize_evidence_references(
    references: list[str],
    valid_ids: set[str],
) -> tuple[list[str], list[str]]:
    accepted: list[str] = []
    rejected: list[str] = []
    for ref in references:
        if ref in valid_ids:
            accepted.append(ref)
        else:
            rejected.append(ref)
    return sorted(set(accepted)), sorted(set(rejected))


def enforce_specialist_evidence(
    assessment: SpecialistAssessment,
    valid_ids: set[str],
) -> SpecialistAssessment:
    accepted, rejected = sanitize_evidence_references(
        assessment.evidence_references,
        valid_ids,
    )
    assessment.evidence_references = accepted
    if rejected:
        assessment.missing_evidence.append(
            "Unsupported evidence references removed by deterministic governance: "
            + ", ".join(rejected)
        )
    if assessment.material_risks and not assessment.evidence_references:
        assessment.missing_evidence.append(
            "No validated deterministic finding ID supports the material-risk statements."
        )
        assessment.confidence = min(assessment.confidence, 0.35)
    return assessment


def enforce_challenge_evidence(
    review: ChallengeReview,
    valid_ids: set[str],
) -> ChallengeReview:
    accepted, rejected = sanitize_evidence_references(
        review.supported_evidence_ids,
        valid_ids,
    )
    review.supported_evidence_ids = accepted
    if rejected:
        review.challenged_claims.append(
            "Challenge agent referenced unsupported finding IDs that were removed: "
            + ", ".join(rejected)
        )
        review.release_recommendation = "revise"
    return review


def enforce_leader_evidence(
    synthesis: LeaderSynthesis,
    valid_ids: set[str],
) -> LeaderSynthesis:
    accepted, rejected = sanitize_evidence_references(
        synthesis.evidence_references,
        valid_ids,
    )
    synthesis.evidence_references = accepted
    if rejected:
        synthesis.unresolved_uncertainties.append(
            "Leader synthesis contained unsupported finding IDs that were removed: "
            + ", ".join(rejected)
        )
    return synthesis
