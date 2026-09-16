# NAAIL OpenLab™ — Microsoft Proof of Concept / Prototype V1

**Golden Anchor Company:** Microsoft Corporation  
**Fiscal anchor:** FY ended June 30, 2026  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Canonical architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**. **No third core.**

**Canonical upgraded build-and-validation contract:** [MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md](./MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md)  
**Executed results:** [prototype_v1_results.md](./prototype_v1_results.md)  
**15-test coverage matrix:** [VALIDATION_MATRIX_15_TESTS.md](./VALIDATION_MATRIX_15_TESTS.md)  
**Falsification & robustness register:** [FALSIFICATION_ROBUSTNESS_REGISTER.md](./FALSIFICATION_ROBUSTNESS_REGISTER.md)

> Bounded proof of concept only. It is not production-ready and does not claim scientific validation beyond executed evidence. The upgraded 15-test contract must not convert `NOT EXECUTED` work into PASS.

## End-to-end objective

**Microsoft real public evidence → Data & Evidence Mesh™ → SEC/XBRL + CAM + ICFR + textual analytics → Accounting/Audit/Finance/Innovation → Microsoft Digital Twin → BSC/ABC/TDABC/AI Costing → Open AI Model Benchmark → Human–AI Experiment → Evidence Passport™ → Robustness/Replication/Falsification → Human Approval Gate™**

## What V1 actually executes

- SEC interactive-XBRL facts from **R2 (income statement), R4 (balance sheet), R6 (cash flows), and R107 (segments)**.
- Derived accounting/finance features.
- FY2026 MSFT market-price snapshot: **251 IEX daily bars**, FY start/last close proxy **$492.10 → $372.92**, simple price return **-24.22%** (not dividend-adjusted).
- FY-end U.S. 10-year Treasury snapshot **4.44%**.
- FY2026 CAM/ICFR mapping.
- Two bounded filing-text samples transformed into numerical text features without redistributing the underlying text.
- Innovation proxies: R&D intensity and Microsoft GitHub public metadata.
- Synthetic ABC/TDABC/AI-cost microcase.
- Current LiveBench external model-quality/cost snapshot.
- Evidence Passport instance and Human Gate publication decision.
- Human–AI experiment **structure/design only**.

## Validation state after contract upgrade

The historical reproducibility harness passed **12/12 offline unit tests** on 2026-09-16. The upgraded contract now defines **15 explicit tests** and a formal falsification program.

Mapping existing evidence to that new contract currently yields:

- **13 PASS**
- **2 NOT EXECUTED** — dedicated variable-dictionary validation and explicit dashboard data-load/integrity validation
- **0 FAIL**
- **0 BLOCKED**

This is a coverage mapping, **not** a claim that a new dedicated 15-test automated harness has already been executed.

The separate Human–AI Experiment success gate remains **NOT EXECUTED** because no participant run has occurred. TEST 13 verifies only the T0–T3 experimental structure.

## Core FY2026 financial state (USD millions)

Revenue **331,839**; operating income **155,237**; net income **133,749**; assets **758,376**; liabilities **315,989**; equity **442,387**; operating cash flow **182,935**; additions to PP&E **115,948**; FCF proxy **66,987**; R&D **35,562**.

Segments: Productivity & Business Processes **139,996**; Intelligent Cloud **137,791**; More Personal Computing **54,052**.

## Audit / CAM / ICFR

Deloitte & Touche LLP issued an unqualified FY2026 ICFR opinion. V1 maps two CAMs:
1. **Revenue Recognition**
2. **Income Taxes — Uncertain Tax Positions**

The mapping follows:
`ACCOUNT → ASSERTION → RISK → CAM → AUDIT PROCEDURE → EVIDENCE → JUDGMENT`.

## Text analytics

`microsoft_text_features.csv` stores bounded-sample word/sentence/readability and dictionary-proxy measures. Raw filing samples are deliberately not republished.

## Finance

Executed: profitability, liquidity, leverage, cash-flow measures, FY2026 simple MSFT price return, FY-end DGS10, and a clearly labeled risk-free-plus-mature-ERP illustration.  
Not executed: Fama–French regression and a Microsoft-specific WACC. The **8.64%** RF+ERP figure is a teaching proxy, **not** Microsoft WACC.

## Innovation

Executed: R&D intensity and public GitHub metadata snapshot.  
Registered, not executed: aggregate PatentsView assignee/citation measures.

## Management accounting

The public package uses a **NAAIL synthetic Microsoft-like management-accounting Digital Twin** to demonstrate BSC/ABC/TDABC/AI-ABC/TTD-AIC logic:

`RESOURCE → COST POOL → ACTIVITY → COST DRIVER → TIME → TOKENS → COMPUTE → TOOL CALLS → HUMAN REVIEW → OUTPUT → QUALITY → COST → VALUE`.

No Microsoft internal cost or capacity data are inferred, and no claim is made that Microsoft uses this costing model.

## AI model benchmark

`ai_cost_benchmark.csv` uses the LiveBench 2026-06-25 release. The cost field is **LiveBench cost per successful task**—an external objective benchmark—not a NAAIL professional-verification rate.

## Human–AI experiment

T0 Human only; T1 Human+AI; T2 Human+AI+explanation; T3 Human+AI+contradictory evidence. Design complete, participant run not executed.

Measures planned include accuracy, confidence, confidence–accuracy gap, AI reliance, override, evidence requested, contradictory-evidence recognition, professional skepticism, decision revision, decision time and final judgment quality.

## Falsification / robustness boundary

The upgraded contract requires explicit challenges to each major result. Open work includes cross-source financial replication, independent CAM coding, alternative text models/specifications, Fama–French sensitivity, PatentsView construct corroboration, AI-cost sensitivity, professional-task benchmark comparison, leakage review, Evidence Passport replay, dashboard reconciliation, participant execution and independent Human Gate review.

Contradictory evidence must be retained and documented rather than silently removed.

## Current FT50 research design anchors

Current FT50 membership is checked dynamically. V1 uses a small design benchmark set: Loughran & McDonald (financial text, *JF*); Burke et al. (CAMs, *TAR*); Fama & French (factor models, *JFE*); Roach & Cohen (patent citations, *Management Science*); plus current *Management Science* human–AI experiment designs. Article text is not copied.

## Success boundary

V1 demonstrates **REAL DATA + REPRODUCIBLE ANALYSIS + MULTIPLE NAAIL ENGINES + ONE COMPANY DIGITAL TWIN + AI COST MEASUREMENT + BEHAVIORAL EXPERIMENT DESIGN + EVIDENCE PROVENANCE + HUMAN REVIEW**.

It does **not** yet demonstrate a fully executed 15-test harness, participant results, live Fama–French exposure, aggregate patent citations, production deployment, completed falsification, or independent replication.

**Overall success gate: NOT PASSED.**

## Next gate

Finish Microsoft V1 first. Do not advance to SAP/Walmart/Intuit/Shopify/JPMorgan/ExxonMobil/Fluor/Boeing until the upgraded Microsoft V1 validation contract is satisfied and independently replicated.
