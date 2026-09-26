"""Free deterministic Phase-3 research agent.

Examples:
  python research_agent.py profile MSFT
  python research_agent.py cam TSLA
  python research_agent.py icfr AAPL
  python research_agent.py sources META
"""

import argparse
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
PHASE2 = BASE.parent / "sec-10-company-phase2"

def load(path):
    with path.open(newline="", encoding="utf-8") as f:
        return {r["ticker"]: r for r in csv.DictReader(f)}

cam = load(BASE / "cam_latest.csv")
icfr = load(BASE / "icfr_latest.csv")
gov = load(BASE / "governance_source_registry.csv")
esg = load(BASE / "esg_source_registry.csv")
financials = load(PHASE2 / "phase2_summary.csv")

parser = argparse.ArgumentParser(description="Deterministic 10-company research agent")
sub = parser.add_subparsers(dest="cmd", required=True)
for cmd in ("profile","cam","icfr","sources"):
    p = sub.add_parser(cmd)
    p.add_argument("ticker")
args = parser.parse_args()
ticker = args.ticker.upper()
if ticker not in cam:
    raise SystemExit(f"Unknown ticker: {ticker}")

if args.cmd == "profile":
    f = financials[ticker]
    print(f"{f['company']} ({ticker})")
    print("--- Financial layer ---")
    print(f"Latest fiscal year end: {f['latest_fiscal_year_end']}")
    print(f"Revenue (USDm): {f['revenue_musd']}")
    print(f"Net income (USDm): {f['net_income_musd']}")
    print(f"Revenue growth: {f['revenue_growth_pct']}%")
    print(f"Net margin: {f['net_margin_pct']}%")

if args.cmd in ("profile","cam"):
    r = cam[ticker]
    print("--- CAM layer ---")
    print(f"Latest CAM count: {r['cam_count']}")
    print(f"CAM topics: {r['cam_topics']}")
    print(f"Auditor: {r['auditor']}")
    print(f"10-K source: {r['source_url']}")

if args.cmd in ("profile","icfr"):
    r = icfr[ticker]
    print("--- ICFR layer ---")
    print(f"Management assessment: {r['management_assessment']}")
    print(f"Auditor ICFR opinion: {r['auditor_icfr_opinion']}")
    print(f"Material weakness flag: {r['material_weakness_flag']}")
    print(f"Framework: {r['framework']}")

if args.cmd in ("profile","sources"):
    print("--- Governance / ESG source layer ---")
    print(f"Governance source: {gov[ticker]['governance_source_locator']}")
    print(f"Governance targets: {gov[ticker]['target_variables']}")
    print(f"ESG source: {esg[ticker]['source_locator']}")
    print(f"ESG targets: {esg[ticker]['target_dimensions']}")
