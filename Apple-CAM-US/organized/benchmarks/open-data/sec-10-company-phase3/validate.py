"""Deterministic validation for Phase 3 research modules."""

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
FILES = {
    "cam": BASE / "cam_latest.csv",
    "icfr": BASE / "icfr_latest.csv",
    "governance": BASE / "governance_source_registry.csv",
    "esg": BASE / "esg_source_registry.csv",
}
EXPECTED = {"MSFT","AAPL","GOOGL","AMZN","NVDA","META","JPM","WMT","XOM","TSLA"}

tables = {}
for name, path in FILES.items():
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    tickers = {r["ticker"] for r in rows}
    assert tickers == EXPECTED, (name, EXPECTED - tickers, tickers - EXPECTED)
    assert len(rows) == 10, (name, len(rows))
    tables[name] = rows

cam_total = sum(int(r["cam_count"]) for r in tables["cam"])
assert cam_total == 14, cam_total
assert all(int(r["cam_count"]) >= 1 for r in tables["cam"])
assert all(r["source_url"].startswith("https://www.sec.gov/Archives/edgar/data/") for r in tables["cam"])

assert all(r["management_assessment"] == "Effective" for r in tables["icfr"])
assert all(r["material_weakness_flag"] == "0" for r in tables["icfr"])
assert all(r["framework"] == "COSO 2013" for r in tables["icfr"])

assert all(r["coding_status"] == "SOURCE_REGISTERED" for r in tables["governance"])
assert all(r["coding_status"] == "SOURCE_REGISTERED" for r in tables["esg"])

print("PASS: Phase 3 modules contain the same 10-company universe.")
print(f"CAM observations: 10 companies; total latest-year CAMs: {cam_total}.")
print("ICFR: 10/10 effective in the curated latest 10-K snapshot; 0 coded material weaknesses.")
print("Governance and ESG: 10/10 source registries ready for metric extraction.")
