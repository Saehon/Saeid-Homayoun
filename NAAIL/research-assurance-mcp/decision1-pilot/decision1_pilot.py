#!/usr/bin/env python3
"""NAAIL Decision-1 ICFR pilot: synthetic-only, fail-closed, no automatic audit approval.

Run offline (no API/no charge): python decision1_pilot.py
Optional Vercel AI Gateway: python decision1_pilot.py --provider gateway --confirm-spend
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import statistics
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = "microsoft/microsoft-decision-1"
CLASSES = ("HIGH", "MODERATE", "LOW")
CRITERIA = {
    "HIGH": "Strong indications of control failure, override, or substantial ICFR exposure.",
    "MODERATE": "Control deviations or unresolved deficiencies requiring targeted testing.",
    "LOW": "Documented controls and no significant exceptions in the available synthetic facts.",
    "INSUFFICIENT": "The supplied facts do not support a credible risk triage.",
}
PROMPT = ("Classify the ICFR control-risk triage based ONLY on the supplied evidence. "
          "Do not infer material weakness or operating effectiveness. "
          "Select INSUFFICIENT if supporting evidence is absent or ambiguous.")
VERSION = "decision1-icfr-pilot/0.1.0"

class ContractError(ValueError):
    """Invalid evidence/model contract: never silently approve."""

def fixtures():
    cases = json.loads((HERE / "synthetic_icfr_cases.json").read_text(encoding="utf-8"))
    ids = [c.get("case_id") for c in cases]
    if len(ids) != len(set(ids)) or any(not c for c in ids):
        raise ContractError("Duplicate/missing case ID")
    for c in cases:
        if c.get("data_class") != "SYNTHETIC" or c.get("gold_label") not in CLASSES:
            raise ContractError("Only labelled SYNTHETIC cases permitted")
    return cases

def evidence_status(case):
    evidence = case.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return "MISSING_EVIDENCE"
    ids = [e.get("evidence_id") for e in evidence if isinstance(e, dict)]
    if len(set(ids)) != len(ids) or not all(ids):
        return "BAD_EVIDENCE_IDS"
    if any(not e.get("source_uri", "").startswith("synthetic://")
           or not e.get("fact", "").strip() for e in evidence):
        return "MISSING_PROVENANCE"
    if any(e.get("contradicts") is True for e in evidence):
        return "CONTRADICTORY_EVIDENCE"
    return "COMPLETE"

def candidate_state(case):
    """Never pass gold labels, assessor notes or private provenance to model."""
    return {
        "case_id": case["case_id"],
        "scope": "Synthetic internal-control risk triage for educational research, not an audit opinion.",
        "evidence": [{"id": e["evidence_id"], "fact": e["fact"]}
                     for e in case["evidence"]],
    }

def offline_baseline(state):
    """Uncalibrated, deterministic teaching baseline; NOT Microsoft-Decision-1."""
    blob = " ".join(e["fact"] for e in state["evidence"]).lower()
    red = sum(t in blob for t in ("override", "unreconciled", "unauthorized", "material error",
                                  "unrestricted", "untested privileged"))
    medium = sum(t in blob for t in ("exception", "late", "not documented",
                                     "incomplete", "manual", "untested"))
    if red >= 1:
        return "HIGH", None, None
    if medium >= 1:
        return "MODERATE", None, None
    return "LOW", None, None

def gateway_decision(state, *, timeout=30):
    """Opt-in Decisions API example. Schema/provider response must be validated."""
    key = os.environ.get("AI_GATEWAY_API_KEY")
    if not key:
        raise ContractError("AI_GATEWAY_API_KEY missing; no request made")
    body = {
        "model": MODEL,
        "input": json.dumps(state, sort_keys=True),
        "questions": [{
            "name": "risk", "type": "choice", "instructions": PROMPT,
            "choices": [{"value": k, "description": v} for k, v in CRITERIA.items()],
        }],
    }
    req = urllib.request.Request(
        "https://ai-gateway.vercel.sh/v1/decisions",
        data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.loads(response.read())
    except (urllib.error.URLError, ValueError) as exc:
        raise ContractError(f"Gateway failed, results unverified: {type(exc).__name__}") from exc
    answers = payload.get("answers", [])
    if not isinstance(answers, list):
        raise ContractError("Unexpected decision response schema")
    answer = next((a for a in answers if isinstance(a, dict)
                   and a.get("name") == "risk"), None)
    if not answer:
        raise ContractError("No risk answer; fail closed")
    selected = answer.get("choice", answer.get("value", answer.get("answer")))
    if isinstance(selected, dict):
        selected = selected.get("value")
    if selected not in CRITERIA:
        raise ContractError("Unsupported risk choice")
    # Probability schemas can vary; missing/invalid probabilities trigger review.
    raw = answer.get("probabilities")
    probs = None
    if isinstance(raw, dict):
        probs = raw
    elif isinstance(raw, list):
        probs = {x.get("value"): x.get("probability") for x in raw
                 if isinstance(x, dict)}
    if probs is not None:
        if set(probs) != set(CRITERIA):
            raise ContractError("Incomplete choice probabilities")
        if not all(isinstance(p, (int, float)) and not isinstance(p, bool)
                   and 0 <= p <= 1 for p in probs.values()):
            raise ContractError("Invalid probabilities")
        if abs(sum(probs.values()) - 1) > 0.02:
            raise ContractError("Probabilities not normalized")
        confidence = float(probs[selected])
    else:
        confidence = None
    return selected, confidence, probs

def assess(case, *, provider="offline", confirm_spend=False, threshold=0.85):
    if case.get("data_class") != "SYNTHETIC":
        raise ContractError("External/restricted/real cases prohibited in this pilot")
    status = evidence_status(case)
    request = None
    selected = "INSUFFICIENT"
    confidence, probs = None, None
    elapsed_ms = None
    if status == "COMPLETE":
        request = candidate_state(case)
        t0 = time.perf_counter()
        if provider == "offline":
            selected, confidence, probs = offline_baseline(request)
        elif provider == "gateway":
            if not confirm_spend:
                raise ContractError("--confirm-spend is required for paid gateway calls")
            selected, confidence, probs = gateway_decision(request)
        else:
            raise ContractError("Unknown provider")
        elapsed_ms = round(1000 * (time.perf_counter() - t0), 3)
    if status != "COMPLETE":
        queue = "EVIDENCE_GAP_REVIEW"
    elif selected == "INSUFFICIENT" or confidence is None or confidence < threshold:
        queue = "UNCERTAIN_HUMAN_REVIEW"
    else:
        queue = "PRIORITY_HUMAN_REVIEW" if selected == "HIGH" else "HUMAN_REVIEW"
    return {
        "case_id": case["case_id"], "provider": "OFFLINE_RULE_BASELINE" if provider == "offline" else MODEL,
        "version": VERSION, "model_prediction": selected, "confidence": confidence,
        "probabilities": probs, "gold_label": case.get("gold_label"),  # evaluation record ONLY
        "evidence_status": status, "evidence_ids": [e.get("evidence_id") for e in case.get("evidence", [])],
        "candidate_state_sha256": hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
            if request is not None else None,
        "prompt_sha256": hashlib.sha256(PROMPT.encode()).hexdigest(),
        "latency_ms": elapsed_ms, "review_queue": queue,
        "human_gate": "AWAITING_INDEPENDENT_HUMAN_APPROVAL",
        "approved": False, "production_action": None,
        "run_utc": datetime.now(timezone.utc).isoformat(), "data_class": "SYNTHETIC",
    }

def summarize(records):
    eligible = [r for r in records if r["model_prediction"] in CLASSES]
    n = len(eligible)
    accuracy = (sum(r["model_prediction"] == r["gold_label"] for r in eligible) / n) if n else None
    f1s = []
    for label in CLASSES:
        tp = sum(r["model_prediction"] == label and r["gold_label"] == label for r in eligible)
        fp = sum(r["model_prediction"] == label and r["gold_label"] != label for r in eligible)
        fn = sum(r["model_prediction"] != label and r["gold_label"] == label for r in eligible)
        f1s.append(2*tp/(2*tp+fp+fn) if (2*tp+fp+fn) else 0.0)
    high_brier = [
        (r["probabilities"]["HIGH"]-int(r["gold_label"] == "HIGH"))**2
        for r in eligible if r["probabilities"] is not None
    ]
    latencies = [r["latency_ms"] for r in records if r["latency_ms"] is not None]
    return {
        "cases": len(records), "classifiable": n, "accuracy_on_classifiable": accuracy,
        "macro_f1_on_classifiable": statistics.mean(f1s) if n else None,
        "high_risk_brier_if_calibrated": statistics.mean(high_brier) if high_brier else None,
        "median_latency_ms": statistics.median(latencies) if latencies else None,
        "evidence_gap_cases": sum(r["evidence_status"] != "COMPLETE" for r in records),
        "human_approval_count": sum(r["approved"] for r in records),
        "NOTE": "Synthetic only; offline baseline is not Microsoft-Decision-1; no empirical superiority claim.",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["offline", "gateway"], default="offline")
    parser.add_argument("--confirm-spend", action="store_true")
    parser.add_argument("--output", type=Path, help="Write local JSON result file")
    args = parser.parse_args()
    cases = fixtures()
    results = [assess(case, provider=args.provider, confirm_spend=args.confirm_spend)
               for case in cases]
    payload = {"summary": summarize(results), "records": results}
    if args.output:
        args.output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))

if __name__ == "__main__":
    main()
