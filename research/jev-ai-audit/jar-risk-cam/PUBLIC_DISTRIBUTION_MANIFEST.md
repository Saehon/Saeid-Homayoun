# Public distribution manifest — 2026-10-16

| Platform | Canonical role | Current status |
|---|---|---|
| Google Drive | Private authoritative manuscript/data archive | SAVED |
| GitHub | Public code, tests, synthetic example, provenance | SAVED in draft PR #186 |
| Hugging Face | Public synthetic dataset/card | PREPARED; current ChatGPT HF OAuth lacks write-repos |
| Kaggle | Public synthetic dataset | PREPARED; no Kaggle connector/credentials available in this workspace |

## Publication boundary
Only synthetic data, validation code, documentation, and source links may be published to GitHub/Hugging Face/Kaggle. The unpublished manuscript and private/raw research data stay in Google Drive unless Dr. Saeid Homayoun explicitly authorizes public release after journal-policy review.

## Required credentials for final publication
- Hugging Face: write-enabled `HF_TOKEN` or reconnect account with repository write scope.
- Kaggle: `KAGGLE_USERNAME` and `KAGGLE_KEY` configured as GitHub Actions secrets or a connected Kaggle integration.

The workflow `.github/workflows/publish-risk-cam-public.yml` is manual only and requires the protected `research-publication` environment.
