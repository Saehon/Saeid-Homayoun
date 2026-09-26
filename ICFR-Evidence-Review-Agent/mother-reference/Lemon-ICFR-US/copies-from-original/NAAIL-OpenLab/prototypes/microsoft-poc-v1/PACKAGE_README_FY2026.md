# Microsoft Golden Anchor POC V1 — Executable Package

**Maturity:** `RESEARCH_PROTOTYPE`

This directory contains the bounded FY2026 Microsoft Golden Anchor proof of concept for NAAIL OpenLab™ — V2026.3.

Canonical architecture remains exactly two permanent cores:
1. Stable Knowledge Core™
2. Replaceable Technology Core™

**No third permanent core is permitted.**

## Canonical V1 documents

- [Microsoft POC V1 status and executed scope](./MICROSOFT_POC_V1.md)
- [Microsoft POC V1 build-and-validation contract](./MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md)
- [Prototype V1 executed results](./prototype_v1_results.md)
- [Unified 15-test validation matrix](./VALIDATION_MATRIX_15_TESTS.md)
- [Timestamped 15-test run](./VALIDATION_RUN_15_TESTS_2026_09_16.md)
- [Falsification & robustness register](./FALSIFICATION_ROBUSTNESS_REGISTER.md)
- [Microsoft FY2026 Fama–French reproducibility status](./MICROSOFT_FAMA_FRENCH_EXECUTION_STATUS_2026_09_16.md)
- [Human–AI experiment design](./human_ai_experiment_design.md)
- [Prototype dashboard](./dashboard.html)
- [GitHub / Google Drive sync manifest](./SYNC_MANIFEST_2026_09_16.md)

## Current executable validation — 2026-09-16

The dedicated unified artifact-validation harness reports:

```text
15 passed in 0.08s
```

This closes the former variable-dictionary and dashboard-reconciliation automation gaps. The harness is published at `tests/test_microsoft_poc_v1_15_contract.py` and a dedicated workflow is published at `.github/workflows/microsoft_poc_v1_15_test.yml`.

**GitHub Actions CI success is not claimed until a completed workflow run is separately verified.**

## Microsoft Fama–French finance validation package

The next finance-validation gate has now been implemented reproducibly, while execution remains conservatively unclaimed:

- frozen MSFT month-end IEX inputs: `microsoft_fama_french_fy2026_input.csv`;
- CAPM / FF3 / FF5 runner: `code/msft_fama_french_fy2026.py`;
- execution/publishing workflow: `.github/workflows/microsoft_poc_v1_fama_french.yml`;
- status record: `MICROSOFT_FAMA_FRENCH_EXECUTION_STATUS_2026_09_16.md`.

The runner uses the official Kenneth R. French monthly U.S. five-factor archive and is designed to produce merged data, coefficients and provenance automatically. At the current verified state, no completed GitHub Actions execution or generated regression outputs have been observed, so the factor regression remains **`REGISTERED_NOT_EXECUTED`**. No alpha/beta/factor coefficient is claimed.

The planned FY2026 regression uses 12 monthly close-to-close **price returns**, excludes dividends, and is exploratory because the five-factor model has very low residual degrees of freedom at n=12.

## Package contents

The package includes SEC/XBRL financial evidence, CAM/ICFR mapping, bounded filing-text features, finance and market features, innovation proxies, a synthetic ABC/TDABC/AI-cost microcase, an external AI benchmark snapshot, Human–AI experiment design, Evidence Passport schema/instance, reproducible Python tests, and a simple HTML dashboard.

## Scientific boundary

Despite the 15/15 artifact-validation result, these remain open before broader scientific validation or expansion:

- completed/verified Microsoft Fama–French execution and later total-return/longer-window sensitivity;
- actual T0–T3 participant experiment;
- aggregate PatentsView patent/citation/technology-diversity measures;
- NAAIL-specific professional-task model pass-rate and Cost per Verified Professional Output™;
- independent cross-source and reviewer replication;
- remaining falsification/robustness challenges.

Important boundaries:
- no production-readiness claim;
- no independent scientific-validation claim;
- participant experiment remains design-only;
- Fama–French implementation is published but execution remains unverified;
- aggregate PatentsView measures remain unexecuted;
- Microsoft internal management-accounting data are not inferred;
- Human Gate approval is limited to research-prototype publication;
- public availability is not treated as unrestricted redistribution permission;
- patent-hold and non-enabling public-disclosure rules remain in force.

## Expansion gate

Do not advance the Golden Anchor sequence to SAP, Walmart, Intuit, Shopify, JPMorgan Chase, ExxonMobil, Fluor, or optional Boeing until Microsoft V1 has the remaining scientific validation and replication evidence required by the build-and-validation contract.
