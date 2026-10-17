# Systematic review and meta-analysis protocol — draft

**Status: draft protocol; not registered; no screened records.** Preserve a date-stamped exact-search audit rather than presenting an automated summary as a formal systematic review.

## Scope and retrieval

Finance, accounting, auditing, management and economics studies; prioritize FT50 and verified AJG 4*, 4 and 3, with foundational studies outside these groups where necessary. Search from 2020 through 10 October 2026, adding prespecified seminal studies before 2020. Target sources: Google Scholar (discovery), Crossref/OpenAlex (metadata), publisher websites and research replication archives, SSRN, ScienceDirect/Mendeley, journal data policies, Kaggle/Hugging Face/GitHub where licenses allow. Google Scholar and publisher indexing require their own access/usage terms.

Search concepts (adapt and archive exact platform syntax):
- (ICFR OR "internal control" OR "material weakness") AND ("stock return" OR "cost of equity" OR "price discovery")
- ("10-K" OR "10-Q" OR "financial disclosure") AND ("textual change" OR "semantic novelty" OR "return prediction")
- ("model disagreement" OR "agentic AI" OR "selective prediction") AND (finance OR audit OR disclosure)
- ("replication code" OR "data availability") AND (finance OR accounting OR auditing)

For each retrieval, record query, retrieval date, source, filters, DOI, landing URL, deduplication key, inclusion/exclusion reason, full-text availability, independent screener decision, journal tier verification source, data/code link and rights status. Do not scrape restricted databases.

## Screening and evidence

Two independent screeners or a documented human arbitration mechanism; preserve exclusions and null results. Distinguish studies of disclosure content/returns, ICFR-risk pricing, forecast disagreement, pre-disclosure risk measurement and audit-evidence credibility. Extract sample, unit of analysis, outcome, estimand, SE, timing, design and confounds. Quality-grade by identification, selection, label construction, look-ahead bias, rights and executable replication.

Meta-analysis is **conditional** on comparable effect sizes and sufficiently independent studies. If outcomes or models are incompatible, provide a structured synthesis instead. When pooled, disclose effect-size conversion, dependence handling, random-effects/hierarchical model, heterogeneity, influence checks and small-study bias.

## Reporting

Follow PRISMA 2020 where applicable: https://www.prisma-statement.org/prisma-2020 . The CSV registry in this scaffold is an *empty candidate intake template*. It is neither a completed search log nor a verified evidence table. All statistical findings need an independently reviewed, separate results package.