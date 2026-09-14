import importlib.util
from pathlib import Path
import numpy as np
import pandas as pd

MODULE = Path(__file__).with_name("run_study.py")
spec = importlib.util.spec_from_file_location("study", MODULE)
study = importlib.util.module_from_spec(spec)
spec.loader.exec_module(study)


def test_parse_ff5_monthly_block():
    raw = """header\n,Mkt-RF,SMB,HML,RMW,CMA,RF\n202401,1.0,2.0,3.0,4.0,5.0,0.4\n202402,-1.0,0.0,1.0,2.0,3.0,0.5\n Annual Factors\n"""
    df = study.parse_ff5(raw)
    assert list(df.columns) == ["date"] + study.FACTORS
    assert len(df) == 2
    assert np.isclose(df.loc[0, "Mkt-RF"], 0.01)
    assert np.isclose(df.loc[1, "RF"], 0.005)


def test_parse_portfolios_monthly_block():
    raw = """Average Value Weighted Returns -- Monthly\n,SMALL LoBM,ME1 BM2,SMALL HiBM,BIG LoBM,ME2 BM2,BIG HiBM\n202401,1,2,3,4,5,6\n202402,2,3,4,5,6,7\n Annual\n"""
    df = study.parse_port6(raw)
    assert len(df) == 2
    assert np.isclose(df.loc[0, "BIG HiBM"], 0.06)


def test_dcs_and_reversal_logic():
    dates = pd.date_range("2020-01-01", periods=36, freq="MS")
    old = pd.DataFrame({"date": dates, "SMB": np.linspace(-.02, .02, 36)})
    new = old.copy()
    new["SMB"] = old["SMB"] + .001
    t = study.dcs_table(old, new, ["SMB"], "factor")
    assert np.isclose(t.loc[0, "DCS_mean_abs_bps"], 10.0)
    assert t.loc[0, "correlation"] > .99


def test_align_uses_common_dates_only():
    a = pd.DataFrame({"date": pd.to_datetime(["2020-01-01", "2020-02-01"]), "x": [1,2]})
    b = pd.DataFrame({"date": pd.to_datetime(["2020-02-01", "2020-03-01"]), "x": [2,3]})
    aa, bb = study._align(a,b)
    assert len(aa) == len(bb) == 1
    assert aa.loc[0,"date"] == pd.Timestamp("2020-02-01")
