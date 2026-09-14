from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data" / "processed" / "econova_ff_damodaran_panel.csv"
OUT = ROOT / "results" / "baseline"


def safe(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", s).strip("_").lower()


def detect(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    cols = {safe(c): c for c in df.columns}
    wanted_fund = [
        "beta_beta", "beta_d_e_ratio", "beta_unlevered_beta",
        "wacc_cost_of_capital", "wacc_cost_of_equity",
        "eva_roe", "eva_roc", "eva_roc_wacc",
    ]
    fund = [cols[x] for x in wanted_fund if x in cols]
    factor = [c for c in df.columns if safe(c).startswith("ff_beta_")]
    return fund, factor


def table1(fund: list[str], factor: list[str]) -> pd.DataFrame:
    rows = [
        ("future_industry_return_1y", "Outcome", "FF49 industry return in year t+1"),
        ("industry_return", "Market outcome", "FF49 industry return in year t"),
    ]
    rows += [(x, "Damodaran fundamental", f"Year-t Damodaran industry measure: {x}") for x in fund]
    rows += [(x, "Fama-French exposure", f"Rolling 60-month FF5+Momentum loading available at end of year t: {x}") for x in factor]
    return pd.DataFrame(rows, columns=["variable", "role", "definition"])


def describe(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    d = df[cols].describe(percentiles=[0.25, 0.5, 0.75]).T
    return d[["count", "mean", "std", "min", "25%", "50%", "75%", "max"]]


def fit_clustered(df: pd.DataFrame, predictors: list[str]) -> pd.DataFrame:
    use = df[["future_industry_return_1y", "ff49_industry", "year"] + predictors].dropna().copy()
    if len(use) < 30 or not predictors:
        return pd.DataFrame()

    X = pd.get_dummies(
        use[predictors + ["ff49_industry", "year"]].assign(year=use["year"].astype(str)),
        columns=["ff49_industry", "year"],
        drop_first=True,
        dtype=float,
    )
    X = sm.add_constant(X, has_constant="add")
    y = use["future_industry_return_1y"].astype(float)
    model = sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": use["ff49_industry"]})

    keep = ["const"] + predictors
    rows = []
    for v in keep:
        if v not in model.params:
            continue
        rows.append({
            "variable": v,
            "coef": model.params[v],
            "std_err_cluster_industry": model.bse[v],
            "t": model.tvalues[v],
            "p_value_descriptive_not_fitness": model.pvalues[v],
            "n": int(model.nobs),
            "adj_r2": model.rsquared_adj,
            "industry_fe": True,
            "year_fe": True,
            "se_cluster": "industry",
        })
    return pd.DataFrame(rows)


def expanding_oos(df: pd.DataFrame, predictors: list[str], label: str) -> dict:
    use = df[["year", "ff49_industry", "future_industry_return_1y"] + predictors].dropna().copy()
    years = sorted(use["year"].unique())
    preds, actual, benchmark = [], [], []
    for test_year in years[5:]:
        train = use[use["year"] < test_year]
        test = use[use["year"] == test_year]
        if train.empty or test.empty:
            continue

        combined = pd.concat([train, test], ignore_index=True)
        X = pd.get_dummies(
            combined[predictors + ["ff49_industry"]],
            columns=["ff49_industry"],
            drop_first=True,
            dtype=float,
        )
        X_train = X.iloc[:len(train)]
        X_test = X.iloc[len(train):]
        model = LinearRegression().fit(X_train, train["future_industry_return_1y"])
        pred = model.predict(X_test)

        preds.extend(pred.tolist())
        actual.extend(test["future_industry_return_1y"].tolist())
        benchmark.extend([train["future_industry_return_1y"].mean()] * len(test))

    if not actual:
        return {"model": label, "n_oos": 0, "oos_r2": np.nan, "mae": np.nan, "rmse": np.nan}

    y = np.asarray(actual)
    p = np.asarray(preds)
    b = np.asarray(benchmark)
    sse = np.square(y - p).sum()
    sse_b = np.square(y - b).sum()
    return {
        "model": label,
        "n_oos": len(y),
        "oos_r2": 1 - sse / sse_b if sse_b > 0 else np.nan,
        "mae": mean_absolute_error(y, p),
        "rmse": mean_squared_error(y, p) ** 0.5,
        "validation": "expanding_window_temporal",
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(PANEL)
    fund, factor = detect(df)
    if not fund:
        raise RuntimeError("No canonical Damodaran predictors detected; inspect processed column names.")
    if not factor:
        raise RuntimeError("No rolling FF factor exposures detected; run build_factor_exposures.py first.")

    table1(fund, factor).to_csv(OUT / "table1_variable_definitions.csv", index=False)
    desc_cols = ["future_industry_return_1y", "industry_return"] + fund + factor
    describe(df, desc_cols).to_csv(OUT / "table2_descriptive_statistics.csv")
    df[desc_cols].corr().to_csv(OUT / "table3_correlations.csv")

    models = []
    for label, x in [
        ("Factor-exposure-only", factor),
        ("Fundamentals-only", fund),
        ("Combined", factor + fund),
    ]:
        res = fit_clustered(df, x)
        if not res.empty:
            res.insert(0, "model", label)
            models.append(res)
    if not models:
        raise RuntimeError("No baseline regression had sufficient complete observations.")
    pd.concat(models, ignore_index=True).to_csv(OUT / "table4_main_regressions.csv", index=False)

    oos = pd.DataFrame([
        expanding_oos(df, factor, "Factor-exposure-only"),
        expanding_oos(df, fund, "Fundamentals-only"),
        expanding_oos(df, factor + fund, "Combined"),
    ])
    factor_r2 = oos.loc[oos["model"].eq("Factor-exposure-only"), "oos_r2"].iloc[0]
    oos["incremental_oos_r2_vs_factor_only"] = oos["oos_r2"] - factor_r2
    oos.to_csv(OUT / "table5_temporal_oos_and_data_value.csv", index=False)

    print(f"Wrote Tables 1-5 to {OUT}")
    print(f"Damodaran predictors: {fund}")
    print(f"Industry-specific FF exposures: {factor}")


if __name__ == "__main__":
    main()
