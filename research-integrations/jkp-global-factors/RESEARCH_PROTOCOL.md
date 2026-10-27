# Scientific protocol — AI investment and JKP factors

**Status:** preregistration-style design sketch (not executed, not preregistered). No data-dependent significance claims.

## Research question

Does accounting-based AI investment/disclosure information predict future equity outcomes after established global factor, industry and firm-characteristic benchmarks, including careful out-of-sample validation?

## Proposed hypotheses — all untested

- H1: Timely AI-investment/accounting information is associated with future returns after established controls.
- H2: Any incremental association varies by industry, investment intensity and institutional context.
- H3: AI-supported discovery improves truly held-out forecasting or factor replication **only if** robust to multiple-testing adjustment, alternate measures and data revisions.

## Data and timing

- Main sample candidate: 2020-01-01 to 2024-12-31, subject to availability.
- JKP factors: choose monthly country/region-specific series, disclose source download/version/date and transformations.
- AI measure: firm-year SEC/XBRL or other auditable filings, including reporting year, filing date, publication date and first legally usable investment signal date.
- Equities: licensed firm/month identifiers, returns including delisting where applicable, country and industry.
- Never equate fiscal year-end with public availability; require a conservative reporting lag where exact timestamps are unavailable.
- Avoid survivorship, hindsight selection and stale mapping across identifiers, currencies or countries.

## Models

1. Traditional benchmark: time-series asset-pricing attribution and/or classic predictive characteristics, as appropriate.
2. Prespecified incremental AI measure: firm return at t+1 related to lagged information-available AI measure at t plus predeclared controls; for contemporaneous factor attribution, period t+1 factor realizations are ex post explanatory controls only.
3. ML/NN challenger: blocked rolling/expanding training windows with all tuning within training blocks and truly out-of-sample holdouts.
4. Sensitivity: alternative AI definitions, geography, size, reporting delay and factor choice, plus null/negative controls.

A model with **future realized factor returns** in its features must not be described as a tradeable out-of-sample forecast.

## Inference and reporting

- Report panel grain, matched/missing counts, return measurement and coverage maps.
- Choose clustered / time-series robust inference based on panel structure.
- Separate discovery from confirmatory analysis and predefine multiplicity family.
- Record nonsignificant effects, unsuccessful runs and model/threshold changes.
- For multiple dependent tests, investigate FDR, FWER and selective inference assumptions before applying controls.
- Compare equal-information baselines; include stability and economic magnitudes, not only p-values.
- Report exact source hashes and version dates; preserve file-level evidence passports without redistributing data.

## Integration gates

- G0 Licensing/provenance: source, valid legal access, allowed distribution, raw-data exclusion.
- G1 Data validation: distinct asset × period × country mapping; source and factor units confirmed.
- G2 Leakage firewall: public-availability timing, lookback/holdout boundaries and chronological joins.
- G3 Scientific controls: baseline, full specification registry, multiplicity checks and falsification.
- G4 Independent replication: deterministic code, environment versions, records of PASS/FAIL.
- G5 Human scientific review: release only approved and permitted results.

**Current state:** source bridge and synthetic tests cover part of G1 only. G0 requires data-specific inspection. No G2–G5 evidence or actual returns-model results have yet been produced.
