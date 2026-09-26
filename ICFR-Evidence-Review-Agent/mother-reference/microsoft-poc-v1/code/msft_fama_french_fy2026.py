#!/usr/bin/env python3
"""Execute a bounded Microsoft FY2026 Fama-French factor validation.

Public/reproducible inputs only:
- Frozen MSFT monthly IEX closing-price observations in microsoft_fama_french_fy2026_input.csv.
- Kenneth R. French U.S. Fama/French 5 Factors (2x3), monthly CSV archive.

Important boundary: MSFT returns here are close-to-close PRICE returns and exclude dividends.
The 12-month FY2026 regression is exploratory and is not a production risk model.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
import re
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "microsoft_fama_french_fy2026_input.csv"
MERGED = ROOT / "microsoft_fama_french_fy2026_merged.csv"
RESULTS = ROOT / "microsoft_fama_french_results.csv"
PROVENANCE = ROOT / "microsoft_fama_french_provenance.json"
REPORT = ROOT / "MICROSOFT_FAMA_FRENCH_FY2026.md"

FF_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip"
FF_LIBRARY = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"
START_MONTH = "2025-07"
END_MONTH = "2026-06"


def download_ff5() -> tuple[pd.DataFrame, dict]:
    req = urllib.request.Request(
        FF_URL,
        headers={
            "User-Agent": "NAAIL-OpenLab/2026 academic-research reproducibility; public-data validation"
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = resp.read()
    digest = hashlib.sha256(payload).hexdigest()
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        names = zf.namelist()
        csv_name = next((n for n in names if n.lower().endswith(".csv")), None)
        if not csv_name:
            raise RuntimeError(f"No CSV found in Fama-French archive: {names}")
        text = zf.read(csv_name).decode("utf-8-sig", errors="replace")

    rows = []
    for line in text.splitlines():
        parts = [p.strip() for p in line.split(",")]
        if not parts or not re.fullmatch(r"\d{6}", parts[0]):
            continue
        if len(parts) < 7:
            continue
        try:
            values = [float(x) for x in parts[1:7]]
        except ValueError:
            continue
        rows.append([parts[0], *values])

    ff = pd.DataFrame(rows, columns=["yyyymm", "Mkt_RF", "SMB", "HML", "RMW", "CMA", "RF"])
    if ff.empty:
        raise RuntimeError("Parsed zero monthly Fama-French observations")
    ff["month"] = pd.to_datetime(ff["yyyymm"], format="%Y%m").dt.to_period("M").astype(str)
    if ff["yyyymm"].max() < "202606":
        raise RuntimeError(
            f"Fama-French archive is stale for FY2026: latest month={ff['yyyymm'].max()}"
        )
    meta = {
        "source_url": FF_URL,
        "data_library_url": FF_LIBRARY,
        "archive_sha256": digest,
        "archive_bytes": len(payload),
        "archive_member": csv_name,
        "latest_month_in_archive": ff["yyyymm"].max(),
    }
    return ff, meta


def build_msft_returns() -> pd.DataFrame:
    px = pd.read_csv(INPUT)
    required = {"month", "close_usd", "source", "feed", "status"}
    missing = required - set(px.columns)
    if missing:
        raise RuntimeError(f"Missing MSFT input columns: {sorted(missing)}")
    if px["month"].duplicated().any():
        raise RuntimeError("Duplicate month in MSFT price input")
    px = px.sort_values("month").reset_index(drop=True)
    if list(px["month"])[0] != "2025-06" or list(px["month"])[-1] != "2026-06":
        raise RuntimeError("MSFT input must span baseline 2025-06 through 2026-06")
    px["msft_price_return_pct"] = px["close_usd"].pct_change() * 100.0
    out = px[(px["month"] >= START_MONTH) & (px["month"] <= END_MONTH)].copy()
    if len(out) != 12 or out["msft_price_return_pct"].isna().any():
        raise RuntimeError(f"Expected 12 FY2026 monthly returns, got {len(out)}")
    return out


def fit_model(df: pd.DataFrame, model: str, factors: list[str]) -> tuple[object, list[dict]]:
    y = df["msft_excess_price_return_pct"]
    X = sm.add_constant(df[factors], has_constant="add")
    fit = sm.OLS(y, X).fit(cov_type="HC3")
    rows = []
    for term in fit.params.index:
        rows.append(
            {
                "model": model,
                "term": term,
                "coefficient": float(fit.params[term]),
                "hc3_se": float(fit.bse[term]),
                "hc3_t": float(fit.tvalues[term]),
                "hc3_p": float(fit.pvalues[term]),
                "n": int(fit.nobs),
                "r_squared": float(fit.rsquared),
                "adj_r_squared": float(fit.rsquared_adj),
            }
        )
    return fit, rows


def fnum(x: float, digits: int = 4) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "NA"
    return f"{x:.{digits}f}"


def main() -> None:
    ff, ff_meta = download_ff5()
    msft = build_msft_returns()
    ff_window = ff[(ff["month"] >= START_MONTH) & (ff["month"] <= END_MONTH)].copy()
    merged = msft.merge(ff_window[["month", "Mkt_RF", "SMB", "HML", "RMW", "CMA", "RF"]], on="month", how="inner")
    if len(merged) != 12:
        missing = sorted(set(msft["month"]) - set(merged["month"]))
        raise RuntimeError(f"Expected 12 merged months; got {len(merged)}; missing={missing}")

    merged["msft_excess_price_return_pct"] = merged["msft_price_return_pct"] - merged["RF"]
    merged.to_csv(MERGED, index=False)

    model_specs = {
        "CAPM": ["Mkt_RF"],
        "FF3": ["Mkt_RF", "SMB", "HML"],
        "FF5": ["Mkt_RF", "SMB", "HML", "RMW", "CMA"],
    }
    fits = {}
    result_rows = []
    for name, factors in model_specs.items():
        fit, rows = fit_model(merged, name, factors)
        fits[name] = fit
        result_rows.extend(rows)
    pd.DataFrame(result_rows).to_csv(RESULTS, index=False)

    ff5 = fits["FF5"]
    alpha = float(ff5.params["const"])
    alpha_ann = ((1.0 + alpha / 100.0) ** 12 - 1.0) * 100.0 if alpha > -100 else float("nan")
    market_beta = float(ff5.params["Mkt_RF"])

    provenance = {
        "prototype_id": "NAAIL-MSFT-POC-V1-FY2026",
        "execution_status": "EXECUTED_BOUNDED_MONTHLY_FF5",
        "period": "2025-07 through 2026-06",
        "observations": 12,
        "msft_input": {
            "file": INPUT.name,
            "source": "Alpaca market-data connector / IEX monthly bars",
            "return_definition": "month-end close-to-close simple PRICE return; dividends excluded",
        },
        "fama_french": ff_meta,
        "models": model_specs,
        "inference": "OLS coefficients with HC3 heteroskedasticity-robust standard errors; exploratory because n=12",
        "limitations": [
            "MSFT returns exclude dividends and therefore are not total shareholder returns.",
            "Only 12 monthly FY2026 observations are available; FF5 has very low residual degrees of freedom.",
            "This is a bounded factor-exposure validation, not a causal model or forecast.",
            "Independent replication remains required.",
        ],
    }
    PROVENANCE.write_text(json.dumps(provenance, indent=2), encoding="utf-8")

    coef_lines = []
    for term in ["const", "Mkt_RF", "SMB", "HML", "RMW", "CMA"]:
        coef_lines.append(
            f"| {term} | {fnum(float(ff5.params[term]))} | {fnum(float(ff5.bse[term]))} | {fnum(float(ff5.tvalues[term]))} | {fnum(float(ff5.pvalues[term]))} |"
        )

    report = f"""# Microsoft FY2026 Fama–French Validation — Executed Bounded Monthly Model

