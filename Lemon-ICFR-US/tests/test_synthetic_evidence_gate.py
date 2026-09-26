from lemon_icfr.models import EvidenceItem
from lemon_icfr.orchestrator import LemonOrchestrator


class NeverCalledProvider:
    name = "never"

    def generate_hypotheses(self, *args, **kwargs):
        raise AssertionError("Provider should not run when evidence gate blocks.")

    def challenge_claim(self, *args, **kwargs):
        raise AssertionError("Provider should not run when evidence gate blocks.")

    def lineage(self):
        return "never:1"


def test_synthetic_only_case_is_blocked():
    result = LemonOrchestrator().run(
        case_id="SYNTH-ONLY",
        question="Is this a real control failure?",
        evidence=[
            EvidenceItem(
                evidence_id="S-1",
                source="synthetic generator",
                provenance="synthetic/test",
                rights_status="generated",
                content="simulated missing approval",
                evidence_class="synthetic",
            )
        ],
        provider=NeverCalledProvider(),
        coso_context_supplied=True,
        reproducibility_ref="tests/test_synthetic_evidence_gate.py",
    )
    assert result.status.startswith("BLOCKED:")
    assert "real_evidence_anchor" in result.status
