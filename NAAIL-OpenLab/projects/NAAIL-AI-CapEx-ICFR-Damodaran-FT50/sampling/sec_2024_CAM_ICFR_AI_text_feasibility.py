"""Reproducible FY2024 SEC filing text feasibility study with independent sampling.

All CAM, ICFR, AI capital investment expressions here are UNVERIFIED SCREENING FLAGS,
not labeled audit opinions, CAM-risk mismatch or AI-specific CapEx amounts.
"""
import csv,hashlib,json,re,time,sys
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import pandas as pd,requests
from bs4 import BeautifulSoup
def term_context(s,pattern,span=160):
    m=re.search(pattern,s,flags=re.I)
    if not m:return ""
    return s[max(0,m.start()-span):min(len(s),m.end()+span)].strip()[:450]
def main(original,asfiled,priority,out):
    out.mkdir(parents=True,exist_ok=True)
    official=pd.read_csv(asfiled,dtype={"original_cik":str,"sec_cik":str,"source_report_end":str},low_memory=False)
    o=official[(official.fiscal_year==2024)&official.sic_as_filed_screen.eq("NONFINANCIAL")].copy()
    o=o[o.original_cik.str.lstrip("0").eq(o.sec_cik.str.lstrip("0"))]
    o["period_official"]=pd.to_datetime(o.source_report_end,format="%Y%m%d",errors="coerce")
    o["period_original"]=pd.to_datetime(o.period_end,errors="coerce")
    o=o[((o.period_official-o.period_original).dt.days.abs()<=7)]
    assert o.original_cik.nunique()>3000
    with Path(priority).open(encoding="utf8",newline="") as f:
        priority_ciks={r["cik"] for r in csv.DictReader(f)}
    candidates=o[o.original_cik.isin(priority_ciks)].copy()
    general=o[~o.original_cik.isin(priority_ciks)].copy()
    general["hash_sort"]=general.original_cik.apply(lambda x:hashlib.sha256(("NAAIL-2026-10-10-"+x).encode()).hexdigest())
    chosen=pd.concat([candidates,general.sort_values("hash_sort").head(120)]).drop_duplicates("original_cik")
    with Path(original).open(newline="",encoding="utf8") as f:
        hist={(r["cik"],r["fiscal_year"]):r for r in csv.DictReader(f) if r["fiscal_year"]=="2024"}
    session=requests.Session()
    session.headers.update({"User-Agent":"NAAIL-OpenLab Accounting Academic Research (research-contact@example.org)","Accept":"text/html,text/plain"})
    outrows=[];errors=Counter()
    for i,row in enumerate(chosen.itertuples(),1):
        rowkey=(row.original_cik,"2024")
        h=hist.get(rowkey,{})
        url=h.get("original_SEC_URL","")
        source={"cik":row.original_cik,"fiscal_year":2024,
            "group":"TECH_OR_SUPPLIER_SCREEN" if row.original_cik in priority_ciks else "HISTORICAL_INDEPENDENT_HASH_RANDOM",
            "accession":row.accession,"source_10k_url":url,"sec_filing_date":row.filing_date,
            "HTML_access_status":"NOT_FETCHED","CAM_phrase_screen":"UNVERIFIED","ICFR_material_weakness_phrase_screen":"UNVERIFIED",
            "AI_capex_phrase_screen":"UNVERIFIED","ai_only_capex_dollars_verified":False,
            "CAM_context":"","ICFR_context":"","AI_capex_context":"","content_sha256":""}
        if not url or not url.startswith("https://www.sec.gov/Archives/"):
            source["HTML_access_status"]="NO_SOURCE_DOCUMENT_URL";errors["NO_SOURCE_DOCUMENT_URL"]+=1
        else:
            try:
                resp=session.get(url,timeout=30)
                source["HTML_access_status"]=str(resp.status_code)
                if resp.status_code==200 and len(resp.content)>1000:
                    sha=hashlib.sha256(resp.content).hexdigest()
                    html=resp.text[:10000000]
                    txt=BeautifulSoup(html,"lxml").get_text(" ",strip=True)
                    txt=re.sub(r"\s+"," ",txt)
                    source["content_sha256"]=sha
                    source["CAM_context"]=term_context(txt,r"critical audit matters?")
                    source["ICFR_context"]=term_context(txt,r"material weaknesses? (?:in|relating to|over) internal control")
                    source["AI_capex_context"]=term_context(txt,r"(?:AI|artificial intelligence).{0,175}(?:capital expenditures?|capital investments?)|(?:capital expenditures?|capital investments?).{0,175}(?:AI|artificial intelligence)")
                    source["CAM_phrase_screen"]="PRESENT" if source["CAM_context"] else "NOT_OBSERVED_IN_EXTRACT"
                    source["ICFR_material_weakness_phrase_screen"]="PRESENT" if source["ICFR_context"] else "NOT_OBSERVED_IN_EXTRACT"
                    source["AI_capex_phrase_screen"]="PRESENT" if source["AI_capex_context"] else "NOT_OBSERVED_IN_EXTRACT"
                else:errors["HTTP_"+str(resp.status_code)]+=1
            except requests.RequestException as e:
                source["HTML_access_status"]="FETCH_ERROR_"+type(e).__name__
                errors[source["HTML_access_status"]]+=1
            time.sleep(0.27)
        outrows.append(source)
        if i%50==0:print("SEC_FY2024_TEXT_SCREEN_PROGRESS",i,len(chosen),dict(errors),flush=True)
    cols=list(outrows[0])
    with (out/"SEC_FY2024_CAM_ICFR_AI_TEXT_UNVERIFIED_CANDIDATES.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(outrows)
    successful=[r for r in outrows if r["HTML_access_status"]=="200" and r["content_sha256"]]
    q={"source":"Original SEC 10-K primary filing URLs referenced by historical SEC filings metadata",
       "data_timestamp_utc":datetime.now(timezone.utc).isoformat(),
       "candidate_records":len(outrows),"priority_technology_supplier_candidates":sum(r["group"]=="TECH_OR_SUPPLIER_SCREEN" for r in outrows),
       "random_2024_company_candidates":sum(r["group"]=="HISTORICAL_INDEPENDENT_HASH_RANDOM" for r in outrows),
       "primary_10k_HTML_success":len(successful),
       "access_failure_counts":dict(errors),
       "CAM_phrase_present_preliminary":sum(r["CAM_phrase_screen"]=="PRESENT" for r in successful),
       "ICFR_material_weakness_phrase_present_preliminary":sum(r["ICFR_material_weakness_phrase_screen"]=="PRESENT" for r in successful),
       "AI_capex_phrase_present_preliminary":sum(r["AI_capex_phrase_screen"]=="PRESENT" for r in successful),
       "validated_numeric_AI_ONLY_capex":0,
       "RESEARCH_INTEGRITY":"Plain phrase presence in 10-K is NOT proof of a current CAM topic, current SOX material weakness or actual AI-only dollar CapEx. File/original context must receive blinded manual validation and AS3101 eligibility before any regression."}
    (out/"SEC_FY2024_TEXT_SCREEN_QA.json").write_text(json.dumps(q,indent=2),encoding="utf-8")
    print(json.dumps(q,indent=2))
if __name__=="__main__":
    if len(sys.argv)!=5:raise SystemExit("usage: script SEC_ORIGINAL.csv OFFICIAL_XBRL.csv PRIORITY_119.csv OUT")
    main(*sys.argv[1:4],Path(sys.argv[4]))
