# AI CapEx × ICFR × Damodaran | FT50 Research Project

**Stage:** New research project; no empirical results yet.
**Google Drive canonical folder:** https://drive.google.com/drive/folders/1O5fzl-AIMKGzwtfNavzKawBk6FfaFTR9
**GitHub status:** Project-specific development branch in the existing NAAIL umbrella repository; NOT a standalone repository.

## Research question
Does internal-control reporting risk moderate the relationship between AI-related investments, realized free cash flow, and capital-market valuation?

## Research contributions to test
- Damodaran-based valuation: free cash flow to the firm (FCFF), incremental return on invested capital (ROIC), weighted average cost of capital (WACC), and reinvestment intensity.
- ICFR/accounting: material weaknesses, information reliability, and timing-safe latent risk proxies.
- AI measurement: distinguish AI-specific capex from total capital expenditures; combine structured SEC facts with manually validated disclosures.
- Empirical finance: examine future cash-flow realization, market responses, and pricing errors; causal claims require identification beyond fixed effects.
- Neural research: benchmark FinBERT and temporal models (including TimesFM) against transparent econometric and tree-based baselines.

## Hypotheses — proposals, not findings
- H1: The relation between disclosed AI investment and future cash-flow realization varies with prior ICFR risk.
- H2: The market response to AI investment disclosures depends jointly on internal-control risk and the earnings–cash-flow gap.
- H3: As-of-date ICFR risk signals add incremental out-of-time information about future restatements, impairments or valuation surprises.

## Research integrity gates
1. Record source URL, accession number, CIK, filing date, extracted text span, fiscal period, license and ingestion version.
2. Define a reproducible AI investment construct with a manual labeling protocol; SEC standard capex is NOT AI capex.
3. Train only on information that existed by the decision cutoff; chronological testing and purged boundaries.
4. Report missingness, selection, calibration, imbalance metrics (PR-AUC), confidence intervals, and economic payoffs.
5. Compare to Logit / firm+time fixed-effect models / XGBoost before claiming neural superiority.
6. Separate synthetic proof-of-concept data from real empirical samples; do not treat early pilots as FT50 evidence.
7. No automatic publication, data redistribution or claims of statistical significance without independent review.

## Public source starting points
- SEC EDGAR API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- SEC Financial Statement Datasets: https://www.sec.gov/dera/data/financial-statement-data-sets.html
- Damodaran sector valuation data: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
- Ken French factor data: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- Google TimesFM source: https://github.com/google-research/timesfm

## Project files
- `PROJECT_MASTER_INDEX.md` — cross-platform links and milestones.
- `research/PRE_ANALYSIS_PLAN.md` — hypotheses, variables, identification, falsification.
- `research/DATA_REGISTER.md` — access/license rules and provenance.
- `src/damodaran_core.py` — auditable valuation calculation helpers.
- `tests/test_damodaran_core.py` — synthetic unit tests only.
- `AGENTS.md` — instructions for Codex in VS Code.

**Privacy:** This branch is in a PUBLIC umbrella repository. Never commit confidential manuscripts, private notes, credentials, licensed raw datasets, or restricted model weights. Keep the master archive in the Google Drive folder above.


## PCAOB inspection and CAM extension (2026-10-10)
The research scope now includes a distinct account-level CAM risk-alignment channel and a **previously-public auditor-firm-level PCAOB inspection exposure** channel. The substantive economic outcomes remain AI investment, free-cash-flow realization, ROIC-WACC and market pricing. Do not infer engagement-specific PCAOB findings from anonymous issuer identifiers.

**Required method documents**: [PCAOB/CAM integration](research/PCAOB_CAM_INTEGRATION.md), [FT50 literature matrix](research/FT50_PCAOB_CAM_LITERATURE.md), [audit oversight prototype](src/audit_oversight.py), and [synthetic unit-test specifications](tests/test_audit_oversight.py).

- **H4 (CAM mismatch):** ex ante high-risk accounts without corresponding CAM disclosures and AI investment economic outcomes.
- **H5 (PCAOB exposure):** publicly known auditor-firm inspection deficiencies condition AI-investment valuation and/or subsequent cash-flow realization.
- **H6 (exploratory):** Part I.B CAM compliance findings and information content of CAM-to-risk alignment.
- **Added Google Drive protocol:** https://docs.google.com/document/d/1N1IhXWiVYsuBxhDaL7fAFir_a3PuFw04ae5fIzgWBHs/edit
- **Free matching data:** PCAOB AuditorSearch / Form AP https://pcaobus.org/resources/auditorsearch ; official inspection datasets https://pcaobus.org/oversight/inspections/firm-inspection-reports.

*Status: research design and unexecuted scaffold only; no PCAOB/CAM sample downloaded or validated.*
