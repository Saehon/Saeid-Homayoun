# Hugging Face × Google Drive × GitHub — cross-project integration plan
**Owner:** Dr Saeid Homayoun · **Date:** 2026-10-17 · **Status:** Integration registry prepared; releases NOT authorized.

**Purpose:** Link all 15 canonical projects and four supporting research tracks into one no-cost Static HTML Hugging Face website, plus **optional future project-specific** model cards and synthetic/public benchmarks where evidence and licenses permit.

## What is already connected
- Public website (Vercel): https://saeid-audit-ai-research-library.vercel.app
- GitHub PR for the website: https://github.com/Saehon/Saeid-Homayoun/pull/187
- Hugging Face account: https://huggingface.co/SADHON (ChatGPT connection: read only).
- Existing Hugging Face portfolio index: https://huggingface.co/datasets/SADHON/accounting-audit-ai-portfolio
- Existing public synthetic project: https://huggingface.co/datasets/SADHON/darwin-jev-risk-cam-synthetic-replication — existence does **not** certify release safety.

## Exact classification (not a maturity/quality score)
| # | Canonical project | HF integration | Priority | Allowed next artifact (not yet approved) |
|---|---|---|---|---|
| 01 | Making Risk Public | Metadata only | High | Manuscript and linked CAM evidence controlled in Drive; publish descriptive research summary only after author/right-to-release approval |
| 02 | Risk–CAM Alignment | Synthetic/demo candidate | Very high | Synthetic risk schema, reproducibility documentation; existing HF synthetic starter needs separate release audit |
| 03 | CAM-ADAPT | Synthetic/demo candidate | High | Synthetic diagnostic-vs-response changes, frozen topic codebook, comparison scripts after release clearance |
| 04 | CAM-SHADOW | Synthetic/demo candidate | High | Synthetic eligible-risk vs disclosure-selection benchmark; not undisclosed audit-effort labels |
| 05 | ICFR–SEC–TimesFM | Model blueprint | Very high | Time-series evaluation schema, synthetic firm histories and model card; hourly research remains Drive-only |
| 06 | DARWIN–ACRIS | Model blueprint | High | Research taxonomy and independently coded/synthetic auditor-response benchmark only |
| 07 | Constructing Audit Significance | Metadata only | Low | Qualitative fieldwork and draft manuscript remain private; project navigation only |
| 08 | AI CapEx Audit Oversight | Synthetic/demo candidate | Medium | Illustrative CapEx and internal-control data dictionary; actual CapEx verification required |
| 09 | CAM/KAM–AuditBERT | Model blueprint | Very high | Separate US CAM and UK KAM model cards; future public weights only after licensed-data and bias assessment |
| 10 | Verifiable Human–AI | Synthetic/demo candidate | High | Human-in-the-loop evaluation cards and traceable synthetic agent reasoning tests |
| 11 | AI Investment and Valuation | Synthetic/demo candidate | Medium | Synthetic scenario generation and model comparisons; no undocumented AI investment panel |
| 12 | Fama–French AI Asset Pricing | Metadata only | Low | Navigation only. Canonical hourly data and code remain Drive-only; GitHub execution paused |
| 13 | Damodaran AI Valuation | Metadata only | Low | Navigation only. Canonical hourly data and code remain Drive-only; GitHub execution paused |
| 14 | Tokenized AI Management Accounting | Synthetic/demo candidate | High | TDABC token-level synthetic costing and data-center energy/risk benchmark; no proprietary meter records |
| 15 | Forensic Agentic AI | Synthetic/demo candidate | High | Synthetic fraud/AAER-style validation cases, human gate; no unverified accusations or private records |

## Supporting programs (not additional manuscripts)
- **JEV Common Risk Engine:** Synthetic/demo candidate; Existing synthetic artifact; verify leakage, rights and evaluation before more releases.
- **NAAIL / LEMON-ICFR / POMELO:** Documentation only; Governance and controlled simulation plans only; do not activate paused CI or training pipelines.
- **MacAma Multi-Agent Scientist / paper2agent:** Documentation only; Agent workflow diagrams/public literature references only; private RAG/evidence datasets stay controlled.
- **ESG / SDG / Sustainability Analysis:** Synthetic/demo candidate; Only openly licensed or synthetic ESG documents; no licensed scores or vendor datasets.

## Read/write architecture
1. **Google Drive** remains sole authoritative storage of empirical data, private research plans and manuscripts. No automatic upload.
2. **Private GitHub (RISK-INDEX)** stores minimal metadata and this project-to-platform crosswalk only. Never activate workflows for confidential corpus. This index is not a transfer of data access or release rights.
3. **Public GitHub website** contains only explicitly public links, model blueprints and this site registry. GitHub branch protection and PR review remain mandatory.
4. **Hugging Face** supports reads through ChatGPT connector; the free Static Space can receive **website-only** files by a manually authorized, one-repository Trusted Publisher workflow after owner review.
5. Future **individual model/dataset repos** require a separate verified repo, owner authorization, per-repository Trusted Publisher configuration and artifact-specific release manifest. This configuration is not yet created. No CI auto-push to many HF repositories.
6. **Kaggle** and **Google Scholar** are profile/publication links; do not claim automatic synchronization.

## Sequence (user priority CAM → ICFR → PC)
- **Phase A (priority CAM):** #01, #02, #03, #04, #06, #09 + JEV — publish **navigation pages only now**. Later, independently cleared CAM classifier cards and synthetic demonstration baselines; no licensed opinions.
- **Phase B (ICFR):** #05 + #08, LEMON-ICFR support — document label taxonomy `effective/ineffective/unknown`, as-of features, and time-series benchmarking. Keep routine ICFR GitHub processing paused.
- **Phase C (PCAOB/PC):** #08, #15 and NAAIL relevant assurance agents — use auditor-level published inspection evidence without invented firm identifiers.
- **Phase D (other relevant):** #10, #11, #14 plus ESG and agentic infrastructure — only synthetic, licensed-open, or documentation-level releases.
- **Index-only projects:** #07 qualitative, #12 Fama–French, #13 Damodaran — do not start new HF publications or GitHub hourly execution.

## Scientific and security release gates
**All must be PASS** before any new public data/model/weights push:
1. Written **owner approval identifying exact file list**, HF target, and visibility.
2. **Data rights**: licensed CAM/KAM/ICFR and private Drive content never publicly mirrored; vendor-derived synthetic content requires a leakage and rights audit.
3. **Secrets**: rotate/revoke previously exposed tokens; scan notebook outputs and Git history, not just current files.
4. **Scientific**: firm-year chronology, geographic UK-only filtering for UK KAM, independence of CAM selection vs effectiveness and ICFR effective/ineffective/unknown; ASC 606 for US GAAP, IFRS15 only for IFRS filers; human label QA, proper held-out test.
5. **Reproducibility**: documented checksum, code version, split logic, model card, uncertainty, null findings, independent readback and no fictitious results.
6. **CI governance**: no paid compute, auto-triggered training, large-data pulls, or running paused pipelines. Only the already-prepared static website publisher may be manually run after initial Space and OIDC configuration by user.

## Acceptance checklist
- [x] All 15 projects classified by integration type, priority and public/private boundaries.
- [x] Four supporting tracks identified; all 15 can be reached from the public portfolio.
- [x] GitHub source/links prepared for human review on PR.
- [ ] Website PR merged and changes redeployed on Hugging Face (currently unauthorized write).
- [ ] Static Space created by account owner.
- [ ] Site-only Trusted Publisher configured and first readback verified.
- [ ] Each optional future model/dataset upload individually approved and verified.
