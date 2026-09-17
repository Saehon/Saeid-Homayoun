# NAAIL OpenLab™ — Multi-Company Free-Data Replication V1

**Date:** 2026-09-17  
**Status:** `RESEARCH_PROTOTYPE`  
**Golden Anchor:** Microsoft Corporation

[Open the executable replication package →](./prototypes/multi-company-free-data-v1/README.md)

## First public-data cohort

`MSFT · WMT · JPM · INTU · XOM · FLR · BA`

These seven companies have verified public SEC annual-report/iXBRL evidence and verified connected IEX market-data access. Their replication pipelines are scaffolded but, except for the bounded Microsoft Golden Anchor work, are not yet claimed as executed scientific results.

## Cross-border extension

`SHOP · SAP`

Both have verified SEC/iXBRL and U.S.-market data access, but they remain a separate extension until issuer jurisdiction, accounting framework, currency/listing, and factor-model adapters are explicit.

## Public/free evidence sources

- SEC EDGAR and SEC XBRL APIs
- connected IEX market data
- Kenneth R. French factor data
- USPTO PatentsView / Open Data Portal bulk patent data
- FRED
- issuer annual reports and investor-relations materials
- public GitHub metadata where appropriate
- OpenAlex / Crossref metadata where appropriate

## Package

- [Free-data company gate](./prototypes/multi-company-free-data-v1/FREE_DATA_COMPANY_GATE_2026_09_17.md)
- [Company registry](./prototypes/multi-company-free-data-v1/company_registry_free_public_v1.csv)
- [Package README](./prototypes/multi-company-free-data-v1/README.md)
- `prototypes/multi-company-free-data-v1/code/sec_free_public_probe.py`

The canonical two-core architecture remains unchanged. Data access is not treated as validation; missing, conflicting, or unsupported evidence must remain visible through the Evidence Passport™, falsification register, and Human Gate™.

**PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**
