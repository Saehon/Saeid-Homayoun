"""Join SEC's OFFICIAL quarterly financial statement ZIP to exact original SEC 10-K accessions.

The source SEC 'sub' table contains SIC at the time the 10-K was filed.
This is source-FILING SIC, not reconstructed SIC history for other observations.
No AI-specific capital spending claims are created.
"""
import argparse,csv,json,zipfile
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import pandas as pd

METRICS={
  "NetCashProvidedByUsedInOperatingActivities":"operating_cash_flow_usd",
  "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations":"operating_cash_flow_continuing_usd",
  "PaymentsToAcquirePropertyPlantAndEquipment":"gross_cash_ppe_capex_usd",
  "NetIncomeLoss":"net_income_usd",
  "ProfitLoss":"profit_loss_usd",
  "Assets":"assets_usd",
  "Revenues":"revenue_usd",
  "RevenueFromContractWithCustomerExcludingAssessedTax":"revenue_from_contracts_usd"
}
INSTANT={"Assets"}
def load_originals(csv_path):
    with csv_path.open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    return {row["accession"].strip():row for row in rows if row["form"]=="10-K" and 2021<=int(row["fiscal_year"])<=2025}
def main(zip_paths,source_orig,out):
    out.mkdir(parents=True,exist_ok=True)
    original=load_originals(source_orig)
    selected={}
    num_rows=[]
    per_quarter=[]
    for zp in zip_paths:
        quarter=Path(zp).stem
        with zipfile.ZipFile(zp) as z:
            names={n.lower():n for n in z.namelist()}
            subname=next((names[k] for k in names if k.endswith("sub.txt")),None)
            numname=next((names[k] for k in names if k.endswith("num.txt")),None)
            if not subname or not numname:raise RuntimeError(f"Missing SEC SUB/NUM tables {zp}: {list(names)[:12]}")
            with z.open(subname) as stream:
                sub=pd.read_csv(stream,sep="\t",dtype=str,low_memory=False,encoding="utf-8")
            if not {"adsh","cik","form","period","sic","filed"}.issubset(sub.columns):
                raise ValueError(f"SEC SUB source schema unexpected: {list(sub.columns)}")
            sub=sub[sub.form.eq("10-K") & sub.adsh.isin(original)]
            sub=sub.drop_duplicates("adsh")
            lookup={}
            for v in sub.to_dict("records"):
                accession=str(v["adsh"])
                historic=original[accession]
                sec_sic=pd.to_numeric(v.get("sic"),errors="coerce")
                sic=int(sec_sic) if pd.notna(sec_sic) else None
                x={"accession":accession,"source_quarter":quarter,"source_report_end":str(v.get("period","")),
                   "sec_cik":str(v.get("cik","")),"original_cik":historic["cik"],
                   "fiscal_year":historic["fiscal_year"],"period_end":historic["period_end"],
                   "filing_date":historic["filing_date"],"SEC_SUB_filed":str(v.get("filed","")),
                   "as_filed_SIC":sic,"sic_as_filed_screen":"MISSING" if sic is None else "FINANCIAL" if 6000<=sic<=6999 else "NONFINANCIAL",
                   "sector_screen_basis":"SEC_10K_SUB_AS_FILED_FILING_SNAPSHOT","SEC_fiscal_form":"10-K",
                   "XBRL_financial_available":"PENDING_NUM_TAG_JOIN"}
                selected[accession]=x
                lookup[accession]=x
            count=0
            with z.open(numname) as stream:
                for chunk in pd.read_csv(stream,sep="\t",dtype=str,chunksize=160000,low_memory=False,encoding="utf-8",on_bad_lines="skip"):
                    keep=chunk.adsh.isin(lookup)&chunk.tag.isin(METRICS)&chunk.version.fillna("").str.startswith("us-gaap")
                    if "coreg" in chunk:keep &=chunk.coreg.isna()|chunk.coreg.astype(str).eq("")
                    if "segments" in chunk:keep &=chunk.segments.isna()|chunk.segments.astype(str).eq("")
                    filtered=chunk[keep]
                    if filtered.empty:continue
                    for x in filtered.to_dict("records"):
                        tag=x["tag"];acc=x["adsh"];info=lookup[acc]
                        expected_q=0 if tag in INSTANT else 4
                        if str(x.get("qtrs","")).strip()!=str(expected_q):continue
                        if str(x.get("ddate","")).replace("-","") !=info["period_end"].replace("-",""):continue
                        try: amount=float(x["value"])
                        except (ValueError,TypeError):continue
                        if pd.isna(amount):continue
                        if str(x.get("uom",""))!="USD":continue
                        num_rows.append({"accession":acc,"source_quarter":quarter,"cik":info["original_cik"],
                            "fiscal_year":info["fiscal_year"],"tag":tag,"metric":METRICS[tag],
                            "value_usd":amount,"source_end":str(x["ddate"]),
                            "qtrs":str(x["qtrs"]),"uom":"USD"})
                        count+=1
            per_quarter.append({"quarter":quarter,"matched_original_10K":len(lookup),"matched_primary_financial_fact_rows":count,
                                "as_filed_nonfinancial":sum(x["sic_as_filed_screen"]=="NONFINANCIAL" for x in lookup.values()),
                                "as_filed_missing_SIC":sum(x["sic_as_filed_screen"]=="MISSING" for x in lookup.values())})
            print(json.dumps(per_quarter[-1]),flush=True)
    # No cross-quarter duplicate asset registrations silently overwritten:
    # original accession should have been accepted in exactly one quarterly dataset.
    facts=pd.DataFrame(num_rows)
    if facts.empty:raise RuntimeError("No exact original 10-K fact matches; inspect official quarterly SEC schema")
    duplicates=facts.duplicated(subset=["accession","metric"],keep=False)
    alternatives=facts[duplicates].sort_values(["accession","metric"]).copy()
    if len(alternatives)>0:
        alternatives.to_csv(out/"DUPLICATE_PRIMARY_GAAP_FACTS_REVIEW.csv",index=False)
    facts=facts.drop_duplicates(["accession","metric"],keep=False)
    wide=facts.pivot(index="accession",columns="metric",values="value_usd")
    metadata=pd.DataFrame(list(selected.values())).drop_duplicates("accession").set_index("accession")
    joined=metadata.join(wide,how="left").reset_index()
    got=set(facts.accession)
    joined["XBRL_financial_available"]=joined["accession"].isin(got)
    joined["AI_only_capex_usd"]=pd.NA
    joined["ICFR_material_weakness_verified"]=pd.NA
    joined["CAM_account_risk_alignment_verified"]=pd.NA
    joined["PCAOB_public_inspection_issuer_asof_verified"]=pd.NA
    joined["OCF_minus_gross_PPE_capex_usd"]=pd.to_numeric(joined.get("operating_cash_flow_usd"),errors="coerce")-pd.to_numeric(joined.get("gross_cash_ppe_capex_usd"),errors="coerce")
    joined.to_csv(out/"SEC_OFFICIAL_ASFILED_SIC_XBRL_FACTS_PILOT.csv",index=False)
    facts.to_csv(out/"SEC_OFFICIAL_GAAP_FACT_SOURCE_LINES.csv",index=False)
    audit={
        "run_utc":datetime.now(timezone.utc).isoformat(),"source":"SEC official quarterly XBRL rendered financial statement datasets",
        "quarters":per_quarter,"original_10K_rows_matched":len(joined),
        "unambiguous_gaap_fact_rows":len(facts),
        "duplicate_fact_rows_requiring_reconciliation":len(alternatives),
        "available_CFO":int(joined.get("operating_cash_flow_usd",pd.Series(dtype=float)).notna().sum()),
        "available_cash_PPE_capex":int(joined.get("gross_cash_ppe_capex_usd",pd.Series(dtype=float)).notna().sum()),
        "available_both_cash_flow_and_PPE":int((joined.get("operating_cash_flow_usd",pd.Series(index=joined.index,dtype=float)).notna()&joined.get("gross_cash_ppe_capex_usd",pd.Series(index=joined.index,dtype=float)).notna()).sum()),
        "as_filed_SIC_status":joined.sic_as_filed_screen.value_counts().to_dict(),
        "LIMITS":"PARTIAL OFFICIAL QUARTER PILOT ONLY. SEC SUB SIC as-filed, not proven entity historic beyond filing. Missing XBRL tags may mean custom taxonomy, not zero cash flows. Company-wide PP&E is not AI-only CapEx, CFO-CapEx is not FCFF. No ICFR/CAM/FormAP/PCAOB/AI-specific data was joined."}
    (out/"SEC_OFFICIAL_QUARTER_SIC_XBRL_PILOT_QA.json").write_text(json.dumps(audit,indent=2),encoding="utf8")
    print(json.dumps(audit,indent=2,default=str))
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--zip",nargs="+",required=True,type=Path)
    p.add_argument("--originals",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();main(a.zip,a.originals,a.out)
