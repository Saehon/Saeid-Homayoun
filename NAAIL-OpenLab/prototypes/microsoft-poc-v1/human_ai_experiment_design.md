# NAAIL Microsoft POC V1 — Human–AI Experiment Design

**Maturity:** `RESEARCH_PROTOTYPE`  
**Execution:** `DESIGN_COMPLETE_NOT_EXECUTED`

## Research question
How does AI advice, explanation and contradictory evidence affect professional revenue-recognition judgment?

## Case
A synthetic Microsoft-like cloud/software contract inspired by public revenue-recognition issues. It is **not** an actual Microsoft customer contract.

## Randomized conditions
- **T0 Human only**
- **T1 Human + AI recommendation**
- **T2 Human + AI recommendation + explanation**
- **T3 Human + AI recommendation + contradictory evidence**

## Manipulated factors
AI advice availability; explanation availability; contradictory evidence. A later preregistered extension may manipulate AI confidence, anchor strength, information order, time pressure and management pressure.

## Outcomes
Accuracy; confidence; calibration; AI reliance; AI override; evidence requests; professional skepticism; decision revision; advice taking; completion time.

## Primary confirmatory design
Random assignment at participant level. Pre-specify one primary accuracy outcome and one reliance/calibration outcome. Conduct power analysis before recruitment. Log treatment delivery and completion time. Retain null results.

## Analysis
Difference-in-means/OLS with treatment indicators; heteroskedasticity-robust standard errors; preregistered contrasts T1–T0, T2–T1, T3–T2. Exploratory heterogeneity must be labeled exploratory.

## oTree implementation
`code/otree_experiment_stub.py` provides a minimal implementation skeleton. No participant data have been collected.

## Safeguards
Behavioral measures are empirical proxies, not psychological diagnoses. No causal conclusion is made before randomization, manipulation checks and completed analysis. Human approval is required before confirmatory launch.
