"""Synthetic tests for the public OpenCloud URC schema."""
from opencloud.core.urc import Request, ProviderStrategy

def test_provider_strategy_values():
    assert ProviderStrategy.PRIMARY_ONLY.value == "primary-only"
    assert ProviderStrategy.MULTI_PROVIDER_COMPARISON.value == "multi-provider-comparison"

def test_request_construction():
    request = Request(
        request_id="req-test-001",
        project_id="synthetic-project",
        strategy=ProviderStrategy.PRIMARY_ONLY,
        primary_provider="provider-a",
        challenger_providers=["provider-b"],
        payload={"case_id": "synthetic-case-001"},
        human_gate_required=True,
    )
    assert request.request_id == "req-test-001"
    assert request.primary_provider == "provider-a"
    assert request.human_gate_required is True

def test_multi_provider_request():
    request = Request(
        request_id="req-test-002",
        project_id="synthetic-project",
        strategy=ProviderStrategy.MULTI_PROVIDER_COMPARISON,
        primary_provider="provider-a",
        challenger_providers=["provider-b", "provider-c"],
        payload={},
    )
    assert len(request.challenger_providers) == 2
