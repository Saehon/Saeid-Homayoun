# Google Drive Synchronization

This ECONOVA-S™ v0.3 study is synchronized with a canonical Google Drive study record.

**Study:** MNSc–FamaFrench–01 — *When Data Construction Changes Asset Pricing: The FIZ–CIZ Transition and the Stability of Fama–French Factors*

**Google Drive canonical study record:**
https://docs.google.com/document/d/1vseh8YEFbnCkCcfzRxZfNIgXUGn20g8mGzWHV2oXUso/edit

**Latest synchronized Drive revision:**
`ANLCKQl5iFkwt8umdkcJJ2bZ9-oP_rSB4q3oG4Ht-WQ_oumqxXNg6BOn_OzymJDTWK7Hu5CLyXD1q2Hav17lhOvXE5bwGMFrytel9XnHvzc`

**ECONOVA-S canonical architecture master:**
https://docs.google.com/document/d/1l3cZJY23FJr_9oiEPc2vRCrH6Er96AfQX-WAoCzJIRQ/edit

## Source of truth

GitHub remains the executable source of truth for code, tests, workflows, protocol manifests, and version history. Google Drive preserves the canonical study record, design, scientific gates, and cross-system checkpoint.

## V3 discovery package now frozen in GitHub

- `v3/study_manifest.json`
- `v3/protocol/ATTRIBUTION_FIREWALL.md`
- `v3/protocol/01_RESEARCH_GOAL.md`
- `v3/protocol/02_LITERATURE_GROUNDING.md`
- `v3/protocol/03_HYPOTHESIS_TOURNAMENT.json`
- `v3/protocol/04_CAUSAL_DAG.md`
- `v3/protocol/05_VARIABLE_DNA.csv`
- `v3/protocol/06_EMPIRICAL_MANIFEST.json`
- `v3/protocol/07_DISCOVERY_SEARCH.json`
- `v3/protocol/08_LATENT_STRUCTURE.md`
- `v3/protocol/09_REPLICATION_REPORT.md`
- `v3/protocol/10_RED_TEAM_REPORT.md`
- `v3/protocol/11_FALSIFICATION_REPORT.md`
- `v3/protocol/12_CHAIN_OF_EVIDENCE.json`
- `v3/protocol/13_COE_AUDIT.json`
- `v3/protocol/14_EVIDENCE_PASSPORT.json`
- `v3/protocol/15_HUMAN_GATE.md`

## Critical interpretation rule

The July-2024 vs July-2025 comparison estimates **archive / construction-regime sensitivity**. It does not identify the pure causal effect of FIZ→CIZ because ordinary revisions, corrections, reclassifications, or other archive maintenance may also contribute to vintage differences.

The Damodaran / NYU Stern layer is a **complementary industry benchmark**, not validation or identification of the FIZ→CIZ transition.

## Validation checkpoint

- Main workflow-integration commit: `14d37f2f7090b837955831cfff701af876ed2bcc`
- Validation PR: https://github.com/Saehon/Saeid-Homayoun/pull/15
- Validation branch: `validation/mnsc-v3-protocol`
- PR head commit: `293fdc8d405e4280c6282cf9b3921f37e1d33963`
- Connected GitHub interface currently exposes no workflow run for this PR head; CI is therefore **not claimed as passed**.

## Current scientific status

- Research goal and hypothesis tournament frozen.
- DAG / attribution firewall frozen.
- Variable DNA and empirical manifest frozen.
- Discovery search rules frozen; no p-value optimization permitted.
- Replication, adversarial review, falsification, Chain-of-Evidence, CoE Audit, and final Human Gate remain incomplete.
- `identification_gate = false` for pure FIZ→CIZ causality.
- `human_gate_approved = false`.
- `discovery_claim_allowed = false`.

**Synchronized:** 2026-09-14
