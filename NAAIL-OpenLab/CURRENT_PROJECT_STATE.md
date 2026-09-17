# NAAIL OpenLab™ — Current Project State

**Canonical public state date:** 2026-09-17  
**Architecture target:** `V2026.3 Multi-Agent Digital Twin`  
**Constitution:** `FROZEN`  
**Permanent cores:** exactly two — **Stable Knowledge Core™** + **Replaceable Technology Core™**  
**Validated executable checkpoint:** `v0.2.3 / Audit Workspace V0.4 / Prototype 003`  
**Golden Anchor company POC:** `NAAIL-MSFT-POC-V1 / RESEARCH_PROTOTYPE`  
**Newest replication release:** `MULTI_COMPANY_FREE_DATA_V1 / RESEARCH_PROTOTYPE`

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Constitutional rule

The **[NAAIL Two-Core Constitution](./TWO_CORE_CONSTITUTION.md)** is the governing architecture rule. No company, domain, dataset, AI model, vendor, agent or prototype may create a third permanent core.

## Microsoft Golden Anchor POC V1

[Open Microsoft POC V1](./prototypes/microsoft-poc-v1/MICROSOFT_POC_V1.md)

Microsoft Corporation remains the first integrated Golden Anchor used to test whether NAAIL can connect real public company evidence, reproducible analysis, multiple domain modules, a company Digital Twin, AI-cost measurement, behavioral experiment design, Evidence Passport™ and Human Gate™ in one bounded package.

### Current Microsoft public package

- [Build & Validation Contract](./prototypes/microsoft-poc-v1/MICROSOFT_POC_V1_BUILD_AND_VALIDATION_SPEC.md)
- [Executed Results](./prototypes/microsoft-poc-v1/prototype_v1_results.md)
- [15-Test Validation Matrix](./prototypes/microsoft-poc-v1/VALIDATION_MATRIX_15_TESTS.md)
- [Timestamped 15-Test Run](./prototypes/microsoft-poc-v1/VALIDATION_RUN_15_TESTS_2026_09_16.md)
- [Falsification & Robustness Register](./prototypes/microsoft-poc-v1/FALSIFICATION_ROBUSTNESS_REGISTER.md)
- [Fama–French Reproducibility Status](./prototypes/microsoft-poc-v1/MICROSOFT_FAMA_FRENCH_EXECUTION_STATUS_2026_09_16.md)
- [GitHub / Google Drive Sync Manifest](./prototypes/microsoft-poc-v1/SYNC_MANIFEST_2026_09_16.md)
- [Prototype Dashboard](./prototypes/microsoft-poc-v1/dashboard.html)

### Executed Microsoft evidence

- FY2026 Microsoft SEC/interactive-XBRL public facts, including income statement, balance sheet, cash-flow and segment evidence;
- reproducible accounting and finance calculations;
- FY2026 MSFT market-price evidence and FY-end FRED DGS10 snapshot;
- two FY2026 CAM mappings and ICFR status;
- bounded filing-text feature extraction without redistributing raw filing sections;
- R&D intensity plus Microsoft public GitHub metadata snapshot;
- synthetic Microsoft-like ABC/TDABC/AI-cost microcase anchored only to public company scale;
- external LiveBench 2026-06-25 benchmark snapshot, separated from NAAIL professional-task validation;
- Evidence Passport schema/instance and research-publication Human Gate boundary;
- T0–T3 Human–AI experiment structure/design;
- historical offline reproducibility harness: **12/12 PASS**;
- dedicated unified artifact-validation harness: **15/15 PASS**.

The dedicated harness `tests/test_microsoft_poc_v1_15_contract.py` executed on 2026-09-16:

```text
...............                                                          [100%]
15 passed in 0.08s
```

This closes the former TEST 03 variable-dictionary and TEST 14 dashboard-reconciliation automation gaps. A dedicated GitHub Actions workflow is published, but **CI success is not claimed until a completed run is separately verified**.

### Microsoft Fama–French milestone

The Microsoft Finance module now has a published reproducibility runner, frozen monthly MSFT input, and GitHub Actions workflow for CAPM/FF3/FF5. Its current verified status remains `REGISTERED_NOT_EXECUTED` because no completed workflow run and coefficient/provenance output have been verified. No alpha, beta, factor loading, p-value or R² is claimed.

### Major Microsoft scientific gates still open

- verified Fama–French execution and robustness;
- aggregate PatentsView patent/citation analysis and technology-diversity measures;
- NAAIL-specific professional-task model verification and Cost per Verified Professional Output™;
- actual participant execution of the T0–T3 Human–AI experiment;
- remaining falsification/robustness challenges;
- independent cross-source and reviewer replication.

