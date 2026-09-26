"""Refresh the Microsoft accounting demo from SEC CompanyFacts.

Set SEC_USER_AGENT before running, for example:
    SEC_USER_AGENT="Researcher Name researcher@example.edu" python fetch_sec.py
"""

import csv
import json
import os
import urllib.request
from pathlib import Path

CIK = "0000789019"
YEARS = (2024, 2025, 2026)
END_DATES = {year: f"{year}-06-30" for year in YEARS}
BASE = Path(__file__).parent
OUT = BASE / "microsoft_financials.csv"

CONCEPTS = {
    "revenue_musd": [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "SalesRevenueNet",
    ],
    "gross_profit_musd": ["GrossProfit"],
    "operating_income_musd": ["OperatingIncomeLoss"],
    "net_income_musd": ["NetIncomeLoss"],
}

user_agent = os.environ.get("SEC_USER_AGENT", "").strip()
if not user_agent or "@" not in user_agent:
    raise SystemExit("Set SEC_USER_AGENT to an identifying name and contact email.")

url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"
request = urllib.request.Request(
    url,
    headers={"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate", "Host": "data.sec.gov"},
)

with urllib.request.urlopen(request, timeout=60) as response:
    payload = json.load(response)

facts = payload["facts"]["us-gaap"]

def annual_fact(concept_candidates, end_date):
    candidates = []
    for concept in concept_candidates:
        concept_obj = facts.get(concept)
        if not concept_obj:
            continue
        for item in concept_obj.get("units", {}).get("USD", []):
            if item.get("end") == end_date and item.get("form") == "10-K" and item.get("fp") == "FY":
                candidates.append((item.get("filed", ""), concept, item))
    if not candidates:
        raise KeyError(f"No annual 10-K fact found for {concept_candidates} at {end_date}")
    _, concept, item = max(candidates, key=lambda x: x[0])
    return concept, item

rows = []
selected = {}
for year in YEARS:
    row = {"fiscal_year": year}
    selected[str(year)] = {}
    for column, concepts in CONCEPTS.items():
        concept, item = annual_fact(concepts, END_DATES[year])
        row[column] = round(item["val"] / 1_000_000)
        selected[str(year)][column] = {
            "concept": concept,
            "end": item["end"],
            "filed": item.get("filed"),
            "accn": item.get("accn"),
            "form": item.get("form"),
        }
    rows.append(row)

with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "fiscal_year", "revenue_musd", "gross_profit_musd",
        "operating_income_musd", "net_income_musd"
    ])
    writer.writeheader()
    writer.writerows(rows)

manifest = {"company": payload.get("entityName"), "cik": CIK, "source": url, "selection": selected}
(BASE / "sec_refresh_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {OUT}")
print("Wrote sec_refresh_manifest.json")
