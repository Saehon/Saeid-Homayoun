#!/usr/bin/env python3
"""Validate MSFT FY2023-25 cash-flow rows against original SEC 10-K data.
Run: python validate_msft_sec.py /path/to/authorized_original.csv
Source: SEC CIK 0000789019; USD millions. No AI-specific CapEx claim.
"""
import csv, sys, json
from pathlib import Path
SEC = {
  2023: (87582,28107,72361,"2023-07-27","0000950170-23-035122"),
  2024: (118548,44477,88136,"2024-07-30","0000950170-24-087843"),
  2025: (136162,64551,101832,"2025-07-30","0000950170-25-100235"),
}
COLS=("operating_cash_flow_usd_m","gross_cash_capex_usd_m","net_income_usd_m")
def validate(path):
    with Path(path).open(newline="",encoding="utf-8-sig") as f:
        rows=[r for r in csv.DictReader(f) if r.get("ticker")=="MSFT"]
    assert len(rows)==3 and {int(r["fiscal_year"]) for r in rows}==set(SEC)
    result=[]
    for r in sorted(rows,key=lambda x:int(x["fiscal_year"])):
        fy=int(r["fiscal_year"]); cfo,capex,ni,filed,accession=SEC[fy]
        diffs=[float(r[k])-v for k,v in zip(COLS,(cfo,capex,ni))]
        fcf=float(r[COLS[0]])-float(r[COLS[1]])
        assert diffs==[0,0,0] and fcf==float(r["fcf_gross_proxy_usd_m"])
        result.append(dict(fy=fy,accession=accession,filed=filed,financial_differences=diffs,fcf_proxy=fcf))
    return dict(n_company_years=3,sec_financial_matches=9,fcf_arithmetic_matches=3,rows=result,
                caveat="FCF is CFO minus cash PP&E only; not FCFF or AI-specific CapEx")
if __name__=="__main__":
    print(json.dumps(validate(sys.argv[1]),indent=2))