Therefore Microsoft V1 remains **`RESEARCH_PROTOTYPE`**. Production approval remains **NO** and scientific validation remains **PENDING INDEPENDENT REPLICATION**. Microsoft V1 does not change Prototype 003's status as the only `EXECUTED_VALIDATED` checkpoint.

## Multi-Company Free-Data Replication V1

[Open Multi-Company Cohort](./MULTI_COMPANY_FREE_DATA_COHORT.md)  
[Open Replication Package](./prototypes/multi-company-free-data-v1/README.md)

NAAIL has now published an official nine-company cohort selected from companies with a documented public/free evidence path and verified connected market access.

### Final cohort

**Wave 0 — Golden Anchor**

1. Microsoft Corporation (`MSFT`)

**Wave 1 — U.S. SEC replication cohort**

2. Walmart Inc. (`WMT`)
3. JPMorgan Chase & Co. (`JPM`)
4. Intuit Inc. (`INTU`)
5. Exxon Mobil Corporation (`XOM`)
6. Fluor Corporation (`FLR`)
7. The Boeing Company (`BA`)

**Wave 2 — controlled cross-border extension**

8. Shopify Inc. (`SHOP`)
9. SAP SE (`SAP`)

Wave 2 must not be mechanically pooled with Wave 1. Jurisdiction, GAAP/IFRS, currency, listing/ADR and factor-model adapters must be explicit first.

### Public/free evidence gate

The cohort is supported by a documented minimum evidence stack:

- SEC EDGAR annual filings and inline XBRL;
- SEC CompanyFacts / CompanyConcept interfaces subject to SEC fair-access rules;
- connected IEX market evidence for all nine tickers;
- Kenneth R. French factor data, with cross-border model review where required;
- USPTO PatentsView / Open Data Portal public patent-data routes subject to current service availability, source terms and entity-resolution controls;
- FRED macroeconomic data;
- issuer annual reports / investor-relations disclosures;
- public GitHub metadata where applicable;
- OpenAlex/Crossref metadata where needed.

Public access does not equal public-domain status. Registered data access does not equal executed analysis.

### Standard replication contract

For each company:

`Public Filing → XBRL/Financial Evidence → Variable Dictionary → Audit/CAM/ICFR Evidence → Bounded Text → Market Data → Factor Package → Innovation Evidence → Evidence Passport™ → Robustness/Falsification → Human Gate™`

### Current company status

- `MSFT`: `EXECUTED_PARTIAL_GOLDEN_ANCHOR`.
- `WMT`, `JPM`, `INTU`, `XOM`, `FLR`, `BA`: `REGISTERED_NOT_EXECUTED`.
- `SHOP`, `SAP`: `REGISTERED_NOT_EXECUTED_CROSS_BORDER`.

No firm is promoted merely because its data are accessible. The multi-company SEC probe workflow is published at `.github/workflows/multi_company_free_data_probe.yml`, but a successful completed run is not claimed until separately verified.

### Published multi-company records

- [Public Release Record](./prototypes/multi-company-free-data-v1/MULTI_COMPANY_FREE_DATA_PUBLIC_RELEASE_2026_09_17.md)
- [GitHub Publication Manifest](./prototypes/multi-company-free-data-v1/GITHUB_PUBLICATION_MANIFEST_2026_09_17.md)
- [Final Company Selection & Execution Order](./prototypes/multi-company-free-data-v1/FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md)
- [Free-Data Company Gate](./prototypes/multi-company-free-data-v1/FREE_DATA_COMPANY_GATE_2026_09_17.md)
- [Company Registry CSV](./prototypes/multi-company-free-data-v1/company_registry_free_public_v1.csv)

## Stable Knowledge Core™

Governed scientific/professional meaning includes accounting, auditing, finance, economics, management, behavioral science, innovation/entrepreneurship theory, Nobel-inspired theory, IFRS/assurance knowledge, sustainability, causal inference, research design, construct definitions, professional judgment, replication, falsification and scientific governance.

Stable management-accounting knowledge includes Balanced Scorecard/Strategy Maps, ABC, TDABC, budgeting, responsibility accounting, variance analysis, cost pools/drivers, profitability, capacity and performance measurement.

## Replaceable Technology Core™

Replaceable implementation includes LLMs, agents, model routers, RAG/GraphRAG/KAG frameworks, vector/graph databases, Python/R/Stata, simulation engines, APIs, connectors, GitHub packages, MCP/A2A, benchmark/evaluation tools, AI FinOps, observability/telemetry and dashboard/visualization software.

## Current public maturity boundary

