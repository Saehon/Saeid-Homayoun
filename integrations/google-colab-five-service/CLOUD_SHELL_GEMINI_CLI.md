# Gemini CLI in Google Cloud Shell — setup and verification

**Target project:** `third-serenity-428705-g2`  
**GitHub code bridge:** `Saehon/Saeid-Homayoun`, branch `main`  
**Data archive:** Google Drive remains authoritative  
**Scope:** Gemini CLI (terminal coding agent), separate from Colab's built-in Gemini assistant and Vertex AI SDK.

## Why Cloud Shell?

Per Google Cloud documentation, Gemini CLI comes **preinstalled in Cloud Shell**, and its authentication can typically use the Cloud Shell identity. Therefore **do not install Gemini CLI on the user's Windows PC**, and there is no need to install the Gemini CLI Node package inside Colab. Cloud Shell and Colab are separate runtime environments; neither shares interactive sessions or Drive mounts automatically.

## Manual startup — no paid model call needed for initial checks

1. Visit [Google Cloud Console](https://console.cloud.google.com/) and activate **Cloud Shell** with the terminal icon.
2. Execute in the **Cloud Shell terminal**:

```bash
gcloud config set project third-serenity-428705-g2
gcloud config get-value project
gemini --version
```

3. Confirm project output is `third-serenity-428705-g2`; record the installed CLI version in your research setup log. If `gemini --version` fails, consult [Google's official CLI installation guide](https://geminicli.com/docs/get-started/installation/) before installing or modifying anything.
4. To start the agent, run `gemini`. Select **Sign in with Google** or your explicitly approved authentication method as applicable. This is a separate consent and may consume requests or incur charges based on the selected access mode.
5. To inspect the shared public repository code only, optionally use:

```bash
git clone --depth 1 https://github.com/Saehon/Saeid-Homayoun.git
cd Saeid-Homayoun/integrations/google-colab-five-service
git status --short
```

Do **not** rerun `git clone` inside a directory that already exists. Cloning is a manual, read-only checkout action; do not configure a GitHub push token unless separately authorized.

## Google Cloud project caveat

Cloud Shell has environment defaults that can differ from `gcloud config get-value project`. Gemini CLI may read `GOOGLE_CLOUD_PROJECT` from environment or an applicable `.gemini/.env`. If you deliberately choose a project-based Code Assist or Vertex AI auth method, check `geminicli.com/docs/get-started/authentication/` for that flow; do not assume the Cloud Shell default represents this user's project. Only choose Vertex AI after verifying API/IAM and any billing requirements. Never commit `.env` or credentials.

## Guardrails

- Google Drive is the canonical storage/archive; **Gemini CLI does not automatically have access to Colab's Drive mount**.
- Keep model prompts and tooling scoped to the integration folder; do not expose confidential CAM/ICFR data to unapproved services.
- Do not instruct Gemini CLI to execute unrestricted shell commands, commit/push code, alter IAM, activate paid APIs, delete datasets or overwrite results without explicit user approval.
- Gemini CLI produces proposals or reviews; ChatGPT remains the coordinating research assistant through connected GitHub/Drive, with a **human approval gate** before consequential execution.
- A version check verifies installation, **not** Gemini CLI authentication or actual model calls. A live model request is a separate test.
- No keys in GitHub; preserve `main` branch protection through pull requests.

## Verification record

| Check | How | Expected before running |
|---|---|---|
| Cloud Shell console access | Open terminal | NOT TESTED |
| Gemini CLI installed | `gemini --version` | NOT TESTED |
| Project selected | `gcloud config get-value project` | NOT TESTED |
| Gemini CLI authenticated | Interactive `gemini` login | NOT TESTED |
| GitHub code available | `git clone` and `git status --short` | NOT TESTED |
| Colab connection | Separate notebook Drive/Cloud tests | NOT TESTED |
| Drive access from Cloud Shell | Separate explicit authorization/workflow | NOT CONFIGURED |

Source: [Gemini CLI installation](https://geminicli.com/docs/get-started/installation/) · [Gemini CLI auth](https://geminicli.com/docs/get-started/authentication/) · [Google Cloud Shell guide](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal/).
