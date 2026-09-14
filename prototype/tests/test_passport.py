from econova.engine import StageRecord, HumanDecision, make_evidence_passport


def test_passport_never_allows_discovery_claim():
    stages = [
        StageRecord("discovery", "r1", "gpt-5.6-sol", "high", "x"),
        StageRecord("era", "r2", "gpt-5.6-sol", "high", "y"),
        StageRecord("red_team", "r3", "gpt-5.6-sol", "high", "z"),
    ]
    passport = make_evidence_passport(
        "Q?", "", stages,
        HumanDecision("APPROVE FOR NEXT STAGE", "Reviewer", "ok"),
        False,
    )
    assert passport["next_stage_allowed"] is True
    assert passport["discovery_claim_allowed"] is False
    assert passport["gates"]["real_data_provenance"] is False


def test_human_reject_blocks_next_stage():
    stages = [StageRecord("discovery", "r1", "gpt-5.6-sol", "high", "x")]
    passport = make_evidence_passport(
        "Q?", "", stages,
        HumanDecision("REJECT", "Reviewer", "no"),
        False,
    )
    assert passport["next_stage_allowed"] is False
