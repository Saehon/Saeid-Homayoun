# DATASETFREE — research and replication protocol

**Scientific master:** https://docs.google.com/document/d/1BB81Xw7saXGXqnN9nSg8PW3lgeEsH3LyrexDqUsMFXA/edit  
**Dataset rights and evidence:** https://docs.google.com/document/d/1hPYrxjBYlkimg3qLytwjKpwzw8_ygNtfor6QGcAbqdo/edit  
**Replication audit:** https://docs.google.com/document/d/1VicujJHE8fOHVteXhhiUYQN3UDAdf2xZ0bp73muAeo0/edit

## Phase 1 — systematic review and meta-analysis (protocol, not completed)
Review AI staffing, disclosure, innovation, accounting reporting, auditing and pricing research in FT50 and AJG/ABS 4/3 finance, accounting, economics and management journals; code journal classification against dated published ranking editions. Document searchable sources, DOI, screen date, preregistered queries, exclusion rationale, effect estimates, standard errors, population, controls, dataset access and robustness.

Use PRISMA 2020 screening, independently verified source extraction and independent human adjudication. Adapt [MacAma](https://github.com/YilinYuan/MacAma) as a multi-agent review assistant with human sign-off. Its medical-trial standardized mean differences are not an automatic template for financial panel regressions. Pool only commensurable estimates; handle paper-level effect dependence and identification heterogeneity. No meta-analytic numeric effect estimate has been calculated yet.

## Phase 2 — reproduction qualification
Start from the [twelve-package repository registry](replication_packages_2026-10-10.csv): identify DOI, access rights, version, input checksums, dependencies, runnable commands, benchmark result, numerical tolerance and explanation of discrepancies. A working script on fake inputs is not evidence of replication of original results.

Babina et al. (2024) [JFE Mendeley V3](https://data.mendeley.com/datasets/s26kxvspn7/3) substitutes pseudo-data for proprietary inputs, including commercial professional-history and financial inputs. Those original microdata cannot be reconstructed freely from the public package.

## Phase 3 — company-year dataset and economics
Unit: public-company CIK × fiscal year. Candidate data: [SEC EDGAR XBRL and 10-K](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [USPTO AI patent information](https://www.uspto.gov/ip-policy/economic-research/research-datasets), [trademark cases](https://www.uspto.gov/ip-policy/economic-research/research-datasets/trademark-case-files-dataset), [SRAF dictionaries](https://sraf.nd.edu/) and [Kenneth French factors](https://mba.tuck.dartmouth.edu/pages/faculty/Ken.french/data_library.html). Factor returns are NOT individual security returns; pricing-event analysis needs a lawful complete, adjusted security price source.

Candidate propositions (not asserted to be novel or statistically significant):
1. Greater AI narrative/capability mismatch at year t predicts elevated next-year ICFR and accounting reporting risk.
2. Observable AI capability paired with implementation-specific claims predicts stronger subsequent trademark/product-class innovation than claims alone.
3. At reporting events, large lagged narrative/capability gaps predict stronger pricing reversals, conditional on obtaining legal single-stock price data.

Identification threats: unobserved outsourced AI, patent-selection, measurement and entity-linking error, time-varying technological shifts, reverse causality, event timing, stock delisting and multiplicity. Use transparent pre-specified controls, time and firm effects, industry-year shock controls, clustered errors, negative controls, hand-labeling and holdouts. Do not claim fixed effects ensure causality.

**Digital twin:** synthetic tests for estimator size, coverage, power, document coding errors and rare ICFR events. This tests research procedure, not whether real-world hypotheses are significant.

## Legal and version-control gates
No Cognism or Compustat source records; no restricted personal résumés, third-party paid code or private credentials in GitHub. Google Drive is source of truth, GitHub holds public code/manifest, HF/Kaggle publication awaits account permissions and rights review. Archive a DOI, release, hash and method provenance for every real download.
