# DARA All-in-One Colab — Gemini + Google Workspace + Cloud Checks

**Open in Google Colab:** https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/DARA/colab/DARA_All_In_One_Google_Colab_Integration.ipynb

## Canonical topology

- GPT / ChatGPT: science/research coordination; **separate** Drive and GitHub connectors.
- Google Drive: Knowledge & Data Spine, authoritative DARA/archive folders.
- GitHub: Technology & Code Spine, code/notebooks/PR review; do **not** route every service through it.
- Colab: temporary Python runtime that directly mounts authorized Google Drive; authenticates Google Cloud separately.
- Gemini sidebar in Colab: interactive assistant; **no automatic universal access to all Google apps**.
- Gemini CLI + Workspace CLI: **Cloud Shell**, with independently authorized OAuth scopes and human approval.
- BigQuery / Vertex AI: optional metadata probes; no paid model inference or SQL queries here.

## Execute in Colab

1. Open the notebook linked above.
2. In Colab, select **Runtime → Run all**; this notebook contains no blocking Python `input()` prompts.
3. Approve the separate Google Drive mount and Google Cloud authentication prompts.
4. Read the status matrix printed near the end. A BLOCKED/UNKNOWN API is not silently converted into PASS.
5. Colab saves `DARA_ALL_IN_ONE_VERIFICATION_<run>.json` in **MyDrive/DARA_ResearchOS/**, then reads it back.
6. Copy the notebook's **Master Prompt** section into Gemini's Colab sidebar **if the sidebar is available**. Prompt text cannot grant tools or authorize Google Workspace APIs.
7. Return to ChatGPT and request an evidence-grounded review of the new JSON report through the existing connected Drive app.

**DARA canonical Drive folder:** https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL

## Google Cloud Shell (separate optional setup)

```bash
gcloud config set project third-serenity-428705-g2
gcloud config get-value project
gemini --version
node --version
npm --version
command -v gws || true
```

Do not run `gws auth setup` unreviewed. It may change APIs or create resources. Google Workspace OAuth clients and Drive scopes require interactive approval. If authorized, install `@googleworkspace/cli` **in Cloud Shell only** and follow official manual OAuth steps, beginning with read-only Drive. Do not store secrets in notebooks, version control, model prompts or reports.

## PASS interpretation

- Drive mount + readback: filesystem data access, **not** Gemini sidebar permission.
- Drive REST metadata: Google Workspace API permission for the tested credentials, **not** universal access.
- BigQuery datasets.list: read-only metadata, **not** SQL permission or dataset content.
- Vertex AI models.list: custom-model metadata, **not** Gemini text generation.
- Gemini / OpenAI secret status: presence only, **not** valid/paid model API inference.
- Cloud Shell Gemini CLI: requires separate terminal/runtime; not automatically tested by Colab.

Version 1.0, 2026-10-14. No GitHub code changes to other research projects or Drive data migrations.
