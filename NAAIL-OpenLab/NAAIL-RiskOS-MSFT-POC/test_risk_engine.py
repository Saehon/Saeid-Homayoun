from pathlib import Path
from risk_engine import load_case, weighted_score, RiskOSOrchestrator

HERE = Path(__file__).resolve().parent

def test_formula_identity():
    case = load_case(HERE / "microsoft_case.json")
    r = RiskOSOrchestrator(case).run()["audit_risk_decomposition"]
    assert abs(r["AR_index"] - round(r["IR_index"] * r["CR_index"] * r["DR_index"], 4)) <= 0.0002

def test_weights_positive():
    case = load_case(HERE / "microsoft_case.json")
    for component in ("IR", "CR", "DR"):
        assert weighted_score(case["illustrative_uncalibrated_inputs"][component]) >= 0

def test_applicability_boundary():
    case = load_case(HERE / "microsoft_case.json")
    assert case["company"]["reporting_basis"] == "US_GAAP"
    assert case["company"]["audit_regime"] == "PCAOB_CAM"

def test_no_production_claim():
    case = load_case(HERE / "microsoft_case.json")
    assert case["verified_poc_facts"]["production_approval"] == "NO"

def test_human_gate_required():
    case = load_case(HERE / "microsoft_case.json")
    assert RiskOSOrchestrator(case).run()["final_state"] == "HUMAN_REVIEW_REQUIRED"
