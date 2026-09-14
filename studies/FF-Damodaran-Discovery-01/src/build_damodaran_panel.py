from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "damodaran"
OUT = ROOT / "data" / "processed"
SOURCES = {"DAM_BETA": "beta", "DAM_WACC": "wacc", "DAM_EVA": "eva"}


def slug(x: object) -> str:
    s = str(x).strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "unnamed"


def read_damodaran_xls(path: Path, prefix: str, year: int) -> pd.DataFrame:
    preview = pd.read_excel(path, header=None)
    header_row = None
    for i in range(min(len(preview), 30)):
        vals = preview.iloc[i].astype(str).str.strip().str.lower().tolist()
        if any(v == "industry name" for v in vals):
            header_row = i
            break
    if header_row is None:
        raise ValueError(f"Could not locate 'Industry Name' header in {path}")

    df = pd.read_excel(path, header=header_row)
    df = df.dropna(how="all").copy()
    industry_col = next((c for c in df.columns if str(c).strip().lower() == "industry name"), None)
    if industry_col is None:
        raise ValueError(f"Industry column missing in {path}")

    df = df.rename(columns={industry_col: "damodaran_industry"})
    df["damodaran_industry"] = df["damodaran_industry"].astype(str).str.strip()
    df = df[~df["damodaran_industry"].str.lower().isin({"nan", "total market", "total market (without financials)"})]
    df = df[df["damodaran_industry"].ne("")]

    rename = {}
    for c in df.columns:
        if c == "damodaran_industry":
            continue
        rename[c] = f"{prefix}_{slug(c)}"
    df = df.rename(columns=rename)
    df.insert(0, "year", year)
    return df


def load_source(source_id: str, prefix: str) -> pd.DataFrame:
    folder = RAW / source_id.lower()
    frames = []
    for path in sorted(folder.glob(f"{source_id}_*.xls")):
        year = int(path.stem.rsplit("_", 1)[1])
        frames.append(read_damodaran_xls(path, prefix, year))
    if not frames:
        raise FileNotFoundError(f"No files found in {folder}. Run download_sources.py first.")
    return pd.concat(frames, ignore_index=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    merged = None
    for source_id, prefix in SOURCES.items():
        df = load_source(source_id, prefix)
        key = ["year", "damodaran_industry"]
        if df.duplicated(key).any():
            dups = df.loc[df.duplicated(key, keep=False), key]
            raise ValueError(f"Duplicate Damodaran industry-year keys in {source_id}:\n{dups.head()}")
        merged = df if merged is None else merged.merge(df, on=key, how="outer", validate="one_to_one")

    assert merged is not None
    merged = merged.sort_values(["year", "damodaran_industry"]).reset_index(drop=True)
    merged.to_csv(OUT / "damodaran_industry_year.csv", index=False)
    print(f"Damodaran industry-year rows: {len(merged):,}; years: {merged['year'].min()}-{merged['year'].max()}")


if __name__ == "__main__":
    main()
