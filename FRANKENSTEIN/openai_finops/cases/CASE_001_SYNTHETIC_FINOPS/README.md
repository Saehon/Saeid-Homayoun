# CASE 001 — Synthetic Finance & Operations Audit

**FRANKENSTEIN OpenAI Finance & Operations Audit Profile**

This directory preserves the first reproducible deterministic audit run of the OpenAI Finance & Operations Audit profile.

## State

- **Execution:** EXECUTED
- **Evidence:** synthetic demonstration population
- **Validation:** NOT VALIDATED
- **Model/API call:** none
- **Human Approval Gate:** PENDING
- **Professional audit conclusion:** not permitted from this case alone

This distinction follows NAAIL governance: an executed software run is not automatically a validated empirical result or professional conclusion.

## Objective

Perform a first population-level finance and operations audit screening run, preserve traceable evidence, and establish a reproducible baseline before generative specialist interpretation.

## Input

- 12 synthetic transactions
- total absolute transaction value: **314,207.15**
- source SHA-256: `ab0847e0e68dce878f1453a41d42e5f1ec9ce0023e2e270c6f4481e9a7b9ad78`

## Deterministic result

The engine produced **7 risk-indicator groups** and an illustrative deterministic risk score of **91/100**.

| Finding | Severity | Indicator | Transactions |
|---|---|---|---|
| F-001 | High | Duplicate transaction identifier | TX-1002 |
| F-002 | High | Missing approval evidence | TX-1005 |
| F-003 | Critical | Requester and approver are the same person | TX-1003 |
| F-004 | Medium | Weekend posting | TX-1002, TX-1003, TX-1004, TX-1010 |
| F-005 | Medium | Out-of-hours posting | TX-1003, TX-1010 |
| F-006 | High | Robust amount outlier | TX-1003, TX-1006 |
| F-007 | Medium | Large round-value transaction | TX-1003, TX-1006, TX-1010 |

The robust amount threshold for this population was **18,068.625** using median plus six median absolute deviations.

## Interpretation boundary

These results are **screening indicators only**. They do not establish fraud, misconduct, accounting error, regulatory non-compliance, ineffective controls, an ICFR deficiency classification, or an audit opinion.

For example, weekend activity and round-value transactions can have legitimate business explanations. Even the segregation-of-duties indicator requires corroboration with the actual workflow, delegated-authority rules, system access, and source documents.

## Required human follow-up

Before any conclusion is promoted, a qualified reviewer should obtain and examine:

1. invoices, contracts and payment support for flagged transactions;
2. approval workflow/history and delegated authority;
3. user-access and segregation-of-duties configuration;
4. bank/payment evidence for high-value transactions;
5. entity-specific materiality and control thresholds;
6. business explanations for weekend/out-of-hours processing.

## Files

- `deterministic_report.json` — preserved row-level deterministic findings.
- `RUN_MANIFEST.json` — source, runtime, configuration and governance provenance.

## Next experiment

The next controlled step is to run the 11 specialist agents and independent Evidence Challenger against this same frozen evidence population, then compare their claims with the deterministic finding allow-list before the Human Approval Gate.
