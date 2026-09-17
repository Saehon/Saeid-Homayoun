from pathlib import Path
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
RET = ROOT / "three_company_market_returns_2024_01_2026_07.csv"
FF = ROOT / "fama_french_5_factor_snapshot_2024_01_2026_07.csv"

def fit(df, factors):
    X = sm.add_constant(df[factors])
    y = df["excess_return"]
    return sm.OLS(y, X).fit(cov_type="HC3")

def main():
    ret = pd.read_csv(RET)
    ff = pd.read_csv(FF)
    ff["month"] = ff["month"].astype(str)
    results=[]
    for ticker in ["MSFT","WMT","JPM"]:
        for return_col, label in [("price_return","price"),("dividend_inclusive_return","dividend_inclusive_approx")]:
            merged = ret.loc[ret.ticker.eq(ticker), ["month",return_col]].merge(ff, on="month", how="inner")
            merged["excess_return"] = merged[return_col] - merged["RF"]
            for model, factors in [
                ("CAPM",["Mkt_RF"]),
                ("FF3",["Mkt_RF","SMB","HML"]),
                ("FF5",["Mkt_RF","SMB","HML","RMW","CMA"]),
            ]:
                m=fit(merged, factors)
                rec={"ticker":ticker,"return_type":label,"model":model,"n":int(m.nobs),"r2":m.rsquared,"adj_r2":m.rsquared_adj}
                for v in ["const"]+factors:
                    rec[v]=m.params[v]
                    rec[f"{v}_se_hc3"]=m.bse[v]
                    rec[f"{v}_p_hc3"]=m.pvalues[v]
                results.append(rec)
    out=pd.DataFrame(results)
    out.to_csv(ROOT/"reproduced_factor_results_v1_2.csv",index=False)
    assert len(out)==18
    assert set(out["n"])=={31}
    print("PASS: reproduced 18 CAPM/FF3/FF5 specifications across three companies and two return bases.")

if __name__ == "__main__":
    main()
