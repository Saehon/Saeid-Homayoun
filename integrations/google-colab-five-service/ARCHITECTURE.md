# GPT ↔ GitHub ↔ Google Ecosystem: Research Integration Blueprint

**Architecture approved in principle:** GPT/ChatGPT is the research controller, GitHub is the bridge for code and revisions, and Google Drive is the canonical archive.

## Authority and execution boundaries

| System | Role | Access and limits |
|---|---|---|
| ChatGPT/GPT | Plans experiments, analyzes results, reviews notebooks, prepares commits and PRs | Uses independently connected GitHub and Drive apps; does not directly control a running Colab kernel |
| GitHub (`Saehon/Saeid-Homayoun`, `main`) | Public source-code bridge, version control, reviewable PR changes | Never secrets or private research datasets; no runtime tokens |
| Google Colab | Interactive online Python executor | Opens notebook from GitHub; user approves notebook execution, mounts Drive and authenticates Cloud |
| Google Drive | Canonical storage, master index, datasets, model results, reports, manuscripts | ChatGPT accesses via connected app; Colab accesses via its own mount; distinct approvals |
| Google Cloud (`third-serenity-428705-g2`) | Cloud identity, BigQuery / Vertex AI services when explicitly used | IAM/APIs/billing require separate authorization; none assumed enabled |
| Gemini in Colab | Google UI coding assistant | Distinct from programmatic Gemini inference |
| Gemini Vertex AI | Optional model API via Google Cloud SDK | Dedicated API/permissions, explicit cost approval |
| OpenAI Platform GPT in Colab | **Optional** separate programmatic GPT inference from notebook | Requires Colab Secret `OPENAI_API_KEY` and its own Platform billing; NOT needed for ChatGPT connectors |

## Preferred loop: human approval as a gate

1. ChatGPT develops or reviews a **small-scope** notebook change.
2. Change is submitted as a GitHub branch / pull request to the main repository and merged subject to protections.
3. Open GitHub notebook in Colab; approve **Drive** and **Cloud** authorizations independently.
4. Colab runs approved notebook code in its own runtime, optionally using Gemini and Cloud services subject to API and billing readiness.
5. Colab writes permitted result files and execution logs to a named Drive project folder, preserving source files.
6. ChatGPT reads Drive report, checks evidence and reproducibility, and proposes the next GitHub code revision.

## What the bridge does *not* do

- GitHub does not share ChatGPT, Colab, Drive or Google Cloud login sessions.
- GitHub content commits do not launch a Colab runtime automatically.
- A Colab Drive mount is not a ChatGPT-to-Colab API connection.
- Colab does not inherit the ChatGPT Google Drive connector authorization.
- ChatGPT controls the **development/review loop**, not arbitrary remote code execution.
- SDK installation and client construction do not prove model API readiness.
- OpenAI GPT may operate in ChatGPT over connectors without providing `OPENAI_API_KEY` to Colab.

## Project rules

- **Canonical Google Drive** per project, with PROJECT_MASTER_INDEX, source/version lineage and read-back verified saves.
- **GitHub** for code/PR traceability only in this integration scope; preserve ongoing project-specific GitHub pause instructions.
- **No automatic secrets**: use interactive Google credentials and, only if optional OpenAI API is used, Colab Secrets.
- **No automatic paid inference or provisioning**, no data deletion, no broad cloud administrative rights.
- Version date: 2026-10-14.
