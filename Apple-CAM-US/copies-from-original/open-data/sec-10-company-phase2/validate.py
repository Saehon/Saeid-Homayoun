"""Deterministic validation for the Phase-2 SEC 10-company accounting panel."""

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "sec_10_company_panel.csv"
REGISTRY = BASE / "companies.json"
MANIFEST = BASE / "sec_refresh_manifest.json"

registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

with DATA.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

expected = {c["ticker"] for c in registry["companies"]}
actual = {row["ticker"] for row in rows}
assert actual == expected, (expected - actual, actual - expected)
assert len(rows) == 30, f"Expected 30 rows, found {len(rows)}"

counts = Counter(row["ticker"] for row in rows)
assert all(counts[t] == 3 for t in expected), counts

keys = [(row["ticker"], row["fiscal_year_end"]) for row in rows]
assert len(keys) == len(set(keys)), "Duplicate ticker/period rows found."

by_ticker = defaultdict(list)
for row in rows:
    by_ticker[row["ticker"]].append(row)
    assert row["source_url"].startswith("https://www.sec.gov/Archives/edgar/data/")
    assert row["revenue_musd"] != "", f"Missing revenue: {row['ticker']} {row['fiscal_year_end']}"
    assert row["net_income_musd"] != "", f"Missing net income: {row['ticker']} {row['fiscal_year_end']}"

for ticker, group in by_ticker.items():
    ends = [r["fiscal_year_end"] for r in group]
    assert ends == sorted(ends), f"Periods are not ascending for {ticker}: {ends}"

# Frozen Microsoft controls inherited from Phase 1.
msft_expected = {
    "2024-06-30": ("245122", "171008", "109433", "88136"),
    "2025-06-30": ("281724", "193893", "128528", "101832"),
    "2026-06-30": ("331839", "225465", "155237", "133749"),
}
msft_rows = {r["fiscal_year_end"]: r for r in rows if r["ticker"] == "MSFT"}
for end, expected_values in msft_expected.items():
    row = msft_rows[end]
    actual_values = (
        row["revenue_musd"],
        row["gross_profit_musd"],
        row["operating_income_musd"],
        row["net_income_musd"],
    )
    assert actual_values == expected_values, (end, actual_values, expected_values)

digest = hashlib.sha256(DATA.read_bytes()).hexdigest()
assert digest == manifest["data_sha256"], (digest, manifest["data_sha256"])
assert manifest["company_count"] == 10
assert manifest["row_count"] == 30

optional_gross = sum(1 for r in rows if r["gross_profit_musd"])
optional_operating = sum(1 for r in rows if r["operating_income_musd"])

print("PASS: 10 companies × 3 annual periods validated.")
print("Required coverage: revenue 30/30; net income 30/30.")
print(f"Optional coverage: gross profit {optional_gross}/30; operating income {optional_operating}/30.")
print(f"SHA256: {digest}")
