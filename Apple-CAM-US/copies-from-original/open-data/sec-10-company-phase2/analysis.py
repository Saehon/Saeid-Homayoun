"""Create a compact latest-period accounting summary from the Phase-2 panel."""

import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "sec_10_company_panel.csv"
OUT = BASE / "phase2_summary.csv"

def number(value):
    return None if value in ("", None) else float(value)

with DATA.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

groups = defaultdict(list)
for row in rows:
    groups[row["ticker"]].append(row)

output = []
for ticker, group in sorted(groups.items()):
    group.sort(key=lambda r: r["fiscal_year_end"])
    previous, latest = group[-2], group[-1]
    rev_now = number(latest["revenue_musd"])
    rev_prev = number(previous["revenue_musd"])
    net = number(latest["net_income_musd"])
    assets = number(latest["assets_musd"])

    revenue_growth = (
        (rev_now / rev_prev - 1) * 100
        if rev_now is not None and rev_prev not in (None, 0)
        else None
    )
    net_margin = (
        net / rev_now * 100
        if net is not None and rev_now not in (None, 0)
        else None
    )

    output.append({
        "ticker": ticker,
        "company": latest["company"],
        "latest_fiscal_year_end": latest["fiscal_year_end"],
        "revenue_musd": latest["revenue_musd"],
        "net_income_musd": latest["net_income_musd"],
        "assets_musd": latest["assets_musd"],
        "revenue_growth_pct": "" if revenue_growth is None else f"{revenue_growth:.2f}",
        "net_margin_pct": "" if net_margin is None else f"{net_margin:.2f}",
        "quality_flags": latest["quality_flags"],
    })

fields = [
    "ticker", "company", "latest_fiscal_year_end", "revenue_musd",
    "net_income_musd", "assets_musd", "revenue_growth_pct",
    "net_margin_pct", "quality_flags",
]
with OUT.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(output)

print(f"Wrote {OUT} with {len(output)} company summaries.")
