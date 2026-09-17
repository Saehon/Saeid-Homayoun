# NAAIL OpenLab™ — Multi-Company Free-Data Replication Public Release

**Public release date:** 2026-09-17  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Golden Anchor:** Microsoft Corporation  
**Architecture:** exactly two permanent cores — Stable Knowledge Core™ + Replaceable Technology Core™. No third permanent core.  
**Public-data rule:** use only public/free or connected evidence with documented provenance, access conditions and rights/terms boundaries.

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Public release scope

This release publishes the official NAAIL nine-company free-data replication cohort and its execution governance. It extends the Microsoft Golden Anchor programme into a controlled replication design without claiming that the newly selected company pipelines have already been executed.

## Final cohort

### Wave 0 — Golden Anchor

1. Microsoft Corporation (`MSFT`)

### Wave 1 — U.S. SEC replication cohort

2. Walmart Inc. (`WMT`)
3. JPMorgan Chase & Co. (`JPM`)
4. Intuit Inc. (`INTU`)
5. Exxon Mobil Corporation (`XOM`)
6. Fluor Corporation (`FLR`)
7. The Boeing Company (`BA`)

### Wave 2 — controlled cross-border extension

8. Shopify Inc. (`SHOP`)
9. SAP SE (`SAP`)

Wave 2 is retained in the official cohort but must not be mechanically pooled with the U.S. replication cohort. Jurisdiction, GAAP/IFRS, currency, listing/ADR and factor-model adapters must be explicit first.

## Published evidence-access decision

At the selection date, the cohort has a documented minimum public/free evidence stack:

- SEC EDGAR annual filings and inline XBRL;
- SEC CompanyFacts / CompanyConcept structured-XBRL interfaces subject to SEC fair-access rules;
- connected IEX market-data access for all nine tickers;
- Kenneth R. French factor data for research designs, with cross-border model-selection review where required;
- USPTO PatentsView / Open Data Portal public patent-data routes, subject to current service availability, source terms and entity-resolution controls;
- FRED macroeconomic data;
- issuer annual reports / investor-relations disclosures;
- public GitHub metadata where applicable;
- OpenAlex/Crossref bibliographic metadata where needed.

Public accessibility is not treated as public-domain status, and registered connectors are not treated as executed analyses.

## Standard replication contract

For each company:

`Public Filing → XBRL/Financial Evidence → Variable Dictionary → Audit/CAM/ICFR Evidence → Bounded Text → Market Data → Factor Package → Innovation Evidence → Evidence Passport™ → Robustness/Falsification → Human Gate™`

Common minimum outputs include a source/provenance registry, filing/XBRL extraction record, standardized and sector-specific variable dictionary, audit/CAM/ICFR mapping where applicable, bounded filing-text features, market-return package, factor-model record, innovation evidence with entity-resolution notes, company-specific Evidence Passport™, falsification/robustness record and Human Gate decision.

## Sector and jurisdiction controls

- `MSFT`: technology/cloud/AI reference implementation.
- `WMT`: retail inventory, margins, lease and supply-chain controls.
- `JPM`: bank-specific balance-sheet, credit-loss, capital and financial-instrument variables.
- `INTU`: software/subscription/revenue-recognition and AI-service variables.
- `XOM`: reserves, commodity exposure, impairment and capital-intensity variables.
- `FLR`: contract-estimate, project-risk and engineering/construction controls.
- `BA`: program accounting, contract estimates, production and aerospace/defense risk controls.
- `SHOP`: cross-border issuer/currency and regional factor-selection controls.
- `SAP`: IFRS, 20-F, ADR and European/developed-market factor-selection controls.

## Execution status at release

- `MSFT`: `EXECUTED_PARTIAL_GOLDEN_ANCHOR`; broader scientific gates remain open.
- `WMT`, `JPM`, `INTU`, `XOM`, `FLR`, `BA`: `REGISTERED_NOT_EXECUTED`.
- `SHOP`, `SAP`: `REGISTERED_NOT_EXECUTED_CROSS_BORDER`.

No company is promoted merely because its data are accessible.

## Execution order

1. Finish remaining Microsoft scientific gates.
2. Execute the standardized replication runner for `WMT → JPM → INTU → XOM → FLR → BA`.
3. Run Wave 1 cross-company robustness and independent replication.
4. Activate `SHOP` and `SAP` only after cross-border adapters pass review.
5. Compare all nine companies through common Evidence Passport™, falsification and Human Gate outputs without forcing artificial accounting comparability.

## Canonical public GitHub records

- [`FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md`](./FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md)
- [`FREE_DATA_COMPANY_GATE_2026_09_17.md`](./FREE_DATA_COMPANY_GATE_2026_09_17.md)
- [`company_registry_free_public_v1.csv`](./company_registry_free_public_v1.csv)
- [`README.md`](./README.md)
- SEC public-data probe code under `code/`
- GitHub Actions workflow: `.github/workflows/multi_company_free_data_probe.yml`
- Top-level reviewer entry: `NAAIL-OpenLab/MULTI_COMPANY_FREE_DATA_COHORT.md`

## Google Drive mirrors

Canonical NAAIL OpenLab folder:

https://drive.google.com/drive/folders/193O-ICy6843wEgP0gy713cGUbYq8rGy0

- Free-Data Gate & Replication Cohort: https://docs.google.com/document/d/1ttkGkKns5GYRBruO5qFFC_vLBsCVJocGklVc5FoSrSY/edit
- Final Multi-Company Selection & Execution Order: https://docs.google.com/document/d/1syNQtUqKTWzqEui5LNNMtFetHaxtMOPS0zcXzW9erGo/edit

## Scientific and CI boundary

This release is a cohort-selection, data-access and reproducibility-infrastructure release. It does not claim company-level empirical results for companies 2–9. The multi-company SEC probe workflow is published, but no successful GitHub Actions execution is claimed unless a completed workflow run is separately verified.

Microsoft remains the Golden Anchor and NAAIL remains `RESEARCH_PROTOTYPE`. Production approval is not claimed, independent scientific validation is not claimed, and `NOT EXECUTED` is never converted into `PASS` merely because data are available.
