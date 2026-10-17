// Public-source deterministic checks; NO restricted data, NO raw-PDF byte reproduction.
// Official PCAOB Form AP ID 146520; SEC AVGO 10-K FY2025.
const f={
  "form_id": 146520,
  "issuer_cik": "1730168",
  "issuer": "Broadcom Inc.",
  "auditor": "PricewaterhouseCoopers LLP",
  "sec_filed_date": "2025-12-18",
  "audit_report_date": "2025-12-18",
  "fiscal_end": "2025-11-02",
  "form_ap_signed_date": "2026-01-05",
  "form_ap_filed_at": null,
  "filename_date": "2026-01-06",
  "engagement_partner_count": 1,
  "large_participant_firms": 1,
  "large_participant_country": "Singapore",
  "large_participant_min_pct": 5,
  "large_participant_max_exclusive_pct": 10,
  "small_participant_firms": 1,
  "small_participant_aggregate_max_exclusive_pct": 5,
  "ai_only_capex": null
};
const checks={
  id:f.form_id===146520,
  cik:f.issuer_cik==="1730168",
  auditor:f.auditor==="PricewaterhouseCoopers LLP",
  fiscal_end_before_report:f.fiscal_end<f.audit_report_date,
  report_date:f.audit_report_date==="2025-12-18",
  signed_after_sec:f.form_ap_signed_date>f.sec_filed_date,
  partner_not_public_at_sec:f.form_ap_signed_date>f.sec_filed_date,
  filing_datetime_unverified:f.form_ap_filed_at===null,
  filename_not_filing_proof:f.filename_date!==f.form_ap_signed_date&&f.form_ap_filed_at===null,
  partner_count:f.engagement_partner_count===1,
  singapore_participant_band:f.large_participant_firms===1&&f.large_participant_country==="Singapore"&&f.large_participant_min_pct===5&&f.large_participant_max_exclusive_pct===10,
  other_small_firm:f.small_participant_firms===1&&f.small_participant_aggregate_max_exclusive_pct===5,
  ai_only_capex_unknown:f.ai_only_capex===null
};
const failed=Object.entries(checks).filter(([,v])=>!v).map(([k])=>k);
if(failed.length) throw Error("FAIL: "+failed.join(","));
console.log(JSON.stringify({fixture_checks:Object.keys(checks).length,passed:Object.keys(checks).length,source:"OFFICIAL_PCAOB_PDF_TRANSCRIPTION",raw_pdf_replication:"NOT_RUN",form_ap_filing_datetime:"UNKNOWN",causal_models:"NOT_RUN"}));
