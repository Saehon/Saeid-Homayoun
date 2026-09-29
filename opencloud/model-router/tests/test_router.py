from opencloud.model_router.router import Risk, choose_route

def test_routine_is_local_first():
    route = choose_route(Risk.ROUTINE)
    assert route.provider == "ollama"
    assert route.model_family == "ibm-granite"
    assert route.human_approval is False

def test_high_risk_requires_human_gate():
    assert choose_route(Risk.HIGH).human_approval is True

def test_failed_validation_escalates():
    assert choose_route(Risk.ROUTINE, failed_validation=True).provider == "multi-provider"
