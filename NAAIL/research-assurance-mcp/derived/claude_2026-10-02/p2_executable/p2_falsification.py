#!/usr/bin/env python3
"""Falsification suite for p2_adversarial_v2_executable.py (DERIVED, stdlib only).
A 19/19 score from a self-designed benchmark is weak evidence. This script tries to break it:
  F1 false-positive robustness: 30 independently seeded clean packages must yield zero findings.
  F2 evasion probes: realistic variants of real errors that the current detector is EXPECTED to miss.
     A probe that is caught is reported too; probes document detector boundaries, they are not failures.
  F3 determinism: two full benchmark runs must agree on detected taxonomy IDs per fixture.
Usage: python3 p2_falsification.py <path to NAAIL/research-assurance-mcp> [out.json]
"""
import json, sys, copy, subprocess, hashlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import p2_adversarial_v2_executable as B

res = {}
# F1 -------------------------------------------------------------------------------------------
fp_runs, skipped = [], 0
for s in range(1, 200):
    if len(fp_runs) == 30: break
    try: pkg = B.build_clean(seed=s)
    except AssertionError: skipped += 1; continue          # design requires insignificant z; skip, count it
    f = B.detect(pkg)
    fp_runs.append({"seed": s, "findings": sorted({x["taxonomy_id"] for x in f})})
fp = [r for r in fp_runs if r["findings"]]
res["F1_clean_seed_false_positives"] = {"clean_packages": len(fp_runs), "seeds_skipped_by_design_assert": skipped,
                                        "packages_with_findings": len(fp), "examples": fp[:5]}

# F2 -------------------------------------------------------------------------------------------
def probe(name, tid, fn):
    p = copy.deepcopy(B.build_clean()); fn(p)
    got = sorted({x["taxonomy_id"] for x in B.detect(p)})
    return {"probe": name, "target_id": tid, "detected_ids": got, "caught": tid in got}
P = [
 probe("RPT-01 alteration inside rounding precision (+0.0004)", "RPT-01",
       lambda p: p["table"]["T2"].__setitem__("coef_x", p["table"]["T2"]["coef_x"] + 0.0004)),
 probe("RPT-01 on a cell the check does not cover (n)", "RPT-01",
       lambda p: p["table"]["T2"].__setitem__("n", p["table"]["T2"]["n"] + 1)),
 probe("RPT-03 paraphrase without the phrase 'statistically significant'", "RPT-03",
       lambda p: p["manuscript"]["claims"][1].__setitem__("text", "z has a meaningful, reliable effect (p<.05).")),
 probe("INT-01 causal claim using an unlisted verb ('increases')", "INT-01",
       lambda p: p["manuscript"]["claims"][0].__setitem__("text", "Raising x increases y.")),
 probe("DAT-04 scaling applied consistently to data AND dictionary factor", "DAT-04",
       lambda p: (p["dictionary"]["assets_musd"].__setitem__("factor", 1.0), p.__setitem__("analytic", B.derive_analytic(p)))),
 probe("DAT-03 look-ahead with availability metadata also falsified", "DAT-03",
       lambda p: B.m_DAT03(p) or [r.__setitem__("x_available_period", r["decision_period"]) for r in p["panel"]]),
 probe("IDN-04 leakage without declaring the target in feature recipe", "IDN-04",
       lambda p: ([r.__setitem__("x", 0.7 * r["x"] + 0.3 * r["y"]) for r in p["panel"]], B.regenerate(p))),
 probe("REP-05 hidden state that is declared as an input", "REP-05",
       lambda p: (B.m_REP05(p), p.__setitem__("declared_inputs", ["ENV:WINSOR"]))),
 probe("SPC-01 control removed from BOTH code and manuscript", "SPC-01",
       lambda p: (p["spec"].__setitem__("controls", []), p["manuscript"]["declared_spec"].__setitem__("controls", []), B.regenerate(p))),
]
res["F2_evasion_probes"] = {"probes": P, "caught": sum(x["caught"] for x in P), "missed": sum(not x["caught"] for x in P)}

# F3 -------------------------------------------------------------------------------------------
mcp = sys.argv[1]; here = Path(__file__).parent; ids = []
for k in (1, 2):
    o = here / f"_det_run{k}.json"
    subprocess.run([sys.executable, str(here / "p2_adversarial_v2_executable.py"), mcp, str(o)], capture_output=True)
    ids.append({c["id"]: c["detected_ids"] for c in json.loads(o.read_text())["cases"]}); o.unlink()
res["F3_determinism_detected_ids_identical"] = ids[0] == ids[1]

print(json.dumps(res, indent=2))
if len(sys.argv) > 2: Path(sys.argv[2]).write_text(json.dumps(res, indent=2) + "\n")
sys.exit(0 if (not fp and res["F3_determinism_detected_ids_identical"]) else 1)
