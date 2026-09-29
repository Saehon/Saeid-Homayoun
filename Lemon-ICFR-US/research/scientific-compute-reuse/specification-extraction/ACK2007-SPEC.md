# ACK2007 — Specification Extraction

Status: SCIENTIFIC-HOLD / COEFFICIENT-ORIGIN-UNVERIFIED / NOT M1-LOCKED

Estimand: joint existence + discovery/reporting of ICD under pre-SOX-404 mandatory-audit regime.
Estimator: Logit.
N: 4,810.
Likelihood-ratio chi-square: 233.53.
Concordant: 66.3%; discordant: 33.0%.

| Variable | Beta | SE |
|---|---:|---:|
| Intercept | -3.752 | 0.225 |
| SEGMENTS | 0.078 | 0.029 |
| FOREIGN_SALES | 0.466 | 0.099 |
| M&A | 0.177 | 0.090 |
| RESTRUCTURE | 0.296 | 0.091 |
| RGROWTH | 0.064 | 0.016 |
| INVENTORY | 0.785 | 0.323 |
| SIZE | -0.048 | 0.014 |
| %LOSS | 0.192 | 0.129 |
| RZSCORE | -0.016 | 0.020 |
| AUDITOR_RESIGN | 1.506 | 0.299 |
| AUDITOR | 0.965 | 0.140 |
| RESTATEMENT | 0.470 | 0.140 |
| INST_CON | 0.085 | 0.042 |
| LITIGATION | 0.263 | 0.092 |

Executable form after ontology lock:
z = intercept + sum(beta_k * x_k)
p = 1/(1+exp(-z))

DARWIN gate:
- Coefficients/intercept: PENDING_PRIMARY_TABLE. The vector is retained as a regression/engineering pin only; the currently recovered matching JAR 2009 values are secondary evidence and do not establish the published JAE 2007 coefficient column.
- Estimand alignment: CONDITIONAL; joint existence/reporting, not pure latent MW.
- Variable ontology: PENDING exact definitions/formulas/timing.
- Replication package: PENDING.
- Transportability: PENDING.
Decision: SCIENTIFIC-HOLD, NOT M1-LOCKED. Do not repair or scientifically freeze the coefficient vector until the published JAE 2007 primary results table is directly cross-checked.
