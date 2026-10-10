# AICapEx-Value

**Full project title:** AI Capital Expenditure, Earnings–Cash Flow Divergence, and the Pricing of Economic Value: Evidence from IFRS Reporting Firms

**Target journal:** The Accounting Review (TAR)  
**Short name:** AICapEx-Value  
**Status:** First empirical research-design draft; no estimated results yet.

## Canonical source of truth
Google Drive is the authoritative archive:
https://drive.google.com/drive/folders/1LjayXBs0qielb5rWLZVPyhOqqCBDkDEJ

Main manuscript:
https://docs.google.com/document/d/15E9e1-VaLb9irRBVjAnrv3_5qqXsI2r_/edit

## Research objective
Test whether capital markets distinguish economically value-creating AI investment from accounting earnings accompanied by large cash commitments, and whether IFRS disclosure improves that distinction.

## Main hypotheses
- H1: Greater AI investment intensity is associated with larger earnings–cash-flow divergence.
- H2: For AI-intensive firms, the market response to earnings is stronger when ROIC exceeds WACC.
- H3: Higher-quality IFRS disclosure improves the market's differentiation between positive and negative value-creation spreads.

## Core constructs
- AI Investment Intensity
- Earnings–Cash Flow Divergence
- Value-Creation Spread = ROIC − WACC
- AI Disclosure Quality
- Fama–French-adjusted CAR

## Free-data architecture
- IFRS ESEF/UKSEF/XBRL filings
- filings.xbrl.org
- issuer annual reports
- Kenneth French factor data
- Aswath Damodaran industry/WACC benchmarks
- SRAF / Analytext for U.S. validation
- Hugging Face for NLP models/datasets
- Kaggle for public notebooks/replication mirrors where licensing permits

## Repository structure
- `data/` — data dictionaries, source registries, download scripts
- `src/` — analysis and NLP code
- `replication/` — third-party replication notes and reproduction logs
- `cross_platform/` — Hugging Face and Kaggle synchronization notes

Do not commit licensed or restricted raw data. Preserve provenance, licenses, hashes, and retrieval dates.
