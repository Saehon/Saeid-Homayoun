"""Microsoft SEC/XBRL Pilot 001 — public-data execution scaffold.
Downloads SEC CompanyFacts, selects benchmark concepts, creates an evidence table,
runs deterministic accounting checks, and writes reproducible CSV/JSON outputs.
No model API key is required for the deterministic baseline.
"""
import json, csv, hashlib, urllib.request
from pathlib import Path
from datetime import datetime, timezone

CIK="0000789019"
URL=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"
CONCEPTS=["Assets","Liabilities","StockholdersEquity","Revenues","NetIncomeLoss",
"CashAndCashEquivalentsAtCarryingValue","NetCashProvidedByUsedInOperatingActivities"]
OUT=Path("outputs"); OUT.mkdir(exist_ok=True)
req=urllib.request.Request(URL,headers={"User-Agent":"Academic research contact: repository owner"})
with urllib.request.urlopen(req) as r: raw=r.read()
(OUT/"companyfacts_raw.json").write_bytes(raw)
snapshot=hashlib.sha256(raw).hexdigest()
data=json.loads(raw)
rows=[]
for concept in CONCEPTS:
    node=data.get("facts",{}).get("us-gaap",{}).get(concept,{})
    for unit, obs in node.get("units",{}).items():
        for x in obs:
            if x.get("form") in {"10-K","10-Q"}:
                rows.append({"evidence_id":f"{concept}:{x.get('accn')}:{x.get('end')}:{unit}",
                "cik":CIK,"entity":data.get("entityName"),"concept":concept,"unit":unit,
                "value":x.get("val"),"start":x.get("start"),"end":x.get("end"),
                "fy":x.get("fy"),"fp":x.get("fp"),"form":x.get("form"),
                "filed":x.get("filed"),"accn":x.get("accn"),"snapshot_sha256":snapshot})
fields=list(rows[0]) if rows else []
with open(OUT/"microsoft_xbrl_evidence.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
checks={"snapshot_sha256":snapshot,"rows":len(rows),"duplicate_evidence_ids":len(rows)-len({r["evidence_id"] for r in rows}),
"missing_values":sum(r["value"] is None for r in rows),"generated_utc":datetime.now(timezone.utc).isoformat()}
(OUT/"deterministic_checks.json").write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
