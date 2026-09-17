# NAAIL OpenLab™ — Multi-Company Free-Data Gate

**Date:** 2026-09-17  
**Maturity:** `RESEARCH_PROTOTYPE`  
**Purpose:** select replication companies only where public/free evidence can be accessed reproducibly.  
**Architecture:** exactly two permanent cores — Stable Knowledge Core™ + Replaceable Technology Core™. No third core.

## Decision

Start the replication cohort with seven U.S. SEC 10-K issuers for which both structured SEC evidence and IEX market data are directly verifiable in the current environment:

1. Microsoft Corporation (`MSFT`, CIK `0000789019`) — Golden Anchor
2. Walmart Inc. (`WMT`, CIK `0000104169`)
3. JPMorgan Chase & Co. (`JPM`, CIK `0000019617`)
4. Intuit Inc. (`INTU`, CIK `0000896878`)
5. Exxon Mobil Corporation (`XOM`, CIK `0000034088`)
6. Fluor Corporation (`FLR`, CIK `0001124198`)
7. The Boeing Company (`BA`, CIK `0000012927`)

Cross-border extension candidates are retained but separated from the first comparable cohort:

8. Shopify Inc. (`SHOP`, CIK `0001594805`) — public SEC/iXBRL and IEX evidence available; cross-border issuer considerations require explicit treatment.
9. SAP SE (`SAP`, CIK `0001000184`) — public SEC 20-F/iXBRL and U.S. ADR market evidence available; IFRS/ADR comparability requires a jurisdiction/accounting adapter.

## Free/public evidence stack

### SEC EDGAR / XBRL
- SEC EDGAR filings are public.
- SEC CompanyFacts / CompanyConcept APIs are public structured-XBRL interfaces subject to SEC fair-access rules.
- Recent annual filings with interactive XBRL are verified for the selected cohort.
- CAM/ICFR evidence is taken from the public auditor report in the annual filing where applicable.

### Market data
- IEX market-data access is verified through the connected Alpaca market-data source for all nine tickers: `MSFT`, `WMT`, `JPM`, `INTU`, `XOM`, `FLR`, `BA`, `SHOP`, and `SAP`.
- Provider terms apply. Market availability is not treated as public-domain status.

### Factor data
- Kenneth R. French Data Library provides public academic factor series suitable for CAPM/FF3/FF5 research designs.
- U.S. factor models are the default for the seven-company U.S. cohort.
- Shopify/SAP require explicit regional/incorporation/ADR model-selection logic rather than automatic reuse of the U.S.-issuer specification.

### Patent / innovation data
- USPTO PatentsView remains an open-access data resource.
- During the 2026 migration to the USPTO Open Data Portal, bulk downloads/data dictionaries remain available while some API/search functions are temporarily paused or reintroduced.
- Company-assignee normalization must be validated before patent counts or citations are claimed.

### Additional free/public sources
- FRED macroeconomic series.
- Issuer annual reports / investor-relations materials.
- Public GitHub metadata where an identifiable company organization exists.
- OpenAlex/Crossref for bibliographic metadata where needed.

## Cohort design

### Cohort A — start now
`MSFT`, `WMT`, `JPM`, `INTU`, `XOM`, `FLR`, `BA`

Common minimum modules:
1. SEC annual filing + XBRL provenance
2. standardized accounting features
3. CAM / ICFR evidence mapping
4. bounded filing-text features
5. market-return features
6. factor-model input package
7. innovation proxies
8. Evidence Passport™
9. falsification register
10. Human Approval Gate™

### Cohort B — cross-border extension
`SHOP`, `SAP`

Do not pool Cohort B mechanically with Cohort A. Add explicit GAAP/IFRS, issuer-jurisdiction, currency, listing/ADR, and factor-model adapters first.

## Scientific boundary

This file starts the **free-data replication infrastructure**. It does not claim that companies 2–9 have completed the Microsoft end-to-end scientific validation. Microsoft remains the Golden Anchor until its remaining factor, innovation, professional-benchmark, human-experiment, falsification, and independent-replication gates are closed.

## Status vocabulary

- Data access verified: `FREE_PUBLIC_SOURCE_VERIFIED`
- Market connector verified: `CONNECTED_MARKET_DATA_VERIFIED`
- Pipeline scaffolded, not run: `REGISTERED_NOT_EXECUTED`
- Executed derived result: `DERIVED_EXECUTED`
- Scientifically replicated: only after independent replication and Human Gate approval.

**PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**
