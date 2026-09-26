"""Deterministic validation for the Microsoft Phase-1 accounting dataset."""

import csv
import hashlib
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "microsoft_financials.csv"

EXPECTED = {
    "2024": (245122, 171008, 109433, 88136),
    "2025": (281724, 193893, 128528, 101832),
    "2026": (331839, 225465, 155237, 133749),
}

with DATA.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

assert [row["fiscal_year"] for row in rows] == ["2024", "2025", "2026"]
assert len(rows) == 3

for row in rows:
    actual = tuple(int(row[k]) for k in (
        "revenue_musd", "gross_profit_musd", "operating_income_musd", "net_income_musd"
    ))
    assert actual == EXPECTED[row["fiscal_year"]], (row["fiscal_year"], actual)

digest = hashlib.sha256(DATA.read_bytes()).hexdigest()
assert digest == "b0fc573642135624b8f87fc4fb25cea6ce6992d617f0d36301ec2b51f7c20631"

print("PASS: Microsoft FY2024-FY2026 dataset matches the frozen FY2026 10-K control totals.")
print(f"SHA256: {digest}")
