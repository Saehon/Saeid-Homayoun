# Changelog

All notable public changes to ECONOVA-S™ are documented here.

## [Unreleased]

### AI-to-AI scientific automation
- Added `AI_TO_AI_AUTOMATION.md` as the canonical multi-agent automation and governance specification.
- Added a formal Agent → Theory/DAG → Empirical Design → Independent Replicator → Scientific Red-Team → Welfare Review → Evidence Passport → Human Gate sequence.
- Added machine-readable handoff fields for task identity, claims, evidence, methods, assumptions, confidence, contradictions, failure status, provenance and required next action.
- Added `automation/ai_handoff.schema.json` for the canonical handoff contract.
- Added `automation/sample_handoff.json` as an auditable example.
- Added `automation/validate_handoff.py` with schema, role-separation and SHA-256 integrity checks.
- Added `.github/workflows/ai_to_ai_contract.yml` as a zero-secret CI contract validator.
- Added the public rule `agent_consensus != scientific_truth` and preserved `discovery_claim_allowed = false`.
- Elevated AI-to-AI scientific automation to the root README with a GitHub-rendered architecture diagram and workflow badge.

### Documentation and research-software publication layer
- Redesigned the root `README.md` as a professional research-software landing page with explicit version semantics, quick start, flagship study, implemented capabilities, provenance policy, scientific limits and repository map.
- Added `ARCHITECTURE.md` as the canonical public description of the two-core V2.5 architecture.
- Added `SCIENTIFIC_ASSURANCE.md` with evidence classes, scientific gates, anti-p-hacking rules, adversarial review and Evidence Passport requirements.
- Added `RESEARCH_SOFTWARE_CARD.md` documenting intended use, users, inputs, outputs, known limitations, independence and data governance.
- Added `REPRODUCIBILITY.md` with provenance, chronology, environment, commit and validation requirements.
- Added `docs/QUICKSTART.md` and synchronized the public `/docs` landing page.
- Added explicit independence language so references to OpenAI, Microsoft, Google, DeepMind and related systems do not imply sponsorship or affiliation.

### In progress
- Execute and archive the first official FIZ→CIZ real-data workflow artifacts.
- Replicate on FF3 and additional archived portfolio families.
- Reduced-rank factor-dimension and multiplicity/FDR extensions.
- SEC × Fama–French × Damodaran chronology-safe empirical extension.

## [0.3.0-dev] — 2026-09-14

### Added
- Official public-data ingestion layer for Fama–French, Damodaran / NYU Stern and SEC EDGAR XBRL CompanyFacts.
- SEC filing-date chronology gate and source-provenance rules.
- Frozen first real-data study: `MNSc-FamaFrench-01`.
- Official July 2024 FIZ-era vs July 2025 CIZ-era Fama–French archive comparison design.
- Data Construction Sensitivity (DCS).
- Conclusion Reversal construct.
- HAC/Newey–West factor-premium inference.
- CAPM, FF3 and FF5 alpha-stability analysis.
- Six-table empirical output contract.
- SHA-256 source archive fingerprints and Evidence Passport™.
- Offline parser/logic tests and manual GitHub Actions real-data workflow.

### Scientific status
- Real-data reproducibility / measurement-change study under active validation.
- `discovery_claim_allowed = false` remains enforced.

## [0.2.0] — 2026-09-14

### Added
- GPT-5.6 Sol replaceable model backend.
- Controlled evidence metadata registry and relevance-gated RAG.
- Official Fama–French real-data adapter and verified CSV ingestion path.
- Six-table empirical runner with fixed effects, clustered/HC3 inference and temporal OOS checks.
- Stata `.do` export.
- Independent scientific red-team stage.
- Deterministic Evidence Passport™ and Human Gate.
- Google Drive synchronized archive.

### Scientific status
- Research workbench / pre-discovery.
- `discovery_claim_allowed = false` remains enforced.

## [0.1.0] — 2026-09-14

### Added
- Initial GPT-5.6 Sol Streamlit product prototype.
- Systems map and hypothesis tournament.
- ERA-style empirical design.
- Independent red-team review.
- Deterministic governance tests.

## [POC-001] — 2026-09-14

### Added
- First executable proof of concept using deterministic synthetic data.
- Two-core architecture validation.
- OOS specification tournament and Evidence Passport™.
