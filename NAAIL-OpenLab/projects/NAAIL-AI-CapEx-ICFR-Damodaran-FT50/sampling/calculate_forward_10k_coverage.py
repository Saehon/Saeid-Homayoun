"""Compute 10-K longitudinal follow-up coverage for a downloaded NAAIL GitHub Actions artifact.

Run: python calculate_forward_10k_coverage.py path/to/NAAIL_REAL_SEC_HISTORICAL_10K_FY2021_2024_20260930.zip
"""
import json,zipfile,sys
import pandas as pd
path=sys.argv[1]
with zipfile.ZipFile(path) as z:
    def read(name):return pd.read_csv(z.open(name),dtype={"cik":str},low_memory=False)
    all_obs=read("SEC_10K_FY2017_2025_UNIVERSE.csv")
    exposure=read("SEC_10K_FY2021_2024_PROVISIONAL_NONFINANCIAL.csv")
idx=set(zip(all_obs.cik,all_obs.fiscal_year))
assert len(exposure)==18336
def horizon(years):
    subset=exposure[exposure.fiscal_year<=2025-years]
    selected=subset[[ (c,int(y)+years) in idx for c,y in zip(subset.cik,subset.fiscal_year)]]
    return dict(eligible_exposure_company_years=len(subset),followup_10K_company_years=len(selected),
                unique_issuer_CIK=selected.cik.nunique(),coverage=len(selected)/len(subset))
print(json.dumps({"tplus1":horizon(1),"tplus2":horizon(2),
    "note":"Follow-up 10-K presence only; not verified AI CapEx, CFO, CAM, ICFR, PCAOB, or final analytic panel."},indent=2))
