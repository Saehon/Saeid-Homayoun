# DARA Phase 3 — Gemini, Gemini CLI, BigQuery, Vertex AI and optional GPT

**Executable Colab notebook:** [Open Phase 3 in Colab](https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/DARA/colab/DARA_Phase3_AI_Service_Verification.ipynb)

**Cloud project:** `third-serenity-428705-g2`  
**Canonical Drive folder:** https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL  
**GitHub main repository:** https://github.com/Saehon/Saeid-Homayoun

## Execution instructions

1. Open the notebook from the GitHub/Colab link and choose **Runtime → Run all**.
2. Approve the Google Drive and Google Cloud authorization prompts; they are separate identity authorizations.
3. The notebook inspects Google API enablement, read-only BigQuery dataset metadata, and read-only Vertex AI custom-model metadata **only if permitted and enabled**.
4. Configure OpenAI Platform **only if** you want GPT model access **directly from Colab Python code**. Store `OPENAI_API_KEY` in Colab **Secrets** (key icon) and grant notebook access. It uses OpenAI `models.list` only, not paid inference. Your ChatGPT ↔ Drive/GitHub apps **do not** require this key.
5. Open the Gemini sidebar in Colab and test one benign question. Report the outcome when the notebook prompts you; this is a **user-reported** test, not an independently verified API connection.
6. For Gemini CLI, open **Google Cloud Shell** in a separate browser tab and run the shell checks below. The CLI is included in Cloud Shell and should not be installed on the PC or forcibly installed in Colab.
7. The Colab notebook asks you to enter the non-sensitive CLI version (or skip) and whether you intentionally performed an interactive CLI test. Do not paste credentials, OAuth tokens or API keys.
8. Last cell saves `DARA_PHASE3_VERIFICATION_<UTC>_<run>.json` to your **existing** DARA Drive folder, with readback validation. Return to ChatGPT for review through its independently connected Google Drive app.

## Cloud Shell — copy/paste

```bash
gcloud config set project third-serenity-428705-g2
gcloud config get-value project
command -v gemini
gemini --version
```

To check repository code availability **without writing to GitHub**:

```bash
git ls-remote https://github.com/Saehon/Saeid-Homayoun.git HEAD
```

Only if you approve a Gemini CLI interactive operation and its possible usage quotas, run `gemini` and sign in with your chosen account/method. A successful `gemini --version` means **CLI installed**, not authenticated or model access proven.

## Evidence semantics

| Test | A PASS proves | It does NOT prove |
|---|---|---|
| Colab Drive readback | A new test file was written/read | Every research dataset is accessible |
| Google Cloud ADC | Identity and configured project | Service API/IAM/billing access |
| BigQuery datasets.list | Read-only metadata endpoint accessible | SQL queries or billing-free processing |
| Vertex AI models.list | Authorized metadata endpoint responds | Gemini publisher model inference |
| OpenAI models.list | OpenAI API key authenticates | Paid GPT inference availability |
| Gemini Colab sidebar | User observed assistant response | SDK Vertex API works |
| Gemini CLI --version | CLI is installed in Cloud Shell | CLI is authenticated |
| Gemini CLI interactive test | User observed response | Continuous automated operation |

**No inference calls, service enablement, billing edits, resource provisioning, GitHub commits or writes to existing research files are executed by the notebook.**

Google documentation:
- https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal
- https://docs.cloud.google.com/bigquery/docs/listing-datasets
- https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/list
- https://platform.openai.com/docs/api-reference/models/list

Prepared: 2026-10-14.
