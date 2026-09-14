from __future__ import annotations

from difflib import SequenceMatcher
from pathlib import Path
import re

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
OUT = ROOT / "crosswalk" / "candidate_crosswalk.csv"

ALIASES = {
    "agric": "agriculture farming",
    "food": "food processing",
    "soda": "beverage soft",
    "beer": "beverage alcoholic",
    "smoke": "tobacco",
    "toys": "recreation entertainment",
    "fun": "recreation entertainment",
    "books": "publishing newspaper",
    "hshld": "household products",
    "clths": "apparel",
    "hlth": "healthcare products services",
    "medeq": "healthcare products medical equipment",
    "drugs": "drugs biotechnology pharmaceutical",
    "chems": "chemical",
    "rubbr": "rubber tire",
    "txtls": "textile apparel",
    "bldmt": "building materials",
    "cnstr": "construction engineering",
    "steel": "steel metals mining",
    "fabpr": "fabricated products machinery",
    "mach": "machinery",
    "elceq": "electrical equipment",
    "autos": "auto truck auto parts",
    "aero": "aerospace defense",
    "ships": "shipbuilding marine transportation",
    "guns": "aerospace defense",
    "gold": "precious metals mining gold",
    "mines": "metals mining",
    "coal": "coal related energy",
    "oil": "oil gas energy",
    "util": "utility power",
    "telcm": "telecom wireless",
    "persv": "business consumer services",
    "bussv": "business services",
    "hardw": "computers peripherals hardware",
    "softw": "software system application",
    "chips": "semiconductor",
    "labeq": "electronics instruments",
    "paper": "paper forest products",
    "boxes": "packaging container",
    "trans": "transportation logistics",
    "whlsl": "wholesale distributors",
    "rtail": "retail",
    "meals": "restaurant food service",
    "banks": "banks banking",
    "insur": "insurance",
    "rlest": "real estate",
    "fin": "financial services",
}


def norm(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def score(ff: str, dam: str) -> float:
    a = norm(ALIASES.get(norm(ff), ff))
    b = norm(dam)
    seq = SequenceMatcher(None, a, b).ratio()
    ta, tb = set(a.split()), set(b.split())
    jac = len(ta & tb) / max(1, len(ta | tb))
    return 0.65 * seq + 0.35 * jac


def main() -> None:
    ff = pd.read_csv(PROCESSED / "ff49_industry_year.csv", usecols=["year", "ff49_industry"]).drop_duplicates()
    dam = pd.read_csv(PROCESSED / "damodaran_industry_year.csv", usecols=["year", "damodaran_industry"]).drop_duplicates()
    rows = []
    for year, ff_y in ff.groupby("year"):
        dam_y = dam.loc[dam["year"].eq(year), "damodaran_industry"].tolist()
        if not dam_y:
            continue
        for ff_name in sorted(ff_y["ff49_industry"].unique()):
            ranked = sorted(((d, score(ff_name, d)) for d in dam_y), key=lambda x: x[1], reverse=True)[:5]
            for rank, (d, s) in enumerate(ranked, start=1):
                rows.append({
                    "year": year,
                    "ff49_industry": ff_name,
                    "damodaran_industry": d,
                    "candidate_rank": rank,
                    "lexical_score": round(s, 6),
                    "mapping_confidence": "UNVERIFIED",
                    "manual_review": True,
                    "approved": False,
                    "mapping_weight": "",
                    "notes": "Candidate only; validate economic/SIC correspondence before approval.",
                })
    out = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"Wrote {len(out):,} candidate mapping rows to {OUT}")


if __name__ == "__main__":
    main()
