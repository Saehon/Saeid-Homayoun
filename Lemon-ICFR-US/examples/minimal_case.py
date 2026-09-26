from lemon_icfr.models import EvidenceItem
from lemon_icfr.orchestrator import LemonOrchestrator


class ExampleProvider:
    name = "example"

    def lineage(self):
        return "example:local"

    def generate_hypotheses(self, case_id, evidence, question):
        from lemon_icfr.models import Finding
        return [
            Finding(
                agent="co-scientist",
                claim="The supplied evidence suggests an approval-control exception requiring review.",
                evidence_refs=[evidence[0].evidence_id],
                alternative_explanations=[
                    "The approval may exist in a source not included in the evidence package."
                ],
                model_tool_version=self.lineage(),
            )
        ]

    def challenge_claim(self, case_id, evidence, finding):
        from lemon_icfr.models import Finding
        return Finding(
            agent="independent-falsification",
            claim="Challenge: determine whether the missing approval is a population-completeness issue rather than a control failure.",
            evidence_refs=[evidence[0].evidence_id],
            model_tool_version=self.lineage(),
        )


if __name__ == "__main__":
    result = LemonOrchestrator().run(
        case_id="LEMON-DEMO-001",
        question="Is the approval control operating effectively?",
        evidence=[
            EvidenceItem(
                evidence_id="E-001",
                source="approved demo fixture",
                provenance="examples/minimal_case.py",
                rights_status="repository demo",
                content="One sampled item has no approval field in the supplied evidence.",
            )
        ],
        provider=ExampleProvider(),
        coso_context_supplied=True,
        reproducibility_ref="examples/minimal_case.py",
    )
    print(result.status)
    for gate in result.gates:
        print(gate.gate, gate.passed, gate.notes)
