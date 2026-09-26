from __future__ import annotations

from lemon_icfr.models import EvidenceItem, Finding, GateResult, LemonCaseResult
from lemon_icfr.providers.base import ModelProvider


_REQUIRED_GATES = (
    "provenance",
    "rights_license",
    "icfr_coso_grounding",
    "evidence_sufficiency",
    "independent_review",
    "falsification",
    "reproducibility",
    "human_approval",
)


class LemonOrchestrator:
    """Minimal Lemon workflow enforcing non-bypassable scientific/assurance gates."""

    def _evidence_gates(self, evidence: list[EvidenceItem]) -> list[GateResult]:
        provenance_ok = bool(evidence) and all(e.provenance.strip() for e in evidence)
        rights_ok = bool(evidence) and all(e.rights_status.strip() for e in evidence)
        return [
            GateResult("provenance", provenance_ok, [] if provenance_ok else ["Missing evidence provenance."]),
            GateResult("rights_license", rights_ok, [] if rights_ok else ["Missing rights/license status."]),
        ]

    def run(
        self,
        *,
        case_id: str,
        question: str,
        evidence: list[EvidenceItem],
        provider: ModelProvider,
        coso_context_supplied: bool,
        reproducibility_ref: str | None,
    ) -> LemonCaseResult:
        gates = self._evidence_gates(evidence)
        gates.append(
            GateResult(
                "icfr_coso_grounding",
                coso_context_supplied,
                [] if coso_context_supplied else ["COSO/ICFR mapping context is required."],
            )
        )

        if not all(g.passed for g in gates):
            missing = [g.gate for g in gates if not g.passed]
            return LemonCaseResult(
                case_id=case_id,
                findings=[],
                gates=gates,
                contradictions=[],
                status=f"BLOCKED:{','.join(missing)}",
            )

        hypotheses = provider.generate_hypotheses(case_id, evidence, question)
        evidence_ids = {e.evidence_id for e in evidence}
        support_ok = bool(hypotheses) and all(
            h.evidence_refs and set(h.evidence_refs).issubset(evidence_ids) for h in hypotheses
        )
        gates.append(
            GateResult(
                "evidence_sufficiency",
                support_ok,
                [] if support_ok else ["Every material hypothesis must cite supplied evidence IDs."],
            )
        )

        challenges: list[Finding] = []
        if hypotheses:
            challenges = [provider.challenge_claim(case_id, evidence, h) for h in hypotheses]

        reviewer_ok = bool(hypotheses)
        falsification_ok = bool(challenges)
        gates.extend(
            [
                GateResult("independent_review", reviewer_ok, [] if reviewer_ok else ["No reviewable hypothesis."]),
                GateResult("falsification", falsification_ok, [] if falsification_ok else ["No independent challenge generated."]),
                GateResult(
                    "reproducibility",
                    bool(reproducibility_ref),
                    [] if reproducibility_ref else ["Missing reproducibility reference."],
                ),
                # A machine run can never pass this gate by itself.
                GateResult("human_approval", False, ["Authorized human disposition required."]),
            ]
        )

        contradictions = [c.claim for c in challenges if c.claim]
        status = "AWAITING_HUMAN_APPROVAL"
        if any(not g.passed for g in gates if g.gate != "human_approval"):
            status = "REVIEW_REQUIRED"

        return LemonCaseResult(
            case_id=case_id,
            findings=hypotheses + challenges,
            gates=gates,
            contradictions=contradictions,
            status=status,
        )

    @staticmethod
    def required_gates() -> tuple[str, ...]:
        return _REQUIRED_GATES
