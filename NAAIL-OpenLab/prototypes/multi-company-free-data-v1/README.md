# Multi-Company Free-Data Replication V1

**Status:** `RESEARCH_PROTOTYPE` / replication infrastructure started  
**Golden Anchor:** Microsoft Corporation  
**Rule:** exactly two permanent cores; no architecture expansion.

This package operationalizes the next NAAIL replication step using only public/free data sources with documented provenance and access conditions.

## Cohort A — comparable U.S. public-data cohort

- Microsoft (`MSFT`) — Golden Anchor
- Walmart (`WMT`)
- JPMorgan Chase (`JPM`)
- Intuit (`INTU`)
- Exxon Mobil (`XOM`)
- Fluor (`FLR`)
- Boeing (`BA`)

## Cohort B — cross-border extension after adapters

- Shopify (`SHOP`)
- SAP (`SAP`)

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

- `FREE_DATA_COMPANY_GATE_2026_09_17.md` — evidence-access decision and cohort rules
- `company_registry_free_public_v1.csv` — company/CIK/form/fiscal-period/data-access registry

## Execution sequence

For every Cohort A company:

`SEC filing → XBRL facts → variable dictionary → CAM/ICFR → bounded text → market returns → factor package → innovation proxies → Evidence Passport™ → falsification → Human Gate™`

No company is labeled executed merely because its public data are accessible. `REGISTERED_NOT_EXECUTED` remains the default until a reproducible run is completed and reviewed.

## Comparability controls

- JPMorgan requires a bank-specific accounting-variable adapter.
- ExxonMobil requires an energy-sector adapter.
- Fluor requires engineering/construction contract-accounting controls.
- Boeing requires aerospace/program-accounting controls.
- Shopify and SAP remain outside the first pooled U.S. cohort until cross-border/GAAP-IFRS/currency/listing-factor adapters are explicit.

## Next build task

Create one standardized public-data ingestion/validation runner for Cohort A. The runner must produce company-specific Evidence Passports and retain failures, missing tags, conflicting periods, and unsupported mappings rather than silently harmonizing them.

**PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**
