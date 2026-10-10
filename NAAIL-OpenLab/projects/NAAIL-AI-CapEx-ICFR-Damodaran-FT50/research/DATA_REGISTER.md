# Research data register — sourcing plan (no downloads claimed)

| Source | Candidate fields | Public link | Handling |
|---|---|---|---|
| SEC EDGAR filings | 10-K, 10-Q, 8-K, audit/internal controls, AI-capex narrative | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | Record accession number, public availability timestamp, textual evidence, SEC fair-access policies |
| SEC Financial Statement Data Sets | XBRL facts and financial statement measures | https://www.sec.gov/dera/data/financial-statement-data-sets.html | Standard accounting facts are NOT AI-specific CapEx |
| Damodaran data | Industry WACC, ROIC, reinvestment / valuation conventions | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html | Industry aggregates, not company-level proprietary values |
| Kenneth French | Factor returns and reference portfolios | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Confirm factor vintage and frequency |
| Google TimesFM | Forecasting code and model assets | https://github.com/google-research/timesfm | Evaluate each weight's license separately |
| Stanford filings corpora | Processed filing text | https://github.com/Stanford-Advanced-FinTech-Lab-SAFTL/stanford-edgar-filings-dataset | Check exact dataset version, license, temporal coverage |

## Required provenance columns
firm_cik, accession_number, fiscal_year, filed_at_utc, publicly_available_at_utc, field_name, value, unit, document_url, disclosure_quote_start, disclosure_quote_end, acquisition_timestamp, source_version, licensed_for_redistribution, coder_id, validation_status.

## No-leakage contract
A predictor with source public timestamp AFTER the forecast cutoff is prohibited. Log every join, backfill and restatement adjustment.

## Status
No bulk SEC filings, restricted raw datasets, or proprietary valuation inputs have been downloaded or uploaded by this scaffold.
