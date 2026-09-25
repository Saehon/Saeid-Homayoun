# Cross-Platform Connection Gateway

This repository uses **GitHub as the permanent integration hub** for OpenAI/GPT, Kaggle, Hugging Face, and AWS.

## Architecture

```text
ChatGPT / OpenAI API
        |
        | OPENAI_API_KEY
        v
GitHub Actions  <---- canonical automation hub
   |     |     |
   |     |     +---- AWS (GitHub OIDC -> IAM role)
   |     +---------- Hugging Face (HF_TOKEN)
   +---------------- Kaggle (KAGGLE_API_TOKEN)

GitHub itself uses the automatic GITHUB_TOKEN.
```

## Why this reduces repeated approvals

Provider credentials are stored once in **GitHub Actions secrets**. Workflows then authenticate automatically on each run. AWS uses **OIDC**, so no long-lived AWS access key is required.

A provider may still require a new one-time authorization if a token is revoked, expires, is rotated, or its permissions change. GitHub and ChatGPT security confirmations cannot and should not be bypassed.

## Required repository secrets

Configure these under:

**Repository -> Settings -> Secrets and variables -> Actions**

| Service | Secret | Recommended permission |
|---|---|---|
| OpenAI / GPT | `OPENAI_API_KEY` | Project key with only the API access needed |
| Hugging Face | `HF_TOKEN` | Fine-grained token; write only to the repositories you publish |
| Kaggle | `KAGGLE_API_TOKEN` | Kaggle API token |
| AWS | `AWS_ROLE_ARN` | ARN of an IAM role trusted by GitHub OIDC |

Optional repository variable:

- `AWS_REGION` — defaults to `eu-north-1` in the gateway.

Do **not** commit credentials to the repository.

## AWS one-time OIDC setup

Create an AWS IAM role whose trust policy permits GitHub's OIDC provider `token.actions.githubusercontent.com` and restrict the subject to this repository:

```text
repo:Saehon/Saeid-Homayoun:*
```

Then store only the role ARN as the GitHub secret `AWS_ROLE_ARN`.

For production, narrow the trust condition further to the exact branch or GitHub environment and attach only the minimum AWS permissions required.

## Gateway workflow

Workflow:

```text
.github/workflows/cross-platform-connection-gateway.yml
```

It runs:

- manually with `workflow_dispatch`;
- every day as a connection-health check;
- whenever the gateway workflow or this document changes.

The jobs verify:

1. GitHub automatic token;
2. OpenAI API authentication;
3. Hugging Face authentication;
4. Kaggle CLI connectivity;
5. AWS STS identity through GitHub OIDC.

Missing credentials do not expose secrets. They generate a visible setup notice. Invalid configured credentials fail their service job, making the broken connection easy to identify.

## Operating rule

Use GitHub as the source of truth for automation and publishing. ChatGPT can work with the GitHub connector interactively, but durable unattended synchronization should run through GitHub Actions rather than relying on an interactive ChatGPT approval session.
