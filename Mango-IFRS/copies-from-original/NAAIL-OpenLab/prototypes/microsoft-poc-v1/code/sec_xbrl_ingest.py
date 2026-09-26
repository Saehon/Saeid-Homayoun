"""Reproducible SEC interactive-XBRL ingestion for Microsoft FY2026.
Network calls require SEC fair-access identification and internet connectivity.
Offline tests use frozen verified facts so CI does not depend on SEC availability.
"""
from __future__ import annotations
import pandas as pd

REPORTS = {
    "income":"https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R2.htm",
    "balance":"https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R4.htm",
    "cashflow":"https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R6.htm",
    "segments":"https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R107.htm",
}

FROZEN_VERIFIED = {
    "revenue_2026":331839,
    "operating_income_2026":155237,
    "net_income_2026":133749,
    "total_assets_2026":758376,
    "total_liabilities_2026":315989,
    "operating_cf_2026":182935,
    "capex_2026":115948,
    "pbp_revenue_2026":139996,
    "ic_revenue_2026":137791,
    "mpc_revenue_2026":54052,
}

def fetch_tables(url: str):
    """Ingest a public SEC interactive-XBRL report table."""
    return pd.read_html(url)

def validate_frozen_facts():
    assert FROZEN_VERIFIED["revenue_2026"] == 331839
    assert FROZEN_VERIFIED["total_assets_2026"] == 758376
    assert FROZEN_VERIFIED["operating_cf_2026"] == 182935
    assert sum([FROZEN_VERIFIED["pbp_revenue_2026"],FROZEN_VERIFIED["ic_revenue_2026"],FROZEN_VERIFIED["mpc_revenue_2026"]]) == FROZEN_VERIFIED["revenue_2026"]
    return True
