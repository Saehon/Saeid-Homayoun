from __future__ import annotations

from ifrs_value_os.adversarial.core import AdversarialCore
from ifrs_value_os.agentic.router import AgenticRouter
from ifrs_value_os.contracts import DecisionCase, DecisionResult
from ifrs_value_os.knowledge.core import KnowledgeCore
from ifrs_value_os.science.core import ScienceCore
from ifrs_value_os.value.core import ValueCore


class IFRSValueOrchestrator:
    """Coordinates knowledge, science, adversarial review, value and human gating."""

    def __init__(self) -> None:
        self.knowledge = KnowledgeCore()
        self.science = ScienceCore()
        self.adversarial = AdversarialCore()
        self.router = AgenticRouter()
        self.value = ValueCore()

    def run(self, case: DecisionCase) -> DecisionResult:
        audit_trail: list[str] = []

        bundle = self.knowledge.retrieve(case)
        audit_trail.append(f"knowledge:{len(bundle.evidence_ids)}_evidence_items")

        route = self.router.route(case.risk)
        audit_trail.append(
            f"route:{route.primary_provider}:{route.reviewer_provider}:{route.falsifier_provider}"
        )

        hypotheses = self.science.generate_hypotheses(case)
        audit_trail.append(f"science:{len(hypotheses)}_hypotheses")

        challenged = [self.adversarial.challenge(h) for h in hypotheses]
        audit_trail.append("adversarial:challenged_all")

        selected = max(challenged, key=lambda h: h.score, default=None)

        _ = self.value.assess()
        audit_trail.append("value:assessment_initialized")

        return DecisionResult(
            case_id=case.case_id,
            selected_hypothesis=selected,
            hypotheses=challenged,
            requires_human_approval=route.human_gate,
            audit_trail=audit_trail,
        )
