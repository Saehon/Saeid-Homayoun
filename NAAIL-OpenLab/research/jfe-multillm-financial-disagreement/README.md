# NAAIL Trust Finance — Multi-LLM Financial Risk / JFE Project

**Research branch:** `research/jfe-multillm-2026-10-04`  
**Target journal:** Journal of Financial Economics (JFE)  
**Researcher:** Saeid Homayoun, University of Gävle  
**Date:** 2026-10-04

## Research question
**Does disagreement among frontier large language models contain incremental information about future financial outcomes?**

## Core construct
`AIDisagreement_it = SD(score_GPT, score_Claude, score_Gemini, score_Llama, ...)`

Baseline model:

`Outcome_i,t+1 = α + β1 AIConsensus_it + β2 AIDisagreement_it + γ Controls_it + Firm FE + Time FE + ε_it`

## Package
- `JFE_Manuscript_Overview.md` — manuscript abstract, theory, hypotheses, design, and contribution.
- `Figure_NAAIL_Trust_Finance_JFE_Framework.svg` — GitHub-native research framework figure.
- `Microsoft_FY2026_Simple_POC.html` — simple Microsoft FY2026 proof of concept.
- `Microsoft_FY2026_POC_Evidence.md` — evidence snapshot and caveats.
- `literature_replication_matrix.csv` — literature / code / replication matrix.
- `REPLICATION_MANIFEST.md` — JFE-aligned reproducibility protocol.
- `WORD_AND_DRIVE_LINKS.md` — exact Drive links to the Word manuscript, PNG figure, ZIP bundle, and project folder.

## Important scientific boundary
The Microsoft scores are illustrative POC screening scores. They are **not** audit opinions, investment recommendations, or claimed outputs from Claude/Gemini/Llama. The large-sample empirical results remain to be run.

## Replication foundation
This project builds on reproducible LLM-finance research including de Kok (Management Science), Lopez-Lira & Tang (JFE), Jha-Liu-Manela (RFS), and He-Lv-Manela-Wu (JFE forthcoming / ChronoLLM).

## Google Drive
Project folder: https://drive.google.com/drive/folders/1sKMJbQdDXJ2a_B4tpsSDB3vKlANHFusD
