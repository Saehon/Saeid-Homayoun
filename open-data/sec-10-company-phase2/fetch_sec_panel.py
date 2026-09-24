"""Phase 2: build a 10-company annual accounting panel from SEC CompanyFacts.

No API key is required. The script identifies itself, limits request frequency,
selects annual 10-K facts, normalizes values to USD millions, and writes a
machine-readable provenance manifest.

Environment:
    SEC_USER_AGENT="Research Project contact@example.com" python fetch_sec_panel.py
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
REGISTRY = BASE / "companies.json"
OUT = BASE / "sec_10_company_panel.csv"
MANIFEST = BASE / "sec_refresh_manifest.json"

DEFAULT_USER_AGENT = (
    "Saeid-Homayoun-Open-Accounting-Research "
    "saehon@users.noreply.github.com"
)
USER_AGENT = os.environ.get("SEC_USER_AGENT", DEFAULT_USER_AGENT).strip()

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
    "gross_profit_musd": {
        "kind": "duration",
        "candidates": ["GrossProfit"],
    },
    "operating_income_musd": {
        "kind": "duration",
        "candidates": ["OperatingIncomeLoss"],
    },
    "net_income_musd": {
        "kind": "duration",
        "candidates": [
            "NetIncomeLoss",
            "ProfitLoss",
        ],
    },
    "assets_musd": {
        "kind": "instant",
        "candidates": ["Assets"],
    },
    "liabilities_musd": {
        "kind": "instant",
        "candidates": ["Liabilities"],
    },
    "equity_musd": {
        "kind": "instant",
        "candidates": [
            "StockholdersEquity",
            "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
        ],
    },
}


def request_json(url: str, attempts: int = 4) -> dict:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Host": "data.sec.gov",
    }
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt == attempts:
                raise
            time.sleep(2 ** (attempt - 1))
    raise RuntimeError("unreachable")


def usd_items(facts: dict, concept: str) -> list[dict]:
    obj = facts.get(concept) or {}
    return list((obj.get("units") or {}).get("USD") or [])


def annual_duration(item: dict) -> bool:
    if item.get("form") != "10-K" or item.get("fp") != "FY":
        return False
    start, end = item.get("start"), item.get("end")
    if not start or not end:
        return False
    try:
        days = (
            datetime.fromisoformat(end) - datetime.fromisoformat(start)
        ).days
    except ValueError:
        return False
    return 300 <= days <= 430


def latest_for_end(items: list[dict], end: str, *, duration: bool) -> dict | None:
    selected = []
    for item in items:
        if item.get("end") != end or item.get("form") != "10-K":
            continue
        if duration and not annual_duration(item):
            continue
        selected.append(item)
    if not selected:
        return None
    return max(
        selected,
        key=lambda x: (
            x.get("filed") or "",
            x.get("accn") or "",
        ),
    )


def select_metric(facts: dict, spec: dict, end: str) -> tuple[str | None, dict | None]:
    for concept in spec["candidates"]:
        item = latest_for_end(
            usd_items(facts, concept),
            end,
            duration=(spec["kind"] == "duration"),
        )
        if item is not None:
            return concept, item
    return None, None


def discover_annual_ends(facts: dict) -> list[str]:
    preferred = [
        "NetIncomeLoss",
        "ProfitLoss",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "OperatingIncomeLoss",
    ]
    ends: set[str] = set()
    for concept in preferred:
        for item in usd_items(facts, concept):
            if annual_duration(item) and item.get("end"):
                ends.add(item["end"])
        if len(ends) >= 3:
            break
    if len(ends) < 3:
        raise ValueError("Fewer than three annual 10-K periods were found.")
    return sorted(ends)[-3:]


def to_musd(item: dict | None) -> str:
    if not item:
        return ""
    value = item.get("val")
    if value is None:
        return ""
    return str(round(float(value) / 1_000_000))


registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
rows: list[dict] = []
manifest_companies: list[dict] = []

for position, company in enumerate(registry["companies"]):
    ticker = company["ticker"]
    cik = company["cik"].zfill(10)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    payload = request_json(url)
    facts = (payload.get("facts") or {}).get("us-gaap") or {}
    ends = discover_annual_ends(facts)

    company_manifest = {
        "ticker": ticker,
        "cik": cik,
        "entity_name_sec": payload.get("entityName"),
        "source_url": url,
        "periods": {},
    }

    for end in ends:
        row = {
            "company": payload.get("entityName") or company["name"],
            "ticker": ticker,
            "cik": cik,
            "sector": company["sector"],
            "fiscal_year_end": end,
            "fiscal_year_end_year": end[:4],
        }
        period_manifest = {}
        reference_item = None
        missing = []

        for column, spec in CONCEPTS.items():
            concept, item = select_metric(facts, spec, end)
            row[column] = to_musd(item)
            period_manifest[column] = {
                "concept": concept,
                "accn": item.get("accn") if item else None,
                "filed": item.get("filed") if item else None,
                "start": item.get("start") if item else None,
                "end": item.get("end") if item else end,
            }
            if item and reference_item is None and column in ("net_income_musd", "revenue_musd"):
                reference_item = item
            if item is None:
                missing.append(column)

        row["accession"] = (reference_item or {}).get("accn", "")
        row["filed"] = (reference_item or {}).get("filed", "")
        row["source_url"] = url
        row["quality_flags"] = "OK" if not missing else "MISSING:" + "|".join(missing)
        rows.append(row)
        company_manifest["periods"][end] = period_manifest

    manifest_companies.append(company_manifest)
    if position < len(registry["companies"]) - 1:
        time.sleep(0.30)

fieldnames = [
    "company",
    "ticker",
    "cik",
    "sector",
    "fiscal_year_end",
    "fiscal_year_end_year",
    "revenue_musd",
    "gross_profit_musd",
    "operating_income_musd",
    "net_income_musd",
    "assets_musd",
    "liabilities_musd",
    "equity_musd",
    "accession",
    "filed",
    "source_url",
    "quality_flags",
]

rows.sort(key=lambda r: (r["ticker"], r["fiscal_year_end"]))
with OUT.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
manifest = {
    "version": "2.0.0",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "source": "SEC EDGAR CompanyFacts API",
    "registry_source": registry.get("source"),
    "company_count": len(registry["companies"]),
    "row_count": len(rows),
    "request_interval_seconds": 0.30,
    "data_sha256": digest,
    "companies": manifest_companies,
}
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(f"Wrote {OUT} with {len(rows)} rows.")
print(f"Wrote {MANIFEST}.")
print(f"SHA256: {digest}")
