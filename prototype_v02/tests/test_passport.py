from econova.engine import StageRecord, HumanDecision, make_evidence_passport

def test_discovery_gate_is_never_auto_true():
    s=[StageRecord("d","1","gpt-5.6-sol","high","x"),
       StageRecord("e","2","gpt-5.6-sol","high","y"),
       StageRecord("r","3","gpt-5.6-sol","high","z")]
    p=make_evidence_passport(
        "q","",[],s,HumanDecision("APPROVE FOR NEXT STAGE","H","ok"),
        {"real_data":True,"source":"test"},
        {"credible_identification":True}
    )
    assert p["next_stage_allowed"] is True
    assert p["discovery_claim_allowed"] is False
