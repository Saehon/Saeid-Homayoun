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
- [Human–AI experiment design](./human_ai_experiment_design.md)
- [Prototype dashboard](./dashboard.html)
- [GitHub / Google Drive sync manifest](./SYNC_MANIFEST_2026_09_16.md)

## Current executable validation — 2026-09-16

The dedicated unified artifact-validation harness now reports:

```text
15 passed in 0.08s
```

This closes the former variable-dictionary and dashboard-reconciliation automation gaps. The harness is published at:

`tests/test_microsoft_poc_v1_15_contract.py`

A dedicated CI workflow is also published at:

`.github/workflows/microsoft_poc_v1_15_test.yml`

**GitHub Actions CI success is not claimed until a completed workflow run is separately verified.**

## Package contents

The package includes SEC/XBRL financial evidence, CAM/ICFR mapping, bounded filing-text features, finance and market features, innovation proxies, a synthetic ABC/TDABC/AI-cost microcase, an external AI benchmark snapshot, Human–AI experiment design, Evidence Passport schema/instance, reproducible Python tests, and a simple HTML dashboard.

## Scientific boundary

Despite the 15/15 artifact-validation result, these remain open before broader scientific validation or expansion:

- actual T0–T3 participant experiment;
- Microsoft Fama–French regression;
- aggregate PatentsView patent/citation/technology-diversity measures;
- NAAIL-specific professional-task model pass-rate and Cost per Verified Professional Output™;
- independent cross-source and reviewer replication;
- remaining falsification/robustness challenges.

Important boundaries:
- no production-readiness claim;
- no independent scientific-validation claim;
- participant experiment remains design-only;
- Fama–French regression and aggregate PatentsView measures remain unexecuted;
- Microsoft internal management-accounting data are not inferred;
- Human Gate approval is limited to research-prototype publication;
- public availability is not treated as unrestricted redistribution permission;
- patent-hold and non-enabling public-disclosure rules remain in force.

## Expansion gate

Do not advance the Golden Anchor sequence to SAP, Walmart, Intuit, Shopify, JPMorgan Chase, ExxonMobil, Fluor, or optional Boeing until Microsoft V1 has the remaining scientific validation and replication evidence required by the build-and-validation contract.
