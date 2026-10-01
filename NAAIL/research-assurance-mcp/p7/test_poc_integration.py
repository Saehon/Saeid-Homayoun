#!/usr/bin/env python3
"""P7 integration checks for NAAIL Research Assurance POC (stdlib only)."""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"p5"))
from naail_mcp_poc import load_json, validate_evidence_graph, map_table_to_code, trace_provenance, generate_assurance_report, score_detection

GRAPH=ROOT/"evidence-graph"/"evidence_graph_v1_case001.json"
BENCH=ROOT/"benchmark"/"adversarial_benchmark_v2.json"

def check(cond,msg):
    if not cond: raise AssertionError(msg)

def main():
    g=load_json(GRAPH); b=load_json(BENCH)
    v=validate_evidence_graph(g)
    check(v["pass"],f"graph invalid: {v}")
    check(v["node_count"]==13 and v["edge_count"]==13,"graph count drift")
    m=map_table_to_code(g,"TABLE_REG")
    check(any(x["code"].get("id")=="CODE_MAIN" for x in m["code_paths"]),"TABLE_REG not mapped to CODE_MAIN")
    ap=trace_provenance(g,"CLAIM_AOC")["nodes"]
    mp=trace_provenance(g,"CLAIM_MSFT")["nodes"]
    aids={x["id"] for x in ap}; mids={x["id"] for x in mp}
    check({"CLAIM_AOC","TABLE_REG","RESULT_AOC","CODE_MAIN","DATA_REG","SOURCE_PAPER","LIMIT_FULL_REPRO","LIMIT_METHOD"}<=aids,"author provenance incomplete")
    check({"CLAIM_MSFT","RESULT_MSFT","CODE_MSFT","DATA_MSFT","SOURCE_SEC","LIMIT_FULL_REPRO","LIMIT_METHOD"}<=mids,"MSFT provenance incomplete")
    report=generate_assurance_report(g)
    check(report["overall_state"]=="PARTIAL","overall assurance must remain PARTIAL")
    check(report["state_counts"]["PARTIAL"]>=1 and report["state_counts"]["HUMAN_REVIEW"]>=1,"scope guards missing")
    cases=b["cases"]; ids=[c["id"] for c in cases]
    check(len(cases)==19 and len(ids)==len(set(ids)),"benchmark fixture count/uniqueness drift")
    kinds={c["kind"] for c in cases}
    check({"clean_control","single","compound","blinded"}<=kinds,"benchmark class missing")
    clean=[c for c in cases if c["kind"]=="clean_control"]
    check(len(clean)==1 and clean[0]["expected"]=="NO_FLAG","clean control contract invalid")
    expected=sorted({t for c in cases for t in c.get("taxonomy_ids",[])})
    perfect=score_detection(expected,expected)
    check(perfect["precision"]==1 and perfect["recall"]==1 and perfect["f1"]==1,"scoring sanity failed")
    out={"status":"PASS","graph_validation":v,"table_to_code_paths":len(m["code_paths"]),
         "author_trace_nodes":len(ap),"microsoft_trace_nodes":len(mp),
         "assurance_overall":report["overall_state"],"benchmark_fixtures":len(cases),
         "benchmark_kinds":sorted(kinds),"taxonomy_ids_exercised":len(expected),
         "scoring_sanity":perfect,
         "scope_guards":["264/264 is author-output consistency only","Microsoft is one-company public-SEC construct reconstruction only","full-paper independent reproduction remains PARTIAL","methodological validity remains HUMAN_REVIEW"]}
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
