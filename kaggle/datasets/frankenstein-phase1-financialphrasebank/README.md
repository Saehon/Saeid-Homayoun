# FRANKENSTEIN Phase 1 — Kaggle Package

This folder is the Kaggle publication package for the first FRANKENSTEIN data-connection example.

## Flow

**Hugging Face → FRANKENSTEIN provenance registry → GitHub → Kaggle**

## Contents

- `financialphrasebank_sample.csv` — three-row demonstration sample.
- `provenance.json` — source and reproducibility metadata.
- `dataset-metadata.json` — Kaggle publishing metadata.

## Upstream source

FinancialPhraseBank:
https://huggingface.co/datasets/lmassaron/FinancialPhraseBank

## GitHub source

FRANKENSTEIN:
https://github.com/Saehon/Saeid-Homayoun/tree/main/FRANKENSTEIN

## Expected Kaggle URL

https://www.kaggle.com/datasets/sadhon/frankenstein-phase1-financialphrasebank

The existing GitHub Actions Kaggle Sync workflow creates new datasets privately by default. Public release should occur only after checking the rendered Kaggle dataset card, attribution and license.
