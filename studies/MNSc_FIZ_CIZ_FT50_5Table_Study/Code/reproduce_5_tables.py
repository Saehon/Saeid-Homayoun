from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
TABLES = ROOT / "Tables"
TABLES.mkdir(exist_ok=True)

ff = pd.read_csv(DATA / "fama_french_ff5_github_2010_2020.csv")
dam = pd.read_csv(DATA / "damodaran_wacc_github_2024_subset.csv")

def describe(df, cols, panel):
    out = []
    for c in cols:
        x = pd.to_numeric(df[c], errors="coerce").dropna()
        out.append({
            "Panel": panel, "Variable": c, "N": len(x),
            "Mean": x.mean(), "SD": x.std(ddof=1), "Min": x.min(),
            "P25": x.quantile(.25), "Median": x.median(),
            "P75": x.quantile(.75), "Max": x.max()
        })
    return pd.DataFrame(out)

t2 = pd.concat([
    describe(ff, ["Mkt_RF","SMB","HML","RMW","CMA","RF"], "A: Fama-French"),
    describe(dam, ["WACC","Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"], "B: Damodaran")
], ignore_index=True)
t2.to_csv(TABLES / "Table_2_reproduced.csv", index=False)

rows = []
for panel, df, cols in [
    ("A: Fama-French", ff, ["Mkt_RF","SMB","HML","RMW","CMA"]),
    ("B: Damodaran", dam, ["WACC","Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"])
]:
    C = df[cols].corr()
    for i, r in enumerate(cols):
        for j, c in enumerate(cols):
            if j > i:
                rows.append([panel, r, c, C.loc[r,c]])
pd.DataFrame(rows, columns=["Panel","Variable_1","Variable_2","Pearson_r"]).to_csv(
    TABLES / "Table_3_reproduced.csv", index=False
)

def fit(y, xs, df=dam, cov="HC3"):
    X = sm.add_constant(df[xs].astype(float))
    return sm.OLS(df[y].astype(float), X).fit(cov_type=cov)

models = [
    ("(1)", ["Beta"]),
    ("(2)", ["Beta","D_weight"]),
    ("(3)", ["Beta","D_weight","Stock_SD"]),
    ("(4)", ["Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"])
]
out = []
for label, xs in models:
    m = fit("WACC", xs)
    for v in m.params.index:
        out.append([label,v,m.params[v],m.bse[v],m.tvalues[v],m.pvalues[v],
                    int(m.nobs),m.rsquared,m.rsquared_adj])
pd.DataFrame(out, columns=[
    "Model","Variable","Coefficient","Robust_SE_HC3","t","p","N","R2","Adj_R2"
]).to_csv(TABLES / "Table_4_reproduced.csv", index=False)

rob = []
for cov in ["nonrobust","HC1","HC3"]:
    X = sm.add_constant(dam[["Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"]])
    m = sm.OLS(dam["WACC"], X).fit() if cov=="nonrobust" else \
        sm.OLS(dam["WACC"], X).fit(cov_type=cov)
    rob.append(["SE estimator", cov, "WACC", "Beta", m.params["Beta"],
                m.bse["Beta"], m.pvalues["Beta"], int(m.nobs), m.rsquared])

m = fit("Cost_Equity", ["Beta","D_weight","Stock_SD"])
rob.append(["Alternative DV","HC3","Cost_Equity","Beta",m.params["Beta"],
            m.bse["Beta"],m.pvalues["Beta"],int(m.nobs),m.rsquared])

w = dam.copy()
for c in ["WACC","Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"]:
    lo, hi = w[c].quantile([.05,.95])
    w[c] = w[c].clip(lo,hi)
m = fit("WACC", ["Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"], w)
rob.append(["5/95 winsorized","HC3","WACC","Beta",m.params["Beta"],
            m.bse["Beta"],m.pvalues["Beta"],int(m.nobs),m.rsquared])

mask = ~dam["Industry"].str.contains("Bank|Financial|Insurance|Investment", case=False, regex=True)
nf = dam.loc[mask].copy()
m = fit("WACC", ["Beta","D_weight","Stock_SD","AfterTax_Cost_Debt"], nf)
rob.append(["Exclude financials","HC3","WACC","Beta",m.params["Beta"],
            m.bse["Beta"],m.pvalues["Beta"],int(m.nobs),m.rsquared])

pd.DataFrame(rob, columns=[
    "Robustness_Test","SE","Dependent_Variable","Focus_Variable",
    "Coefficient","SE_Value","p","N","R2"
]).to_csv(TABLES / "Table_5_reproduced.csv", index=False)

print("Replication complete.")
print("Important: Damodaran WACC specifications are construction/consistency validation, not causal tests.")
