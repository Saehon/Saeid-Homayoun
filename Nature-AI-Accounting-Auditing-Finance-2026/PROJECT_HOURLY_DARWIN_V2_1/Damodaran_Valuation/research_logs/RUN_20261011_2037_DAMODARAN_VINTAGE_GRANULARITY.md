# DARWIN V5 — Damodaran vintage, granularity and rights audit
Run ID: RUN_20261011_2037_DAMODARAN_VINTAGE_GRANULARITY
Run local time: 2026-10-11 20:37:33 Europe/Stockholm
Scientific step: official Damodaran source-vintage/granularity/rights verification; no company regression or valuation.
Operating protocol: DARWIN V5 Mother Brain + Saeid Research Systems Skill V4.0.
Prior verified state: Drive index through 2026-10-11 18:35 CEST; GitHub latest-status lagged at AVGO 13:40; a 19:35 META source check was reported in the task thread but is not reflected in the canonical Drive index.

## Evidence (primary official pages)
1. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html — latest full update January 9, 2026; explicitly industry groupings and company-level raw data not available for download.
2. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html — US cost of equity/capital by industry, data as of January 2026; 11 columns including industry, number of firms, beta and cost of capital.
3. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datahistory.html — annual update timing, market/accounting reporting lags, multiple underlying licensed commercial data providers, permissive usage guidance for publicly reported aggregates; underlying company-level data not redistributable from this source.
4. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/dataarchived.html — archived US industry cost-of-capital vintages including January 2023, 2024, 2025; archived data availability must be checked for the specific variable and valuation date.
5. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/databreakdown.html — sector averages vs individual company lookup; company-level downloads discontinued due to provider restrictions.

## Four selected observed US industry rows (MANUAL transcription from official HTML, not firm observations)
Industry | N underlying firms | Beta | Industry cost of capital (%)
Computer Services | 64 | 1.09 | 7.83
Semiconductor | 66 | 1.52 | 10.55
Software (Internet) | 29 | 1.69 | 10.66
Software (System & Application) | 309 | 1.28 | 9.34
Executed local Python descriptive check: 4 manually transcribed industry rows; WACC minimum 7.83%, maximum 10.66%, range 2.83 percentage points. No sample inference.
SHA-256 of normalized selected-row JSON (NOT original publisher HTML/XLS bytes): 184b1ca752fee12de8624fbb4a21d5f495c1056c12bfeca968475f6322820432.
Official HTML/XLS binary SHA-256: NOT_CAPTURED; direct file download failed once; do not claim source-file integrity verification.

## Decision and limits
SOURCE_IDENTITY=VERIFIED_OFFICIAL_WEBPAGE; DATA_GRANULARITY=INDUSTRY_AGGREGATE; RELEASE_VINTAGE=JANUARY_2026; PUBLIC_AGGREGATE_USAGE=PERMISSIVE_WITH_ATTRIBUTION; UNDERLYING_COMPANY_DATA_RIGHTS=RESTRICTED; HISTORICAL_ARCHIVE_LINKS=VERIFIED_EXIST; HISTORICAL_ARCHIVE_FILE_BYTES=NOT_INSPECTED; FIRM_YEAR_JOIN=NOT_RUN.
No 2026 industry WACC should be assigned to 2023–2025 firm-years as contemporaneous data. Require vintage<=valuation date and independently verified firm-to-industry mapping, preserving source/industry granularity and uncertainty. No AI-specific CapEx, ROIC, FCFF, regression, DOI/Nature35 transfer, or causal inference tested.
Five canonical living artifacts remain in original Drive folder; this run supplements source provenance and variables/methods; does not pretend native Docs/Sheets are exported CSV or DOCX.
Eight scientific gates: source identity PARTIAL (official webpage verified, original bytes not hashed), rights PARTIAL, point-in-time joins BLOCKED, construct validation PARTIAL, identification NOT_RUN, falsification NOT_RUN, independent reproduction NOT_RUN, human approval NOT_RUN.
Writer lock and CI for this specific project scope: NOT_VERIFIED (no proof of exclusive lock or run-specific CI). Existing GitHub update blocker remains in repair queue; no merges.
Next eligible step: inspect archived US industry cost-of-capital files from Jan 2023/2024/2025 and record exact bytes/hash and availability dates; only then propose time-safe industry-level benchmarks for SEC firm-level panel.
