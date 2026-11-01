"""Construct source-validated SEC GAAP fiscal-year panel + PCAOB Form AP legal auditor registry.

This is a FINANCIAL DATA AND AUDITOR-ID MATCH, not an AI investment or PCAOB
inspection treatment panel. A Form AP filing may occur AFTER the SEC 10-K
publication; do not infer its public information was known on the 10-K date.
"""
import argparse,json
from pathlib import Path
from datetime import datetime,timezone
import pandas as pd
import numpy as np

TYPE="Issuer, other than Employee Benefit Plan or Investment Company"
def main(gaap_path,formap_path,out):
    out.mkdir(parents=True,exist_ok=True)
    g=pd.read_csv(gaap_path,dtype={"original_cik":str,"sec_cik":str,
        "source_report_end":str,"period_end":str},low_memory=False)
    assert len(g)==29550 and not g.accession.duplicated().any()
    g["sec_cik_equals_mirror_CIK"]=g.sec_cik.str.lstrip("0")==g.original_cik.str.lstrip("0")
    gd=pd.to_datetime(g.source_report_end,format="%Y%m%d",errors="coerce")
    hd=pd.to_datetime(g.period_end,errors="coerce")
    g["source_fye_difference_days"]=(gd-hd).dt.days.abs()
    g["issuer_CIK_FYE_source_match"]=g.sec_cik_equals_mirror_CIK & g.source_fye_difference_days.le(7)
    g=g[g.issuer_CIK_FYE_source_match].copy()
    assert len(g)==29313
    work=g[g.fiscal_year.between(2021,2024)&g.sic_as_filed_screen.eq("NONFINANCIAL")].copy()
    assert len(work)==17492
    assert not work[["original_cik","fiscal_year"]].duplicated().any()
    future=g.set_index(["original_cik","fiscal_year"])
    assert not future.index.duplicated().any()
    for step in [1,2]:
        pair=[(c,int(y)+step) for c,y in zip(work.original_cik,work.fiscal_year)]
        work[f"tplus{step}_CFO_usd"]=[
            future.at[k,"operating_cash_flow_usd"] if k in future.index else float("nan")
            for k in pair]
        work[f"tplus{step}_source_10k"]=[
            future.at[k,"accession"] if k in future.index else ""
            for k in pair]
    work["has_CFO_and_cashPPE"]=work.operating_cash_flow_usd.notna() & work.gross_cash_ppe_capex_usd.notna()
    work["has_CFO_and_cashPPE_and_tplus1_CFO"]=work.has_CFO_and_cashPPE & work.tplus1_CFO_usd.notna()
    work["has_CFO_and_cashPPE_and_tplus2_CFO"]=work.has_CFO_and_cashPPE & work.tplus2_CFO_usd.notna() & work.fiscal_year.le(2023)
    assert int(work.has_CFO_and_cashPPE_and_tplus1_CFO.sum())==9602

    form=pd.read_csv(formap_path,dtype={"cik":str,"pcaob_registered_firm_id":str},low_memory=False)
    form=form[form.fiscal_year.between(2021,2024)
        &form.audit_report_type.eq(TYPE)
        &form.form_ap_latest_form_flag.astype(str).eq("1")].copy()
    form["audit_report_dt"]=pd.to_datetime(form.audit_report_date,errors="coerce")
    form["filing_sec_dt"]=pd.to_datetime(form.sec_10k_filing_date,errors="coerce")
    invalid_audit_date=int((form.audit_report_dt>form.filing_sec_dt).sum())
    form=form[form.audit_report_dt.le(form.filing_sec_dt)].copy()
    firm_ct=form.groupby(["cik","fiscal_year"]).pcaob_registered_firm_id.nunique()
    only_one=firm_ct[firm_ct.eq(1)].index
    multi_firm_count=int(firm_ct.gt(1).sum())
    valid=set(only_one)
    form=form[[tuple(x) in valid for x in zip(form.cik,form.fiscal_year)]]
    form=form.sort_values(["cik","fiscal_year","audit_report_dt"]).drop_duplicates(["cik","fiscal_year"],keep="last")
    assert not form[["cik","fiscal_year"]].duplicated().any()
    cols=["cik","fiscal_year","pcaob_registered_firm_id","pcaob_firm_legal_name",
          "audit_report_date","form_ap_first_filed_or_amended_date",
          "FORMAP_FILED_AFTER_SEC_10K"]
    merged=work.merge(form[cols],how="left",left_on=["original_cik","fiscal_year"],
        right_on=["cik","fiscal_year"],validate="1:1",indicator=True)
    merged["auditor_registered_FirmID_verified"]=merged._merge.eq("both")
    merged["FORMAP_FIRM_ID_PUBLIC_AT_SEC_10K_DATE"]=np.where(
        merged.auditor_registered_FirmID_verified,~merged.FORMAP_FILED_AFTER_SEC_10K.fillna(True).astype(bool),False)
    merged["issuer_owned_AI_only_capex"]="UNVERIFIED"
    merged["SOX_ICFR_302_404_weakness"]="UNVERIFIED"
    merged["CAM_account_specific_risk_alignment"]="UNVERIFIED"
    merged["public_PCAOB_inspection_asof"]="UNVERIFIED_FIRST_PUBLIC_RELEASE"
    all_linked=merged[merged.auditor_registered_FirmID_verified].copy()
    outcomes=all_linked[all_linked.has_CFO_and_cashPPE_and_tplus1_CFO].copy()
    assert len(all_linked)==17104 and len(outcomes)==9487
    assert outcomes.original_cik.nunique()==3157
    all_linked.drop(columns=["_merge"]).to_csv(out/"SEC_FY2021_2024_GAAP_SIC_FORMAP_VERIFIED_AUDITOR.csv",index=False)
    outcomes.drop(columns=["_merge"]).to_csv(out/"SEC_FY2021_2024_CFO_CAPEX_FUTURE_CFO_FORMAP_N9487.csv",index=False)
    meta={
       "source":"23 SEC official XBRL quarterly zip sources 2021Q1–2026Q3 and 2026-10-10 Form AP AuditorSearch full zip",
       "built_utc":datetime.now(timezone.utc).isoformat(),
       "full_29k_original_10K_rows":29550,
       "full_CIK_mismatches":228,
       "full_report_date_mismatch_gt7days":11,
       "valid_issuer_match_CIK_and_fiscal_end_7day":29313,
       "FY2021_2024_nonfinancial_asfiled_SIC_pass":17492,
       "FY2021_2024_form_ap_issuer_latest_audit_report_date_after_SEC_rejected":invalid_audit_date,
       "FY2021_2024_multiple_distinct_legal_firms_flagged":multi_firm_count,
       "FY2021_2024_nonfinancial_with_single_registered_auditor":len(all_linked),
       "FY2021_2024_distinct_legal_registered_auditors":all_linked.pcaob_registered_firm_id.nunique(),
       "FY2021_2024_distinct_CIK_with_registered_auditor":all_linked.original_cik.nunique(),
       "FY2021_2024_CFO_cashPPE_future_CFO_AND_single_auditor_rows":len(outcomes),
       "FY2021_2024_CFO_cashPPE_future_CFO_AND_single_auditor_distinct_CIK":outcomes.original_cik.nunique(),
       "yearly":[{"fiscal_year":y,
         "financial_source_issuer_years":int(work.fiscal_year.eq(y).sum()),
         "audit_registry_matched":int(all_linked.fiscal_year.eq(y).sum()),
         "future_CFO_eligible_with_auditor":int(outcomes.fiscal_year.eq(y).sum())} for y in [2021,2022,2023,2024]],
       "limits":"Source matching SEC registration+52-53 week date tolerance is not a signed audit legal firm's public as-of information until Form AP source filed. No quantified AI-only investment, CAM, ICFR or public PCAOB inspection release exposure is verified. Full causal H1-H5 sample N remains unknown.",
       "quality_gates":{"GAAP_original_accession_exact":True,"CIK_equal":True,"historical_fiscal_end_diff_7d":True,
         "as_filed_SIC":True,"FormAP_CIK_FYE":True,"single_registered_auditor":True,
         "auditor_report_not_later_than_SEC_filing":True,
         "public_PCAOB_inspection_release_verified":False,"AI_only_capex_verified":False,
         "CAM_ICFR_verified":False}}
    (out/"SEC_GAAP_FORMAP_FULL_MATCH_ACTUAL_QA.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    print(json.dumps(meta,indent=2))
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--gaap",required=True,type=Path)
    p.add_argument("--formap",required=True,type=Path)
    p.add_argument("--out",required=True,type=Path)
    a=p.parse_args();main(a.gaap,a.formap,a.out)
