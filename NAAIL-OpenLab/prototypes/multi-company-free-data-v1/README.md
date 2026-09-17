# Multi-Company Free-Data Replication V1

**Status:** `RESEARCH_PROTOTYPE` / replication infrastructure started  
**Golden Anchor:** Microsoft Corporation  
**Rule:** exactly two permanent cores; no architecture expansion.

This package operationalizes the next NAAIL replication step using only public/free data sources with documented provenance and access conditions.

## Final selected cohort

The official nine-company cohort and execution order are published in:

[FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md](./FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md)

### Wave 0 — Golden Anchor

- Microsoft (`MSFT`)

### Wave 1 — comparable U.S. public-data replication cohort

- Walmart (`WMT`)
- JPMorgan Chase (`JPM`)
- Intuit (`INTU`)
- Exxon Mobil (`XOM`)
- Fluor (`FLR`)
- Boeing (`BA`)

### Wave 2 — cross-border extension after adapters

- Shopify (`SHOP`)
- SAP (`SAP`)

All nine are retained. Wave 2 is deliberately separated until jurisdiction, GAAP/IFRS, currency, listing/ADR and factor-model adapters are explicit.

## Current verified source families

1. SEC EDGAR annual filings and inline XBRL
2. SEC CompanyFacts / CompanyConcept APIs
3. connected IEX market data for all nine tickers
4. Kenneth R. French factor library
5. USPTO PatentsView/Open Data Portal bulk patent data
6. FRED macroeconomic data
7. issuer investor-relations/annual-report materials
8. public GitHub metadata where applicable

## Current package files

- `FINAL_COMPANY_SELECTION_AND_EXECUTION_ORDER_2026_09_17.md` — final cohort, waves, adapters and execution plan
- `FREE_DATA_COMPANY_GATE_2026_09_17.md` — evidence-access decision and cohort rules
- `company_registry_free_public_v1.csv` — company/CIK/form/fiscal-period/data-access registry
- SEC access/probe code and the dedicated free-data probe workflow

## Execution sequence

For every company:

`SEC filing → XBRL facts → variable dictionary → CAM/ICFR → bounded text → market returns → factor package → innovation proxies → Evidence Passport™ → falsification → Human Gate™`

No company is labeled executed merely because its public data are accessible. `REGISTERED_NOT_EXECUTED` remains the default until a reproducible run is completed and reviewed.

## Comparability controls

- JPMorgan requires a bank-specific accounting-variable adapter.
- ExxonMobil requires an energy-sector adapter.
- Fluor requires engineering/construction contract-accounting controls.
- Boeing requires aerospace/program-accounting controls.
- Shopify and SAP remain outside the first pooled U.S. cohort until cross-border/GAAP-IFRS/currency/listing-factor adapters are explicit.

## Current execution order

1. Finish the remaining Microsoft scientific gates.
2. Execute WMT → JPM → INTU → XOM → FLR → BA with the standardized public-data runner.
3. Run Wave 1 cross-company robustness and independent replication.
4. Activate SHOP and SAP only after cross-border adapters pass review.
5. Compare all nine companies through common Evidence Passport™, falsification and Human Gate outputs without forcing artificial accounting comparability.

**PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**
