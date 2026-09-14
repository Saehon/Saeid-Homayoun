from automation.orchestrator import Orchestrator, AgentResult, validate_chain, DeterministicDemoAdapter, ROLE_SEQUENCE


def test_demo_chain_valid():
    chain = Orchestrator().run("Does AI improve measured productivity?")
    assert chain["chain_length"] == 7
    assert chain["human_gate_required"] is True
    assert chain["human_gate_approved"] is False
    assert chain["discovery_claim_allowed"] is False
    assert validate_chain(chain) == []


def test_hash_chain_links():
    chain = Orchestrator().run("Test question")
    handoffs = chain["handoffs"]
    assert handoffs[0]["parent_content_sha256"] is None
    for previous, current in zip(handoffs, handoffs[1:]):
        assert current["parent_content_sha256"] == previous["content_sha256"]


def test_stop_on_blocking_failure():
    class FailingReplicator:
        name = "replicator-isolated"
        version = "1.0"

        def run(self, role, payload):
            return AgentResult(
                claim="replication failed",
                method="independent replay",
                assumptions=[],
                confidence=0.1,
                contradictions=[],
                failed=True,
                failure_reasons=["replication_failed"],
                evidence=[],
                required_next_action="return_to_empirical_design",
            )

    adapters = {role: DeterministicDemoAdapter() for role in ROLE_SEQUENCE}
    adapters["independent_replicator"] = FailingReplicator()
    chain = Orchestrator(adapters).run("Test blocking failure")
    assert chain["stopped"] is True
    assert chain["chain_length"] == 4
    assert chain["handoffs"][-1]["failure_status"]["failed"] is True
    assert validate_chain(chain) == []
