#!/usr/bin/env python3
"""P7 regression harness v2 (DERIVED, stdlib only). Does NOT modify originals.
Usage: python3 p7_regression_v2.py <path-to-NAAIL/research-assurance-mcp> <path-to-this-derived-folder>
Adds executable checks the original P7 lacks: its 'scoring_sanity' scores expected-vs-expected (always 1.0).
"""
import json, sys, subprocess, copy, importlib.util, csv, os
from pathlib import Path
MCP, DER = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
C1 = MCP / "case-001-management-science"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
R = []
def rec(cid, ok, detail, blocking=True): R.append(dict(id=cid, ok=bool(ok), blocking=blocking, detail=detail))
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def mod(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# T1 original P7 harness executes and passes
p = subprocess.run([sys.executable, str(MCP/"p7/test_poc_integration.py")], capture_output=True, text=True)
rec("T1_original_p7", p.returncode == 0 and '"status": "PASS"' in p.stdout, f"exit={p.returncode}")

# T2 parser unit tests (pytest-free runner)
sys.path.insert(0, str(C1)); t = mod("tp", C1/"tests/test_parsers.py"); res = {}
for n in [x for x in dir(t) if x.startswith("test_")]:
    try: getattr(t, n)(); res[n] = "PASS"
    except Exception as e: res[n] = f"FAIL {e!r}"
rec("T2_parser_tests", all(v == "PASS" for v in res.values()), res)

# T3/T4/T5 real detector execution on the executable synthetic fixture
det = mod("det", C1/"benchmark/detector.py"); gold = load(C1/"benchmark/fixtures/gold_fixture.json")["gold"]
rec("T3_clean_control_no_flags", det.detect(gold, copy.deepcopy(gold)) == [], det.detect(gold, gold))
MUT = {"E01":("beta",0.214),"E02":("p_value",0.040),"E03":("significance",""),"E04":("n",5021),"E05":("cluster","industry"),
       "E06":("variable_definition","ALTERED"),"E07":("fixed_effects",["gvkey"]),"E08":("future_information",True),
       "E09":("pipeline_steps",["load","clean","estimate","export"]),"E10":("manuscript_claim","Post causes EADelay.")}
single = {}
for eid,(k,v) in MUT.items():
    c = copy.deepcopy(gold); c[k] = v; single[eid] = det.detect(gold, c)
rec("T4_single_mutations_exact", all(single[e] == [e] for e in MUT), single)
man = load(C1/"benchmark/fixtures/compound_case_manifest.json"); c = copy.deepcopy(gold)
for e in man["mutations"]: c[MUT[e][0]] = MUT[e][1]
obs = det.detect(gold, c)
rec("T5_compound_executed_not_stored", obs == sorted(man["expected_detection"]), {"executed": obs, "manifest_claims": man["observed_detection"]})
# known limitation probe: E03 masking (p moved across threshold AND stars updated consistently) -> expected E02 only
c = copy.deepcopy(gold); c["p_value"] = 0.04; c["significance"] = "**"
rec("T6_masking_probe_E02_only", det.detect(gold, c) == ["E02"], det.detect(gold, c), blocking=False)

# T7 Microsoft: frozen CSV vs independent EDGAR retrieval (levels AND vector, accession-level)
ind = load(DER/"msft_filinglag_independent_check_v2.json")
ind_by = {o["obs"].replace("_","-"): o for o in ind["observations"]}
rows = list(csv.DictReader(open(C1/"reexecution/sec_one_company_msft/msft_one_company_final.csv")))
mism = [r["calendar_quarter"] for r in rows if int(r["filing_lag_days"]) != ind_by[r["calendar_quarter"]]["filing_lag"]
        or r["filing_date"] != ind_by[r["calendar_quarter"]]["filed"]]
vec = [int(r["change_vs_same_quarter_2019"]) for r in rows if r["calendar_quarter"][-4:] != "2019"]
rec("T7_msft_levels_match_independent", not mism and len(rows) == 10, {"mismatched_quarters": mism, "n_rows": len(rows)})
rec("T8_msft_vector_match", vec == ind["project_reported_vector"], {"frozen_csv": vec, "independent": ind["project_reported_vector"]})
# T9 provenance: does committed code generate the frozen 10-row artifact?
code = (C1/"reexecution/sec_one_company_msft/sec_one_company_check.py").read_text()
n_targets = code.count('("10-')
rec("T9_msft_artifact_has_generator", n_targets >= 10 and "covid" in code.lower(),
    {"periods_targeted_by_code": n_targets, "rows_in_artifact": len(rows), "covid_logic_in_code": "covid" in code.lower()}, blocking=False)

# T10 adversarial benchmark V2 executability audit (informational)
b = load(MCP/"benchmark/adversarial_benchmark_v2.json")
exe = [x["id"] for x in b["cases"] if any(k in x for k in ("generator","payload","data","mutation_spec"))]
rec("T10_adv_v2_executable_fixtures", len(exe) == len(b["cases"]), {"cases": len(b["cases"]), "with_executable_payload": len(exe)}, blocking=False)

# T11 state hygiene: non-canonical labels in Microsoft artifacts
STATES = {"VERIFIED","CONSISTENT","PARTIAL","FLAGGED","HUMAN_REVIEW"}
fj = load(C1/"reexecution/sec_one_company_msft/msft_one_company_final.json"); oj = load(C1/"reexecution/sec_one_company_msft/msft_sec_observations.json")
bad = [v for v in list(fj["assurance_state"].values()) + [oj["assurance_state"]] if v not in STATES]
rec("T11_canonical_states_only", not bad, {"non_canonical": bad}, blocking=False)

blocking_fail = [r["id"] for r in R if r["blocking"] and not r["ok"]]
out = dict(harness="p7_regression_v2", python=sys.version.split()[0], results=R,
           blocking_failures=blocking_fail, nonblocking_findings=[r["id"] for r in R if not r["blocking"] and not r["ok"]],
           status="PASS" if not blocking_fail else "FAIL")
print(json.dumps(out, indent=2)); sys.exit(0 if not blocking_fail else 1)
