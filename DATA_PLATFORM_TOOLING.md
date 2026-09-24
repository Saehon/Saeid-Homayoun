# Unified Data & ML Platform Tooling

This repository is configured to work with three external research and analytics platforms:

| Platform | Primary role in this repository | CLI |
|---|---|---|
| Kaggle | benchmark datasets, notebooks, reproducible public experiments | `kaggle` |
| Hugging Face | public datasets, models, agents and dataset/model cards | `hf` |
| Databricks | scalable analytics, notebooks, jobs and reproducible data/ML workflows | `databricks` |

GitHub remains the source of truth for code, configuration, documentation, manifests, small reproducible examples and provenance.

## Current repository status

### Kaggle

Kaggle is already integrated through:

- `kaggle/`
- `.github/workflows/kaggle-sync.yml`
- the repository secret `KAGGLE_API_TOKEN` when publishing is enabled.

### Hugging Face

Hugging Face is already integrated through:

- `huggingface/`
- Hugging Face publishing scripts
- GitHub workflows such as `.github/workflows/huggingface-microsoft-data-sync.yml`
- the repository secret `HF_TOKEN` when publishing is enabled.

### Databricks

Databricks support is added through:

- `databricks/README.md`
- the unified installation scripts
- `.github/workflows/data-platform-tooling-check.yml`

Databricks authentication is intentionally not stored in this public repository.

## One-command local installation

### Windows PowerShell

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-data-platform-clis.ps1
```

### macOS / Linux

```bash
bash scripts/install-data-platform-clis.sh
```

## Verify the three CLIs

```text
kaggle --version
hf --help
databricks -v
```

## Authentication

Do not commit credentials.

### Kaggle

Use Kaggle's API/OAuth setup. The existing GitHub workflow expects:

```text
KAGGLE_API_TOKEN
```

as a GitHub Actions repository secret.

### Hugging Face

Authenticate locally with:

```bash
hf auth login
```

The existing GitHub publication workflows use:

```text
HF_TOKEN
```

as a GitHub Actions repository secret.

### Databricks

For local interactive use, configure the Databricks CLI against your Databricks workspace according to the Databricks authentication documentation.

For GitHub Actions, prefer workload identity / service-principal authentication where your Databricks account supports it. If a token-based workflow is used, store the host and token only as GitHub Actions secrets such as:

```text
DATABRICKS_HOST
DATABRICKS_TOKEN
```

Never put these values in tracked files.

## Recommended architecture

```text
                     GitHub
          code + provenance + workflows
              /          |          \
             /           |           \
        Kaggle      Hugging Face    Databricks
     benchmarks      datasets /       scalable
     notebooks       models / agents  analytics
```

The same validated source dataset can therefore be prepared once in GitHub and distributed to the appropriate platform without changing the canonical research record.

## Official documentation

- Kaggle CLI: https://github.com/Kaggle/kaggle-cli
- Hugging Face Hub CLI: https://huggingface.co/docs/huggingface_hub/guides/cli
- Databricks CLI: https://docs.databricks.com/aws/en/dev-tools/cli/
