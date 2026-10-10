"""NAAIL public SEC filings cohort builder — live reconstruction from pinned mirror.

Input is SEC filings historical metadata parquet (Sept 30 2026 mirror).
Never equate a 2026 SIC with an original historic SIC, and never invent CAM,
ICFR, inspection, or AI-specific CapEx observations from filing metadata.
"""
from __future__ import annotations
import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import duckdb

VERSION="2026-09-30"
SOURCE="https://github.com/iangow/sec_submissions_data/releases/tag/2026-09-30"
NAMES={
 "cik":["cik"],"accession":["accessionNumber","accession_number"],
 "filed":["filingDate","filing_date"],"period":["reportDate","report_date"],
 "form":["form"],"accepted":["acceptanceDateTime"],
 "document":["primaryDocument"],"is_xbrl":["isXBRL"],
 "timestamp_provenance":["timestamp_provenance"],
 "timestamp_interpretation":["timestamp_interpretation"]
}
def locate(fields, options):
    dic={s.lower():s for s in fields}
    for x in options:
        if x.lower() in dic:return dic[x.lower()]
    return None
def quote(p):
    return str(p).replace("'","''")
def records(db,filings,companies):
    fields=[x[0] for x in db.execute("DESCRIBE SELECT * FROM read_parquet(?)",[str(filings)]).fetchall()]
    resolved={key:locate(fields,choices) for key,choices in NAMES.items()}
    for req in ("cik","accession","filed","period","form"):
        if not resolved[req]:raise ValueError("Missing required field "+req)
    def c(k,typ="VARCHAR"):
        return "TRY_CAST(\""+resolved[k]+"\" AS "+typ+")" if resolved[k] else "NULL::"+typ
    sql="SELECT "+",".join([
        c("cik","BIGINT")+" AS cik",
        c("accession")+" AS accession",
        c("filed","DATE")+" AS filed",
        c("period","DATE")+" AS period",
        c("form")+" AS form",
        c("accepted")+" AS accepted",
        c("document")+" AS document",
        c("is_xbrl","BOOLEAN")+" AS is_xbrl",
        c("timestamp_provenance")+" AS timestamp_provenance",
        c("timestamp_interpretation")+" AS timestamp_interpretation",
    ])+" FROM read_parquet('"+quote(filings)+"') WHERE "+c("form")+" IN ('10-K','10-KT') AND "+c("period","DATE")+" BETWEEN DATE '2017-01-01' AND DATE '2025-12-31' AND "+c("filed","DATE")+" <= DATE '2026-09-30'"
    data=db.execute(sql).fetchdf()
    company_fields=[x[0] for x in db.execute("DESCRIBE SELECT * FROM read_parquet(?)",[str(companies)]).fetchall()]
    kc=locate(company_fields,["cik"]);sc=locate(company_fields,["sic"]);nc=locate(company_fields,["name","companyName","entityName"])
    meta={}
    if kc:
        fieldlist=['TRY_CAST("'+kc+'" AS BIGINT) AS cik']
        if sc:fieldlist.append('TRY_CAST("'+sc+'" AS INTEGER) AS sic')
        if nc:fieldlist.append('"'+nc+'" AS name')
        q="SELECT "+",".join(fieldlist)+" FROM read_parquet('"+quote(companies)+"')"
        for row in db.execute(q).fetchdf().to_dict("records"):
            try:meta[int(row["cik"])]=row
            except(ValueError,TypeError):pass
    out=[]
    for r in data.to_dict("records"):
        try:
            if r["cik"] is None or r["period"] is None or r["filed"] is None:continue
            cik=int(r["cik"]);fy=int(str(r["period"])[:4]);filing_date=str(r["filed"])[:10];period_end=str(r["period"])[:10]
            if "NaT" in (filing_date,period_end):continue
            accession=str(r["accession"]);form=str(r["form"])
            if accession in ("nan","None",""):continue
            cc=meta.get(cik,{})
            sic_raw=cc.get("sic"); sic=""
            try:sic=int(sic_raw)
            except(ValueError,TypeError):pass
            status="MISSING_SIC" if sic=="" else "FINANCIAL_SNAPSHOT" if 6000<=sic<=6999 else "NONFINANCIAL_SNAPSHOT"
            doc=str(r["document"] or "").strip()
            if doc in ("nan","None"):doc=""
            entry={"cik":f"{cik:010d}","company_name_2026_snapshot":str(cc.get("name") or ""),
                   "fiscal_year":fy,"period_end":period_end,"filing_date":filing_date,
                   "accession":accession,"form":form,"acceptance_timestamp":str(r["accepted"] or ""),
                   "timestamp_provenance":str(r["timestamp_provenance"] or ""),
                   "timestamp_interpretation":str(r["timestamp_interpretation"] or ""),
                   "sic_2026_snapshot":sic,"current_sic_screen":status,
                   "is_XBRL":str(r["is_xbrl"]),
                   "original_SEC_URL":f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-','')}/{doc}" if doc else "",
                   "asof_archive":"2026-09-30","historical_SIC_verified":"NO",
                   "AI_only_capex_verified":"NO","CAM_verified":"NO","ICFR_verified":"NO","PCAOB_verified":"NO"}
            out.append(entry)
        except Exception as ex:raise RuntimeError("Inconsistent SEC record: "+str(r)[:300]) from ex
    return out
