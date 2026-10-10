# PROJECT MASTER INDEX — AICapEx-Value

**Full title:** AI Capital Expenditure, Earnings–Cash Flow Divergence, and the Pricing of Economic Value: Evidence from IFRS Reporting Firms  
**Short name:** AICapEx-Value  
**Primary target:** The Accounting Review (TAR)  
**Status:** First empirical research-design draft; no empirical results estimated yet.

## Canonical archive
Google Drive is the source of truth:  
https://drive.google.com/drive/folders/1LjayXBs0qielb5rWLZVPyhOqqCBDkDEJ

Main manuscript:  
https://docs.google.com/document/d/15E9e1-VaLb9irRBVjAnrv3_5qqXsI2r_/edit

## Research objective
Examine whether capital markets distinguish economically value-creating AI investment from accounting earnings accompanied by large cash commitments, and whether IFRS disclosure improves that distinction.

## Hypotheses
- **H1:** Greater AI investment intensity is associated with larger earnings–cash-flow divergence.
- **H2:** For AI-intensive firms, the capital-market response to earnings is stronger when ROIC exceeds WACC.
- **H3:** Higher-quality IFRS disclosure improves the market's differentiation between positive and negative value-creation spreads.

## Core constructs
- AI Investment Intensity
- Earnings–Cash Flow Divergence
- Value-Creation Spread = ROIC − WACC
- AI Disclosure Quality
- Fama–French-adjusted CAR

## Free-data architecture
- IFRS ESEF/UKSEF/XBRL filings and annual reports
- filings.xbrl.org
- Kenneth French factor data
- Aswath Damodaran industry/WACC/valuation datasets
- SRAF / Analytext for a separate U.S.-GAAP validation sample
- Hugging Face for licensed/public NLP models and derived text resources
- Kaggle for public notebooks/benchmark mirrors where licensing permits

## Google Drive structure
- 01_MANUSCRIPT
- 02_LITERATURE_REPLICATION
- 03_FREE_DATA_SOURCES
- 04_TEXT_NLP
- 05_CAPITAL_MARKET
- 06_CODE
- 07_RESULTS
- 08_REPLICATION_PACKAGE
- 09_CROSS_PLATFORM

## GitHub
Project section:  
https://github.com/Saehon/Saeid-Homayoun/tree/main/AICapEx-Value

Purpose: code, provenance, reproducibility notes, public-safe metadata, and replication scripts. Restricted raw data must never be committed.

## Hugging Face
Authenticated account: SADHON.  
Planned dataset/research asset name: **SADHON/AICapEx-Value-IFRS**.  
Current connector is read-only for repositories, so remote creation/upload must wait for a write-capable connection or a user-created blank repository.

## Kaggle
Planned slug: **aicapex-value-ifrs**.  
Use for public notebooks, benchmark subsets and reproducible demonstrations. A Kaggle connector is not currently available in this ChatGPT environment, so no remote Kaggle asset is claimed as created.

## Governance
Google Drive remains authoritative. GitHub/Hugging Face/Kaggle are mirrors or execution/discovery layers. Preserve prior versions; do not delete source artifacts; record licenses, retrieval dates, hashes, and transformation steps.
