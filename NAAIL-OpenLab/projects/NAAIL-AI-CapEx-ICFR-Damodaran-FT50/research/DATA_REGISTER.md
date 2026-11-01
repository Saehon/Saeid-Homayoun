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


## Extension sources — PCAOB, CAM and auditor identity
| Dataset | Keys and content | Official download/source | Warning |
|---|---|---|---|
| PCAOB published inspection firm data | registered auditor-firm ID, report ID, inspection vintage, publication datetime, selected-audit denominator | https://pcaobus.org/oversight/inspections/firm-inspection-reports | Inspected audits are nonrandom; not overall quality scores |
| PCAOB Part I.A JSON/CSV/XML | public deficiency, audit area, ICFR/financial audit indicators, anonymous issuer reference | https://pcaobus.org/oversight/inspections/firm-inspection-reports | Do not resolve anonymous issuer label to public company |
| PCAOB Part I.B JSON/CSV/XML | CAM reporting compliance and other standards/rules issues | https://pcaobus.org/oversight/inspections/firm-inspection-reports | Different meaning from insufficient evidence under I.A |
| PCAOB AuditorSearch / Form AP | issuer CIK, signed audit report/partner, PCAOB firm ID | https://pcaobus.org/resources/auditorsearch | Form AP typically filed AFTER audit report; respect public availability |
| SEC audit reports within 10-K | exact issuer CAM narratives and account topics | https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data | Rules apply only to eligible audits and dates |

Added required keys: pcaob_registered_firm_id, form_ap_filed_at_utc, audit_report_date, cam_text_span, cam_account_topic, cam_eligibility_flag, independent_account_risk, inspection_report_id, inspection_year, inspection_public_at_utc, selected_audits_denominator, part_ia_issuer_anonymized, part_ib_cam_issue, inspection_source_vintage, topic_label_validator, matched_firm_id_confidence.

**Part II:** public only under qualifying remediation disclosure; otherwise unavailable. **No data acquisition implied by these entries.**
