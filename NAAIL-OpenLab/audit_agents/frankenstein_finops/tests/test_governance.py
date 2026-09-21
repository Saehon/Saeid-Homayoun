from frankenstein_finops.governance import (
    enforce_challenge_evidence,
    enforce_specialist_evidence,
)
from frankenstein_finops.schemas import ChallengeReview, SpecialistAssessment


def test_specialist_invalid_evidence_is_removed_and_confidence_is_capped():
    assessment = SpecialistAssessment(
        specialist_name="Test",
        domain="forensic",
        conclusion="Test conclusion",
        material_risks=["A risk"],
        evidence_references=["F-001", "F-999"],
        missing_evidence=[],
        recommended_actions=[],
        confidence=0.9,
    )

    governed = enforce_specialist_evidence(assessment, {"F-001"})

    assert governed.evidence_references == ["F-001"]
    assert any("F-999" in item for item in governed.missing_evidence)


def test_challenge_invalid_evidence_forces_revision():
    review = ChallengeReview(
        supported_evidence_ids=["F-777"],
        challenged_claims=[],
        missing_evidence=[],
        unresolved_uncertainties=[],
        release_recommendation="proceed_to_human_review",
    )

    governed = enforce_challenge_evidence(review, {"F-001"})

    assert governed.supported_evidence_ids == []
    assert governed.release_recommendation == "revise"
