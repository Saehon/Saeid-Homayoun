from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "data" / "processed"
CW = ROOT / "crosswalk" / "reviewed_crosswalk.csv"
OUT = P / "econova_ff_damodaran_panel.csv"


def as_bool(s: pd.Series) -> pd.Series:
    return s.astype(str).str.strip().str.lower().isin({"true", "1", "yes", "y"})


def main() -> None:
    ff = pd.read_csv(P / "ff49_industry_year.csv")
    factors = pd.read_csv(P / "ff_factors_year.csv")
    dam = pd.read_csv(P / "damodaran_industry_year.csv")
    cw = pd.read_csv(CW)

    if cw.empty:
        raise RuntimeError(
            "reviewed_crosswalk.csv is empty. Run suggest_crosswalk.py, review mappings, "
            "assign weights, and copy approved rows into reviewed_crosswalk.csv."
        )

    required = {"year", "ff49_industry", "damodaran_industry", "mapping_weight", "mapping_confidence", "manual_review", "approved"}
    missing = required - set(cw.columns)
    if missing:
        raise ValueError(f"Crosswalk missing columns: {sorted(missing)}")

    cw = cw[as_bool(cw["approved"])].copy()
    if cw.empty:
        raise RuntimeError("No approved crosswalk rows.")
    cw["mapping_weight"] = pd.to_numeric(cw["mapping_weight"], errors="raise")
    if (cw["mapping_weight"] <= 0).any():
        raise ValueError("All approved mapping weights must be > 0.")

    sums = cw.groupby(["year", "ff49_industry"])["mapping_weight"].sum()
    bad = sums[~np.isclose(sums, 1.0, atol=1e-6)]
    if not bad.empty:
        raise ValueError(f"Mapping weights must sum to 1 within each year×FF49 industry:\n{bad.head(20)}")

    mapped = cw.merge(dam, on=["year", "damodaran_industry"], how="left", validate="many_to_one", indicator=True)
    missing_dam = mapped.loc[mapped["_merge"].ne("both"), ["year", "ff49_industry", "damodaran_industry"]]
    if not missing_dam.empty:
        raise ValueError(f"Approved mappings absent from Damodaran data:\n{missing_dam.head(20)}")
    mapped = mapped.drop(columns="_merge")

    numeric_cols = [c for c in dam.columns if c not in {"year", "damodaran_industry"} and pd.api.types.is_numeric_dtype(dam[c])]
    for c in numeric_cols:
        mapped[c] = mapped[c] * mapped["mapping_weight"]

    agg = mapped.groupby(["year", "ff49_industry"], as_index=False)[numeric_cols].sum(min_count=1)
    meta = mapped.groupby(["year", "ff49_industry"], as_index=False).agg(
        mapped_damodaran_industries=("damodaran_industry", "nunique"),
        min_mapping_confidence=("mapping_confidence", lambda x: ";".join(sorted(set(map(str, x)))))
    )
    agg = agg.merge(meta, on=["year", "ff49_industry"], validate="one_to_one")

    panel = ff.merge(agg, on=["year", "ff49_industry"], how="inner", validate="one_to_one")
    panel = panel.merge(factors, on="year", how="left", validate="many_to_one")
    panel = panel.sort_values(["ff49_industry", "year"]).reset_index(drop=True)
    panel["future_industry_return_1y"] = panel.groupby("ff49_industry")["industry_return"].shift(-1)
    panel.to_csv(OUT, index=False)

    coverage = len(panel) / max(1, len(ff))
    print(f"Wrote {len(panel):,} rows to {OUT}; FF49 coverage={coverage:.1%}")


if __name__ == "__main__":
    main()
