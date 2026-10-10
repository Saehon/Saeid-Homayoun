"""Download-derived PCAOB official datasets: inspect exact fields and preserve as-of uncertainty."""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

URLS = {
 "firm_inspections": "https://pcaobus.org/docs/default-source/generated-reports/inspecton-reports-csv.csv?download=true&sfvrsn=1cadcbfa_1193",
 "part_I_A": "https://pcaobus.org/docs/default-source/generated-reports/part-i-a-flat-file-%28csv%29.csv?download=true&sfvrsn=c59cce67_5",
 "part_I_B": "https://pcaobus.org/docs/default-source/generated-reports/part-i-b-flat-file-%28csv%29.csv?download=true&sfvrsn=68eeaca9_5"
}
AUDITORS = {
 "deloitte": ("deloitte",), "ernst_young": ("ernst & young", "ernst and young"),
 "pricewaterhousecoopers": ("pricewaterhousecoopers", "pwc"),
 "kpmg": ("kpmg",), "bdo": ("bdo",), "grant_thornton": ("grant thornton",)
}
def header_and_rows(path):
    with path.open("r",encoding="utf-8-sig",errors="replace",newline="") as f:
        raw=f.read(50000);f.seek(0)
        try: dialect=csv.Sniffer().sniff(raw,delimiters=",;\t|")
        except csv.Error: dialect=csv.excel
        rows=list(csv.DictReader(f,dialect=dialect))
    return rows
def main(files, out):
    out.mkdir(parents=True,exist_ok=True)
    report={"source":"PCAOB official downloadable public firm inspection reports and Part I.A/I.B",
      "retrieved_utc":datetime.now(timezone.utc).isoformat(),"urls":URLS,
      "as_of_rule":"Source data may include 2026 released reports; no observation may be attributed to pre-release event until release_date and legal auditor firm ID are verified.",
      "datasets":{},"named_firms":{},"filer_year_issuer_join":"NOT COMPLETED: Form AP legal firm IDs and issuer matching must be constructed separately",
      "causal_pcaob_features_ready":False}
    matches=[]
    for name,path in zip(URLS,files):
        rows=header_and_rows(Path(path))
        hdr=list(rows[0]) if rows else []
        cand=[h for h in hdr if any(k in h.lower() for k in ("name","firm","registr","date","year","report","inspection","audit","part","id","type"))]
        counts={h:sum(bool(str(r.get(h,"")).strip()) for r in rows) for h in cand}
        report["datasets"][name]={"rows":len(rows),"fields":hdr,"field_coverage":counts,
          "sample_safe_values":{h:list(dict.fromkeys(str(r.get(h,""))[:75] for r in rows[:20]))[:6] for h in cand[:12]}}
        for row in rows:
            norm=" ".join(str(row.get(k,"")) for k in hdr if any(x in k.lower() for x in ("firm", "name", "auditor")))
            norm=re.sub(r"\s+"," ",norm.lower())
            for group,searches in AUDITORS.items():
                if any(token in norm for token in searches):
                    matches.append(dict(source_table=name,matched_group=group,
                        **{str(k):str(v)[:2500] for k,v in row.items()}))
                    break
    report["matched_public_rows"]=len(matches)
    for key in AUDITORS:
        report["named_firms"][key]=Counter(r["source_table"] for r in matches if r["matched_group"]==key)
    (out/"PCAOB_PUBLIC_SOURCE_AUDIT_SCHEMA_QA.json").write_text(json.dumps(report,indent=2,default=dict),encoding="utf-8")
    (out/"PCAOB_MATCHED_AUDITOR_RECORDS.json").write_text(json.dumps(matches,indent=1),encoding="utf-8")
    print(json.dumps({"dataset_rows":{k:v["rows"] for k,v in report["datasets"].items()},
        "dataset_fields":{k:v["fields"] for k,v in report["datasets"].items()},
        "matched_group_rows":{k:dict(v) for k,v in report["named_firms"].items()},
        "rows_matched":len(matches),"ready_for_issuer_join":False},indent=2))
if __name__=="__main__":
    if len(sys.argv)!=5:raise SystemExit("usage: script firm_csv partIA_csv partIB_csv OUTPUT_FOLDER")
    main(sys.argv[1:4],Path(sys.argv[4]))
