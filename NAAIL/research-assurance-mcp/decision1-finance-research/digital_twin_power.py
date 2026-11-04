#!/usr/bin/env python3
"""EX ANTE POWER digital twin ONLY. This fabricates no firm data or real empirical claims.
Run: python digital_twin_power.py --firms 100 --periods 4 --reps 80 --output result.json
Dependencies: numpy, pandas, statsmodels
"""
from __future__ import annotations
import argparse
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm

SEED = 271828
TERMS = ["assurance_surprise", "disagreement_x_evidence", "peer_exposure_x_credibility"]

def generate(rng: np.random.Generator, n_firms: int, n_periods: int, effects: tuple[float,float,float]) -> pd.DataFrame:
    if n_firms < 30 or n_periods < 3:
        raise ValueError("Need >=30 firms and >=3 periods for this illustration")
    n = n_firms * n_periods
    firms = np.repeat(np.arange(n_firms), n_periods)
    period = np.tile(np.arange(n_periods), n_firms)
    firm_fe = rng.normal(0, .025, n_firms)[firms]
    t_fe = rng.normal(0, .01, n_periods)[period]
    risk = rng.normal(size=n)
    disagreement = rng.normal(size=n)
    evidence = rng.binomial(1, .5, size=n)
    peer = rng.normal(size=n)
    credibility = rng.binomial(1, .5, size=n)
    size = rng.normal(size=n)
    mom = rng.normal(size=n)
    v = np.column_stack((risk, disagreement*evidence, peer*credibility))
    outcome = v @ np.asarray(effects) + .006*size + .008*mom + firm_fe + t_fe + rng.normal(0,.14,n)
    return pd.DataFrame({"firm":firms,"period":period,
      "assurance_surprise":v[:,0],"disagreement_x_evidence":v[:,1],
      "peer_exposure_x_credibility":v[:,2],"size":size,
      "momentum":mom,"return_excess":outcome})

def fit(data: pd.DataFrame) -> dict:
    x=sm.add_constant(data[TERMS+["size","momentum"]],has_constant="add")
    x=pd.concat([x,pd.get_dummies(data["period"].astype("category"),
                         prefix="period",drop_first=True,dtype=float)],axis=1)
    mdl=sm.OLS(data["return_excess"].astype(float),x.astype(float)).fit(
            cov_type="cluster",cov_kwds={"groups":data["firm"]})
    return {term:{"coef":float(mdl.params[term]),
                  "p_value":float(mdl.pvalues[term])} for term in TERMS}

def simulation(n_firms: int=150,n_periods: int=5,reps: int=100,seed: int=SEED) -> dict:
    rng=np.random.default_rng(seed); outcomes={}
    scenarios={"NULL_ALL_ZERO":(0.,0.,0.),
               "ALTERNATIVE_ASSUMED":(-.015,-.020,-.015)}
    for label,effects in scenarios.items():
        rejected={k:[] for k in TERMS}
        for _ in range(reps):
            estimates=fit(generate(rng,n_firms,n_periods,effects))
            for k in TERMS:
                rejected[k].append(estimates[k]["p_value"] < .05)
        outcomes[label]={k:round(float(np.mean(v)),3) for k,v in rejected.items()}
    return {
       "label":"SIMULATED POWER/FALSE POSITIVE RATES, NOT REAL EMPIRICAL RESULTS",
       "seed":seed,"firms":n_firms,"periods":n_periods,
       "replications_per_scenario":reps,
       "assumed_alternative_effects":{"H1":-.015,"H2":-.020,"H3":-.015},
       "test":"cluster-robust OLS by firm; alpha .05, THREE UNADJUSTED hypotheses",
       "caution":"Correct multiple testing before preregistration. Fictional simulated outcomes prove no real-world significance.",
       "rejection_rates":outcomes}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--firms",type=int,default=150)
    ap.add_argument("--periods",type=int,default=5)
    ap.add_argument("--reps",type=int,default=100)
    ap.add_argument("--seed",type=int,default=SEED)
    ap.add_argument("--output")
    a=ap.parse_args(); out=simulation(a.firms,a.periods,a.reps,a.seed)
    text=json.dumps(out,indent=2)
    if a.output:
        from pathlib import Path
        Path(a.output).write_text(text+"\n",encoding="utf-8")
    print(text)
if __name__=="__main__":
    main()
