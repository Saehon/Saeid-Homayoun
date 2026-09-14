from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

from build_ff49_annual import extracted_csv, first_monthly_block

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed" / "ff49_factor_exposures_year.csv"
WINDOW = 60
MIN_OBS = 36


def safe(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", s).strip("_").lower()


def main() -> None:
    ff49 = first_monthly_block(extracted_csv("FF49_MONTHLY"))
    ff5 = first_monthly_block(extracted_csv("FF5_MONTHLY"))
    mom = first_monthly_block(extracted_csv("MOM_MONTHLY"))

    ff5 = ff5.drop(columns=["year"])
    mom = mom.drop(columns=["year"])
    factors = ff5.merge(mom, on="yyyymm", how="inner", validate="one_to_one")
    factors = factors.rename(columns={c: safe(c) for c in factors.columns})

    required = ["mkt_rf", "smb", "hml", "rmw", "cma"]
    mom_col = next((c for c in factors.columns if c in {"mom", "umd", "wml"} or "mom" in c), None)
    rf_col = next((c for c in factors.columns if c == "rf"), None)
    if mom_col is None or rf_col is None or any(c not in factors.columns for c in required):
        raise ValueError(f"Could not identify expected FF5/Momentum columns: {list(factors.columns)}")
    xcols = required + [mom_col]

    id_cols = ["yyyymm", "year"]
    industries = [c for c in ff49.columns if c not in id_cols]
    long = ff49.melt(id_vars=id_cols, value_vars=industries, var_name="ff49_industry", value_name="industry_return")
    long = long.merge(factors, on="yyyymm", how="inner", validate="many_to_one")
    long["excess_return"] = long["industry_return"] - long[rf_col]
    long = long.sort_values(["ff49_industry", "yyyymm"])

    rows = []
    for industry, g in long.groupby("ff49_industry", sort=True):
        g = g.reset_index(drop=True)
        for year in sorted(g["year"].unique()):
            end_idx = g.index[g["year"].eq(year)]
            if len(end_idx) == 0:
                continue
            end = int(end_idx.max())
            start = max(0, end - WINDOW + 1)
            w = g.loc[start:end, ["excess_return"] + xcols].dropna()
            if len(w) < MIN_OBS:
                continue
            X = sm.add_constant(w[xcols], has_constant="add")
            model = sm.OLS(w["excess_return"], X).fit()
            rec = {
                "year": int(year),
                "ff49_industry": industry,
                "factor_window_months": int(len(w)),
                "factor_regression_r2": float(model.rsquared),
            }
            for c in xcols:
                rec[f"ff_beta_{safe(c)}"] = float(model.params[c])
            rows.append(rec)

    out = pd.DataFrame(rows).sort_values(["ff49_industry", "year"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"Wrote {len(out):,} industry-year factor exposure rows to {OUT}")


if __name__ == "__main__":
    main()
