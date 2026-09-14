from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, asdict
from io import BytesIO, StringIO
from pathlib import Path
import zipfile

import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm

BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/Historical_Archives/08%20{year}%20Update/ftp/{file}"
FF5_FILE = "F-F_Research_Data_5_Factors_2x3_CSV.zip"
PORT6_FILE = "6_Portfolios_2x3_CSV.zip"
FACTORS = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "RF"]
PORTS = ["SMALL LoBM", "ME1 BM2", "SMALL HiBM", "BIG LoBM", "ME2 BM2", "BIG HiBM"]
MODELS = {
    "CAPM": ["Mkt-RF"],
    "FF3": ["Mkt-RF", "SMB", "HML"],
    "FF5": ["Mkt-RF", "SMB", "HML", "RMW", "CMA"],
}


@dataclass
class SourceRecord:
    dataset: str
    archive_year: int
    url: str
    sha256: str
    bytes: int


def _get_zip(url: str, timeout: int = 60) -> tuple[bytes, SourceRecord]:
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "ECONOVA-S academic reproducibility study/0.3"})
    r.raise_for_status()
    blob = r.content
    return blob, SourceRecord("", 0, url, hashlib.sha256(blob).hexdigest(), len(blob))


def _zip_text(blob: bytes) -> str:
    with zipfile.ZipFile(BytesIO(blob)) as z:
        candidates = [n for n in z.namelist() if not n.endswith("/")]
        if not candidates:
            raise ValueError("Archive contains no file")
        return z.read(candidates[0]).decode("utf-8", errors="replace")


def _parse_first_monthly_block(raw: str, required_headers: list[str]) -> pd.DataFrame:
    lines = raw.splitlines()
    header_idx = None
    for i, line in enumerate(lines):
        if all(h in line for h in required_headers):
            header_idx = i
            break
    if header_idx is None:
        raise ValueError(f"Could not locate monthly header containing {required_headers}")

    rows: list[str] = []
    for line in lines[header_idx + 1 :]:
        first = line.split(",", 1)[0].strip()
        if first.isdigit() and len(first) == 6:
            rows.append(line)
        elif rows:
            break
    if not rows:
        raise ValueError("No monthly observations found")

    text = lines[header_idx] + "\n" + "\n".join(rows)
    df = pd.read_csv(StringIO(text))
    df.columns = [str(c).strip() for c in df.columns]
    df = df.rename(columns={df.columns[0]: "yyyymm"})
    df["date"] = pd.to_datetime(df["yyyymm"].astype(str), format="%Y%m")
    return df.drop(columns=["yyyymm"])


