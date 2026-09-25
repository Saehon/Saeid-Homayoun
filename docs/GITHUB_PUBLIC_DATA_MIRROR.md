# GitHub to Kaggle and Hugging Face Public Data Mirror

This repository contains an automated publication pipeline for a consolidated research-data snapshot from Saeid Homayoun's public GitHub repositories.

## Distribution targets

- Kaggle: https://www.kaggle.com/datasets/sadhon/github-public-research-data
- Hugging Face: https://huggingface.co/datasets/SADHON/github-public-research-data
- Canonical GitHub account: https://github.com/Saehon
- Workflow: https://github.com/Saehon/Saeid-Homayoun/actions/workflows/publish-all-public-github-data.yml

## Scope

The mirror is intentionally public-safe, not a blind copy of every byte in every repository. The build includes data-oriented files from public, non-archived, non-fork repositories owned by Saehon, while excluding known third-party/code mirrors, credential-like paths, personal-record paths, files that match high-risk secret patterns, and unresolved Git LFS pointers.

This preserves the request to publish GitHub research data while avoiding accidental publication of credentials, private material, or third-party mirrors that should not be redistributed as the user's dataset.

## Provenance

Every publication contains:

- github-public-research-data.zip — the data snapshot preserving repository/path structure;
- DATA_MANIFEST.csv — source repository/path/commit/URL, repository license metadata, size, SHA-256, and mirrored path;
- SOURCE_REPOSITORIES.csv — repository-level inclusion/exclusion decisions;
- EXCLUSIONS.csv — candidate files deliberately excluded and the reason;
- SNAPSHOT_METADATA.json — dataset-level scope and safety policy;
- SNAPSHOT_SHA256.txt — integrity hash for the snapshot archive;
- README.md — dataset card and reuse notes.

The same snapshot is published to both Kaggle and Hugging Face through GitHub Actions using repository secrets KAGGLE_API_TOKEN and HF_TOKEN.
