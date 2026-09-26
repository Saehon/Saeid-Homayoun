from lemon_icfr.models import EvidenceItem
from lemon_icfr.orchestrator import LemonOrchestrator


class FakeProvider:
    name = "fake"

    def lineage(self):
        return "fake:1"

    def generate_hypotheses(self, case_id, evidence, question):
        from lemon_icfr.models import Finding
        return [
            Finding(
                agent="co-scientist",
                claim="Approval evidence may be incomplete.",
                evidence_refs=[evidence[0].evidence_id],
                model_tool_version=self.lineage(),
            )
        ]

    def challenge_claim(self, case_id, evidence, finding):
        from lemon_icfr.models import Finding
        return Finding(
            agent="independent-falsification",
            claim="Alternative explanation: evidence may exist outside the supplied population.",
            evidence_refs=[evidence[0].evidence_id],
            model_tool_version=self.lineage(),
        )


def test_human_gate_is_never_auto_approved():
    evidence = [
        EvidenceItem(
            evidence_id="E-001",
            source="test fixture",
            provenance="fixture/v1",
            rights_status="test-only",
            content="sample approval evidence",
        )
    ]
    result = LemonOrchestrator().run(
        case_id="CASE-001",
        question="Is the approval control operating effectively?",
        evidence=evidence,
        provider=FakeProvider(),
        coso_context_supplied=True,
        reproducibility_ref="tests/test_orchestrator.py",
    )

    assert result.status == "AWAITING_HUMAN_APPROVAL"
    human_gate = [g for g in result.gates if g.gate == "human_approval"][0]
    assert human_gate.passed is False
