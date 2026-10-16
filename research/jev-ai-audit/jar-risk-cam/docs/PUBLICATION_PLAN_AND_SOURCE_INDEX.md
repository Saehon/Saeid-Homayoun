JAR PUBLICATION PLAN AND REPLICATION SOURCE INDEX

Do Auditors Disclose the Risks That Matter? Ex Ante Accounting Risk, CAM Alignment, and Subsequent Reporting Quality

Dr. Saeid Homayoun | Journal of Accounting Research target | 16 October 2026

STATUS: PRE-RESULTS MANUSCRIPT — NOT READY FOR SUBMISSION

A. PROJECT FILES IN THIS FOLDER

1. Word manuscript: JAR_Risk_CAM_Manuscript_Draft_2026-10-16.docx

https://docs.google.com/document/d/1ARsLl2pDqf1wmtwo8GWO2vxr5UKMxegc/edit

2. Replication starter ZIP: JAR_Risk_CAM_Replication_Starter_2026-10-16.zip

https://drive.google.com/file/d/1qGtbIOubT4X6NOxbybTI-F-whWIRETWX/view

3. This publication plan and source index: the single canonical planning document for this manuscript.

The ZIP contains: original schema and point-in-time validation scripts; six passing tests; a clearly labeled synthetic example; verified FT50 replication-source links; a JAR data-description template; and the publication timetable. It does NOT include copies of your private Drive raw datasets, third-party licensed raw data, proprietary model weights, or actual econometric results.

B. AUTHORITATIVE RESEARCH ASSETS (LINKS, NO COPIES)

Risk–CAM canonical data: https://docs.google.com/spreadsheets/d/1sfpwpwXPAztUK4ShIwJBh9qwavPkQM_QjpDhPCuvgFE/edit

KIWI CAM + SEC verification data: https://docs.google.com/spreadsheets/d/1EBHt3Un6mL3_8GPP4C9w-KqNjdaGXs-EwMHATDVi2gY/edit

Risk–CAM results and FT50 replication registry: https://docs.google.com/spreadsheets/d/1q7IFjPfUT5Wx1tDU3pz_VYHpa941yqCrKiDD3xlrB-Y/edit

Risk–CAM variable dictionary: https://docs.google.com/document/d/1mTCLJE_skfkfQzeCM6clhNGkgnamfKYQSYNEAdXXbuM/edit

Existing replication execution specification: https://docs.google.com/document/d/1U9YpLBOKquUpy0ovXnZsLyaqiN1N3wfrvR1vWBcaPjg/edit

DARWIN–JEV shared risk engine and synthetic code: https://github.com/Saehon/Saeid-Homayoun/pull/184

Existing original author code (corrected Bao et al. 2022): https://github.com/JarFraud/FraudDetection

Author reporting-resilience code: https://github.com/TiesdeKok/mnsc.2023.4670

Author robust inference code: https://github.com/dveenman/robust

JAR online replication archive: https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research/online-supplements-and-datasheets

PCAOB official inspection data: https://pcaobus.org/oversight/inspections/firm-inspection-reports

SEC EDGAR API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

C. INTEGRITY GATES AND FEASIBILITY WARNING

Prior methods documents report 609 candidate topic-year records, 44 firms, 87 firm-years, and successful keyed sample joins. However the same audit identified only 11 observations from four firms with a narrow temporally validated risk-feature subset. These values are OLD PIPELINE DIAGNOSTICS, not a current analysis-ready sample; do not include 609 as the regression N or 44 as the final number of independent clusters without a fresh audit.

No JEV inference has been executed. Current GitHub code creates untrained feature candidates and synthetic QA. A score may be used in hypotheses only after out-of-time model fitting, calibrated validation and domain-specific feature verification.

Keep CAM selection separate from CAM effectiveness and ICFR effectiveness. Preserve effective/ineffective/unknown × industry × account-domain taxonomy. Do not equate no CAM with audit failure. Do not infer PCAOB engagement linkages from anonymized public inspection reports.

Disallow any future information from training inputs. Never choose high-risk cutoffs to optimize significance in the held-out sample.

D. 16-WEEK PUBLICATION PATH

Weeks 1–2: source, extraction and license audit; key reconciliation; point-in-time source availability; JAR preregistration applicability assessment.

Weeks 3–4: domain candidate-set construction; independent account risk features; 100-record blind source audit; outcome-definition protocol.

Weeks 5–6: reproduce corrected Bao baseline, estimate logistic/gradient-boosting/Dechow-inspired risk models on historical data; chronological holdout.

Weeks 7–8: separately classify CAM disclosures, independently validate topic agreement, compute risk-weighted misalignment.

Weeks 9–10: construct observed future outcomes; run prespecified H1–H4 models where events, independent firms and clusters support inference.

Weeks 11–12: temporal placebo, materiality screens, within-firm alternatives, firm/auditor effects, robust/cluster inference, incremental information value.

Weeks 13–14: generate Tables 1–6 with reproducible files and logs, fill Results and Discussion, draft appendix and JAR data-description sheet.

Weeks 15–16: clean-environment replication, author review, conflict disclosure, separate anonymized submission file, JAR portal readiness decision.

E. JAR SUBMISSION REQUIREMENTS

Official JAR guidelines: https://onlinelibrary.wiley.com/page/journal/1475679x/homepage/ForAuthors.html

At submission: separate data-description sheet including authors responsible for data, raw source origins and acquisition dates, and proprietary restrictions.

Upon acceptance: raw-to-final code, statistical code, table-generation code, comprehensive logs, identifier files when feasible, and retention assurances for at least six years. JAR does not categorically mandate public release of underlying raw and final data.

Preregistration: from January 2027 mandatory for studies reporting qualifying primary data collection, including experiments and surveys; assess newly constructed human-coded labels before beginning fresh collection.

JAR's standard review is double-anonymized. Create a manuscript without author-identifying information and a separate title page for submission. Confirm updated submission fee and manuscript formatting immediately before submission.

Funding and conflicts of interest must be disclosed accurately; the draft must not invent them.

F. CURRENT STATUS

Word manuscript: CREATED, saved in this folder and visually checked; not empirically finalized.

Replication ZIP: CREATED, 6 schema-level synthetic tests passed; does not reproduce FT50 empirical estimates.

Current real-data regression: NOT RUN.

JEV model installation / actual scoring: NOT RUN.

Outcome linkage and power/cluster sufficiency: NOT VERIFIED.

Human approval for publication submission: PENDING.

Sustainability policy: Google Drive is the authoritative private data archive; avoid unnecessary copies. GitHub retains executable code and history. Hugging Face may store only permission-cleared model artifacts and data.