**Maturity:** `RESEARCH_PROTOTYPE`  
**Execution status:** `EXECUTED_BOUNDED_MONTHLY_FF5`  
**Golden Anchor:** Microsoft Corporation  
**Window:** July 2025–June 2026  
**Observations:** 12 monthly returns  
**Production approval:** NO

## Data and method

MSFT monthly closes are frozen from the Alpaca market-data connector using the IEX feed. Returns are simple month-end close-to-close **price returns** and therefore exclude dividends. The Fama/French five factors are downloaded at execution time from Kenneth R. French's official Data Library monthly U.S. 5-factor archive. Factor values are percentages; the dependent variable is MSFT price return minus the French `RF` series.

Three nested OLS specifications are estimated: CAPM, FF3 and FF5. Reported coefficient uncertainty uses HC3 heteroskedasticity-robust standard errors. With only 12 monthly FY2026 observations, inferential claims are deliberately limited.

## FF5 coefficient table

| Term | Coefficient | HC3 SE | HC3 t | HC3 p |
|---|---:|---:|---:|---:|
{chr(10).join(coef_lines)}

## Model diagnostics

- FF5 R²: **{fnum(float(ff5.rsquared))}**
- FF5 adjusted R²: **{fnum(float(ff5.rsquared_adj))}**
- Monthly alpha (intercept): **{fnum(alpha)} percentage points**
- Mechanically annualized alpha from monthly intercept: **{fnum(alpha_ann)}%** — descriptive only, not a forecast
- Market loading (`Mkt_RF`): **{fnum(market_beta)}**

## Interpretation boundary

This run closes the prior *not-executed* Fama–French implementation gate at a bounded exploratory level, but it does **not** establish a stable long-run Microsoft factor model. Twelve observations are too few for strong FF5 inference, and the stock-return input excludes dividends. The result is useful as a reproducible prototype test of the Finance engine, not as investment advice, causal evidence or production risk estimation.

## Reproducibility artifacts

- `code/msft_fama_french_fy2026.py`
- `microsoft_fama_french_fy2026_input.csv`
- `microsoft_fama_french_fy2026_merged.csv`
- `microsoft_fama_french_results.csv`
- `microsoft_fama_french_provenance.json`

Official factor source: {FF_LIBRARY}

## Remaining Microsoft V1 scientific gates

- independent replication / alternative market-return source;
- total-return sensitivity including dividends;
- longer-window factor-stability sensitivity;
- aggregate PatentsView innovation validation;
- NAAIL professional-task model benchmark and Cost per Verified Professional Output™;
- actual T0–T3 participant experiment;
- remaining falsification/robustness challenges.

**Overall Microsoft V1 maturity remains `RESEARCH_PROTOTYPE`.**
"""
    REPORT.write_text(report, encoding="utf-8")
    print("EXECUTED_BOUNDED_MONTHLY_FF5")
    print(f"n={int(ff5.nobs)} r2={ff5.rsquared:.6f} adj_r2={ff5.rsquared_adj:.6f}")
    print(f"alpha_monthly_pct={alpha:.6f} market_beta={market_beta:.6f}")


if __name__ == "__main__":
    main()
