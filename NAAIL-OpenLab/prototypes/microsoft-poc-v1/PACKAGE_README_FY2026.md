# Microsoft Golden Anchor POC V1 — Executable Package

**Maturity:** `RESEARCH_PROTOTYPE`

This directory contains the bounded FY2026 Microsoft Golden Anchor proof of concept for NAAIL OpenLab™ — V2026.3.

Canonical architecture remains exactly two permanent cores:
1. Stable Knowledge Core™
2. Replaceable Technology Core™

**No third permanent core is permitted.**

## Canonical V1 documents

- [Microsoft POC V1 status and executed scope](./MICROSOFT_POC_V1.md)
- [Upgraded Microsoft POC V1 build-and-validation contract](./MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md)
- [Prototype V1 executed results](./prototype_v1_results.md)
- [15-test validation matrix](./VALIDATION_MATRIX_15_TESTS.md)
- [Falsification & robustness register](./FALSIFICATION_ROBUSTNESS_REGISTER.md)
- [Human–AI experiment design](./human_ai_experiment_design.md)
- [Prototype dashboard](./dashboard.html)

The package includes SEC/XBRL financial evidence, CAM/ICFR mapping, bounded filing-text features, finance and market features, innovation proxies, a synthetic ABC/TDABC/AI-cost microcase, an external AI benchmark snapshot, Human–AI experiment design, an Evidence Passport schema and instantiated Digital Twin, reproducible Python code, tests, and a simple HTML dashboard.

## Upgraded validation contract — 2026-09-16

The canonical contract now requires **15 explicit tests** plus a formal falsification/robustness program. Every test must be classified only as `PASS`, `FAIL`, `NOT EXECUTED`, or `BLOCKED`.

The historical reproducibility harness still records **12/12 offline unit tests passed**. Mapping the currently available evidence to the new 15-test contract yields **13 PASS and 2 NOT EXECUTED** (dedicated variable-dictionary validation and automated dashboard data-load validation). This is a coverage assessment, not a claim that a new 15-test automated harness has already been rerun.

The actual T0–T3 Human–AI participant experiment remains **NOT EXECUTED**. Its structural design test can pass without satisfying the separate Human–AI Experiment success gate.

Still open before broader validation/expansion:
- dedicated variable-dictionary validation test;
- explicit dashboard data-load/integrity test;
- full rerun of the dedicated 15-test harness;
- Microsoft Fama–French regression;
- aggregate PatentsView patent/citation measures;
- actual participant execution of the T0–T3 experiment;
- NAAIL-specific professional-task model pass-rate and cost-per-verified-output validation;
- formal falsification challenges and independent replication.

Important boundaries:
- no production-readiness claim;
- no independent scientific-validation claim;
- participant experiment is design-only;
- Fama–French regression and aggregate PatentsView measures remain unexecuted;
- Microsoft internal management-accounting data are not inferred;
- Human Gate approval is limited to research-prototype publication;
- public availability is not treated as unrestricted redistribution permission;
- patent-hold and non-enabling public-disclosure rules remain in force.

## Expansion gate

Do not advance the Golden Anchor sequence to SAP, Walmart, Intuit, Shopify, JPMorgan Chase, ExxonMobil, Fluor, or optional Boeing until Microsoft V1 has the documented validation evidence required by the upgraded build-and-validation contract.
