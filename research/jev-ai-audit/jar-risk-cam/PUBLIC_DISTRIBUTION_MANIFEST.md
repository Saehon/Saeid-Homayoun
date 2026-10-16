# Public distribution manifest — 2026-10-16

| Platform | Canonical role | Verified status |
|---|---|---|
| Google Drive | Private authoritative manuscript/data archive | **SAVED** |
| GitHub | Public code, tests, synthetic example, provenance | **SAVED** in draft PR #186 |
| Hugging Face | Public synthetic dataset/card | **PUBLISHED AND VERIFIED** |
| Kaggle | Public synthetic dataset | **BLOCKED — GitHub Actions secrets missing** |

## Hugging Face publication

**Dataset:** https://huggingface.co/datasets/SADHON/darwin-jev-risk-cam-synthetic-replication

The 2026-10-16 GitHub Actions publication job completed successfully. The public package includes the synthetic CSV, dataset card, panel validator, unit tests, replication ZIP and public distribution manifest. No unpublished manuscript or private Google Drive observations were uploaded.

## Kaggle publication blocker

The Kaggle GitHub Actions job installed the Kaggle client successfully but stopped before any API upload because both environment variables were empty:

- `KAGGLE_USERNAME`
- `KAGGLE_KEY`

Add those two values as repository or environment secrets, then re-run the manual workflow `.github/workflows/publish-risk-cam-public.yml` with target `kaggle`.

**Intended Kaggle slug:** `sadhon/darwin-jev-risk-cam-synthetic-replication`

## Publication boundary

Only synthetic data, validation code, documentation and source links may be published to GitHub/Hugging Face/Kaggle. The unpublished manuscript and private/raw research data stay in Google Drive unless Dr. Saeid Homayoun explicitly authorizes public release after journal-policy review.

## Scientific status

Public replication artifacts are infrastructure only. They do **not** establish empirical support for the hypotheses, a trained DARWIN/JEV model, Jev API inference, FT50 replication success, or Journal of Accounting Research acceptance.
