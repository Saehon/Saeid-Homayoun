"""P13 — benchmark-gated improvement. Output is ACCEPT_DEVELOPMENT_ONLY or REJECT, never production.
Usage: python tools/improvement_gate.py baseline.json candidate.json --frozen-sha <sha> [--metric recall]"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def decide(base: dict, cand: dict, frozen_sha: str, metric: str = "recall", margin: float = 0.01,
           tolerance: float = 0.0) -> tuple[str, list[str]]:
    why = []
    for name, r in (("baseline", base), ("candidate", cand)):
        if r.get("benchmark_sha") != frozen_sha:
            why.append(f"{name} not run on the frozen benchmark")
        if not r.get("provenance_ok"):
            why.append(f"{name} provenance not verified")
        rh = r.get("replay_hashes", [])
        if len(rh) != 2 or rh[0] != rh[1]:
            why.append(f"{name} not reproducible (replay hashes differ/missing)")
    if cand.get("gate_regressions", 1) > 0:
        why.append("candidate weakens or breaks a gate")
    if cand.get("fn", 10**9) > base.get("fn", 0):
        why.append("candidate increases false negatives")
    if cand.get("fp", 10**9) > base.get("fp", 0) * 1.10 + 1:
        why.append("candidate increases false positives > 10%")
    bm, cm = base.get("metrics", {}), cand.get("metrics", {})
    if cm.get(metric, -1) - bm.get(metric, 0) < margin:
        why.append(f"no improvement ≥ {margin} on {metric}")
    for k, v in bm.items():
        if k != metric and cm.get(k, -1) < v - tolerance:
            why.append(f"{k} worsened")
    return ("REJECT", why) if why else ("ACCEPT_DEVELOPMENT_ONLY", ["all checks passed; still DEVELOPMENT_ONLY"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline")
    ap.add_argument("candidate")
    ap.add_argument("--frozen-sha", required=True)
    ap.add_argument("--metric", default="recall")
    a = ap.parse_args()
    d, why = decide(json.loads(Path(a.baseline).read_text()), json.loads(Path(a.candidate).read_text()),
                    a.frozen_sha, a.metric)
    print(d, *why, sep="\n- ")
    sys.exit(0)
