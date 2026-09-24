"""Phase 1 Microsoft accounting demo.

Reads the latest three Microsoft fiscal years in the canonical CSV and prints
simple growth and profitability measures. Values are USD millions.
"""

import csv
from pathlib import Path

DATA = Path(__file__).parent / "microsoft_financials.csv"

with DATA.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    for key in ("revenue_musd", "gross_profit_musd", "operating_income_musd", "net_income_musd"):
        row[key] = float(row[key])

print("Microsoft Phase-1 accounting demo")
print("-" * 38)

previous = None
for row in rows:
    year = row["fiscal_year"]
    revenue = row["revenue_musd"]
    gross_margin = 100 * row["gross_profit_musd"] / revenue
    operating_margin = 100 * row["operating_income_musd"] / revenue
    net_margin = 100 * row["net_income_musd"] / revenue
    growth = "n/a" if previous is None else f"{100 * (revenue / previous['revenue_musd'] - 1):.2f}%"
    print(
        f"{year}: revenue=${revenue/1000:.3f}bn | "
        f"revenue growth={growth} | "
        f"gross margin={gross_margin:.2f}% | "
        f"operating margin={operating_margin:.2f}% | "
        f"net margin={net_margin:.2f}%"
    )
    previous = row
