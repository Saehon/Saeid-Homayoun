# SEC CAM, ICFR and PCAOB — actual FY2025 ten-firm pilot

**Research stage:** independently sourced public audit-report facts and numerical descriptive diagnostics, not a completed FT50 causal study. Data as documented on 2026-10-10.

## Reproduce
```bash
python -m pip install pandas scipy
python analysis/run_fy2025_cam_pcaob_feasibility.py data/public_FY2025_audit_panel.csv
```

The 10-row `data/public_FY2025_audit_panel.csv` includes original issuer SEC 10-K URLs and the 2025-03-31 PCAOB report publication date. It contains no proprietary third-party cash-flow dataset.

## Results
- FY2025 10-K issuer firms: **10**; mapped CAM topics **13** (builders 7; suppliers 6).
- Ten 2025 auditor ICFR opinions effective; no 2025 auditor-reported material weakness is in the sample, hence this binary regressor has **zero variation**.
- Only **3** auditor legal entities: Deloitte, Ernst & Young, PwC. Auditor firm selection and economic role are highly conflated.
- PCAOB official *2024 inspection* reports released **31 March 2025**: DT 9/63=14.2857%; EY 18/64=28.125%; PwC 10/64=15.625% sampled audits with Part I.A findings.
- Prior-public inspection exposure at *audit report date*: **9/10**, excluding NVIDIA FY2025 2025-02-26 as-of date.
- Exploratory two-sided Fisher test, **uncertain-tax CAM** 4/5 builders versus 1/5 suppliers, p=0.206349.
- Exploratory two-sided Fisher test, **inventory CAM** 0/5 builders versus 2/5 suppliers, p=0.444444.
- **0/10 independently verified monetary AI-only CapEx** and **0/10 valid independent risk-to-CAM mismatch scores** in this initial register. Do NOT treat zeros as zero investment or a negative CAM assessment.
- Five data-invariant unit tests executed in the working runtime and passed, using the complete data version kept in Google Drive.
- No valid H1/H2/H3/H4/H5 moderation or causal estimates can be reported with these data.

## Validation and provenance
- [Detailed full report in Google Drive](https://docs.google.com/document/d/1_nSJJPcjKhtDv_THEekcp6CHWZrgDRbACCsUkjiN7Yg/edit)
- [Source-oriented full SEC/CAM/PCAOB register in Google Drive](https://drive.google.com/file/d/1dr-WwOLyl4i2IQfV3mgyZQqmvDbKNeWI/view)
- [Restricted combined secondary-financial and audit register](https://drive.google.com/file/d/1lf9F5AzT-DmjlfawFlhCj-19Nnya7bbv/view)
- [PCAOB official reports release](https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-posts-report-detailing-significant-improvements-across-largest-firms--alongside-inspection-results-in-record-time)
- [PCAOB inspection reports index](https://pcaobus.org/oversight/inspections/firm-inspection-reports)

**Integrity limits:** First-pass human topic coding needs second-coder review; public PCAOB findings cannot be attributed to anonymous issuer engagements; 2025 reports newly released Aug 2026 must NOT be backdated into 2025; fiscal year 2025 is non-calendar across several firms, and 2025 signed audit date can fall in 2026. No value-creation or AI-specific investment effect is established. Do not merge PR without review.
