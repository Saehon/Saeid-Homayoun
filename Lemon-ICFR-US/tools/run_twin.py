"""P08 — Digital Twin scenarios. Assumptions are analyst-declared and printed with every result.
Usage: python tools/run_twin.py organized/poc/msft/twin_assumptions.json"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from _common import ROOT, dump_json
from lemon_icfr.assurance.twin import TwinControl, TwinModel, TwinRisk, run_scenario

TEMPLATE = {
    "_note": "ANALYST ASSUMPTIONS — illustrative, not estimated from data. Edit and justify each value.",
    "risks": [{"risk_id": "R-ENTITY", "assertion": "entity_level_icfr", "inherent": 0.5}],
    "controls": [{"control_id": "K-MONITOR", "covers": ["R-ENTITY"], "evidence_reliability": 0.8},
                 {"control_id": "K-KEY", "covers": ["R-ENTITY"], "evidence_reliability": 0.7,
                  "depends_on": ["K-MONITOR"], "capacity": 10000}],
    "population": 1000,
    "scenarios": [["control_failure", "K-KEY"], ["evidence_removal", "K-KEY"], ["override_increase", 0.3],
                  ["population_growth", 40000], ["sod_removal", "K-KEY"], ["reliability_change", "K-KEY", 0.2],
                  ["competing_explanation", "R-ENTITY", 0.9], ["key_control_dependency_failure", "K-MONITOR"]]}


def run(path: Path) -> list[dict]:
    a = json.loads(path.read_text())
    m = TwinModel(tuple(TwinRisk(**r) for r in a["risks"]),
                  tuple(TwinControl(**{**c, "covers": tuple(c["covers"]), "depends_on": tuple(c.get("depends_on", ()))})
                        for c in a["controls"]), population=a.get("population", 1000))
    rows = []
    for name, *args in a["scenarios"]:
        r = run_scenario(m, name, *args)
        rows.append({"scenario": name, "args": args, "baseline": r.baseline, "result": r.result, "delta": r.delta,
                     "interpretation": r.interpretation, "evidence_type": r.evidence_type})
    dump_json({"assumptions": a, "results": rows}, path.parent / "twin_results.json")
    return rows


if __name__ == "__main__":
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "organized" / "poc" / "msft" / "twin_assumptions.json"
    if not p.exists():
        dump_json(TEMPLATE, p)
        print(f"wrote assumption template {p}")
    for r in run(p):
        print(f"{r['scenario']:32s} Δ={r['delta']}  [{r['evidence_type']}]")
