#!/usr/bin/env python3
"""Evidence-governed audit research architecture benchmark (synthetic only).
A0 heuristic; A1 evidence checks; A2 Co-Scientist-style candidate comparison;
A3 AlphaEvolve-inspired, bounded validation search. NOT Bao RUSBoost.
Only Python standard library. No audit decisions or external model calls.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

FIELDS = ("case_id", "year", "revenue_growth", "accrual_ratio", "control_exception",
          "cam_present", "fraud_label", "evidence_id", "evidence_complete")
WEIGHTS = (
    (0.15, 0.38, 0.32, 0.15),
    (0.12, 0.30, 0.42, 0.18),
    (0.18, 0.46, 0.22, 0.14),
)
THRESHOLD = 0.42

def fixture():
    """Artificial panel: chronological 2018-2025, 10 observations/year."""
    data = []
    for i in range(80):
        yr, j = 2018 + i // 10, i % 10
        g = ((i * 17 + 7) % 37) / 36
        a = ((i * 11 + 3) % 31) / 30
        ctrl = int((i * 7) % 11 in (0, 1, 2))
        latent = 0.15 + 0.38*g + 0.32*a + 0.15*ctrl
        label = int(latent + (0.11 if i % 13 == 0 else -0.07 if i % 17 == 0 else 0) >= 0.51)
        cam = int(g + a + ctrl * 0.3 > 1.30 or i % 19 == 0)
        data.append({"case_id":f"SYN-{yr}-{j:02d}", "year":yr,
                     "revenue_growth":g, "accrual_ratio":a,
                     "control_exception":ctrl, "cam_present":cam,
                     "fraud_label":label, "evidence_id":f"SIM-{i:03d}",
                     "evidence_complete":int(i % 13 != 0)})
    return data

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not set(FIELDS).issubset(set(reader.fieldnames or [])):
            raise ValueError("Missing required schema columns: " +
                             ", ".join(sorted(set(FIELDS) - set(reader.fieldnames or []))))
        rows = []
        for r in reader:
            row = {"case_id":str(r["case_id"]), "evidence_id":str(r["evidence_id"])}
            if not row["case_id"] or not row["evidence_id"]:
                raise ValueError("case_id/evidence_id may not be empty")
            row["year"] = int(r["year"])
            for k in ("revenue_growth", "accrual_ratio"):
                row[k] = float(r[k])
                if not (0 <= row[k] <= 1 and math.isfinite(row[k])):
                    raise ValueError(f"{k} must be finite and 0..1")
            for k in ("control_exception", "cam_present", "fraud_label", "evidence_complete"):
                row[k] = int(r[k])
                if row[k] not in (0,1):
                    raise ValueError(f"{k} must be 0/1")
            rows.append(row)
    if len(set(r["case_id"] for r in rows)) != len(rows):
        raise ValueError("Duplicate case_id")
    return rows

def risk(row, weights):
    b, wg, wa, wc = weights
    return min(1.0, max(0.0, b + wg*row["revenue_growth"] +
                        wa*row["accrual_ratio"] + wc*row["control_exception"]))

def brier(rows, weights):
    if not rows:
        raise ValueError("Empty split")
    return sum((risk(r, weights) - r["fraud_label"])**2 for r in rows)/len(rows)

def rank_candidates(rows, weights):
    return sorted(weights, key=lambda w: (brier(rows, w), tuple(w)))

def evolve(train, validation, seed):
    """Bounded deterministic specification search; validation never uses test rows."""
    candidates = [seed]
    for idx in (1, 2):
        base = WEIGHTS[idx]
        candidates.append(base)
    for delta in (-0.08, -0.04, 0.04, 0.08):
        b, g, a, c = seed
        candidates.append((b, max(0,g+delta), max(0,a-delta), c))
    # Frozen scientific fitness: validation Brier + small complexity penalty.
    # Identical model size, so penalty is constant and omitted from argmin.
    return min(candidates, key=lambda w:(brier(validation,w), tuple(w))), len(candidates)

def evaluate(rows, weights, gate_evidence):
    scored = []
    for row in rows:
        p = risk(row, weights)
        evidence_ok = bool(row["evidence_complete"] and row["evidence_id"])
        # Gate does not silently change a statistical prediction:
        actionable = not gate_evidence or evidence_ok
        scored.append({"case_id":row["case_id"], "year":row["year"],
                       "risk_score":round(p,6), "fraud_label":row["fraud_label"],
                       "cam_present":row["cam_present"],
                       "high_risk_no_cam":bool(p >= THRESHOLD and not row["cam_present"]),
                       "evidence_id":row["evidence_id"], "evidence_ok":evidence_ok,
                       "actionable_for_review":actionable})
    sorted_rows = sorted(scored, key=lambda r:(-r["risk_score"],r["case_id"]))
    k = max(1,math.ceil(0.2*len(scored)))
    precision = sum(r["fraud_label"] for r in sorted_rows[:k])/k
    return {"n":len(scored),
            "brier":round(sum((r["risk_score"]-r["fraud_label"])**2 for r in scored)/len(scored),6),
            "precision_at_top_20pct":round(precision,6),
            "evidence_coverage":round(sum(r["evidence_ok"] for r in scored)/len(scored),6),
            "high_risk_no_cam_count":sum(r["high_risk_no_cam"] for r in scored),
            "reviewable_count":sum(r["actionable_for_review"] for r in scored),
            "sample_rows":scored[:5]}

def run(rows, source, input_digest):
    train=[r for r in rows if r["year"]<=2022]
    validation=[r for r in rows if r["year"]==2023]
    test=[r for r in rows if r["year"]>=2024]
    if not train or not validation or not test:
        raise ValueError("Requires chronological train <=2022, validation 2023, test >=2024")
    # A0 is an illustrative heuristic, NOT a reproduction of Bao et al. (2020).
    a0=WEIGHTS[0]
    # A2: explicit hypothesis tournament ranked ONLY on training observations.
    a2=rank_candidates(train,WEIGHTS)[0]
    # A3: bounded evolutionary search on validation; test untouched.
    a3,candidate_count=evolve(train,validation,a2)
    arms={}
    for label,w,gated in (("A0",a0,False),("A1",a0,True),("A2",a2,True),("A3",a3,True)):
        arms[label]={"weights":list(w),"test_metrics":evaluate(test,w,gated)}
    return {
      "study":"NAAIL Audit Scientific Discovery / Paper2Agent pilot",
      "source_type":source,"source_sha256":input_digest,
      "research_status":"SYNTHETIC_DEMONSTRATION" if source=="synthetic" else "UNVERIFIED_EXTERNAL_DATA",
      "not_bao_replication":True,"no_causal_claim":True,
      "scientific_discovery_claim_allowed":False,"audit_opinion_allowed":False,
      "human_approval_status":"REQUIRED_NOT_GRANTED",
      "splits":{"train_n":len(train),"validation_n":len(validation),"test_n":len(test),
                "train_max_year":max(r["year"] for r in train),
                "validation_year":2023,"test_min_year":min(r["year"] for r in test)},
      "co_scientist_hypothesis_tournament":[{"weights":list(w),"train_brier":round(brier(train,w),6)}
                                            for w in rank_candidates(train,WEIGHTS)],
      "alphaevolve_inspired_search":{"candidate_count":candidate_count,
        "selection_metric":"validation Brier (fixed before selection)",
        "test_sealed_until_selection":True},
      "comparators":{"A0":"illustrative baseline heuristic",
        "A1":"same predictor plus provenance/evidence review gate",
        "A2":"Co-Scientist-inspired candidate model tournament on training data",
        "A3":"bounded AlphaEvolve-inspired specification search on validation"},
      "arms":arms,
      "limitations":["Synthetic cases cannot establish fraud-detection validity.",
        "Review flags are research triage, never audit findings.",
        "Bao MATLAB implementation must be separately reproduced with rights-cleared inputs.",
        "No real LLM, MCP service, or independently verified external replication was run."]}

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument("--demo",action="store_true",help="Generate deterministic synthetic fixture")
    group.add_argument("--csv",type=Path,help="External CSV matching FIELDS; does not certify labels")
    p.add_argument("--out",type=Path,default=Path("results/pilot_results.json"))
    args=p.parse_args(argv)
    if args.demo:
        rows=fixture()
        raw=json.dumps(rows,sort_keys=True,separators=(",",":")).encode()
        source="synthetic"
    else:
        raw=args.csv.read_bytes()
        rows=read_csv(args.csv)
        source="external_requires_rights_validation"
    result=run(rows,source,hashlib.sha256(raw).hexdigest())
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"wrote {args.out} | status={result['research_status']} | human approval required")
    for name,arm in result["arms"].items():
        m=arm["test_metrics"]
        print(f"{name}: test_n={m['n']}, Brier={m['brier']:.4f}, precision@20%={m['precision_at_top_20pct']:.3f}, reviewable={m['reviewable_count']}")
    return result

if __name__=="__main__":
    main()