def parse_ff5(raw: str) -> pd.DataFrame:
    df = _parse_first_monthly_block(raw, ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "RF"])
    missing = [c for c in FACTORS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing factor columns: {missing}")
    for c in FACTORS:
        df[c] = pd.to_numeric(df[c], errors="coerce") / 100.0
    return df[["date"] + FACTORS].dropna().reset_index(drop=True)


def parse_port6(raw: str) -> pd.DataFrame:
    df = _parse_first_monthly_block(raw, ["SMALL LoBM", "SMALL HiBM", "BIG LoBM", "BIG HiBM"])
    missing = [c for c in PORTS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing portfolio columns: {missing}")
    for c in PORTS:
        df[c] = pd.to_numeric(df[c], errors="coerce") / 100.0
    return df[["date"] + PORTS].dropna().reset_index(drop=True)


def load_snapshot(year: int) -> tuple[pd.DataFrame, pd.DataFrame, list[SourceRecord]]:
    ff_url = BASE.format(year=year, file=FF5_FILE)
    p_url = BASE.format(year=year, file=PORT6_FILE)
    ff_blob, ff_rec = _get_zip(ff_url)
    p_blob, p_rec = _get_zip(p_url)
    ff_rec.dataset, ff_rec.archive_year = "FF5", year
    p_rec.dataset, p_rec.archive_year = "6_Portfolios_2x3", year
    return parse_ff5(_zip_text(ff_blob)), parse_port6(_zip_text(p_blob)), [ff_rec, p_rec]


def _align(old: pd.DataFrame, new: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    common = sorted(set(old["date"]) & set(new["date"]))
    if not common:
        raise ValueError("No common dates between snapshots")
    a = old[old["date"].isin(common)].sort_values("date").reset_index(drop=True)
    b = new[new["date"].isin(common)].sort_values("date").reset_index(drop=True)
    return a, b


def hac_mean_stats(s: pd.Series, lags: int = 6) -> dict:
    y = pd.to_numeric(s, errors="coerce").dropna().astype(float)
    X = np.ones((len(y), 1))
    res = sm.OLS(y.values, X).fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    return {"mean": float(res.params[0]), "se": float(res.bse[0]), "t": float(res.tvalues[0]), "p": float(res.pvalues[0]), "n": int(res.nobs)}


def table1_variable_dna() -> pd.DataFrame:
    rows = []
    for f in FACTORS:
        rows.append({"variable": f, "role": "factor/risk-free", "source": "Kenneth R. French FF5 archive", "unit": "monthly decimal return", "timing": "archive snapshot", "construction": "official archive; no researcher reconstruction"})
    for p in PORTS:
        rows.append({"variable": p, "role": "test asset", "source": "Kenneth R. French 6 Size×B/M portfolios archive", "unit": "monthly decimal return", "timing": "archive snapshot", "construction": "official value-weighted archive"})
    rows += [
        {"variable": "DCS", "role": "measurement-change construct", "source": "ECONOVA-S", "unit": "basis points/month", "timing": "same date old vs new", "construction": "10000 × mean(abs(new-old))"},
        {"variable": "Conclusion_Reversal", "role": "inference-stability construct", "source": "ECONOVA-S", "unit": "indicator", "timing": "same specification old vs new", "construction": "sign change OR 5% significance-status change"},
    ]
    return pd.DataFrame(rows)


def table2_descriptives(old_ff: pd.DataFrame, new_ff: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for label, df in [("FIZ_2024", old_ff), ("CIZ_2025", new_ff)]:
        for f in FACTORS:
            x = df[f]
            s = hac_mean_stats(x)
            rows.append({"snapshot": label, "variable": f, "n": len(x), "mean": x.mean(), "sd": x.std(ddof=1), "min": x.min(), "max": x.max(), "hac_t_mean": s["t"], "hac_p_mean": s["p"]})
    return pd.DataFrame(rows)


def dcs_table(old_df: pd.DataFrame, new_df: pd.DataFrame, columns: list[str], family: str) -> pd.DataFrame:
    rows = []
    for c in columns:
        a, b = old_df[c], new_df[c]
        d = b - a
        rows.append({
            "family": family,
            "variable": c,
            "n": len(d),
            "old_mean": a.mean(),
            "new_mean": b.mean(),
            "mean_difference_bps": 10000 * d.mean(),
            "DCS_mean_abs_bps": 10000 * d.abs().mean(),
            "max_abs_difference_bps": 10000 * d.abs().max(),
            "correlation": a.corr(b),
            "sign_flip_rate": float(((np.sign(a) != np.sign(b)) & (a != 0) & (b != 0)).mean()),
        })
    return pd.DataFrame(rows)


def _alpha(port: pd.Series, rf: pd.Series, factors: pd.DataFrame, xs: list[str], lags: int = 6) -> dict:
    y = (port - rf).astype(float)
    X = sm.add_constant(factors[xs].astype(float), has_constant="add")
    res = sm.OLS(y, X, missing="drop").fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    return {"alpha_monthly": float(res.params["const"]), "alpha_annualized": float(res.params["const"] * 12), "alpha_t": float(res.tvalues["const"]), "alpha_p": float(res.pvalues["const"]), "adj_r2": float(res.rsquared_adj), "n": int(res.nobs)}


def alpha_tables(old_ff: pd.DataFrame, new_ff: pd.DataFrame, old_p: pd.DataFrame, new_p: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, reversals = [], []
    for model, xs in MODELS.items():
        for p in PORTS:
            a = _alpha(old_p[p], old_ff["RF"], old_ff, xs)
            b = _alpha(new_p[p], new_ff["RF"], new_ff, xs)
            sig_a = a["alpha_p"] < 0.05
            sig_b = b["alpha_p"] < 0.05
            sign_change = np.sign(a["alpha_monthly"]) != np.sign(b["alpha_monthly"])
            sig_change = sig_a != sig_b
            reversal = bool(sign_change or sig_change)
            rows.append({"model": model, "portfolio": p, **{f"old_{k}": v for k, v in a.items()}, **{f"new_{k}": v for k, v in b.items()}, "alpha_change_bps_monthly": 10000 * (b["alpha_monthly"] - a["alpha_monthly"])})
            reversals.append({"model": model, "portfolio": p, "old_alpha_sign": int(np.sign(a["alpha_monthly"])), "new_alpha_sign": int(np.sign(b["alpha_monthly"])), "old_significant_5pct": bool(sig_a), "new_significant_5pct": bool(sig_b), "sign_change": bool(sign_change), "significance_change": bool(sig_change), "Conclusion_Reversal": reversal})
    return pd.DataFrame(rows), pd.DataFrame(reversals)


def subperiod_robustness(old_ff: pd.DataFrame, new_ff: pd.DataFrame) -> pd.DataFrame:
    periods = [("full_common", None, None), ("post_1963", "1963-07-01", None), ("post_1990", "1990-01-01", None), ("post_2000", "2000-01-01", None), ("post_GFC", "2009-01-01", None)]
    rows = []
    for name, start, end in periods:
        mask = pd.Series(True, index=old_ff.index)
        if start:
            mask &= old_ff["date"] >= pd.Timestamp(start)
        if end:
            mask &= old_ff["date"] <= pd.Timestamp(end)
        for f in FACTORS[:-1]:
            d = new_ff.loc[mask, f] - old_ff.loc[mask, f]
            rows.append({"subperiod": name, "factor": f, "n": int(mask.sum()), "DCS_mean_abs_bps": 10000 * d.abs().mean(), "mean_difference_bps": 10000 * d.mean(), "max_abs_difference_bps": 10000 * d.abs().max()})
    return pd.DataFrame(rows)


def factor_conclusion_reversals(old_ff: pd.DataFrame, new_ff: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for f in FACTORS[:-1]:
        a = hac_mean_stats(old_ff[f]); b = hac_mean_stats(new_ff[f])
        sign_change = np.sign(a["mean"]) != np.sign(b["mean"])
        sig_change = (a["p"] < .05) != (b["p"] < .05)
        rows.append({"object": "factor_premium", "variable": f, "old_mean": a["mean"], "new_mean": b["mean"], "old_p": a["p"], "new_p": b["p"], "sign_change": bool(sign_change), "significance_change": bool(sig_change), "Conclusion_Reversal": bool(sign_change or sig_change)})
    return pd.DataFrame(rows)


def write_outputs(old_year: int, new_year: int, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    old_ff, old_p, old_src = load_snapshot(old_year)
    new_ff, new_p, new_src = load_snapshot(new_year)
    old_ff, new_ff = _align(old_ff, new_ff)
    old_p, new_p = _align(old_p, new_p)

    # Require the factor and portfolio samples to share the same calendar.
    common = sorted(set(old_ff.date) & set(old_p.date) & set(new_ff.date) & set(new_p.date))
    old_ff = old_ff[old_ff.date.isin(common)].sort_values("date").reset_index(drop=True)
    new_ff = new_ff[new_ff.date.isin(common)].sort_values("date").reset_index(drop=True)
    old_p = old_p[old_p.date.isin(common)].sort_values("date").reset_index(drop=True)
    new_p = new_p[new_p.date.isin(common)].sort_values("date").reset_index(drop=True)

    t1 = table1_variable_dna()
    t2 = table2_descriptives(old_ff, new_ff)
    t3 = pd.concat([dcs_table(old_ff, new_ff, FACTORS, "factor"), dcs_table(old_p, new_p, PORTS, "portfolio")], ignore_index=True)
    t4, alpha_rev = alpha_tables(old_ff, new_ff, old_p, new_p)
    factor_rev = factor_conclusion_reversals(old_ff, new_ff)
    t5 = pd.concat([factor_rev, alpha_rev.assign(object="portfolio_alpha", variable=alpha_rev["portfolio"])], ignore_index=True, sort=False)
    t6 = subperiod_robustness(old_ff, new_ff)

    tables = {"table1_variable_dna": t1, "table2_descriptives": t2, "table3_dcs": t3, "table4_alpha_models": t4, "table5_conclusion_reversals": t5, "table6_subperiod_robustness": t6}
    for name, df in tables.items():
        df.to_csv(outdir / f"{name}.csv", index=False)

    source_records = [asdict(x) for x in (old_src + new_src)]
    passport = {
        "project": "ECONOVA-S",
        "study": "MNSc-FamaFrench-01",
        "title": "When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors",
        "old_archive_year": old_year,
        "new_archive_year": new_year,
        "common_start": str(pd.Timestamp(common[0]).date()),
        "common_end": str(pd.Timestamp(common[-1]).date()),
        "common_months": len(common),
        "sources": source_records,
        "methods": ["paired archive comparison", "HAC/Newey-West mean inference", "CAPM", "FF3", "FF5", "DCS", "Conclusion Reversal", "subperiod robustness"],
        "scientific_classification": "real-data reproducibility / measurement-change study",
        "causal_claim": False,
        "discovery_claim_allowed": False,
        "human_gate_required": True,
        "reversal_count": int(pd.to_numeric(t5["Conclusion_Reversal"], errors="coerce").fillna(False).astype(bool).sum()),
    }
    (outdir / "evidence_passport.json").write_text(json.dumps(passport, indent=2), encoding="utf-8")

    summary = f"""# ECONOVA-S™ Study Run Summary\n\n## Study\nMNSc–FamaFrench–01 — FIZ→CIZ measurement transition\n\n## Archive comparison\n- Old archive: July {old_year}\n- New archive: July {new_year}\n- Common monthly sample: {passport['common_start']} to {passport['common_end']} ({passport['common_months']} months)\n\n## Automated outputs\n- 6 empirical tables\n- DCS for factors and benchmark portfolios\n- CAPM/FF3/FF5 alpha comparison\n- Conclusion Reversal flags\n- subperiod robustness\n- source hashes and Evidence Passport\n\n## Scientific gate\n`discovery_claim_allowed = false`\n\nObserved differences must be interpreted as sensitivity to archived data construction/revisions unless a stronger causal decomposition is separately established.\n"""
    (outdir / "RUN_SUMMARY.md").write_text(summary, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", type=int, default=2024)
    ap.add_argument("--new", type=int, default=2025)
    ap.add_argument("--output", default="artifacts")
    args = ap.parse_args()
    write_outputs(args.old, args.new, Path(args.output))


if __name__ == "__main__":
    main()
