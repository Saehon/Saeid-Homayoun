#!/usr/bin/env python3
"""Read-only Paper2Agent-style tool functions for the SYNTHETIC NAAIL pilot.
NOT an MCP server, RAG system, live data bridge, or original Bao reproduction.
Tool wrappers may later expose these exact contracts over a rights-cleared MCP.
"""
import argparse
import hashlib
import json
from pilot import fixture, run, risk, WEIGHTS

PAPER = {
    "paper_id": "bao-2020-jar",
    "title": "Detecting Accounting Fraud in Publicly Traded U.S. Firms Using a Machine Learning Approach",
    "journal": "Journal of Accounting Research",
    "doi": "10.1111/1475-679X.12292",
    "author_code": "https://github.com/JarFraud/FraudDetection",
    "correction_doi": "10.1111/1475-679X.12454",
    "execution_status": "ORIGINAL_AUTHOR_MODEL_NOT_REPRODUCED",
    "current_runtime": "INDEPENDENT_SYNTHETIC_TOY_COMPARISON",
}

TOOL_CONTRACTS = [
    {"name": "get_paper_method", "args": {}, "returns": "paper provenance and reproducibility caveats"},
    {"name": "run_architecture_benchmark", "args": {}, "returns": "A0–A3 synthetic metrics + Human Gate status"},
    {"name": "inspect_synthetic_case", "args": {"case_id": "SYN-2024-00"},
     "returns": "synthetic inputs, provenance ID, triage flag, limitations"},
]

def get_paper_method():
    return dict(PAPER)

def run_architecture_benchmark():
    rows = fixture()
    digest = hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return run(rows,"synthetic",digest)

def inspect_synthetic_case(case_id):
    if not isinstance(case_id,str) or not case_id.startswith("SYN-"):
        raise ValueError("Only SYN-* synthetic IDs allowed; no live company data")
    rows=fixture()
    row=next((r for r in rows if r["case_id"]==case_id),None)
    if row is None:
        raise ValueError("Synthetic case not found")
    p=risk(row,WEIGHTS[0])
    return {
       "case_id": row["case_id"],"source_type":"SYNTHETIC",
       "source_evidence_id":row["evidence_id"],
       "features":{"revenue_growth":row["revenue_growth"],
                   "accrual_ratio":row["accrual_ratio"],
                   "control_exception":row["control_exception"]},
       "illustrative_a0_score":round(p,6),
       "cam_present":bool(row["cam_present"]),
       "evidence_complete":bool(row["evidence_complete"]),
       "research_triage_high_risk_no_cam":bool(p>=0.42 and not row["cam_present"]),
       "audit_failure_claim_allowed":False,
       "human_approval_status":"REQUIRED_NOT_GRANTED"
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool",choices=("list_tools","get_paper_method","run_architecture_benchmark","inspect_synthetic_case"),required=True)
    parser.add_argument("--case-id",default="SYN-2024-00")
    args=parser.parse_args()
    if args.tool=="list_tools":
        out=TOOL_CONTRACTS
    elif args.tool=="get_paper_method":
        out=get_paper_method()
    elif args.tool=="run_architecture_benchmark":
        out=run_architecture_benchmark()
    else:
        out=inspect_synthetic_case(args.case_id)
    print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False))

if __name__=="__main__":
    main()