def dedupe(rows):
    unique={};extra=[]
    for r in rows:
        if r["form"]!="10-K":continue
        k=(r["cik"],r["fiscal_year"])
        if k not in unique:unique[k]=[]
        unique[k].append(r)
    main=[]
    for k,items in unique.items():
        items.sort(key=lambda v:(v["filing_date"],v["acceptance_timestamp"],v["accession"]))
        v=dict(items[0]);v["same_CIK_FY_original_reports"]=len(items)
        v["multiple_period_ends_flag"]=int(len({i["period_end"] for i in items})>1)
        main.append(v)
        extra.extend(items[1:])
    main.sort(key=lambda v:(v["fiscal_year"],v["cik"]))
    return main,extra
def save(path,rows,fields):
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore")
        w.writeheader();w.writerows(rows)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--filings",required=True,type=Path);ap.add_argument("--companies",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    with duckdb.connect() as db:
        db.execute("PRAGMA threads=4");db.execute("PRAGMA memory_limit='5GB'")
        filings=records(db,a.filings,a.companies)
    if not filings:raise RuntimeError("Empty SEC historical filings source")
    cohort,duplicate=dedupe(filings)
    target=[r for r in cohort if 2021<=r["fiscal_year"]<=2024]
    eligible=[r for r in target if r["current_sic_screen"]=="NONFINANCIAL_SNAPSHOT"]
    transitions=[r for r in filings if r["form"]=="10-KT" and 2021<=r["fiscal_year"]<=2024]
    head=list(cohort[0].keys())
    for name,rs in [
        ("SEC_10K_FY2017_2025_UNIVERSE.csv",cohort),
        ("SEC_10K_FY2021_2024_ALL_CANDIDATES.csv",target),
        ("SEC_10K_FY2021_2024_PROVISIONAL_NONFINANCIAL.csv",eligible),
        ("SEC_10K_FY2021_2024_TRANSITION_10KT_REVIEW.csv",transitions),
    ]:save(a.out/name,rs,head)
    years=[dict(fiscal_year=y,
        original_10K_issuer_years=sum(r["fiscal_year"]==y for r in cohort),
        unique_CIK=len({r["cik"] for r in cohort if r["fiscal_year"]==y}),
        provisional_nonfinancial_rows=sum(r["fiscal_year"]==y and r["current_sic_screen"]=="NONFINANCIAL_SNAPSHOT" for r in cohort),
        missing_SIC_rows=sum(r["fiscal_year"]==y and r["current_sic_screen"]=="MISSING_SIC" for r in cohort)
       ) for y in range(2017,2026)]
    save(a.out/"SEC_FY2017_2025_COUNTS.csv",years,list(years[0]))
    stats=dict(source=SOURCE,archive_date=VERSION,run_utc=datetime.now(timezone.utc).isoformat(),
      status="REAL_SEC_10K_FILING_METADATA_EXTRACT__NOT_FULL_CAUSAL_SAMPLE",
      all_10K_2017_2025_metadata_rows=sum(r["form"]=="10-K" for r in filings),
      unique_CIK_FY_2017_2025=len(cohort),
      FY2021_2024_original_10K_issuer_years=len(target),
      FY2021_2024_original_10K_unique_CIK=len({r["cik"] for r in target}),
      FY2021_2024_PROVISIONAL_nonfinancial_SIC_2026_issuer_years=len(eligible),
      FY2021_2024_PROVISIONAL_nonfinancial_unique_CIK=len({r["cik"] for r in eligible}),
      FY2021_2024_missing_SIC=sum(r["current_sic_screen"]=="MISSING_SIC" for r in target),
      FY2021_2024_10KT_forms_for_review=len(transitions),
      FY2021_2024_nonfirst_originals=sum(2021<=r["fiscal_year"]<=2024 for r in duplicate),
      FY2021_2024_ambiguous_reporting_periods=sum(r["multiple_period_ends_flag"] for r in target),
      year_counts=years,final_FT50_eligible_N=None,final_FT50_eligible_company_years=None,
      historical_SIC_verified=False,original_10K_content_validated=False,AI_CapEx_verified=False,
      CAM_AS3101_filer_year_status_verified=False,ICFR_404b_labels_verified=False,
      auditor_FormAP_PCAOB_asof_verified=False,
      caveat="Full universe includes later delisted firms but historic SIC, EGC CAM exemptions, company-owned AI CapEx and auditor oversight still unverified; 2026 SIC screening is provisional only. No FT50 regression.")
    (a.out/"SEC_FY2021_2024_ACTUAL_COUNTS_AND_LIMITS.json").write_text(json.dumps(stats,indent=2),encoding="utf8")
    print(json.dumps(stats,indent=2))
    assert len(target)>0 and len(eligible)>0
if __name__=="__main__":main()
