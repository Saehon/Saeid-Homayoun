"""Deterministic gate benchmark against a deliberately weak allow-all comparator.
This DOES NOT evaluate an LLM or represent independent blind labels."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from portfolio_roles.google_finance_eval.demo import score_case
PASS_KEY = "pass"
PASS_VALUE = True
SOURCE = "score_case"

def run_gate(example):
    try:
        decision = score_case(example)
        return {"blocked": decision.get(PASS_KEY) != PASS_VALUE, "decision": decision, "error": None}
    except Exception as exc:
        return {"blocked": None, "decision": None, "error": type(exc).__name__}

def metrics(expected, predicted):
    tp = sum(a and b for a, b in zip(expected, predicted))
    tn = sum(not a and not b for a, b in zip(expected, predicted))
    fp = sum(not a and b for a, b in zip(expected, predicted))
    fn = sum(a and not b for a, b in zip(expected, predicted))
    n = len(expected)
    precision = tp / (tp + fp) if tp + fp else 0.
    recall = tp / (tp + fn) if tp + fn else 0.
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.
    p = (tp + tn) / n if n else 0.
    if n:
        z = 1.96
        center = (p + z*z/(2*n)) / (1 + z*z/n)
        half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
        wilson = [round(max(0., center-half), 4), round(min(1., center+half), 4)]
    else:
        wilson = [None, None]
    return {"n": n, "tp_blocked": tp, "tn_ready": tn, "fp_blocked": fp, "fn_ready": fn,
            "accuracy": round(p, 4), "precision_blocked": round(precision, 4),
            "recall_blocked": round(recall, 4), "f1_blocked": round(f1, 4),
            "accuracy_wilson_95pct": wilson}

def evaluate(rows):
    ids = [r.get("id") for r in rows]
    if len(ids) != len(set(ids)) or not all(ids):
        raise ValueError("Missing or duplicate benchmark case ID")
    if not rows or not all(type(r.get("expected_blocked")) is bool for r in rows):
        raise ValueError("Benchmark labels must be nonempty and boolean")
    results = [run_gate(r["input"]) for r in rows]
    if any(r["error"] is not None for r in results):
        raise RuntimeError("Evaluation exceptions; do not report inflated accuracy")
    expected = [r["expected_blocked"] for r in rows]
    predicted = [r["blocked"] for r in results]
    records = [{"id": row["id"], "category": row["category"],
                "expected_blocked": row["expected_blocked"], "actual_blocked": result["blocked"],
                "correct": row["expected_blocked"] == result["blocked"],
                "error_modes": result["decision"].get("failure_modes") or result["decision"].get("failures")
                    or result["decision"].get("gaps") or result["decision"].get("outstanding")
                    or result["decision"].get("errors") or result["decision"].get("issues")
                    or result["decision"].get("blockers") or []}
               for row, result in zip(rows, results)]
    payload = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"evaluation_type": "synthetic_rule_consistency_not_model_evaluation",
            "label_provenance": "handwritten to match anticipated deterministic contracts; not blinded",
            "dataset_sha256": hashlib.sha256(payload).hexdigest(),
            "candidate": SOURCE, "candidate_metrics": metrics(expected, predicted),
            "weak_baseline": "always_ready", "baseline_metrics": metrics(expected, [False]*len(rows)),
            "records": records,
            "limitations": ["Synthetic fixtures; no external validity.",
                "Labels constructed against specification; test scores cannot measure predictive ability.",
                "No LLM calls, production controls, blinded annotators, or independent reviewers.",
                "Do not cite metrics as model quality, compliance, or hiring readiness."]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default=str(Path(__file__).parent / "fixtures" / "cases.json"))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    rows = json.loads(Path(args.cases).read_text(encoding="utf-8"))
    report = json.dumps(evaluate(rows), indent=2, ensure_ascii=False)
    if args.out:
        path = Path(args.out); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report + "\n", encoding="utf-8")
    else:
        print(report)

if __name__ == "__main__":
    main()
