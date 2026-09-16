# NAAIL OpenLab™ — Microsoft Proof of Concept / Prototype V1

**Golden Anchor Company:** Microsoft Corporation  
**Fiscal anchor:** FY ended June 30, 2026  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Canonical architecture:** exactly **Stable Knowledge Core™ + Replaceable Technology Core™**. **No third core.**

**Canonical build-and-validation contract:** [MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md](./MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md)  
**Executed results:** [prototype_v1_results.md](./prototype_v1_results.md)  
**15-test run:** [VALIDATION_RUN_15_TESTS_2026_09_16.md](./VALIDATION_RUN_15_TESTS_2026_09_16.md)

> Bounded proof of concept only. It is not production-ready and does not claim scientific validation beyond the executed tests described here.

## End-to-end objective

**Microsoft public evidence → Data & Evidence Mesh™ → Evidence Passport™ → Accounting/Audit/Finance/Text/Innovation modules → Microsoft Digital Twin → AI benchmark / synthetic costing / experiment design → Human Gate™**

## What V1 actually executes

- SEC interactive-XBRL facts from **R2, R4, R6 and R107**.
- Derived accounting/finance features.
- FY2026 MSFT market-price snapshot: **251 IEX daily bars**, FY start/last close proxy **$492.10 → $372.92**, simple price return **-24.22%** (not dividend-adjusted).
- FY-end U.S. 10-year Treasury snapshot **4.44%**.
- FY2026 CAM/ICFR mapping.
- Two bounded filing-text samples transformed into numerical features without redistributing underlying raw text.
- Innovation proxies: R&D intensity and Microsoft GitHub public metadata.
- Synthetic ABC/TDABC/AI-cost microcase.
- LiveBench external model-quality/cost snapshot.
- Evidence Passport instance and Human Gate publication decision.
- Human–AI experiment **structure/design only**.
- Dedicated unified **15-test artifact-validation harness: 15/15 PASS**.

## Unified 15-test result

`tests/test_microsoft_poc_v1_15_contract.py` executed successfully on 2026-09-16:

```text
...............                                                          [100%]
15 passed in 0.08s
```

This includes dedicated execution of:

- **TEST 03 — Variable dictionary validation**; and
- **TEST 14 — Dashboard data-load/reconciliation validation**.

See [VALIDATION_MATRIX_15_TESTS.md](./VALIDATION_MATRIX_15_TESTS.md) for exact test boundaries.

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

Executed: profitability, liquidity, leverage, cash-flow measures, FY2026 simple MSFT price return, FY-end DGS10, and a labeled risk-free-plus-mature-ERP illustration.  
Not executed: **Fama–French regression** and a Microsoft-specific WACC. The **8.64%** RF+ERP figure is a teaching proxy, **not** Microsoft WACC.

## Innovation

Executed: R&D intensity and public GitHub metadata snapshot.  
Registered, not executed: aggregate PatentsView assignee/citation/technology-diversity measures.

## Management accounting

A synthetic Microsoft-like AI analysis workflow demonstrates BSC/ABC/TDABC/AI-ABC/TTD-AIC logic:
`RESOURCE → ACTIVITY → TIME → TOKENS → COST → OUTPUT → QUALITY → VALUE`.

No Microsoft internal cost or capacity data are inferred.

## AI model benchmark

`ai_cost_benchmark.csv` uses the LiveBench 2026-06-25 release. The cost field is **external cost per successful benchmark task**, not a NAAIL professional-verification rate.

## Human–AI experiment

T0 Human only; T1 Human+AI; T2 Human+AI+explanation; T3 Human+AI+contradictory evidence. The 15-test harness validates the **structure only**. Participant execution remains `DESIGN_COMPLETE_NOT_EXECUTED`.

## CI status

A dedicated GitHub Actions workflow is published at `.github/workflows/microsoft_poc_v1_15_test.yml` for future push/PR validation. **CI success is not claimed until a completed GitHub Actions run is separately verified.**

## Scientific success boundary

The 15/15 automated artifact-validation result does **not** complete the broader scientific success gate.

Still open:
- actual participant T0–T3 experiment;
- MSFT Fama–French regression;
- aggregate PatentsView analysis;
- NAAIL-specific professional-task model benchmark / Cost per Verified Professional Output™;
- remaining falsification/robustness challenges;
- independent replication.

## Next gate

Do not advance to SAP/Walmart/Intuit/Shopify/JPMorgan/ExxonMobil/Fluor until Microsoft V1 is independently replicated and the remaining scientific gates are completed.

**Production approval: NO. Scientific validation: PENDING INDEPENDENT REPLICATION. Final maturity: `RESEARCH_PROTOTYPE`.**
