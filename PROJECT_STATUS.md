# ECONOVA-S™ Project Status

**Architecture specification:** V2.5  
**Current software/research stage:** v0.3 — Official Public Data + First Real Empirical Study  
**Scientific status:** Real-data reproducibility / measurement-change research; pre-discovery  
**Primary maintainer:** Saeid Homayoun  
**ORCID:** 0000-0002-2536-0446

## Operational public components

- Dual-core architecture.
- GPT-5.6 Sol replaceable backend.
- Co-Scientist-style hypothesis tournament.
- ERA-style empirical design.
- Controlled evidence metadata RAG.
- Real-data ingestion paths.
- Official Fama–French data adapters and archive logic.
- Official Damodaran / NYU Stern industry-data adapters.
- SEC EDGAR XBRL CompanyFacts adapter with filing-date chronology controls.
- Six-table econometric runner.
- Temporal/OOS checks.
- Stata export.
- Scientific red-team review.
- Evidence Passport™.
- Human Gate™.
- CI workflows and governance tests.

## v0.3 first frozen study

**MNSc–FamaFrench–01**  
*When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors*

The executable study compares the official July 2024 FIZ-era and July 2025 CIZ-era Fama–French archive snapshots on their common monthly sample. It uses FF5 factors and the six value-weighted Size × Book-to-Market portfolios and produces:

- Data Construction Sensitivity (DCS);
- factor-premium stability with HAC/Newey–West inference;
- CAPM, FF3 and FF5 alpha comparison;
- sign/significance Conclusion Reversal flags;
- subperiod robustness;
- six publication-style output tables;
- source SHA-256 hashes;
- RUN_SUMMARY.md;
- Evidence Passport™.

## Scientific boundary

ECONOVA-S is not a self-validating scientific authority. Fixed effects, statistical significance, predictive accuracy, AI agreement or a successful reproducibility run do not by themselves establish causality or scientific discovery.

`discovery_claim_allowed = false` remains the enforced public status.

## Next gates

1. Execute and archive the official July 2024 vs July 2025 real-data workflow artifacts.
2. Replicate the FIZ→CIZ comparison with FF3 and additional archived portfolio families.
3. Add reduced-rank factor-dimension analysis.
4. Add multiplicity/FDR and conclusion-reversal reliability analysis.
5. Add independent red-team replication and external review.
6. Extend the v0.3 public-data panel with chronology-safe SEC XBRL fundamentals and documented Damodaran industry crosswalks.

See `studies/MNSc-FamaFrench-01/`, `prototype_v03/`, `ROADMAP.md` and `CHANGELOG.md`.
