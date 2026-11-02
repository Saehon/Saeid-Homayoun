# DARWIN V5 | PCAOB 2024 inspection chronology crosswalk

Run start: 2026-10-11 15:11:28 Europe/Stockholm (CEST). Status: PARTIAL SCIENTIFIC GATE; not a causal test.

## Inputs (owner-controlled Google Drive)
- 2025 ten-firm CAM/ICFR/PCAOB pilot CSV: Drive file ID `1dr-WwOLyl4i2IQfV3mgyZQqmvDbKNeWI`.
- Historical six-auditor PCAOB register CSV: Drive file ID `1IO8lhUiuwSmGM5R-WO-0RR97IrRD_oSj`. Its `PUBLIC_RELEASE_DATE` values are explicitly UNVERIFIED.
- Official PCAOB release dated 2025-03-31: https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-posts-report-detailing-significant-improvements-across-largest-firms--alongside-inspection-results-in-record-time

## Actual execution
Connector-fetched two CSV texts. Executed a JavaScript quoted-CSV parser and exact join on `auditor_legal_name = audit_legal_firm` AND `pcaob_inspection_vintage = inspection_year = 2024`. Calculated comparisons and public-availability flags, without any econometric model.

## Observed counts
- Historical rows: **138**; FY2025 pilot rows: **10**; distinct pilot audit firms: **3**.
- Exact unique auditor × 2024-vintage match: **10/10** pilot rows; each of the three firms had one 2024 register record.
- Historical inspection report date for all three: **2025-02-26**; official public release for all six U.S. GNF 2024 reports: **2025-03-31** (33 calendar days later).
- Numerator and denominator agree for **9/9** pilot rows with populated rates; **1/10** (NVDA) is correctly blank because its 2025-02-26 auditor report predates the 2025-03-31 public release.
- Pilot `pcaob_prior_to_auditor_report` flags: **9 true, 1 false**. 2024 firm-level deficiency shares: Deloitte 9/63; EY 18/64; PwC 10/64; these are **NOT client-specific audit findings**.
- 0 observed AI-specific CapEx values in this pilot. No CIK-verified multi-year panel, causal estimate, regression or independent replication established in this run.

## Scientific decision
PASS for **internal 2024 firm × year register consistency and publication chronology check only**. PARTIAL for primary-source row-by-row inspection PDF verification; NOT_RUN for SEC CIK/accession and Form AP audit-firm crosswalk, and for AI-specific CapEx construct. QUARANTINE causal PCAOB × AI CapEx/ICFR estimation until point-in-time firm-year panel and identification exist. Distinguish 2025-02-26 *report date* from 2025-03-31 *publication date*; historical register `PUBLIC_RELEASE_DATE` is unverified and must never substitute for official release dates.

## Next admissible task
Inspect SEC/XBRL–Form AP integrated archive for real CIK10/accession/auditor-entity keys and verify its lineage before joining the 2023–2025 secondary cash-flow pilot. Do not infer AI-specific CapEx from generic gross CapEx or AI mentions.

## Five-artifact status
Manuscript: unchanged (no findings inferred); sample: existing 10 pilot rows unchanged; results: QA counts only, no regressions; variables/methods: chronology rule needs mirrored update; replication: JavaScript crosswalk was executed interactively; standalone reusable script not yet independently run. Human gate PENDING. No auto-merge or submission.
