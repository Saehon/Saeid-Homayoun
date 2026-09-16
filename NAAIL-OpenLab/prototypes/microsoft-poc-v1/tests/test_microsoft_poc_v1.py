import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("bp",ROOT/"src"/"build_prototype.py")
bp=importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

def test_two_core_constitution_is_not_changed():
    import json
    twin=json.loads((ROOT/"microsoft_digital_twin.json").read_text())
    assert twin["architecture"]["permanent_cores"] == ["Stable Knowledge Core™","Replaceable Technology Core™"]
    assert twin["architecture"]["third_core"] is False

def test_fy2026_financial_arithmetic():
    f=bp.financial_features()
    assert round(f["free_cash_flow"],0)==66987
    assert 0.46 < f["operating_margin"] < 0.48
    assert 1.22 < f["current_ratio"] < 1.24

def test_tdabc_cost_rate():
    x=bp.tdabc_example()
    assert round(x["capacity_cost_rate_per_minute"],6)==round(85/48,6)
    assert x["human_activity_cost"] > 0

def test_human_gate_is_research_only():
    import json
    twin=json.loads((ROOT/"microsoft_digital_twin.json").read_text())
    assert "RESEARCH_PROTOTYPE" in twin["human_gate"]["decision"]
    assert twin["maturity"]=="RESEARCH_PROTOTYPE"
