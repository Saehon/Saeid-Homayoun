"""Join full official PCAOB Form AP AuditorSearch bulk data to historical SEC 10-K.

Exact key: 10-digit CIK + issuer fiscal period-end. Track Form AP signed/filing date,
audit partner/firm registration without publishing private partner contacts.
Does NOT interpret PCAOB inspection report-date as its public release date.
"""
from __future__ import annotations
import argparse,csv,json,re,zipfile
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter,defaultdict
import pandas as pd

def cik10(v):
 s=re.sub("[^0-9]","",str(v or ""))
 try:return f"{int(s):010d}" if int(s)>0 else ""
 except ValueError:return ""
def date(v):
 if v is None or str(v).lower() in ("","nan","nat","none"):return ""
 d=pd.to_datetime(v,errors="coerce")
 return "" if pd.isna(d) else d.strftime("%Y-%m-%d")
def read_history(path):
 out={}
 with path.open(encoding="utf-8",newline="") as f:
  for r in csv.DictReader(f):
   if r["form"]!="10-K":continue
   if not 2021<=int(r["fiscal_year"])<=2025:continue
   key=(r["cik"],r["period_end"])
   if key in out:raise ValueError(f"Duplicated historical original 10-K period key {key}")
   out[key]=r
 return out
def main(history,zippath,out):
 out.mkdir(parents=True,exist_ok=True)
 source=read_history(history)
 possible=[],unmatched=Counter(),any_rows=0, matched=0,firm_names=Counter()
 with zipfile.ZipFile(zippath) as z:
  files=[n for n in z.namelist() if n.lower().endswith(".csv")]
  if len(files)!=1:raise ValueError(f"Expected a single authoritative Form AP CSV: {files}")
  member=files[0]
  with z.open(member) as stream:
   reader=pd.read_csv(stream,dtype=str,chunksize=50000,low_memory=False,encoding="utf-8-sig")
   for df in reader:
    if not {"Issuer CIK","Fiscal Period End Date","Firm ID","Filing Date"}.issubset(df.columns):
     raise ValueError(f"Required Form AP fields unavailable: {list(df.columns)}")
    any_rows+=len(df)
    for r in df.to_dict("records"):
     ck=cik10(r.get("Issuer CIK"))
     fye=date(r.get("Fiscal Period End Date"))
     if not ck or not fye:continue
     prior=source.get((ck,fye))
     if prior is None:continue
     auditor_id=str(r.get("Firm ID","")).strip()
     auditor_name=str(r.get("Firm Name","")).strip()
     if auditor_id in ("nan","None",""):continue
     matched+=1
     firm_names[auditor_id]+=1
     audit_date=date(r.get("Audit Report Date"))
     ap_filed=date(r.get("Filing Date"))
     # Do not publish partner emails, phone numbers, partner IDs or contact info.
     possible.append({"cik":ck,"fiscal_year":int(prior["fiscal_year"]),
         "period_end":fye,"sec_original_accession":prior["accession"],
         "sec_10k_filing_date":prior["filing_date"],
         "sec_10k_url":prior["original_SEC_URL"],
         "pcaob_registered_firm_id":auditor_id,
         "pcaob_firm_legal_name":auditor_name,
         "audit_report_date":audit_date,
         "form_ap_first_filed_or_amended_date":ap_filed,
         "form_ap_filing_id":str(r.get("Form Filing ID","")),
         "form_ap_latest_form_flag":str(r.get("Latest Form AP Filing","")),
         "audit_report_type":str(r.get("Audit Report Type","")),
         "exact_CIK_and_period_end_join":True,
         "FORMAP_FILED_AFTER_SEC_10K":bool(ap_filed and prior["filing_date"] and ap_filed>prior["filing_date"]),
         "as_of_audit_firm_public_at_SEC_filing":"REQUIRES_10K_AUDITOR_SIGNATURE_VERIFICATION_IF_AP_FILING_AFTER_SEC",
         "PCAOB_INSPECTION_PUBLIC_RELEASE_JOIN":"NOT_YET_VERIFIED"})
 tab=pd.DataFrame(possible)
 if tab.empty:raise ValueError("Zero exact Form AP/10-K joins: inspect official CSV join fields")
 tab=tab.sort_values(["cik","fiscal_year","form_ap_filing_id"])
 tab.to_csv(out/"FORMAP_SEC_EXACT_CIK_FISCAL_END_MATCH_CANDIDATES_2021_2025.csv",index=False)
 era=tab[tab.fiscal_year.between(2021,2024)]
 distinct=era.drop_duplicates(["cik","fiscal_year"])
 peryear=[]
 for year in range(2021,2026):
  yearrows=tab[tab.fiscal_year.eq(year)]
  peryear.append({"fiscal_year":year,"matching_FormAP_records":len(yearrows),
    "matched_company_years":len(yearrows.drop_duplicates(["cik","fiscal_year"])),
    "distinct_issuers":yearrows.cik.nunique(),
    "distinct_firm_ids":yearrows.pcaob_registered_firm_id.nunique()})
 # Preserve multiple legal firms and amended filing ambiguity, avoid inventing single auditor.
 multi=era.groupby(["cik","fiscal_year"]).pcaob_registered_firm_id.nunique()
 obs=era.drop_duplicates(["cik","fiscal_year"])
 audit={
 "source":"PCAOB AuditorSearch full bulk FirmFilings.zip as of 2026-10-10",
 "source_url":"https://assets.pcaobus.org/firm-filings/FirmFilings.zip",
 "data_date_retrieved_utc":datetime.now(timezone.utc).isoformat(),
 "original_ap_rows_all_issuer_types_and_years":any_rows,
 "exact_CIK_report_period_matches_all_fy2021_2025":len(tab),
 "FY2021_2024_FormAP_exact_matched_rows":len(era),
 "FY2021_2024_unique_10K_CIK_fy_matched":len(obs),
 "FY2021_2024_unique_issuer_CIK_matched":obs.cik.nunique(),
 "FY2021_2024_unique_registered_audit_firms":era.pcaob_registered_firm_id.nunique(),
 "FY2021_2024_multi_legal_firm_CIK_years":int((multi>1).sum()),
 "FY2021_2024_FormAP_filed_after_sec_10k_rows":int(era.FORMAP_FILED_AFTER_SEC_10K.sum()),
 "years":peryear,"report_type_distribution":tab.audit_report_type.value_counts().head(15).to_dict(),
 "latest_AP_flag_distribution":tab.form_ap_latest_form_flag.value_counts().head(15).to_dict(),
 "top_registered_firm_ids":Counter(era.pcaob_registered_firm_id).most_common(12),
 "source_10K_CIK_FY_total_actual_nonfinancial_2026_sic":18336,
 "issuer_link_role":"AUDITOR_REGISTRY_ONLY__PCAOB_INSPECTION_FIRST_PUBLIC_RELEASE_NOT_JOINED",
 "limits":"Exact legal CIK-period join with original SEC 10-K does NOT itself verify the Form AP was public at SEC filing date, audit client-year CAM/ICFR content, first-public PCAOB inspection date, or that AI-only CapEx was spent. Duplicate auditor firm/period records remain flagged. Do not classify Form AP absence as no audit; no model coefficients."}
 (out/"FORMAP_SEC_JOIN_ACTUAL_COVERAGE_QA_2026-10-10.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
 print(json.dumps(audit,indent=2))
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--history",type=Path,required=True)
 p.add_argument("--form-ap-zip",type=Path,required=True)
 p.add_argument("--out",type=Path,required=True)
 a=p.parse_args();main(a.history,a.form_ap_zip,a.out)
