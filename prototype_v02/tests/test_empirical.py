import pandas as pd
import numpy as np
from econova.empirical import EmpiricalSpec, run_six_tables, stata_do

def fixture():
    rows=[]
    rng=np.random.default_rng(7)
    for firm in range(12):
        a=rng.normal()
        for year in range(2019,2026):
            x=rng.normal()+.15*(year-2019)+a*.2
            c=rng.normal()
            y=.5*x+.2*c+a+rng.normal(scale=.6)
            rows.append((f"F{firm:02d}",year,x,c,y))
    return pd.DataFrame(rows,columns=["firm","year","x","control","y"])

def test_six_tables():
    df=fixture()
    s=EmpiricalSpec("y","x",["control"],"firm","year","firm")
    out=run_six_tables(df,s,"year")
    assert len(out)==6
    assert not out["table4_main"].empty
    assert "rmse" in out["table6_oos"].columns

def test_stata_export():
    s=EmpiricalSpec("y","x",["control"],"firm","year","firm")
    d=stata_do(s)
    assert "reg y x control i.firm i.year" in d
    assert "vce(cluster firm)" in d
