# AI-CAP-IFRS v4 — MacAma-informed FT50/AJG research model

**Working title:** Artificial Intelligence Capital Expenditure, Earnings–Cash Flow Divergence, and Equity Valuation: Evidence from IFRS Firms.

## Single authoritative archive (Google Drive)
- [Version 4 folder](https://drive.google.com/drive/folders/1Geq5L9VUFjqpAm1_nz-EnrAAv6OSzb2Y)
- [21-page Word manuscript v4](https://docs.google.com/document/d/1sZIyigbtyK1uHAmJEJ2e3IcPxfW4mAIs/edit)
- [Reproducibility and evidence ZIP](https://drive.google.com/file/d/1RWEOmv5XhhnxAxTLafQ5wYd_9iB2TXKK/view)
- [Original v3 project folder](https://drive.google.com/drive/folders/1UZR8Uaj0a9h6oX6vwXgCUVlUKtXOKFPu) (preserved)

## Phase 1 — Review and evidence synthesis
Adapt [MacAma](https://github.com/YilinYuan/MacAma) with dual human verification, audit logs and finance-specific study-eligibility and bias criteria. The existing verified studies are a **targeted seed evidence map**, not a completed PRISMA review or a statistical meta-analysis. Pool only compatible standardized effects with extracted variance and nonoverlapping samples; publish negative findings.

## Phase 2 — Replication fit
1. [Babina et al. (2024, JFE)](https://doi.org/10.17632/s26kxvspn7.3): AI firm measurement; proprietary source aspects replaced by pseudo-data in public version; previous authors' coefficients **not rerun** here.
2. [Fedyk (2024, Journal of Finance)](https://doi.org/10.1111/jofi.13287): release timing and investor attention; publisher lists replication code but underlying news and intraday equity data are commercial.
3. [Küster et al. (2025, Contemporary Accounting Research)](https://doi.org/10.1111/1911-3846.13070): KAM specific valuation-judgment semantics; original LSEG/Audit Analytics data not open; no confirmed full free replication bundle.
4. [Blankespoor, deHaan & Li (2026, JAR)](https://github.com/ed-dehaan/GenScore): CC-BY-4.0 AI-generation text data, **not** capital expenditure.

## Phase 3 — Open-data options
- IFRS filing API: https://filings.xbrl.org/docs/api
- Fama–French European daily FF5 **factor returns, not stock returns**: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- Damodaran industry data: https://pages.stern.nyu.edu/~adamodar/
- SRAF SEC text, US sample comparison: https://sraf.nd.edu/textual-analysis/code/
- Analytext SEC text, CC-BY-NC4.0 license: https://www.analytext.com/
- FinBERT Apache-2.0: https://github.com/ProsusAI/finBERT

## Three prospective, falsifiable hypotheses
**H1 (cash-backed AI investment valuation):** The contemporaneous CAR response to *verified* AI investment surprises varies positively with available operating cash-flow coverage, net of ex ante growth options.

**H2 (technological recoverability verification):** The signed CAR sensitivity to recognized impairment news is stronger when audited notes provide independently verifiable technological useful-life, obsolescence and CGU valuation assumptions.

**H3 (incremental auditor information):** Management-nonredundant ISA 701 KAM text conditions the contemporaneous CAR response to the accounting-information bundle. Jointly released reports **cannot** identify a separate causal KAM event effect.

These combinations are novelty candidates, not confirmed never-published constructs. Alternative signs and nulls must be tested.

## Synthetic digital-twin status
The exact Python code and Monte Carlo outputs are archived in the Drive ZIP. Under 500 independent synthetic events, 2 pp return noise and a true 0.15 pp/1SD interaction, simulated unadjusted H1 detection was about 35%, not an observed significant effect. No individual company share prices, price CARs or real multivariate coefficients were generated.

**No fraud categorization. No proprietary or user-private data included in this GitHub documentation.**
