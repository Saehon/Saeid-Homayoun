"""Deterministic validator for Microsoft FY2026 SEC Case 002."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CASE=json.loads((ROOT/"case_002_microsoft_sec_2026.json").read_text(encoding="utf-8"))

def calc():
    e={x["id"]:x["fact"] for x in CASE["evidence"]}
    r26=331839
    r25=281724
    gp=225465
    op=155237
    ni=133749
    return {
        "revenue_growth_pct":round((r26-r25)/r25*100,2),
        "gross_margin_pct":round(gp/r26*100,2),
        "operating_margin_pct":round(op/r26*100,2),
        "net_margin_pct":round(ni/r26*100,2),
        "financial_statement_opinion":"unqualified",
        "icfr_opinion":"unqualified",
        "evidence_ids_used":["E1","E2","E3","E4","E5","E6","E7"],
        "unsupported_claims":[]
    }

def score(answer):
    gold=CASE["gold_standard"]
    checks={
        "revenue_growth_pct":answer.get("revenue_growth_pct")==gold["revenue_growth_pct"],
        "gross_margin_pct":answer.get("gross_margin_pct")==gold["gross_margin_pct"],
        "operating_margin_pct":answer.get("operating_margin_pct")==gold["operating_margin_pct"],
        "net_margin_pct":answer.get("net_margin_pct")==gold["net_margin_pct"],
        "financial_statement_opinion":answer.get("financial_statement_opinion")==gold["financial_statement_opinion"],
        "icfr_opinion":answer.get("icfr_opinion")==gold["icfr_opinion"],
        "evidence_complete":set(answer.get("evidence_ids_used",[]))==set(gold["required_evidence_ids"]),
        "unsupported_claims_empty":answer.get("unsupported_claims",[])==[]
    }
    return {"accuracy":sum(checks.values())/len(checks),"components":checks,"passed":all(checks.values())}

if __name__=="__main__":
    answer=calc()
    result={"case_id":CASE["case_id"],"deterministic_answer":answer,"score":score(answer)}
    print(json.dumps(result,indent=2))
