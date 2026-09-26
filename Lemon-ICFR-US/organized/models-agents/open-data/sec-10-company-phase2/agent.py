"""Free deterministic accounting agent for the Phase-2 SEC panel.

Examples:
    python agent.py profile MSFT
    python agent.py compare MSFT AAPL
    python agent.py quality
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "sec_10_company_panel.csv"

def load():
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    groups = defaultdict(list)
    for row in rows:
        groups[row["ticker"].upper()].append(row)
    for group in groups.values():
        group.sort(key=lambda r: r["fiscal_year_end"])
    return groups

def val(row, key):
    raw = row.get(key, "")
    return None if raw == "" else float(raw)

def profile(groups, ticker):
    ticker = ticker.upper()
    if ticker not in groups:
        raise SystemExit(f"Unknown ticker: {ticker}")
    group = groups[ticker]
    prev, latest = group[-2], group[-1]
    revenue = val(latest, "revenue_musd")
    previous_revenue = val(prev, "revenue_musd")
    net = val(latest, "net_income_musd")
    assets = val(latest, "assets_musd")
    growth = None if revenue is None or not previous_revenue else (revenue / previous_revenue - 1) * 100
    margin = None if revenue in (None, 0) or net is None else net / revenue * 100

    print(f"{latest['company']} ({ticker})")
    print(f"Latest fiscal year end: {latest['fiscal_year_end']}")
    print(f"Revenue (USDm): {latest['revenue_musd'] or 'N/A'}")
    print(f"Net income (USDm): {latest['net_income_musd'] or 'N/A'}")
    print(f"Assets (USDm): {latest['assets_musd'] or 'N/A'}")
    print("Revenue growth: " + ("N/A" if growth is None else f"{growth:.2f}%"))
    print("Net margin: " + ("N/A" if margin is None else f"{margin:.2f}%"))
    print(f"Data quality: {latest['quality_flags']}")
    print(f"Source: {latest['source_url']}")

def compare(groups, left, right):
    print("=== LEFT ===")
    profile(groups, left)
    print("\n=== RIGHT ===")
    profile(groups, right)

def quality(groups):
    for ticker in sorted(groups):
        latest = groups[ticker][-1]
        print(f"{ticker}: {latest['quality_flags']} ({latest['fiscal_year_end']})")

parser = argparse.ArgumentParser(description="Free deterministic SEC accounting agent")
sub = parser.add_subparsers(dest="command", required=True)

p = sub.add_parser("profile")
p.add_argument("ticker")

p = sub.add_parser("compare")
p.add_argument("left")
p.add_argument("right")

sub.add_parser("quality")

args = parser.parse_args()
groups = load()

if args.command == "profile":
    profile(groups, args.ticker)
elif args.command == "compare":
    compare(groups, args.left, args.right)
else:
    quality(groups)
