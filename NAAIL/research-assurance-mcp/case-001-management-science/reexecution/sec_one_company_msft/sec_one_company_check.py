"""One-company SEC proof for NAAIL Case 001.

Requires:
    pip install edgartools
    export EDGAR_IDENTITY="Your Name your.email@example.com"

No personal identity is hard-coded. SEC filing metadata are the source of truth.
"""
import os
from datetime import date
from edgar import Company, set_identity

identity=os.getenv("EDGAR_IDENTITY")
if not identity:
    raise RuntimeError("Set EDGAR_IDENTITY before accessing SEC EDGAR.")

set_identity(identity)
company=Company("MSFT")

targets={
    ("10-Q","2019-03-31"),
    ("10-Q","2020-03-31"),
    ("10-K","2019-06-30"),
    ("10-K","2020-06-30"),
}

rows=[]
for form in ("10-Q","10-K"):
    filings=company.get_filings(form=form)
    for filing in filings:
        period=str(filing.period_of_report)
        key=(form,period)
        if key not in targets:
            continue
        filed=str(filing.filing_date)
        lag=(date.fromisoformat(filed)-date.fromisoformat(period)).days
        rows.append({
            "form":form,
            "period_end":period,
            "filing_date":filed,
            "filing_lag_days":lag,
            "accession":filing.accession_no,
        })

for row in sorted(rows,key=lambda x:x["period_end"]):
    print(row)
