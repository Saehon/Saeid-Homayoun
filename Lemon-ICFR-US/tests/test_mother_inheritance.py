from lemon_icfr.contracts import AgentHandoff
from lemon_icfr.synthetic import DeterministicScenarioProvider


def test_handoff_hash_is_stable():
    handoff = AgentHandoff(
        task_id="T1",
        run_id="R1",
        sender="generator",
        receiver="falsifier",
        claim="Test claim",
        evidence_refs=["E1"],
        provenance="fixture",
    )
    assert handoff.content_sha256() == handoff.content_sha256()
    assert len(handoff.content_sha256()) == 64


def test_synthetic_layer_labels_outputs():
    scenarios = DeterministicScenarioProvider().generate(
        scenario_type="missing-approval", count=2, seed=7
    )
    assert len(scenarios) == 2
    assert all(s.evidence_class == "synthetic" for s in scenarios)
