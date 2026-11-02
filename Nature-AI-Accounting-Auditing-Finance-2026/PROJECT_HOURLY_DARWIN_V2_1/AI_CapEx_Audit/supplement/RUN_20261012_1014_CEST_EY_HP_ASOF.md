# DARWIN V5 — EY US / HP FY2024 historical PCAOB exposure
Run ID: AI_CAPEX_DARWIN_V5_20261012_1014_CEST_EY_ASOF
Executed 2026-10-12 10:14 CEST. Status PARTIAL. Previous verified branch commit a34dae86a85bfa24af5448ede4d32cbf81bb7732; previous CI SKIPPED, lock unknown. This is a NEW EY/HP as-of check, not a repeat of KPMG/Cooper.

## Primary source observations
- HP Inc., CIK 0000047217, FY2024, 10-K filed 2024-12-13, accepted 2024-12-12 20:31:46 ET. SEC accession 0000047217-24-000080: https://www.sec.gov/Archives/edgar/data/47217/0000047217-24-000080-index.html
- EY US PCAOB 2023 inspection report 104-2024-095 dated 2024-06-12, PUBLIC 2024-08-15; Part I.A 22 of 59 inspected issuer audits = 37.2881355932%. PDF https://assets.pcaobus.org/pcaob-dev/docs/default-source/inspections/reports/documents/104-2024-095-e-y.pdf ; release https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-posts-2023-annual-inspection-reports-alongside-staff-observations-new-charts-to-boost-transparency
- EY US PCAOB 2024 inspection report 104-2025-037 dated 2025-02-26, PUBLIC 2025-03-31; Part I.A 18 of 64 = 28.125%. PDF https://assets.pcaobus.org/pcaob-dev/docs/default-source/inspections/documents/104-2025-037-e-y.pdf?sfvrsn=b29e7110_2 ; release https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-posts-report-detailing-significant-improvements-across-largest-firms--alongside-inspection-results-in-record-time

## Executed deterministic test and conclusion
1 real firm-year, 1 auditor, 2 inspection-year records; 20/20 Python unittest checks passed locally. As of HP 10-K 2024-12-13, select 2023 report released 120 days earlier. EXCLUDE 2024 report released 108 days AFTER filing. Incorrect future rate would differ by -9.1631355932 percentage points. Boundary checks: 2024-08-14 NULL, 2024-08-15 selects 2023, 2025-03-30 selects 2023, 2025-03-31 selects 2024. Report date must never substitute for public release date.

AI-specific CapEx MISSING, not zero; no inference about HP being inspected; no causal regressions or significance tests. Part I.A ratio is nonrepresentative selected-audit statistic, not issuer-specific ICFR material weakness or population audit failure probability. Primary PDF bytes/hash NOT_VERIFIED; source facts manually transcribed from official text, independent reproduction NOT_RUN.

Five outputs: manuscript unchanged NOT_READY; canonical raw sample unchanged; results QA-only; methods updated with public-date rule; local executable Python code, CSV, JSON, and 20 tests generated. SHA256 local script 62f7b928a1d93609e40181b836f971afa852d5189df5e88084df6a29a50f4ddc; CSV d8a7531137bd86fd8a5bacb6c269a9d64df516f7429495fdae3e683bf96df70a.

Eight gates: provenance PARTIAL, rights PARTIAL, standards PARTIAL, sufficiency PARTIAL, independent review NOT_RUN, falsification PARTIAL, reproducibility PARTIAL, human approval PENDING.
Rivals NOT_TESTED: AI control complexity harms ICFR; AI automation improves ICFR; legacy ERP maturity/auditor selection confound both.
OPEN REPAIR QUEUE: original Form AP 131274; amended KPMG vintage; PCAOB PDF byte hashes; missing AI-specific CapEx; independent replication; writer lock unknown; stale GitHub latest-status index (2 prior failures, do not retry). No merge/submission. Next independent admissible step: verify original EY PDF bytes or extend to a different auditor. Nature35 methods NOT_USED (no article fully audited).
