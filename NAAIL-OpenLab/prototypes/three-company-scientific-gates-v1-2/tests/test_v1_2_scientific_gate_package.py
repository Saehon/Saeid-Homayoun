from pathlib import Path
import json, pandas as pd

ROOT = Path(__file__).resolve().parents[1]

ALLOWED={
"EXECUTED_VALIDATED","RESEARCH_PROTOTYPE","EXECUTED","DERIVED_EXECUTED",
"SYNTHETIC_EXECUTED","DESIGN_ONLY","REGISTERED_NOT_EXECUTED","PATENT_HOLD_NON_ENABLING"
}

def matrix():
    return pd.read_csv(ROOT/"three_company_60_step_execution_matrix_v1_2.csv")

def test_matrix_contract():
    m=matrix()
    assert len(m)==60
    assert set(m.ticker)=={"MSFT","WMT","JPM"}
    assert set(m.status).issubset(ALLOWED)
    for t in {"MSFT","WMT","JPM"}:
        assert sorted(m.loc[m.ticker.eq(t),"step_id"].tolist())==list(range(1,21))

def test_fama_is_executed_for_all_three():
    m=matrix()
    assert set(m.loc[m.step_id.eq(7),"status"])=={"EXECUTED"}

def test_hard_gates_are_not_falsely_promoted():
    m=matrix()
    assert set(m.loc[m.step_id.eq(11),"status"])=={"REGISTERED_NOT_EXECUTED"}
    assert set(m.loc[m.step_id.eq(15),"status"])=={"DESIGN_ONLY"}
    assert m.loc[(m.ticker.isin(["WMT","JPM"])) & m.step_id.eq(16),"status"].eq("REGISTERED_NOT_EXECUTED").all()
    assert set(m.loc[m.step_id.eq(20),"status"])=={"REGISTERED_NOT_EXECUTED"}

def test_walmart_split_is_corrected():
    r=pd.read_csv(ROOT/"three_company_market_returns_2024_01_2026_07.csv")
    feb=r[(r.ticker=="WMT") & (r.month=="2024-02")].iloc[0]
    assert abs(feb.prev_close_adj-55.06)<1e-9
    assert 0.06 < feb.price_return < 0.07

def test_factor_sample_and_json():
    s=pd.read_csv(ROOT/"three_company_fama_french_summary_v1_2.csv")
    assert set(s.ticker)=={"MSFT","WMT","JPM"}
    assert set(s.n_31)=={31}
    data=json.loads((ROOT/"three_company_digital_twin_v1_2.json").read_text())
    assert set(data["twins"])=={"MSFT","WMT","JPM"}

def test_professional_self_pilot_is_not_promotion_eligible():
    b=pd.read_csv(ROOT/"professional_ai_benchmark_self_pilot_v1_2.csv")
    assert len(b)==18
    assert b["exact_match"].all()
    assert (~b["promotion_eligible"]).all()
