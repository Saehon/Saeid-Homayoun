"""Replicable 10-firm Damodaran builder/supplier cash-flow PROXY pilot.

Usage:
    python analysis/run_10firm_pilot.py path/to/10firm_pilot_FY2023_FY2025_secondary_cashflows.csv

Data are held in the canonical (restricted) project Drive, not this public
repo, due to S&P-sourced standardized table redistribution restrictions.
Only publicly share the source manifest, methodology and summary statistics.

RESEARCH CAUTION: company-wide gross PP&E CapEx is NOT AI-specific CapEx;
operating cash flow - gross PP&E CapEx is NOT Damodaran FCFF.
These selected, tiny sample comparisons are descriptive, not causal or
representative tests of FT50 hypotheses on CAM, PCAOB or ICFR.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, fisher_exact, wilcoxon

REQUIRED = {"ticker", "role", "fiscal_year", "operating_cash_flow_usd_m",
            "gross_cash_capex_usd_m"}

def load_and_validate(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if REQUIRED.difference(df.columns):
        raise ValueError(f"Missing columns: {REQUIRED.difference(df.columns)}")
    if len(df) != 30 or df.ticker.nunique() != 10:
        raise ValueError("Expected 30 firm-years and 10 unique issuers")
    if df.duplicated(["ticker", "fiscal_year"]).any():
        raise ValueError("Duplicate ticker/fiscal_year")
    if set(df.fiscal_year) != {2023, 2024, 2025}:
        raise ValueError("Expected FY2023–FY2025")
    n = df[["ticker", "role"]].drop_duplicates().groupby("role").size()
    if n.to_dict() != {"Builder": 5, "Supplier": 5}:
        raise ValueError("Exactly five builders and five suppliers required")
    if (df[["operating_cash_flow_usd_m", "gross_cash_capex_usd_m"]] <= 0).any().any():
        raise ValueError("Cannot compute CapEx/OCF with non-positive denominator")
    df["ratio"] = df.gross_cash_capex_usd_m / df.operating_cash_flow_usd_m
    df["gross_cash_fcf_proxy"] = df.operating_cash_flow_usd_m - df.gross_cash_capex_usd_m
    return df

def permutation_5v5(values, groups):
    x = np.asarray(values, dtype=float)
    mask = np.asarray(groups) == "Builder"
    if len(x) != 10 or int(mask.sum()) != 5:
        raise ValueError("Requires 5:5 sample")
    obs = float(x[mask].mean() - x[~mask].mean())
    null=[]
    for inds in itertools.combinations(range(10), 5):
        m = np.zeros(10,dtype=bool);m[list(inds)] = True
        null.append(float(x[m].mean() - x[~m].mean()))
    return {"mean_diff": obs, "p_two_sided": float(np.mean(np.abs(null) >= abs(obs)-1e-12)),
            "possible_allocations":len(null)}

def analyze(df):
    w = df.pivot(index=["ticker","role"], columns="fiscal_year", values="ratio").reset_index()
    w["delta_2025_2023"]=w[2025]-w[2023]
    b=w[w.role=="Builder"];s=w[w.role=="Supplier"]
    p_a=permutation_5v5(w[2025],w.role)
    p_b=permutation_5v5(w.delta_2025_2023,w.role)
    man=mannwhitneyu(b[2025],s[2025],method="exact",alternative="two-sided")
    wil=wilcoxon(b.delta_2025_2023,method="exact",alternative="greater")
    annual=df.pivot(index=["ticker","role"],columns="fiscal_year",
                    values=["operating_cash_flow_usd_m","gross_cash_capex_usd_m"])
    counts={"Builder":[0,0],"Supplier":[0,0]}
    for (_,group),row in annual.iterrows():
        greater=(row[("gross_cash_capex_usd_m",2025)] / row[("gross_cash_capex_usd_m",2023)] >
                 row[("operating_cash_flow_usd_m",2025)] / row[("operating_cash_flow_usd_m",2023)])
        counts[group][0 if greater else 1]+=1
    fish=fisher_exact([counts["Builder"], counts["Supplier"]], alternative="two-sided")
    pvals=np.array([p_a["p_two_sided"],p_b["p_two_sided"]])
    order=np.argsort(pvals);corrected=np.zeros(2)
    prev=0.0
    for k,index in enumerate(order):
        prev=max(prev,min(1.0,float((2-k)*pvals[index])))
        corrected[index]=prev
    return {"group_median_2025":{"Builder":float(b[2025].median()),"Supplier":float(s[2025].median())},
            "group_median_change_2023_2025":{"Builder":float(b.delta_2025_2023.median()),
              "Supplier":float(s.delta_2025_2023.median())},
            "exact_perm_2025_ratio":p_a, "exact_perm_change":p_b,
            "holm_2025_ratio_and_change":corrected.tolist(),
            "mann_whitney_2025":{"U":float(man.statistic),"p":float(man.pvalue)},
            "wilcoxon_builders_2023_2025":{"W":float(wil.statistic),"p":float(wil.pvalue)},
            "growth_outpaces_operating_cashflow":{**counts,"fisher_p":float(fish.pvalue)},
            "disclaimer":"Nonrandom 10-firm descriptive financial PROXY pilot, not AI CapEx nor audit oversight evidence."}

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("csv_path",help="Download the controlled 30-row CSV from Google Drive")
    args=parser.parse_args()
    print(json.dumps(analyze(load_and_validate(args.csv_path)),indent=2))
