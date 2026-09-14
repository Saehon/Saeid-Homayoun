# ECONOVA-S™ Project Status

**Architecture specification:** V2.5  
**Current software/research stage:** v0.3 — Official Public Data + Governed Scientific Discovery  
**Scientific status:** Real-data reproducibility / measurement-change research; pre-discovery  
**Primary maintainer:** Saeid Homayoun  
**ORCID:** 0000-0002-2536-0446

## Operational public components

- Dual-core architecture.
- Provider-neutral AI-to-AI Scientific Intelligence Fabric™.
- GPT-5.6 Sol replaceable backend in the v0.2 prototype.
- Co-Scientist-style Generation / Reflection / Ranking / Evolution / Proximity / Meta-review logic.
- ERA-style empirical conversion.
- AlphaEvolve-inspired search governance.
- Computational Discovery candidate-lineage and evaluator rules.
- AlphaFold-inspired latent-structure validation rules.
- Science One-inspired Chain-of-Evidence and CoE Audit gates.
- Mirendil-inspired closed-loop R&D containment boundary.
- DAG / systems governance.
- Machine-readable study manifest and discovery gate validator.
- Controlled evidence metadata RAG.
- Real-data ingestion paths.
- Official Fama–French data adapters and archive logic.
- Official Damodaran / NYU Stern industry-data adapters.
- SEC EDGAR XBRL CompanyFacts adapter with filing-date chronology controls.
- Six-table econometric runner.
- Temporal/OOS checks.
- Stata export.
- Independent replicator and scientific red-team roles.
- Evidence Passport™.
- Human Gate™.
- CI workflows and governance tests.

## Canonical scientific-discovery sequence

```text
Literature Grounding
→ Co-Scientist Hypothesis Tournament
→ DAG / Systems Governance
→ ERA Empirical Conversion
→ Real Data + Code + Metrics
→ AlphaEvolve / Computational Discovery
→ AlphaFold-Inspired Latent Structure
→ Independent Replication
→ AI-to-AI Red Team
→ Science One Chain-of-Evidence
→ CoE Audit
→ Falsification
→ Economic / Welfare Interpretation
→ Evidence Passport
→ Human Gate
```

Canonical specification: [`GOOGLE_INSPIRED_DISCOVERY_PROTOCOL.md`](GOOGLE_INSPIRED_DISCOVERY_PROTOCOL.md)

## Machine-enforced discovery boundary

The repository includes:

- `discovery/study_manifest.schema.json`
- `discovery/sample_study_manifest.json`
- `discovery/validate_study_manifest.py`
- `discovery/test_discovery_manifest.py`
- `templates/STUDY_DISCOVERY_TEMPLATE.md`
- `.github/workflows/scientific_discovery_protocol.yml`

The validator prevents a discovery claim from being authorized when required literature, empirical, replication, adversarial, falsification, Chain-of-Evidence, CoE Audit, reproducibility, or Human Gate conditions are missing.

## v0.3 first frozen study

**MNSc–FamaFrench–01**  
*When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors*

The executable study compares official July 2024 FIZ-era and July 2025 CIZ-era Fama–French archive snapshots on their common monthly sample. It produces:

- Data Construction Sensitivity (DCS);
- factor-premium stability with HAC/Newey–West inference;
- CAPM, FF3 and FF5 alpha comparison;
- sign/significance Conclusion Reversal flags;
- subperiod robustness;
- six publication-style output tables;
- source SHA-256 hashes;
- RUN_SUMMARY.md;
- Evidence Passport™.

Its discovery manifest remains intentionally pre-discovery because independent replication, adversarial review, falsification, Chain-of-Evidence, CoE Audit, economic/welfare interpretation and final Human Gate are not complete.

## Scientific boundary

ECONOVA-S™ is not a self-validating scientific authority. Fixed effects, statistical significance, predictive accuracy, evaluator scores, AI agreement, or successful reproducibility runs do not by themselves establish causality or scientific discovery.

`discovery_claim_allowed = false` remains the enforced public status.

## Next gates

1. Execute and archive the official July 2024 vs July 2025 real-data workflow artifacts.
2. Run the full study through the new discovery manifest and study template.
3. Complete independent replication plus red-team/falsification artifacts.
4. Build the study-level Chain-of-Evidence and CoE Audit.
5. Replicate the FIZ→CIZ comparison with FF3 and additional archived portfolio families.
6. Add reduced-rank factor-dimension analysis and latent-structure validation.
7. Add multiplicity/FDR and conclusion-reversal reliability analysis.
8. Extend the public-data panel with chronology-safe SEC XBRL fundamentals and documented Damodaran industry crosswalks.

See `GOOGLE_INSPIRED_DISCOVERY_PROTOCOL.md`, `studies/MNSc-FamaFrench-01/`, `prototype_v03/`, `ROADMAP.md` and `CHANGELOG.md`.
