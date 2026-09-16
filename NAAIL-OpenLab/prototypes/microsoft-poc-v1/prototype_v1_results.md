# Prototype V1 Results — Microsoft Golden Anchor

**Maturity:** `RESEARCH_PROTOTYPE`  
**Run date:** 2026-09-16  
**Contract update:** 2026-09-16 — upgraded to 15-test + falsification/robustness specification  
**Production readiness:** NO  
**Independent replication:** NOT YET

## Executed validation retained from the prior V1 run

| Requirement | Result |
|---|---|
| SEC/XBRL ingestion | **PASS** — SEC interactive-XBRL R2/R4/R6/R107 facts ingested into the frozen V1 snapshot |
| Textual-analysis pipeline | **PASS, bounded** — two FY2026 filing samples transformed to numerical features; raw text withheld |
| Finance calculation | **PASS** — ratios, cash-flow measures, FY2026 price return, DGS10 |
| CAM/audit mapping | **PASS** — 2 FY2026 CAMs + ICFR opinion |
| Innovation measure | **PASS** — R&D intensity + GitHub metadata snapshot; patent analysis remains unexecuted |
| ABC/TDABC/AI-cost | **PASS, synthetic** — internal-process microcase only |
| AI-model benchmark | **PASS, external benchmark** — LiveBench quality and cost-per-successful-task snapshot |
| Human–AI experiment design | **PASS DESIGN / NOT RUN** |
| Evidence Passport | **PASS** — schema + instantiated SEC XBRL passport |
| Human Gate | **PASS FOR RESEARCH-PROTOTYPE PUBLICATION ONLY** |

## New 15-test contract coverage

The upgraded build contract now requires 15 explicit tests using only `PASS`, `FAIL`, `NOT EXECUTED`, or `BLOCKED`.

| Test | Status | Note |
|---|---|---|
| TEST 01 — SEC/XBRL ingestion | **PASS** | Existing frozen-XBRL validation evidence |
| TEST 02 — Financial statement extraction | **PASS** | FY2026 standardized financial artifacts exist and reconcile |
| TEST 03 — Variable dictionary validation | **NOT EXECUTED** | Dictionary exists; no dedicated validation test in prior 12-test harness |
| TEST 04 — Evidence Passport generation | **PASS** | Schema + instantiated provenance artifact |
| TEST 05 — CAM/audit-risk mapping | **PASS** | Two CAMs + ICFR mapping |
| TEST 06 — Text analytics | **PASS** | Bounded source-sample execution |
| TEST 07 — Finance calculation | **PASS** | Selected executed finance measures; factor regression still open |
| TEST 08 — Innovation measure | **PASS** | R&D + GitHub research indicators; PatentsView remains open |
| TEST 09 — ABC calculation | **PASS** | Synthetic management-accounting microcase only |
| TEST 10 — TDABC calculation | **PASS** | Existing unit test validates TDABC arithmetic |
| TEST 11 — AI token/cost calculation | **PASS** | Synthetic AI-cost microcase only |
| TEST 12 — Model benchmark | **PASS** | External LiveBench snapshot only |
| TEST 13 — Human–AI experiment structure | **PASS** | T0–T3 design exists; participant experiment not executed |
| TEST 14 — Dashboard data load | **NOT EXECUTED** | Dashboard exists but explicit automated data-load test is absent |
| TEST 15 — Human Gate decision | **PASS** | Publication-only approval boundary |

**Coverage classification:** 13 PASS / 2 NOT EXECUTED / 0 FAIL / 0 BLOCKED.  
**Important:** this is a mapping of existing evidence to the new contract. A dedicated 15-test automated harness has **not** yet been rerun.

See: [`VALIDATION_MATRIX_15_TESTS.md`](./VALIDATION_MATRIX_15_TESTS.md).

## Selected numerical results

- Revenue growth: **17.75%**
- Operating margin: **46.78%**
- Net margin: **40.31%**
- Current ratio: **1.230**
- Liabilities/assets: **41.67%**
- R&D intensity: **10.72%**
- FCF proxy: **$66,987m**
- FCF margin: **20.19%**
- FY2026 MSFT simple price return (IEX close-to-close, no dividends): **-24.22%**
- DGS10 at 2026-06-30: **4.44%**
- Illustrative DGS10 + mature-market ERP proxy: **8.64% (NOT Microsoft WACC)**

## Audit results

- Revenue Recognition CAM mapped to revenue assertions, contract/performance-obligation risk, procedures and high-judgment conclusion.
- Uncertain Tax Positions CAM mapped to tax-liability valuation/completeness/presentation, transfer-pricing risk, specialist procedures and high-judgment conclusion.
- FY2026 ICFR auditor opinion: **unqualified**.

## AI benchmark

LiveBench 2026-06-25 external snapshot includes overall score + cost per successful task. V1 does not infer professional task fitness from leaderboard rank alone.

## Historical unit-test execution

The earlier reproducibility package passed **12/12 offline unit tests** on 2026-09-16. Those tests cover the two-core constitution, frozen XBRL facts, segment reconciliation, finance calculations, real market-data status, CAM/ICFR mapping, bounded text outputs, innovation boundary, external benchmark labeling, TDABC arithmetic, experiment execution status and Human Gate boundary.

This historical 12/12 result remains valid as a record of that harness. It does not imply that the newly expanded 15-test contract has been fully executed.

## Falsification and robustness status

A formal falsification register is now part of the public package: [`FALSIFICATION_ROBUSTNESS_REGISTER.md`](./FALSIFICATION_ROBUSTNESS_REGISTER.md).

The following remain open and must not be represented as validated:

- cross-source replication of selected financial facts;
- independent CAM/judgment coding;
- alternative text models/specifications;
- Fama–French regression and period/specification sensitivity;
- PatentsView corroboration of innovation constructs;
- sensitivity analysis for synthetic ABC/TDABC/AI-cost assumptions;
- NAAIL professional-task benchmark versus external leaderboard evidence;
- participant execution of T0–T3;
- evaluation-leakage review;
- independent Evidence Passport replay;
- automated dashboard-data reconciliation;
- independent Human Gate reviewer decision.

## Human Gate

**APPROVE_RESEARCH_PROTOTYPE_FOR_PUBLICATION_WITH_LIMITATIONS**

Not approved for production reliance, professional assurance, causal innovation conclusions, or scientific-validation claims.

## Success-gate status

The overall Microsoft V1 success gate is **NOT PASSED** because the actual Human–AI participant experiment, independent replication, and other open validation work remain incomplete. TEST 13 verifies experiment structure only; it does not count as participant execution.

## Remaining unexecuted gates

- dedicated variable-dictionary validation test;
- automated dashboard data-load/integrity test;
- full rerun of the dedicated 15-test harness;
- Fama–French regression;
- aggregate PatentsView metrics;
- full raw-filing text pipeline with reusable/rights-cleared intermediate artifacts;
- actual participant experiment;
- NAAIL-specific model pass-rate / cost-per-verified-professional-output;
- independent replication.

**Final maturity status: `RESEARCH_PROTOTYPE`.**