| Capability | Current public status |
|---|---|
| Two-Core Constitution | `ARCHITECTURE_ADOPTED / FROZEN` |
| Prototype 003 | `EXECUTED_VALIDATED` for frozen synthetic scope |
| Microsoft Golden Anchor POC V1 | `RESEARCH_PROTOTYPE` — 15/15 artifact-validation PASS; broader scientific gates open |
| Multi-Company Free-Data Replication V1 | `RESEARCH_PROTOTYPE` — cohort/access infrastructure published; companies 2–9 not yet executed |
| Prototype 004 provider harness | `IMPLEMENTED_EXECUTION_GATED` |
| Management Accounting & AI Cost Intelligence Layer™ | `PATENT_HOLD_NON_ENABLING` |
| Open Model Benchmark & Cost Intelligence Layer™ | `PATENT_HOLD_NON_ENABLING` |
| Visualization & Decision Intelligence Layer™ | `PATENT_HOLD_NON_ENABLING` |
| Other cross-cutting architecture layers | architecture / patent-hold statuses as registered |
| Specialist programmes/agents | modular; not cores |

Machine-readable state: [`architecture/platform_capability_registry.json`](./architecture/platform_capability_registry.json)

## Falsification and robustness rule

Major promoted results must be challenged using alternative authoritative sources, alternative models/specifications, period sensitivity, contradictory evidence, construct-validity checks, contamination/leakage review and independent reviewer replay where applicable. A contradictory result must be preserved rather than silently removed.

Allowed challenge outcomes include:

`SUPPORTED_AFTER_CHALLENGE` · `REVISED_AFTER_CHALLENGE` · `REQUEST_MORE_EVIDENCE` · `REJECTED_BY_FALSIFICATION` · `BLOCKED` · `NOT_EXECUTED`

## Current execution order

1. Finish the remaining Microsoft scientific gates.
2. Execute `WMT → JPM → INTU → XOM → FLR → BA` with the standardized public-data runner.
3. Run Wave 1 cross-company robustness and independent replication.
4. Activate `SHOP` and `SAP` only after cross-border/jurisdiction/accounting/factor adapters pass review.
5. Compare all nine companies through common Evidence Passport™, falsification and Human Gate outputs without forcing artificial comparability.

## Governance requirement

Every prototype/layer/programme must use, where applicable: provenance, license controls, Evidence Passport™, causal/decision DAGs, versioning, reproducibility, replication, falsification, red-team/adversarial review and Human Approval Gate™. Architecture documentation, public-data availability and artifact-integrity tests do not equal independent scientific validation.

`NOT EXECUTED` must never be silently converted into `PASS`.

## Patent-first boundary

This state record is non-enabling. Detailed unpublished core algorithms, graph/provenance contracts, dependency/revocation logic and patent-sensitive embodiments remain private. Public prototypes publish bounded reproducible arithmetic, source registries and public facts without disclosing confidential patent claim material.

No patent application is represented as filed as of 2026-09-17; **Patent Pending** is not claimed.

## Canonical links

- [Two-Core Constitution](./TWO_CORE_CONSTITUTION.md)
- [Microsoft POC V1](./prototypes/microsoft-poc-v1/MICROSOFT_POC_V1.md)
- [15-Test Validation Matrix](./prototypes/microsoft-poc-v1/VALIDATION_MATRIX_15_TESTS.md)
- [Timestamped 15-Test Run](./prototypes/microsoft-poc-v1/VALIDATION_RUN_15_TESTS_2026_09_16.md)
- [Fama–French Reproducibility Status](./prototypes/microsoft-poc-v1/MICROSOFT_FAMA_FRENCH_EXECUTION_STATUS_2026_09_16.md)
- [Multi-Company Free-Data Cohort](./MULTI_COMPANY_FREE_DATA_COHORT.md)
- [Multi-Company Public Release](./prototypes/multi-company-free-data-v1/MULTI_COMPANY_FREE_DATA_PUBLIC_RELEASE_2026_09_17.md)
- [Final Company Selection & Execution Order](./prototypes/multi-company-free-data-v1/FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md)
- [Public Platform Overview](./PUBLIC_PLATFORM_OVERVIEW.md)
- [Start Here](./00_START_HERE.md)
- [Capability Registry](./architecture/platform_capability_registry.json)
- [Capability & Maturity Matrix](./architecture/PLATFORM_CAPABILITY_MATRIX.md)
- [Prototype 003 Public Runtime](./Prototype_003/runtime/README.md)

> **Two Permanent Cores → Cross-Cutting Layers → Specialist Agents/Programmes → Evidence Governance → Human Approval.**
