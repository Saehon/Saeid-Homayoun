from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error

@dataclass
class EmpiricalSpec:
    outcome: str
    key_x: str
    controls: list[str]
    entity: str | None = None
    time: str | None = None
    cluster: str | None = None

def _formula(spec: EmpiricalSpec) -> str:
    rhs = [spec.key_x] + spec.controls
    if spec.entity:
        rhs.append(f"C({spec.entity})")
    if spec.time:
        rhs.append(f"C({spec.time})")
    return f"{spec.outcome} ~ " + " + ".join(rhs)

def fit_model(df: pd.DataFrame, spec: EmpiricalSpec):
    model = smf.ols(_formula(spec), data=df)
    if spec.cluster and spec.cluster in df.columns and df[spec.cluster].nunique() > 1:
        groups = df.loc[model.data.row_labels, spec.cluster]
        return model.fit(cov_type="cluster", cov_kwds={"groups":groups})
    return model.fit(cov_type="HC3")

def table1_variable_dna(spec: EmpiricalSpec) -> pd.DataFrame:
    rows = [
        {"variable":spec.outcome,"role":"Outcome","construction":"Verify Variable DNA before inference"},
        {"variable":spec.key_x,"role":"Key explanatory/treatment","construction":"Causal status not assumed"},
    ]
    rows += [{"variable":c,"role":"Control","construction":"Pre-specify timing and rationale"} for c in spec.controls]
    if spec.entity: rows.append({"variable":spec.entity,"role":"Entity FE","construction":"Categorical fixed effect"})
    if spec.time: rows.append({"variable":spec.time,"role":"Time FE","construction":"Categorical fixed effect"})
    return pd.DataFrame(rows)

def table2_descriptives(df: pd.DataFrame, vars_: list[str]) -> pd.DataFrame:
    out = df[vars_].apply(pd.to_numeric, errors="coerce").describe(percentiles=[.25,.5,.75]).T
    return out[["count","mean","std","min","25%","50%","75%","max"]].reset_index(names="variable")

def table3_correlations(df: pd.DataFrame, vars_: list[str]) -> pd.DataFrame:
    return df[vars_].apply(pd.to_numeric, errors="coerce").corr().round(4)

def table4_main(df: pd.DataFrame, spec: EmpiricalSpec) -> pd.DataFrame:
    res = fit_model(df, spec)
    rows = []
    for v in [spec.key_x] + spec.controls:
        if v in res.params.index:
            rows.append({
                "variable":v, "coef":res.params[v], "se":res.bse[v], "t":res.tvalues[v],
                "p":res.pvalues[v], "n":int(res.nobs), "r2":res.rsquared,
                "classification":"associational unless Identification Gate is satisfied"
            })
    return pd.DataFrame(rows)

def table5_robustness(df: pd.DataFrame, spec: EmpiricalSpec) -> pd.DataFrame:
    base = fit_model(df, spec)
    reduced = EmpiricalSpec(spec.outcome, spec.key_x, [], spec.entity, spec.time, spec.cluster)
    red = fit_model(df, reduced)
    key = spec.key_x
    sign_same = np.sign(base.params.get(key,np.nan)) == np.sign(red.params.get(key,np.nan))
    return pd.DataFrame([
        {"test":"Baseline vs reduced controls","baseline_coef":base.params.get(key,np.nan),
         "alternative_coef":red.params.get(key,np.nan),"passes":bool(sign_same),
         "interpretation":"Specification sensitivity only; not causal validation."},
        {"test":"Discovery gate","baseline_coef":np.nan,"alternative_coef":np.nan,"passes":False,
         "interpretation":"Construct validity, identification, replication and welfare validation remain required."}
    ])

def table6_temporal_oos(df: pd.DataFrame, spec: EmpiricalSpec, time_col: str) -> pd.DataFrame:
    vals = sorted(df[time_col].dropna().unique())
    if len(vals) < 3:
        return pd.DataFrame([{"status":"Insufficient time periods for temporal holdout"}])
    holdout = vals[-1]
    train = df[df[time_col] != holdout]
    test = df[df[time_col] == holdout]
    ospec = EmpiricalSpec(spec.outcome, spec.key_x, spec.controls, spec.entity, None, spec.cluster)
    model = smf.ols(_formula(ospec), data=train).fit()
    try:
        pred = model.predict(test)
        rmse = float(np.sqrt(mean_squared_error(test[spec.outcome], pred)))
        return pd.DataFrame([{
            "holdout":holdout,"train_n":len(train),"test_n":len(test),"rmse":rmse,
            "model":_formula(ospec),
            "interpretation":"Temporal OOS predictive check; not causal identification."
        }])
    except Exception as e:
        return pd.DataFrame([{"holdout":holdout,"status":f"OOS prediction failed: {e}"}])

def run_six_tables(df: pd.DataFrame, spec: EmpiricalSpec, time_for_oos: str | None=None) -> dict[str,pd.DataFrame]:
    vars_ = [spec.outcome, spec.key_x] + spec.controls
    return {
        "table1_variable_dna": table1_variable_dna(spec),
        "table2_descriptives": table2_descriptives(df, vars_),
        "table3_correlations": table3_correlations(df, vars_),
        "table4_main": table4_main(df, spec),
        "table5_robustness": table5_robustness(df, spec),
        "table6_oos": table6_temporal_oos(df, spec, time_for_oos) if time_for_oos else pd.DataFrame([{"status":"No time field selected"}]),
    }

def stata_do(spec: EmpiricalSpec, csv_name="econova_input.csv") -> str:
    controls = " ".join(spec.controls)
    fe = []
    if spec.entity:
        fe.append(f"i.{spec.entity}")
    if spec.time:
        fe.append(f"i.{spec.time}")
    rhs = " ".join([spec.key_x, controls] + fe).strip()
    cluster = f", vce(cluster {spec.cluster})" if spec.cluster else ", vce(robust)"
    lines = [
        "clear all",
        "set more off",
        f'import delimited using "{csv_name}", clear',
        "",
        "* ECONOVA-S v0.2 associational baseline",
        f"reg {spec.outcome} {rhs}{cluster}",
        "",
        "* IMPORTANT:",
        "* This regression is NOT automatically causal.",
        "* Apply Identification Gate, robustness/falsification, replication,",
        "* economic significance, welfare interpretation, and Human Gate."
    ]
    return "\n".join(lines) + "\n"
