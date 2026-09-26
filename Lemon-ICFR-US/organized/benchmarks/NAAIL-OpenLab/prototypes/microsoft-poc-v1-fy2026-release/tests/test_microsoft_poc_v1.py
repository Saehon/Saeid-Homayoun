import csv, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"code"))
from sec_xbrl_ingest import FROZEN_VERIFIED, validate_frozen_facts
from financial_features import simple_price_return, free_cash_flow_proxy
from management_accounting import capacity_cost_rate, tdabc_cost
from otree_experiment_stub import CONDITIONS

def read_json(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

def test_two_core_constitution():
    twin=read_json("microsoft_digital_twin.json")
    assert twin["architecture"]["permanent_cores"] == ["Stable Knowledge Core™","Replaceable Technology Core™"]
    assert twin["architecture"]["third_core"] is False

def test_xbrl_frozen_ingestion_values():
    assert validate_frozen_facts()
    assert FROZEN_VERIFIED["revenue_2026"] == 331839
    assert FROZEN_VERIFIED["capex_2026"] == 115948

def test_segments_reconcile():
    assert 139996 + 137791 + 54052 == 331839

def test_finance_calculations():
    assert free_cash_flow_proxy(182935,115948) == 66987
    assert round(simple_price_return(492.10,372.92),6) == -0.242187

def test_financial_csv_contains_real_market_data():
    rows=list(csv.DictReader(open(ROOT/"microsoft_financial_features.csv",encoding="utf-8")))
    d={r["variable"]:r for r in rows}
    assert d["msft_fy2026_simple_price_return"]["status"] == "EXECUTED_REAL_MARKET_DATA"
    assert float(d["fred_dgs10_2026_06_30"]["value"]) == 4.44

def test_cam_mapping():
    twin=read_json("microsoft_digital_twin.json")
    topics={x["topic"] for x in twin["audit"]["cams"]}
    assert topics == {"Revenue Recognition","Income Taxes — Uncertain Tax Positions"}
    assert twin["audit"]["icfr_opinion"] == "UNQUALIFIED"

def test_text_pipeline_output():
    rows=list(csv.DictReader(open(ROOT/"microsoft_text_features.csv",encoding="utf-8")))
    assert len(rows) == 2
    assert all(r["execution_status"] == "EXECUTED_ON_BOUNDED_SOURCE_SAMPLE" for r in rows)
    assert all(len(r["sample_sha256"]) == 64 for r in rows)

def test_innovation_measure():
    rows=list(csv.DictReader(open(ROOT/"microsoft_innovation_features.csv",encoding="utf-8")))
    d={r["measure"]:r for r in rows}
    assert float(d["rd_intensity"]["value"]) > 0.10
    assert d["patent_activity"]["status"] == "REGISTERED_NOT_EXECUTED"

def test_ai_benchmark_not_synthetic_quality():
    rows=list(csv.DictReader(open(ROOT/"ai_cost_benchmark.csv",encoding="utf-8")))
    assert len(rows) >= 3
    assert all(r["benchmark_release"] == "LiveBench-2026-06-25" for r in rows)
    assert all(r["cost_metric_status"] == "EXTERNAL_COST_PER_SUCCESSFUL_TASK" for r in rows)

def test_tdabc_example():
    rate=capacity_cost_rate(85,48)
    assert round(tdabc_cost(rate,12),4) == 21.25

def test_experiment_is_design_only():
    twin=read_json("microsoft_digital_twin.json")
    assert twin["human_ai_experiment"]["status"] == "DESIGN_COMPLETE_NOT_EXECUTED"
    assert set(CONDITIONS) == {"T0","T1","T2","T3"}

def test_human_gate_boundary():
    twin=read_json("microsoft_digital_twin.json")
    assert twin["human_gate"]["production_approval"] == "NO"
    assert twin["human_gate"]["scientific_validation"] == "PENDING_INDEPENDENT_REPLICATION"
