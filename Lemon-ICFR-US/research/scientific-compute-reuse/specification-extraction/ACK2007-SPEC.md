# ACK2007 — Specification Extraction

Status: **SCIENTIFIC-HOLD / COEFFICIENT-ORIGIN-UNVERIFIED / NOT M1-LOCKED**

Estimand: joint existence + discovery/reporting of ICD under the pre-SOX-404 mandatory-audit regime.
Estimator: Logit.

## Predictor identity
The primary preview supports a logistic model with an intercept and 14 predictors in this order:

SEGMENTS, FOREIGN_SALES, M&A, RESTRUCTURE, RGROWTH, INVENTORY, SIZE, %LOSS, RZSCORE, AUDITOR_RESIGN, AUDITOR, RESTATEMENT, INST_CON, LITIGATION.

## Coefficient-value authority
This document intentionally does **not** duplicate the numerical coefficient vector or intercept.

The single machine-readable engineering pin is:
`../executable-models/ACK2007/coefficient-contract.json`

That contract remains:
- role: `regression_pin_only`
- coefficient_verification: `PENDING_PRIMARY_TABLE`
- coefficient_origin: `UNKNOWN_ORIGIN`

R-006 records that some Phase-5 values match rows observed in secondary JAR 2009 excerpts. This is a provenance signal only, not scientific verification. Do not change or scientifically freeze the engineering pin until the published JAE 2007 primary results table is directly cross-checked.

## DARWIN gate
- Coefficients/intercept: PENDING_PRIMARY_TABLE.
- Estimand alignment: conditional; joint existence/reporting, not pure latent MW.
- Variable ontology: primary definitions/timing remain unresolved in multiple places.
- Raw construction: fail closed through the canonical construction registry.
- Replication package: PENDING.
- Transportability: PENDING.

Decision: **SCIENTIFIC-HOLD / NOT M1-LOCKED**.
