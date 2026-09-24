# Kaggle Research Workspace

This directory connects the GitHub repository **Saehon/Saeid-Homayoun** with the Kaggle account **sadhon**.

## Architecture

```text
ChatGPT
   ↕
GitHub connector
   ↕
Saehon/Saeid-Homayoun
   ↕
GitHub Actions
   ↕
Kaggle: sadhon
```

GitHub is the source of truth for code, metadata, documentation, and version history. Kaggle is the execution and publication layer for selected notebooks and datasets.

## One-time authentication setup

1. Open Kaggle account settings and create an API token.
2. In GitHub, open **Saehon/Saeid-Homayoun → Settings → Secrets and variables → Actions**.
3. Create a repository secret named exactly:
   `KAGGLE_API_TOKEN`
4. Paste the Kaggle token as the secret value.

Never commit the token, `kaggle.json`, passwords, or other credentials to this repository.

## Notebooks

Place each Kaggle notebook in its own subdirectory:

```text
kaggle/notebooks/<project-name>/
├── kernel-metadata.json
└── <notebook-or-script-file>
```

The workflow discovers every `kernel-metadata.json` below `kaggle/notebooks/` and runs:

```bash
kaggle kernels push -p <project-directory>
```

Privacy, accelerator, Internet access, and data-source settings should be declared in that notebook's Kaggle metadata.

## Datasets

Place each Kaggle dataset in its own subdirectory:

```text
kaggle/datasets/<dataset-name>/
├── dataset-metadata.json
└── <data-files>
```

The workflow discovers every `dataset-metadata.json` below `kaggle/datasets/`.

- If the dataset already exists on Kaggle, a new version is created.
- If it does not exist, the workflow creates it.
- New datasets are **private by default**.
- A manually dispatched workflow can explicitly request public creation.

The dataset `id` in `dataset-metadata.json` should use the Kaggle owner `sadhon`, for example:

```json
{
  "title": "Example Research Dataset",
  "id": "sadhon/example-research-dataset"
}
```

Add the appropriate Kaggle-supported license and descriptive metadata before publication.

## Sync behavior

The workflow is stored at:

`.github/workflows/kaggle-sync.yml`

It runs when Kaggle workspace files change on `main`, and it can also be started manually from the GitHub Actions page.

If `KAGGLE_API_TOKEN` has not yet been configured, the workflow exits successfully without publishing and prints a setup notice.

## Research use

Recommended Kaggle collections can be organized around:

- accounting and financial reporting;
- auditing and assurance;
- CAM/KAM;
- ICFR;
- IFRS;
- ESG and sustainability;
- corporate governance;
- forensic accounting;
- agentic AI and reproducible analytics.

Only data that may lawfully and ethically be published should be placed in Kaggle-facing folders. Confidential, licensed, proprietary, patent-sensitive, or personally identifiable data should remain outside the publication workflow.
