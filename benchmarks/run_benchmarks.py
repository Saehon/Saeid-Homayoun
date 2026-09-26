#!/usr/bin/env python3
"""Zero-dependency smoke benchmark runner for research CI."""
import json, math, pathlib, datetime

ROOT=pathlib.Path(__file__).parent
FIX=ROOT/"fixtures"
OUT=ROOT/"results"
OUT.mkdir(exist_ok=True)

def div(a,b): return a/b if b else 0.0
def classification(rows):
    tp=sum(r["gold"]==1 and r["pred"]==1 for r in rows)
    fp=sum(r["gold"]==0 and r["pred"]==1 for r in rows)
    fn=sum(r["gold"]==1 and r["pred"]==0 for r in rows)
    p=div(tp,tp+fp); r=div(tp,tp+fn)
    return {"precision":p,"recall":r,"f1":div(2*p*r,p+r)}

def brier(rows):
    return sum((r["prob"]-r["gold"])**2 for r in rows)/len(rows)

def numeric(rows):
    ok=0
    for r in rows:
        tol=r.get("tolerance",1e-6)
        ok += abs(r["pred"]-r["gold"]) <= tol
    return {"numeric_tolerance_accuracy":ok/len(rows)}

def load(name):
    return json.loads((FIX/name).read_text())

cam=classification(load("cam_kam.json"))
icfr_rows=load("icfr.json"); icfr={**classification(icfr_rows),"brier_score":brier(icfr_rows)}
fin=numeric(load("financial_reasoning.json"))
result={"status":"smoke-test","generated_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cam_kam":cam,"icfr":icfr,"financial_reasoning":fin,
        "note":"Synthetic fixtures only; not research results."}
(OUT/"smoke-results.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
