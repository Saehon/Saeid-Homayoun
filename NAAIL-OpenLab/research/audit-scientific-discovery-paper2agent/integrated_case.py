#!/usr/bin/env python3
"""Execute genuine repository integrations on synthetic research fixtures only.

Imports the EXISTING Lemon ICFR Python orchestrator and CAM/KAM benchmarking
code from the NAAIL mother repository; no code is copied or vendored.
This is not independent reviewer verification, real CAM disclosure measurement,
audit opinion, or validated fraud model.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import importlib.util
import json
import sys
from dataclasses import asdict
from pathlib import Path

from pilot import fixture, WEIGHTS, risk

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
LEMON=REPO/"Lemon-ICFR-US"/"src"
CAM=REPO/"NAAIL-OpenLab"/"demos"/"cam-kam-agent-benchmark"
if str(LEMON) not in sys.path:
    sys.path.insert(0,str(LEMON))

def load_existing_cam():
    path=CAM/"benchmark.py"
    if not path.is_file():
        raise FileNotFoundError(f"Existing CAM benchmark missing: {path}")
    spec=importlib.util.spec_from_file_location("naail_existing_cam_benchmark",path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_integrated_case(case_id="SYN-2024-00"):
    from lemon_icfr.models import EvidenceItem, Finding
    from lemon_icfr.orchestrator import LemonOrchestrator
    case=next((r for r in fixture() if r["case_id"]==case_id),None)
    if case is None:
        raise ValueError("Only registered SYN-* cases may be analyzed")
    p=risk(case,WEIGHTS[0])
    evidence_content=json.dumps({"source":"synthetic generated fixture",
                                 "case_id":case_id,"risk_score":p,
                                 "control_exception":case["control_exception"],
                                 "cam_present":case["cam_present"]},sort_keys=True)
    evidence=EvidenceItem(evidence_id=case["evidence_id"],
        source="NAAIL explicitly synthetic fixture",
        provenance="NAAIL-OpenLab/research/audit-scientific-discovery-paper2agent/pilot.py::fixture",
        rights_status="synthetic-created-for-public-demo",
        content=evidence_content,version="0.3.0")
    class BoundedProvider:
        name="deterministic-synthetic-hypothesis-provider"
        def generate_hypotheses(self,case_id,evidence,question):
            return [Finding(agent="synthetic-co-scientist",
               claim="Synthetic case requires human review of control evidence; no real-audit finding.",
               evidence_refs=[evidence[0].evidence_id],
               alternative_explanations=["Artificial control score may not reflect any real control deficiency."],
               limitations=["Generated synthetic data", "No independent empirical labels"],
               model_tool_version="synthetic_rule_v0.3")]
        def challenge_claim(self,case_id,evidence,finding):
            return Finding(agent="simulated-challenger",
               claim="Synthetic alternative: score may be arbitrary and unrelated to material misstatement.",
               evidence_refs=[evidence[0].evidence_id],
               limitations=["Same simulated provider; not an independent verifier"],
               model_tool_version="synthetic_rule_v0.3")
    result=LemonOrchestrator().run(
        case_id=case_id,question="What evidence must an auditor review?",
        evidence=[evidence],provider=BoundedProvider(),
        coso_context_supplied=True,
        reproducibility_ref="pilot.py::fixture")
    cam_model=load_existing_cam()
    # CAM text below is an openly labeled SYNTHETIC benchmark fixture.
    rows=[{
       "id":case_id,
       "risk_text":"Revenue recognition risk and material cutoff estimation uncertainty.",
       "procedure_text":"We tested a sample of contracts and invoice cutoff and recalculated revenue.",
       "evidence_text":"Synthetic invoice, contract, recalculation and sample evidence.",
       "assertion_text":"occurrence cutoff accuracy"}]
    cam_scores=cam_model.score_rows(rows)
    passport={
      "case_id":case_id,"data_class":"SYNTHETIC",
      "evidence_sha256":hashlib.sha256(evidence_content.encode()).hexdigest(),
      "source_module":{"lemon":"Lemon-ICFR-US/src/lemon_icfr/orchestrator.py",
                       "cam":"NAAIL-OpenLab/demos/cam-kam-agent-benchmark/benchmark.py"},
      "lemon_status":result.status,
      "lemon_gates":[asdict(g) for g in result.gates],
      "lemon_findings":[asdict(f) for f in result.findings],
      "synthetic_cam_scoring":cam_scores[0],
      "cam_score_is_validated_audit_quality":False,
      "independent_reviewer_executed":False,
      "human_approval_granted":False,
      "scientific_discovery_claim_allowed":False,
      "note":"The CAM benchmark uses synthetic text and contains no genuine auditor's report."
    }
    return passport

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-id",default="SYN-2024-00")
    parser.add_argument("--out",type=Path,default=Path("results/integrated_evidence_passport.json"))
    args=parser.parse_args()
    result=run_integrated_case(args.case_id)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(f"Created synthetic evidence passport: {args.out}")
    print(f"Lemon: {result['lemon_status']} | CAM prototype only | approval NOT granted")

if __name__=="__main__":
    main()
