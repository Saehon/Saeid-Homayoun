#!/usr/bin/env python3
"""P2 Adversarial Benchmark V2 — EXECUTABLE layer (DERIVED, stdlib only, deterministic).

Usage: python3 p2_adversarial_v2_executable.py <path to NAAIL/research-assurance-mcp> [out.json]

* Reads the ORIGINAL 19 fixtures from benchmark/adversarial_benchmark_v2.json (unchanged).
* GENERATOR: builds one synthetic, internally consistent research package (data -> code -> output ->
  table -> manuscript) and applies each fixture's mutation deterministically.
* DETECTOR: blind. It receives only the package (no fixture id, no gold) and checks invariants
  between artifacts, re-executing code where needed. It never compares against a gold copy.
* SCORING: the benchmark's own contract (exact taxonomy IDs; family level; expected-outcome rule).
LIMITATION: generator and detector were written by the same author, so this measures implementation
correctness against designed fixtures, not real-world detection ability. All data are synthetic.
"""
import json, sys, math, random, copy, hashlib
from pathlib import Path

# ---------------------------------------------------------------- estimation (within-FE OLS, 2 regressors)
def _inv2(a, b, c, d):
    det = a * d - b * c
    return (d / det, -b / det, -c / det, a / det)

def estimate(rows, spec, env=None):
    env = env or {}
    rows = [dict(r) for r in rows]
    if "ENV:WINSOR" in spec.get("reads", []):                    # hidden external state (REP-05)
        lvl = float(env.get("WINSOR", "inf"))
        for r in rows: r["y"] = max(-lvl, min(lvl, r["y"]))
    regs = ["x"] + spec["controls"]
    while len(regs) < 2: regs.append(None)
    def col(r, k): return 0.0 if k is None else r[k]
    keys = ["y"] + [k for k in regs if k]
    if "firm" in spec["fixed_effects"]:                           # within transformation
        means = {}
        for r in rows:
            m = means.setdefault(r["firm"], {k: [0.0, 0] for k in keys})
            for k in keys: m[k][0] += r[k]; m[k][1] += 1
        X = [[r[k] - means[r["firm"]][k][0] / means[r["firm"]][k][1] if k else 0.0 for k in regs] for r in rows]
        Y = [r["y"] - means[r["firm"]]["y"][0] / means[r["firm"]]["y"][1] for r in rows]
    else:                                                          # pooled with intercept (demean overall)
        mu = {k: sum(r[k] for r in rows) / len(rows) for k in keys}
        X = [[r[k] - mu[k] if k else 0.0 for k in regs] for r in rows]
        Y = [r["y"] - mu["y"] for r in rows]
    if regs[1] is None: X = [[x[0], 0.0] for x in X]
    sxx = [[sum(x[i] * x[j] for x in X) for j in range(2)] for i in range(2)]
    if regs[1] is None: sxx[1][1] = 1.0
    inv = _inv2(sxx[0][0], sxx[0][1], sxx[1][0], sxx[1][1])
    sxy = [sum(x[i] * y for x, y in zip(X, Y)) for i in range(2)]
    b = [inv[0] * sxy[0] + inv[1] * sxy[1], inv[2] * sxy[0] + inv[3] * sxy[1]]
    u = [y - b[0] * x[0] - b[1] * x[1] for x, y in zip(X, Y)]
    if spec["cluster"] == "firm":
        meat = [[0.0, 0.0], [0.0, 0.0]]; g = {}
        for r, x, e in zip(rows, X, u):
            s = g.setdefault(r["firm"], [0.0, 0.0]); s[0] += x[0] * e; s[1] += x[1] * e
        for s in g.values():
            for i in range(2):
                for j in range(2): meat[i][j] += s[i] * s[j]
        A = [[inv[0], inv[1]], [inv[2], inv[3]]]
        V = [[sum(A[i][k] * meat[k][l] * A[l][j] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
    else:
        s2 = sum(e * e for e in u) / (len(u) - 2)
        V = [[s2 * inv[0], s2 * inv[1]], [s2 * inv[2], s2 * inv[3]]]
    out = {"n": len(rows)}
    for i, k in enumerate(regs):
        if k is None: continue
        se = math.sqrt(V[i][i]); t = b[i] / se
        out[f"coef_{k}"], out[f"se_{k}"] = b[i], se
        out[f"p_{k}"] = 2 * (1 - 0.5 * (1 + math.erf(abs(t) / math.sqrt(2))))
    if spec.get("bootstrap_reps"):                                   # stochastic step (REP-03)
        rng = random.Random(spec["seed"]) if spec.get("seed") is not None else random.Random()
        firms = sorted({r["firm"] for r in rows}); draws = []
        for _ in range(spec["bootstrap_reps"]):
            pick = [rng.choice(firms) for _ in firms]
            br = [dict(r, firm=f"{f}#{i}") for i, f in enumerate(pick) for r in rows if r["firm"] == f]
            sub = dict(spec, bootstrap_reps=0)
            draws.append(estimate(br, sub, env)["coef_x"])
        m = sum(draws) / len(draws)
        out["boot_se_x"] = math.sqrt(sum((d - m) ** 2 for d in draws) / (len(draws) - 1))
    return out

def spec_hash(spec):
    keep = {k: spec[k] for k in ("controls", "fixed_effects", "cluster")}
    return hashlib.sha256(json.dumps(keep, sort_keys=True).encode()).hexdigest()[:12]

# ---------------------------------------------------------------- clean package
def build_clean(seed=20261002):
    rng = random.Random(seed)
    panel, attrs = [], []
    for f in range(40):
        fe = rng.gauss(0, 2)
        attrs.append({"firm": f"F{f:02d}", "industry": f % 4, "assets_kusd": round(rng.uniform(5e4, 5e6), 1)})
        for t in range(6):
            x = 0.6 * fe + rng.gauss(0, 1); z = rng.gauss(0, 1)
            y = 0.5 * x + fe + rng.gauss(0, 1)
            panel.append({"firm": f"F{f:02d}", "period": t, "x": x, "z": z, "y": y,
                          "x_available_period": t, "decision_period": t})
    spec = {"controls": ["z"], "fixed_effects": ["firm"], "cluster": "firm", "reads": [],
            "bootstrap_reps": 20, "seed": 7}
    pkg = {"files": ["data/panel.csv", "data/firm_attrs.csv", "code/estimate.py", "out/out_main.json",
                     "env/lock.json", "manuscript.md"],
           "manifest_required": ["data/panel.csv", "data/firm_attrs.csv", "code/estimate.py", "env/lock.json"],
           "panel": panel, "firm_attrs": attrs, "merge_key": "firm",
           "dictionary": {"assets_musd": {"source": "assets_kusd", "factor": 0.001}},
           "spec": spec, "declared_inputs": [],
           "features": {"x": {"inputs": [{"var": "x", "offset": 0}]}}, "target": "y",
           "env_lock": {"python": "3.12", "statlib": "1.4.2"}, "env_runtime": {"python": "3.12", "statlib": "1.4.2"}}
    pkg["analytic"] = derive_analytic(pkg)
    pkg["outputs"] = {"out_main": dict(estimate(pkg["analytic"], spec), spec_hash=spec_hash(spec))}
    o = pkg["outputs"]["out_main"]
    assert o["p_z"] > 0.10, "clean-package design requires an insignificant control z"
    pkg["table"] = {"T2": {"lineage": "out_main", "coef_x": round(o["coef_x"], 3), "se_x": round(o["se_x"], 3),
                           "coef_z": round(o["coef_z"], 3), "p_z": round(o["p_z"], 3), "n": o["n"]}}
    pkg["manuscript"] = {"design": "observational",
                         "declared_spec": {"controls": ["z"], "fixed_effects": ["firm"], "cluster": "firm"},
                         "declared_n": o["n"],
                         "claims": [{"id": "C1", "text": "x is positively associated with y.", "cites": ["coef_x"]},
                                    {"id": "C2", "text": "z is not statistically significant.", "cites": ["p_z"]}]}
    return pkg

def derive_analytic(pkg):
    by = {}
    for a in pkg["firm_attrs"]: by.setdefault(a[pkg["merge_key"]], []).append(a)
    f = pkg["dictionary"]["assets_musd"]["factor"]
    return [dict(r, assets_musd=a["assets_kusd"] * f) for r in pkg["panel"] for a in by.get(r["firm"], [])]

def regenerate(pkg, update_table=True, update_n=True):
    """Downstream regeneration after an upstream mutation (code -> output -> table)."""
    pkg["analytic"] = derive_analytic(pkg) if "analytic_override" not in pkg else pkg.pop("analytic_override")
    pkg["outputs"]["out_main"] = dict(estimate(pkg["analytic"], pkg["spec"]), spec_hash=spec_hash(pkg["spec"]))
    o = pkg["outputs"]["out_main"]
    if update_table:
        pkg["table"]["T2"].update(coef_x=round(o["coef_x"], 3), se_x=round(o["se_x"], 3), coef_z=round(o["coef_z"], 3) if "coef_z" in o else None,
                                  p_z=round(o["p_z"], 3) if "p_z" in o else None, n=o["n"])
    if update_n: pkg["manuscript"]["declared_n"] = o["n"]
    return pkg

# ---------------------------------------------------------------- generator: one deterministic mutation per taxonomy id
def m_RPT01(p): p["table"]["T2"]["coef_x"] = round(p["table"]["T2"]["coef_x"] + 0.05, 3)
def m_RPT03(p): p["manuscript"]["claims"][1]["text"] = "z is statistically significant at the 5% level."
def m_RPT04(p): p["manuscript"]["claims"].append({"id": "C3", "text": "The model predicts y with 95% out-of-sample accuracy.", "cites": ["oos_accuracy"]})
def m_SPC01(p): p["spec"]["fixed_effects"] = []; regenerate(p)
def m_SPC04(p): p["spec"]["cluster"] = None; regenerate(p)
def m_DAT02(p, declared_unchanged=False):
    p["firm_attrs"].append(dict(p["firm_attrs"][3])); regenerate(p, update_n=not declared_unchanged)
def m_DAT03(p):
    nxt = {(r["firm"], r["period"]): r["x"] for r in p["panel"]}
    for r in p["panel"]:
        if (r["firm"], r["period"] + 1) in nxt: r["x"], r["x_available_period"] = nxt[(r["firm"], r["period"] + 1)], r["period"] + 1
    regenerate(p)
def m_DAT04(p):
    a = derive_analytic(p); a[0]["assets_musd"] *= 1000; p["analytic_override"] = a; regenerate(p)
def m_IDN04(p):
    p["features"]["x"]["inputs"].append({"var": "y", "offset": 0})
    for r in p["panel"]: r["x"] = 0.7 * r["x"] + 0.3 * r["y"]
    regenerate(p)
def m_INT01(p): p["manuscript"]["claims"][0]["text"] = "Increasing x causes y to rise."
def m_REP01(p): p["files"].remove("data/firm_attrs.csv")
def m_REP02(p): p["env_runtime"]["statlib"] = "2.0.0"
def m_REP03(p): p["spec"]["seed"] = None
def m_REP04(p):
    alt = dict(p["spec"], controls=[]); p["outputs"]["out_alt"] = dict(estimate(p["analytic"], alt), spec_hash=spec_hash(alt))
    o = p["outputs"]["out_alt"]; p["table"]["T2"].update(lineage="out_alt", coef_x=round(o["coef_x"], 3), se_x=round(o["se_x"], 3))
def m_REP05(p): p["spec"]["reads"] = ["ENV:WINSOR"]; p["env_runtime"]["WINSOR"] = "1.5"

def m_CMP002(p):  # omit FE in code, keep table pointing at the stale pre-change output, then alter one coefficient
    p["outputs"]["out_prev"] = copy.deepcopy(p["outputs"]["out_main"])
    p["spec"]["fixed_effects"] = []; regenerate(p, update_table=False)
    p["table"]["T2"]["lineage"] = "out_prev"; m_RPT01(p)

GEN = {"ADV-CTRL-001": lambda p: None, "ADV-RPT-001": m_RPT01, "ADV-RPT-002": m_RPT03, "ADV-SPC-001": m_SPC01,
       "ADV-SPC-002": m_SPC04, "ADV-DAT-001": m_DAT02, "ADV-DAT-002": m_DAT03, "ADV-DAT-003": m_DAT04,
       "ADV-IDN-001": m_IDN04, "ADV-INT-001": m_INT01, "ADV-REP-001": m_REP01, "ADV-REP-002": m_REP02,
       "ADV-REP-003": m_REP03, "ADV-REP-004": m_REP04, "ADV-REP-005": m_REP05,
       "ADV-CMP-001": lambda p: (m_DAT03(p), m_IDN04(p), m_RPT04(p)),
       "ADV-CMP-002": m_CMP002,
       "ADV-BLD-001": lambda p: (m_REP02(p), m_REP05(p)),
       "ADV-BLD-002": lambda p: m_DAT02(p, declared_unchanged=True)}

# ---------------------------------------------------------------- blind detector (package only)
CAUSAL = ("causes", "leads to", "effect of", "drives", "results in")
def detect(pkg):
    F = []
    def add(tid, state, ev): F.append({"taxonomy_id": tid, "assurance_state": state, "evidence": ev,
                                       "human_review_required": state == "HUMAN_REVIEW"})
    files = set(pkg["files"]); tbl = pkg["table"]["T2"]; ms = pkg["manuscript"]
    miss = [f for f in pkg["manifest_required"] if f not in files]
    if miss: add("REP-01", "FLAGGED", {"missing": miss})
    drift = {k: (v, pkg["env_runtime"].get(k)) for k, v in pkg["env_lock"].items() if pkg["env_runtime"].get(k) != v}
    if drift: add("REP-02", "PARTIAL", {"lock_vs_runtime": drift})
    undeclared = [r for r in pkg["spec"].get("reads", []) if r not in pkg["declared_inputs"]]
    if undeclared:
        a = estimate(pkg["analytic"], pkg["spec"], {}); b = estimate(pkg["analytic"], pkg["spec"], pkg["env_runtime"])
        add("REP-05", "HUMAN_REVIEW", {"undeclared_reads": undeclared, "output_changes_with_env": abs(a["coef_x"] - b["coef_x"]) > 1e-12})
    if pkg["spec"].get("bootstrap_reps"):
        r1 = estimate(pkg["analytic"], pkg["spec"]); r2 = estimate(pkg["analytic"], pkg["spec"])
        if abs(r1["boot_se_x"] - r2["boot_se_x"]) > 1e-12: add("REP-03", "PARTIAL", {"rerun_boot_se": [r1["boot_se_x"], r2["boot_se_x"]]})
    src = pkg["outputs"].get(tbl["lineage"])
    if src is None: add("REP-04", "FLAGGED", {"lineage_missing": tbl["lineage"]})
    else:
        if src["spec_hash"] != spec_hash(pkg["spec"]): add("REP-04", "FLAGGED", {"lineage_spec_hash": src["spec_hash"], "current_spec_hash": spec_hash(pkg["spec"])})
        bad = {k: (tbl[k], round(src[k], 3)) for k in ("coef_x", "se_x", "coef_z") if tbl.get(k) is not None and k in src and tbl[k] != round(src[k], 3)}
        if bad: add("RPT-01", "FLAGGED", {"table_vs_lineage_output": bad})
    d = ms["declared_spec"]; s = pkg["spec"]
    om = [x for x in d["fixed_effects"] + d["controls"] if x not in s["fixed_effects"] + s["controls"]]
    if om: add("SPC-01", "FLAGGED", {"declared_not_in_code": om})
    if d["cluster"] != s["cluster"]: add("SPC-04", "FLAGGED", {"manuscript": d["cluster"], "code": s["cluster"]})
    keys = [a[pkg["merge_key"]] for a in pkg["firm_attrs"]]
    if len(keys) != len(set(keys)) or len(pkg["analytic"]) != len(pkg["panel"]):
        add("DAT-02", "FLAGGED", {"dup_keys": len(keys) - len(set(keys)), "left_rows": len(pkg["panel"]), "merged_rows": len(pkg["analytic"])})
    executed_n = estimate(pkg["analytic"], dict(s, bootstrap_reps=0), pkg["env_runtime"] if not undeclared else {})["n"]
    if ms["declared_n"] != executed_n: add("SPC-03", "FLAGGED", {"declared_n": ms["declared_n"], "executed_n": executed_n})
    late = sum(1 for r in pkg["panel"] if r["x_available_period"] > r["decision_period"])
    if late: add("DAT-03", "FLAGGED", {"rows_with_predictor_after_decision": late})
    leak = [i for i in pkg["features"]["x"]["inputs"] if i["var"] == pkg["target"] and i["offset"] >= 0]
    if leak: add("IDN-04", "HUMAN_REVIEW", {"target_inputs_to_feature": leak})
    raw = {a["firm"]: a["assets_kusd"] for a in pkg["firm_attrs"]}; fct = pkg["dictionary"]["assets_musd"]["factor"]
    sc = sum(1 for r in pkg["analytic"] if abs(r["assets_musd"] - raw[r["firm"]] * fct) > 1e-6)
    if sc: add("DAT-04", "FLAGGED", {"rows_inconsistent_with_dictionary_factor": sc})
    available = set(tbl) | {k for o in pkg["outputs"].values() for k in o}
    for c in ms["claims"]:
        t = c["text"].lower()
        if any(w in t for w in CAUSAL) and ms["design"] == "observational":
            add("INT-01", "HUMAN_REVIEW", {"claim": c["id"]})
        if "statistically significant" in t and "not statistically significant" not in t:
            ps = [tbl.get(k) for k in c["cites"] if k.startswith("p_")]
            if ps and all(p is not None and p >= 0.10 for p in ps): add("RPT-03", "HUMAN_REVIEW", {"claim": c["id"], "cited_p": ps})
        unsupported = [k for k in c["cites"] if k not in available]
        if unsupported: add("RPT-04", "HUMAN_REVIEW", {"claim": c["id"], "cites_absent_metric": unsupported})
    return F

# ---------------------------------------------------------------- scoring per benchmark contract
def outcome_ok(expected, exp_ids, found):
    ids = {f["taxonomy_id"] for f in found}; states = {f["taxonomy_id"]: f["assurance_state"] for f in found}
    hr = any(f["human_review_required"] for f in found)
    if expected == "NO_FLAG": return not found
    if expected == "FLAG": return all(states.get(i) == "FLAGGED" for i in exp_ids)
    if expected == "FLAG_OR_HUMAN_REVIEW": return all(states.get(i) in ("FLAGGED", "HUMAN_REVIEW") for i in exp_ids)
    if expected == "FLAG_OR_PARTIAL": return all(states.get(i) in ("FLAGGED", "PARTIAL") for i in exp_ids)
    if expected == "HUMAN_REVIEW": return all(states.get(i) == "HUMAN_REVIEW" for i in exp_ids)
    if expected == "MULTI_FLAG": return set(exp_ids) <= ids
    if expected == "MULTI_FLAG_AND_HUMAN_REVIEW": return set(exp_ids) <= ids and hr
    if expected == "DETECT_AT_LEAST_ONE_AND_ESCALATE": return bool(set(exp_ids) & ids) and hr
    if expected == "DETECT_AND_TRACE_SAMPLE_CHANGE": return set(exp_ids) <= ids
    raise ValueError(expected)

def main():
    mcp = Path(sys.argv[1]); out_path = sys.argv[2] if len(sys.argv) > 2 else None
    raw = (mcp / "benchmark/adversarial_benchmark_v2.json").read_bytes(); bench = json.loads(raw)
    clean = build_clean(); rows = []; TP = FP = FN = 0; fam = [0, 0, 0]
    for case in bench["cases"]:
        pkg = copy.deepcopy(clean); GEN[case["id"]](pkg)
        found = detect(pkg)                                   # blind: package only
        exp = set(case["taxonomy_ids"]); got = {f["taxonomy_id"] for f in found}
        tp, fp, fn = len(exp & got), len(got - exp), len(exp - got); TP += tp; FP += fp; FN += fn
        ef, gf = {i[:3] for i in exp}, {i[:3] for i in got}
        fam[0] += len(ef & gf); fam[1] += len(gf - ef); fam[2] += len(ef - gf)
        ok = outcome_ok(case["expected"], case["taxonomy_ids"], found)
        rows.append(dict(id=case["id"], kind=case["kind"], expected=case["expected"], expected_ids=sorted(exp),
                         detected_ids=sorted(got), false_positive_ids=sorted(got - exp), missed_ids=sorted(exp - got),
                         outcome_rule_met=ok, findings=found))
        print(f"{case['id']:13s} {case['kind']:13s} exp={sorted(exp)!s:32s} got={sorted(got)!s:32s} rule={'MET' if ok else 'NOT MET'}")
    pr = lambda t, f: t / (t + f) if t + f else 1.0
    P, R = pr(TP, FP), pr(TP, FN); F1 = 2 * P * R / (P + R) if P + R else 0.0
    fP, fR = pr(fam[0], fam[1]), pr(fam[0], fam[2])
    summary = dict(fixtures=len(rows), executable_fixtures=len(rows), outcome_rule_met=sum(r["outcome_rule_met"] for r in rows),
                   exact_id=dict(tp=TP, fp=FP, fn=FN, precision=P, recall=R, f1=F1),
                   family=dict(tp=fam[0], fp=fam[1], fn=fam[2], precision=fP, recall=fR),
                   clean_control_false_positives=len(rows[0]["detected_ids"]) if rows[0]["kind"] == "clean_control" else None)
    print(json.dumps(summary, indent=2))
    res = dict(benchmark_source="benchmark/adversarial_benchmark_v2.json", benchmark_sha256=hashlib.sha256(raw).hexdigest(),
               python=sys.version.split()[0], synthetic=True, summary=summary, cases=rows,
               limitations=["Generator and detector share one author: measures implementation correctness on designed fixtures, not real-world detection.",
                            "'Blinded' fixtures are blind to the detector input only; the designer knew the mutations.",
                            "All data are synthetic; no author data or published results are used.",
                            "Judgment-dependent findings are escalated to HUMAN_REVIEW; escalation is not a validity judgment."])
    if out_path: Path(out_path).write_text(json.dumps(res, indent=2, default=float) + "\n")
    sys.exit(0 if summary["outcome_rule_met"] == len(rows) and summary["clean_control_false_positives"] == 0 else 1)

if __name__ == "__main__": main()
