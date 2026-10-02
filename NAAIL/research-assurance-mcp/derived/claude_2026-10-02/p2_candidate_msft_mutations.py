"""Candidate P2 extension (derived artifact, NOT yet merged into the NAAIL benchmark).
Deterministic mutation generator + detectors for the Case 001 Microsoft FilingLag reconstruction.
Input: msft_filinglag_independent_check_v2.json (independently retrieved EDGAR dates).
Mutations model realistic reconstruction errors; M1 occurred naturally (GPT addendum, 2026-10-02).
"""
import json, hashlib, copy, sys
from datetime import date, timedelta

SRC = "msft_filinglag_independent_check_v2.json"
raw = open(SRC).read()
REF = json.loads(raw)
PROJECT_VECTOR = REF["project_reported_vector"]          # [5,-2,4,-3,3,-3] per master plan
PAIRS = [("Q1_2020","Q1_2019"),("Q2_2020","Q2_2019"),("Q3_2020","Q3_2019"),
         ("Q4_2020","Q4_2019"),("Q1_2021","Q1_2019"),("Q2_2021","Q2_2019")]
PRIOR = {"Q1_2021":"Q1_2020","Q2_2021":"Q2_2020"}
DEADLINE = {"10-Q":40,"10-K":60}

def base_obs():
    return {o["obs"]:dict(end=date.fromisoformat(o["period_end"]),filed=date.fromisoformat(o["filed"]),
            form=o["form"]) for o in REF["observations"]}

def pipeline(obs, baseline="2019", inclusive=False, sign=+1, deadline=DEADLINE):
    lag = {k:(v["filed"]-v["end"]).days + (1 if inclusive else 0) for k,v in obs.items()}
    vec = []
    for a,b in PAIRS:
        b2 = PRIOR.get(a,b) if baseline=="prior_year" else b
        vec.append(sign*(lag[a]-lag[b2]))
    late = {k:int(lag[k] > deadline[v["form"]]) for k,v in obs.items()}
    return dict(lags=lag, vector=vec, late=late)

def mutated_dates(shift):           # shift: {obs: +days}
    o = base_obs()
    for k,d in shift.items(): o[k]["filed"] += timedelta(days=d)
    return o

CASES = {  # id: (class, description, kwargs builder)
 "C0_clean":            ("clean_control","correct pipeline", lambda: pipeline(base_obs())),
 "M1_prior_year_base":  ("single","2021 quarters compared to 2020 not 2019 (natural GPT error)", lambda: pipeline(base_obs(),baseline="prior_year")),
 "M2_afterhours_rule":  ("single","Q2_2020 10-K moved to next day (acceptance 20:44 treated as next business day)", lambda: pipeline(mutated_dates({"Q2_2020":1}))),
 "M3_inclusive_count":  ("difficult","inclusive day count (+1 to every lag)", lambda: pipeline(base_obs(),inclusive=True)),
 "M4_sign_flip":        ("single","change computed as base minus COVID-era", lambda: pipeline(base_obs(),sign=-1)),
 "M5_10K_deadline_40d": ("difficult","10-K deadline mis-set to 40 days", lambda: pipeline(base_obs(),deadline={"10-Q":40,"10-K":40})),
 "M6_compound_M1_M2":   ("compound","M1 + M2", lambda: pipeline(mutated_dates({"Q2_2020":1}),baseline="prior_year")),
 "M7_provenance_swap":  ("provenance","Q1_2019 date taken from wrong filing (FY2019 Q4 10-Q swapped: +5d)", lambda: pipeline(mutated_dates({"Q1_2019":5}))),
}

ref = pipeline(base_obs())
def detectors(r):
    return {"D1_vector_vs_project": r["vector"] != PROJECT_VECTOR,
            "D2_levels_vs_EDGAR":   r["lags"] != ref["lags"],
            "D3_latefiler_vs_project_zero": any(r["late"].values())}

results, ok = [], True
for cid,(cls,desc,fn) in CASES.items():
    r = fn(); d = detectors(r); flagged = any(d.values())
    expected = cls != "clean_control"
    if cid=="C0_clean" and flagged: ok=False
    results.append(dict(id=cid,cls=cls,desc=desc,vector=r["vector"],detectors=d,flagged=flagged,
                        outcome=("TP" if flagged and expected else "FN" if expected else "FP" if flagged else "TN")))
    print(f"{cid:22s} {cls:13s} vec={r['vector']!s:24s} D1={d['D1_vector_vs_project']!s:5s} "
          f"D2={d['D2_levels_vs_EDGAR']!s:5s} D3={d['D3_latefiler_vs_project_zero']!s:5s} -> {results[-1]['outcome']}")

tp=sum(x["outcome"]=="TP" for x in results); fn=sum(x["outcome"]=="FN" for x in results)
print(f"\nclean control correct: {ok} | mutations detected {tp}/{tp+fn}")
out=dict(source=SRC,source_sha256=hashlib.sha256(raw.encode()).hexdigest(),project_vector=PROJECT_VECTOR,results=results)
s=json.dumps(out,indent=2); open("p2_candidate_msft_mutation_results.json","w").write(s)
print("results sha256:",hashlib.sha256(s.encode()).hexdigest())
sys.exit(0 if ok else 1)
