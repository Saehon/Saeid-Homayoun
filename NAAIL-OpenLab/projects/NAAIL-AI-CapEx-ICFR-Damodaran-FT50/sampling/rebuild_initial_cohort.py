"""Rebuild frozen initial S&P500 screening sample (not historical SEC universe)."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/36472b57910842f4025e8ca8303b93a692d2bbae/data/constituents.csv"
BUILDERS = {"MSFT","GOOGL","AMZN","META","ORCL"}
SUPPLIERS = {"NVDA","AVGO","MU","VRT","ANET"}
KEYS = ["cik","ticker","aliases","company","sector","subindustry","analysis","role","priority","sec_10k_2019_2025_verified","ai_capex_verified","historical_listing_verified","source_snapshot"]
WORDS = ("semiconductor","technology hardware","electronic","electrical equipment","communications equipment","data processing","construction & engineering","industrial machinery")

def screen(rows):
    by = defaultdict(list)
    for row in rows:
        by[row["CIK"]].append(row)
    if len(rows)!=503 or len(by)!=500:
        raise ValueError("Frozen input changed")
    selected, excluded = [], []
    for cik, group in by.items():
        g=group[0]
        symbols=[v["Symbol"] for v in group]
        ticker = "GOOGL" if "GOOGL" in symbols else symbols[0]
        sector = g["GICS Sector"]; sub=g["GICS Sub-Industry"]
        status = "EXCLUDED_FINANCIAL" if sector=="Financials" else ("SEPARATE_INFRA_SPECIAL" if sector in ("Real Estate","Utilities") else "PRIMARY_OPERATING")
        role = "FINANCIAL_OUT_OF_SCOPE" if status=="EXCLUDED_FINANCIAL" else (
            "BUILDER_ANCHOR_CASE" if ticker in BUILDERS else
            "SUPPLIER_ANCHOR_CASE" if ticker in SUPPLIERS else
            "ENERGY_UTILITY_SCREENING" if sector=="Utilities" else
            "REAL_ESTATE_SCREENING" if sector=="Real Estate" else
            "INFRASTRUCTURE_SUPPLY_CANDIDATE_UNVERIFIED" if any(w in sub.lower() for w in WORDS) else
            "TECH_ADOPTION_CANDIDATE_UNVERIFIED" if sector in ("Information Technology","Communication Services") else
            "OTHER_NONFINANCIAL_UNVERIFIED"))
        priority = ("P0_10_FIRMS" if ticker in BUILDERS|SUPPLIERS else
                    "P1_SECTOR_SCREEN" if role in ("INFRASTRUCTURE_SUPPLY_CANDIDATE_UNVERIFIED","ENERGY_UTILITY_SCREENING","REAL_ESTATE_SCREENING") else "P2_GENERAL_SCREEN")
        d={"cik":str(cik).zfill(10),"ticker":ticker,"aliases":"|".join(v for v in symbols if v!=ticker),
           "company":g["Security"],"sector":sector,"subindustry":sub,"analysis":status,"role":role,"priority":priority,
           "sec_10k_2019_2025_verified":"NO","ai_capex_verified":"NO","historical_listing_verified":"NO","source_snapshot":"2026-10-09"}
        (excluded if status=="EXCLUDED_FINANCIAL" else selected).append(d)
    selected.sort(key=lambda x:x["ticker"]); excluded.sort(key=lambda x:x["ticker"])
    assert len(selected)==424 and len(excluded)==76
    assert len({x["cik"] for x in selected})==424
    assert sum(x["analysis"]=="SEPARATE_INFRA_SPECIAL" for x in selected)==61
    assert sum(x["priority"]=="P0_10_FIRMS" for x in selected)==10
    assert sum(x["priority"]=="P1_SECTOR_SCREEN" for x in selected)==126
    assert sum(x["priority"]=="P2_GENERAL_SCREEN" for x in selected)==288
    return selected,excluded

def main(directory):
    req=Request(URL,headers={"User-Agent":"NAAIL-OpenLab academic reproducibility"})
    with urlopen(req,timeout=30) as f: raw=f.read().decode("utf-8")
    groups=screen(list(csv.DictReader(raw.splitlines())))
    directory.mkdir(parents=True,exist_ok=True)
    for name,rows in zip(("INITIAL_424_NONFINANCIAL_FIRMS_2026-10-09.csv","EXCLUDED_76_FINANCIAL_FIRMS_2026-10-09.csv"),groups):
        with open(directory/name,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=KEYS); w.writeheader(); w.writerows(rows)
    print("Selected 424 unique nonfinancial CIK; excluded 76 financial CIK. Historical eligibility unverified.")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output-folder",type=Path,default=Path("."))
    main(ap.parse_args().output_folder)
