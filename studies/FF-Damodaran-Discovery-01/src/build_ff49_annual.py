from __future__ import annotations

import csv
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "fama_french"
OUT = ROOT / "data" / "processed"
MONTH_RE = re.compile(r"^\d{6}$")


def extracted_csv(source_id: str) -> Path:
    folder = RAW / source_id
    files = list(folder.glob("*.CSV")) + list(folder.glob("*.csv"))
    if len(files) != 1:
        raise FileNotFoundError(f"Expected one CSV in {folder}; found {files}")
    return files[0]


def first_monthly_block(path: Path) -> pd.DataFrame:
    lines = path.read_text(encoding="latin1").splitlines()
    rows = list(csv.reader(lines))
    first = None
    for i, row in enumerate(rows):
        if row and MONTH_RE.match(row[0].strip()):
            first = i
            break
    if first is None:
        raise ValueError(f"No YYYYMM monthly block found in {path}")

    header_i = first - 1
    while header_i >= 0 and not any(c.strip() for c in rows[header_i]):
        header_i -= 1
    raw_header = rows[header_i]
    header = ["yyyymm"] + [c.strip() for c in raw_header[1:]]

    data = []
    for row in rows[first:]:
        if not row or not MONTH_RE.match(row[0].strip()):
            break
        values = [row[0].strip()] + [c.strip() for c in row[1:len(header)]]
        data.append(values)

    df = pd.DataFrame(data, columns=header)
    df["yyyymm"] = pd.to_numeric(df["yyyymm"], errors="raise").astype(int)
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
        df[c] = df[c].replace([-99.99, -999.0, -999.99], np.nan) / 100.0
    df["year"] = df["yyyymm"] // 100
    return df


def compound_annual(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    def compound(s: pd.Series) -> float:
        x = s.dropna()
        return np.nan if x.empty else float((1.0 + x).prod() - 1.0)

    return df.groupby("year", as_index=False)[cols].agg(compound)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    ff49 = first_monthly_block(extracted_csv("FF49_MONTHLY"))
    industries = [c for c in ff49.columns if c not in {"yyyymm", "year"}]
    annual49 = compound_annual(ff49, industries)
    long49 = annual49.melt(id_vars="year", var_name="ff49_industry", value_name="industry_return")
    long49.to_csv(OUT / "ff49_industry_year.csv", index=False)

    ff5 = first_monthly_block(extracted_csv("FF5_MONTHLY"))
    mom = first_monthly_block(extracted_csv("MOM_MONTHLY"))
    ff5_cols = [c for c in ff5.columns if c not in {"yyyymm", "year"}]
    mom_cols = [c for c in mom.columns if c not in {"yyyymm", "year"}]
    a5 = compound_annual(ff5, ff5_cols)
    am = compound_annual(mom, mom_cols)
    factors = a5.merge(am, on="year", how="outer", validate="one_to_one")
    factors.to_csv(OUT / "ff_factors_year.csv", index=False)

    print(f"FF49 annual rows: {len(long49):,}; factor years: {len(factors):,}")


if __name__ == "__main__":
    main()
