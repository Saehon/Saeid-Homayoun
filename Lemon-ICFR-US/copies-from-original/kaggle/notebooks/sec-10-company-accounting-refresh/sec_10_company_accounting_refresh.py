"""Kaggle execution layer for the SEC 10-company accounting refresh.

Kaggle provides the network execution surface. GitHub remains the canonical
source of truth after validation and commit-back.
"""

from __future__ import annotations

import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

OUT_DIR = Path("/kaggle/working")
OUT = OUT_DIR / "sec_10_company_panel.csv"
MANIFEST = OUT_DIR / "sec_refresh_manifest.json"

COMPANIES = [
    {"ticker":"MSFT","cik":"0000789019","name":"Microsoft Corporation","sector":"Technology"},
    {"ticker":"AAPL","cik":"0000320193","name":"Apple Inc.","sector":"Technology"},
    {"ticker":"GOOGL","cik":"0001652044","name":"Alphabet Inc.","sector":"Communication Services"},
    {"ticker":"AMZN","cik":"0001018724","name":"Amazon.com, Inc.","sector":"Consumer / Technology"},
    {"ticker":"NVDA","cik":"0001045810","name":"NVIDIA Corporation","sector":"Technology"},
    {"ticker":"META","cik":"0001326801","name":"Meta Platforms, Inc.","sector":"Communication Services"},
    {"ticker":"JPM","cik":"0000019617","name":"JPMorgan Chase & Co.","sector":"Financials"},
    {"ticker":"WMT","cik":"0000104169","name":"Walmart Inc.","sector":"Consumer Staples"},
    {"ticker":"XOM","cik":"0000034088","name":"Exxon Mobil Corporation","sector":"Energy"},
    {"ticker":"TSLA","cik":"0001318605","name":"Tesla, Inc.","sector":"Automotive / Energy"},
]

CONCEPTS = {
    "revenue_musd": {
        "kind": "duration",
        "candidates": [
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "Revenues",
            "SalesRevenueNet",
            "SalesRevenueGoodsNet",
        ],
    },
    "gross_profit_musd": {"kind": "duration", "candidates": ["GrossProfit"]},
    "operating_income_musd": {"kind": "duration", "candidates": ["OperatingIncomeLoss"]},
    "net_income_musd": {"kind": "duration", "candidates": ["NetIncomeLoss", "ProfitLoss"]},
    "assets_musd": {"kind": "instant", "candidates": ["Assets"]},
    "liabilities_musd": {"kind": "instant", "candidates": ["Liabilities"]},
    "equity_musd": {
        "kind": "instant",
        "candidates": [
            "StockholdersEquity",
            "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
        ],
    },
}

HEADERS = {
    "User-Agent": "Saeid-Homayoun-Open-Accounting-Research saehon@users.noreply.github.com",
    "From": "saehon@users.noreply.github.com",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
}

session = requests.Session()
session.headers.update(HEADERS)


def fetch_json(url: str) -> dict:
    last = None
    for attempt in range(5):
        response = session.get(url, timeout=60)
        last = response
        if response.ok:
            return response.json()
        if response.status_code not in (403, 429, 500, 502, 503, 504):
            response.raise_for_status()
        time.sleep(2 ** attempt)
    raise RuntimeError(f"SEC request failed: {last.status_code} {url}")


def annual_duration(item: dict) -> bool:
    if item.get("form") != "10-K" or item.get("fp") != "FY":
        return False
    start, end = item.get("start"), item.get("end")
    if not start or not end:
        return False
    try:
        days = (datetime.fromisoformat(end) - datetime.fromisoformat(start)).days
    except ValueError:
        return False
    return 300 <= days <= 430


def units(facts: dict, concept: str) -> list[dict]:
    return list((((facts.get(concept) or {}).get("units") or {}).get("USD") or []))


def latest_for_end(items: list[dict], end: str, duration: bool) -> dict | None:
    keep = []
    for item in items:
        if item.get("end") != end or item.get("form") != "10-K":
            continue
        if duration and not annual_duration(item):
            continue
        keep.append(item)
    if not keep:
        return None
    return max(keep, key=lambda x: (x.get("filed") or "", x.get("accn") or ""))


def pick(facts: dict, spec: dict, end: str):
    for concept in spec["candidates"]:
        item = latest_for_end(units(facts, concept), end, spec["kind"] == "duration")
        if item is not None:
            return concept, item
    return None, None


def discover_ends(facts: dict) -> list[str]:
    concepts = [
        "NetIncomeLoss",
        "ProfitLoss",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "OperatingIncomeLoss",
    ]
    ends = set()
    for concept in concepts:
        for item in units(facts, concept):
            if annual_duration(item) and item.get("end"):
                ends.add(item["end"])
        if len(ends) >= 3:
            break
    if len(ends) < 3:
        raise RuntimeError("Fewer than three annual 10-K periods found")
    return sorted(ends)[-3:]


def musd(item):
    if not item or item.get("val") is None:
        return ""
    return str(round(float(item["val"]) / 1_000_000))


rows = []
manifest_companies = []

for idx, company in enumerate(COMPANIES, 1):
    cik = company["cik"].zfill(10)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    print(f"[{idx}/10] {company['ticker']} {url}", flush=True)
    payload = fetch_json(url)
    facts = ((payload.get("facts") or {}).get("us-gaap") or {})
    ends = discover_ends(facts)
    cm = {
        "ticker": company["ticker"],
        "cik": cik,
        "entity_name_sec": payload.get("entityName"),
        "source_url": url,
        "periods": {},
    }

    for end in ends:
        row = {
            "company": payload.get("entityName") or company["name"],
            "ticker": company["ticker"],
            "cik": cik,
            "sector": company["sector"],
            "fiscal_year_end": end,
            "fiscal_year_end_year": end[:4],
        }
        pm = {}
        reference = None
        missing = []
        for column, spec in CONCEPTS.items():
            concept, item = pick(facts, spec, end)
            row[column] = musd(item)
            pm[column] = {
                "concept": concept,
                "accn": item.get("accn") if item else None,
                "filed": item.get("filed") if item else None,
                "start": item.get("start") if item else None,
                "end": item.get("end") if item else end,
            }
            if reference is None and item and column in ("net_income_musd", "revenue_musd"):
                reference = item
            if item is None:
                missing.append(column)
        row["accession"] = (reference or {}).get("accn", "")
        row["filed"] = (reference or {}).get("filed", "")
        row["source_url"] = url
        row["quality_flags"] = "OK" if not missing else "MISSING:" + "|".join(missing)
        rows.append(row)
        cm["periods"][end] = pm

    manifest_companies.append(cm)
    time.sleep(0.35)

rows.sort(key=lambda r: (r["ticker"], r["fiscal_year_end"]))
fields = [
    "company","ticker","cik","sector","fiscal_year_end","fiscal_year_end_year",
    "revenue_musd","gross_profit_musd","operating_income_musd","net_income_musd",
    "assets_musd","liabilities_musd","equity_musd","accession","filed",
    "source_url","quality_flags",
]
with OUT.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
manifest = {
    "version": "2.0.0",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "execution_layer": "Kaggle",
    "source": "SEC EDGAR CompanyFacts API",
    "company_count": len(COMPANIES),
    "row_count": len(rows),
    "data_sha256": digest,
    "companies": manifest_companies,
}
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(f"PASS: wrote {OUT} with {len(rows)} rows")
print(f"PASS: wrote {MANIFEST}")
print(f"SHA256: {digest}")
