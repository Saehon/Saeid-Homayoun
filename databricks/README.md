# Databricks Workspace Integration

This directory is the GitHub-side entry point for future Databricks notebooks, jobs, data engineering, analytics and ML workflows.

## Role

Use the platforms as follows:

- **GitHub:** canonical source code, configuration, provenance, tests and review.
- **Databricks:** scalable execution, notebooks, jobs, Spark/SQL workflows and ML experiments.
- **Kaggle:** benchmark datasets and public notebooks.
- **Hugging Face:** public datasets, models and agents.

## Install the CLI

The repository includes:

```text
scripts/install-data-platform-clis.ps1
scripts/install-data-platform-clis.sh
```

After installation, verify:

```bash
databricks -v
```

Databricks CLI version 0.205 or later is required by the current Databricks CLI generation.

## Authentication

Do not add workspace tokens, passwords or credentials to this repository.

For local use, configure the Databricks CLI using the authentication method supported by your Databricks workspace.

For GitHub Actions, prefer a service principal / workload-identity approach when available.

If a token-based GitHub Actions workflow is later required, place credentials only in repository or environment secrets, for example:

```text
DATABRICKS_HOST
DATABRICKS_TOKEN
```

## Suggested repository layout

```text
databricks/
├── README.md
├── notebooks/
├── src/
├── tests/
└── resources/
```

Only add a deployable Databricks Asset Bundle after the target Databricks workspace, cloud, authentication method and first concrete workload are known.

## Research integrity

Databricks outputs used in accounting, auditing, finance, ESG or assurance research should preserve:

- data source and retrieval date;
- transformation history;
- notebook/job version;
- Git commit SHA;
- variable construction;
- sample filters;
- model parameters;
- random seed where applicable;
- validation and robustness results;
- human approval for consequential conclusions.
