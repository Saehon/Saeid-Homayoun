# Sampling Protocol V1 — frozen 10 October 2026

## Executed selection
Source: DataHub/Open Knowledge S&P 500 constituent CSV, source commit 36472b57910842f4025e8ca8303b93a692d2bbae, modified 2026-10-09 03:19:58 UTC.
URL: https://raw.githubusercontent.com/datasets/s-and-p-500-companies/36472b57910842f4025e8ca8303b93a692d2bbae/data/constituents.csv
Upstream data license: PDDL 1.0; upstream list derives from Wikipedia, NOT directly the SEC. SEC CIKs pending primary cross-check.
Actual records: 503 ticker share-class rows, de-duplicated to 500 distinct issuers by SEC CIK. Dual classes Alphabet GOOG/GOOGL, Fox FOX/FOXA, News Corp NWS/NWSA each counted once.
Exclude 76 financial sector issuers because standard industrial FCFF/operating asset measures are generally non-comparable; preserve complete exclusion register.
Select 424 nonfinancial issuer CIKs, of which 363 are standard corporate operating and 61 special strata (31 Utilities and 30 Real Estate) requiring separate models.
All ten previous case-study issuers included (5 builders: MSFT GOOGL AMZN META ORCL; 5 suppliers: NVDA AVGO MU VRT ANET).
Pre-classification by GICS: 65 other infrastructure supplier candidates, 44 technology/adopter candidates, 31 Utilities and 30 Real Estate special candidates, 244 other nonfinancial firms, plus the ten anchors. These are screening labels, not validated AI exposure.
Screen priorities: P0 = ten old pilot anchors; P1 = 126 possible supply chain/energy/real estate firms; P2 = 288 other potentially exposed nonfinancial firms. All 424 are retained, including future non-AI comparators.

## Critical sample validity caveat
This is a valid documented CURRENT S&P500 screening roster, NOT the final 2019-2025 historical 10-K sample. It excludes bankrupt/delisted issuers and earlier index exits; 2026 survivorship bias prohibits use as representative historical econometric sample.
The user-requested longer-run approximate 2,000-company target is not yet a selected, validated population. Reconstruct the historical 2019-2025 annual 10-K universe from SEC filings and intersect with legal-entity identities, not only S&P500 current constituents.
2026 headquarters, S&P membership, sector and SEC identifiers do not independently prove US domestic 10-K rather than other forms. No AI-specific CapEx, CAM, MW/ICFR or PCAOB eligibility is yet verified for the additional 414 issuers. Columns state NO for those checks, not that the underlying economics are absent.

## Prespecified next screening
1. Annual SEC issuer universe (10-K, firm-year CIK, fiscal year, accession, public timestamp; check 20-F and foreign company status; retain failures/delistings).
2. Exclude financial company-years for primary corporate FCFF estimand based on contemporaneous SIC; separately handle REIT and utility samples.
3. Label AI build-out, supplier, adopter and untreated uncertainty using manually validated text spans and contracts. Generic SEC CapEx does not identify AI-specific spending.
4. Independently construct account risk and CAM eligibility for AS3101; historical material weakness and audit firm registered IDs with Form AP and PCAOB release date.
5. Define inclusion independently of realized post-event returns, restatements and p-values; only then lock inference sample with timestamps and preperiod controls.

## Source links
SEC EDGAR APIs https://www.sec.gov/search-filings/edgar-application-programming-interfaces
Damodaran 2026 https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices
S&P500 source and licensing https://github.com/datasets/s-and-p-500-companies
Github project draft review https://github.com/Saehon/Saeid-Homayoun/pull/163
