# ECONOVA-S™ v0.3 — Official Public-Data Ingestion Layer

This stage turns the v0.2 research workbench into a chronology-aware empirical data pipeline using three authoritative public sources:

1. **Fama–French Data Library** — market/factor structure and replication benchmarks.
2. **Aswath Damodaran / NYU Stern** — industry valuation, growth, cost-of-capital and EVA priors.
3. **SEC EDGAR XBRL CompanyFacts** — firm-level accounting fundamentals with filing-date chronology.

## Scientific objective

Build a publication-grade research panel in which every variable is tied to a source, transformation, observation date, information-availability date and empirical role.

```text
SEC CompanyFacts firm fundamentals
            +
Fama–French market factors
            +
Damodaran industry priors
            ↓
Chronology-safe research panel
            ↓
Variable DNA™ + source manifest
            ↓
Identification Gate
            ↓
Tables 1–6 / OOS / replication / red team
            ↓
Evidence Passport™ + Human Gate
```

## Important chronology rule

SEC accounting facts become usable only on or after the filing date used in the empirical design. `latest_filed_fact()` therefore filters on `filed <= information_date` before selecting an observation.

Fama–French factors are attached backward in time with `merge_asof`; the adapter never intentionally selects a factor observation after the information date.

## Damodaran rule

Damodaran tables are industry-level benchmarks. They are not automatically merged to SEC firms. A documented SIC/industry crosswalk is required before they enter firm-level tests. This prevents silent or arbitrary industry mapping.

## Current adapters

- `fetch_fama_french_5factor()`
- `fetch_damodaran('wacc'|'fundgr'|'pedata'|'eva')`
- `SECClient.ticker_map()`
- `SECClient.companyfacts(cik)`
- `companyfacts_to_long()`
- `latest_filed_fact()`
- `attach_latest_ff_factors()`

## SEC fair-access requirement

`SECClient` requires a User-Agent containing a contact email. Large-scale studies should cache requests and prefer SEC bulk archives.

## Run tests

```bash
pip install -r requirements.txt
pytest -q
```

The included tests are offline and focus on chronology and transformation logic. They do not claim to validate live third-party availability.

## Scientific status

v0.3 is an ingestion/replication development stage. It does not by itself establish construct validity, causal identification or scientific discovery.

`discovery_claim_allowed = false`
