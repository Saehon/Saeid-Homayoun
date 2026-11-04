# Hugging Face read/write publishing plan (FREE)
**Owner:** Dr Saeid Homayoun  
**Account:** [SADHON](https://huggingface.co/SADHON)  
**Project:** Audit AI Research Library  
**Updated:** 17 October 2026  
**Status:** Prepared in GitHub; Hugging Face write authorization and initial Space creation remain user-controlled.

## 0. Current authorization: know what is possible

- The connected ChatGPT Hugging Face credential has `jobs`, `openid`, `profile`, `read-mcp`, `read-repos` scopes. It does **not** have `write-repos`, `contribute-repos`, `manage-repos`, or `write-collections`.
- Hugging Face tools currently exposed in ChatGPT support inspection and jobs, not repository creation/file commits. Changing ChatGPT conversational permissions cannot grant missing OAuth scopes or new connector operations.
- You can edit your repositories in the Hugging Face web UI as `SADHON`, and GitHub can publish this static website using **Trusted Publishers** (GitHub OIDC) without storing any Hugging Face token.
- Public website: https://saeid-audit-ai-research-library.vercel.app
- Source proposed for merge: https://github.com/Saehon/Saeid-Homayoun/pull/187

## 1. Recommended architecture and costs

| Layer | Read | Write path | Cost |
|---|---|---|---|
| Hugging Face personal account | Web + current ChatGPT connector | HF browser editor, or HF authenticated CLI | Free, within limits |
| `SADHON/audit-research-library` Static Space | Anyone if public | Trusted Publisher: reviewed GitHub Actions workflow | Free static hosting; no compute |
| Hugging Face research Collection | HF browser | HF browser; optional OAuth `write-collections` via capable app | Free |
| US CAM / UK KAM / JEV / ICFR model repositories | Hugging Face browser + read connector | Manual model cards first; later per-repo trusted publishers | Free for modest documentation; storage limits apply |
| GitHub `Saehon/Saeid-Homayoun` | Public repo | Protected-main pull requests | Public repository and standard Actions within plan allowances |
| Google Drive / licensed data | Authorized researchers only | Keep in controlled Drive; never sync wholesale | No HF publication |
| Kaggle | Linked profile/notebooks | Independent publisher with separately validated data | No automatic HF mirroring |

Do **not** create a paid Gradio/Docker Space, GPU job, inference endpoint, or upgraded hardware. All plan steps are documentation and static upload.

## 2. One-time initial setup (user action in browser)

1. Log in to [Hugging Face](https://huggingface.co/login) as **SADHON**.
2. Create a new [Space](https://huggingface.co/new-space):
   - Namespace/owner: `SADHON`
   - Space name: `audit-research-library`
   - SDK: **Static HTML** (`sdk: static`)
   - Visibility: **Public**, since the source contains public links only
   - Do not select paid hardware or billing upgrades.
3. On the new Space, open **Settings → Trusted Publishers → Add Publisher**.
4. Select **GitHub Actions**, then set all three matching claims exactly:

   | Trusted Publisher claim | Value |
   |---|---|
   | `repository` | `Saehon/Saeid-Homayoun` |
   | `branch` | `main` |
   | `workflow` | `publish-hf-audit-library.yml` |

   These exact matches authorize **only** the chosen GitHub workflow to write to **this one** Hugging Face Space with a short-lived token.
5. Review and merge [GitHub PR #187](https://github.com/Saehon/Saeid-Homayoun/pull/187) after checking its website files and `.github/workflows/publish-hf-audit-library.yml`.
6. Open [GitHub Actions](https://github.com/Saehon/Saeid-Homayoun/actions) → **Publish Audit Library to Hugging Face (OIDC)** → **Run workflow** on `main`. The workflow intentionally runs only when manually dispatched; this avoids surprise pushes and unexpected compute.
7. Inspect the workflow logs (do not copy credentials) and verify:
   - [Space source page](https://huggingface.co/spaces/SADHON/audit-research-library) shows `README.md`, `index.html`, `style.css`, `app.js`, `links.json`, and `projects/*.html`.
   - The Space displays the four project pages and cross-platform links.
   - The uploaded `README.md` starts with YAML metadata containing `sdk: static` and `app_file: index.html`.
   - Only public documentation was uploaded.

**If GitHub Actions shows `invalid_grant`:** verify the Space exists and all three Trusted Publisher claims match exactly, including case and workflow filename. You can rerun after correction without rebuilding models.

## 3. Your own read/write options

**Browser (no token):**
- Read models and datasets by visiting [SADHON](https://huggingface.co/SADHON).
- On any repo you own, use **Files and versions → Add file / Upload files** to upload a model card, dataset card or static website file.
- For a website: edit the Space's `README.md` and `index.html` directly; note that the next GitHub publication will overwrite tracked files. Prefer reviewing GitHub PRs as the canonical source.

**Local computer / Google Colab (optional):**
```bash
pip install -U huggingface_hub
hf auth login
hf auth whoami
hf download SADHON/darwin-jev-risk-cam-synthetic-replication README.md --repo-type dataset
# Once the specific Static Space exists and your own login grants write:
hf upload SADHON/audit-research-library ./site . --repo-type space
```
The `./site` directory must contain the site assets and the Space's `README.md`. For a notebook, store any token in **Colab Secrets**, not in source code. Use only a fine-grained write token restricted to the repository you intend to update.

**ChatGPT:**
- Read through the current Hugging Face connector.
- Prepare/modify public site files through the GitHub connector and submit a pull request.
- After review + merge, the OIDC publishing workflow writes to Hugging Face.
- **Direct Hugging Face writes from this ChatGPT connector are not enabled**. Reconnection only helps if the provider supports write scopes **and** exposes write-capable tools. An assistant request cannot grant those capabilities by itself.

## 4. Extend to four models individually

Only after the website succeeds:

| Model ID (prospective; not yet verified created) | Repository type | First public release |
|---|---|---|
| `SADHON/auditbert-us-cam` | model | Model card + license/provenance/validation checklist; **no weights claim** |
| `SADHON/kambert-uk-kam` | model | Model card + UK-only eligibility rules |
| `SADHON/jev-accounting-risk-engine` | model | Synthetic example + point-in-time risk specifications |
| `SADHON/icfr-timesfm-risk` | model | Model card + ICFR label taxonomy and temporal checks |

Create each repository in the Hugging Face browser, preferably **private first** while auditing data and license rights. Each model should have a separately scoped publishing identity/workflow if automation becomes necessary. Do not upload model checkpoints or state predictive performance until independently validated.

## 5. Research safeguards

- **Never publish licensed Audit Analytics CAM/KAM rows**, proprietary firm-level data, confidential documents or raw Drive exports unless explicit redistribution permission is verified.
- Keep CAM selection, CAM informativeness, ICFR control effectiveness (effective / ineffective / unknown) and PCAOB findings distinct. No CAM is not equivalent to an audit failure; no weakness disclosure is not verified control effectiveness.
- For U.S. GAAP revenue matters use **ASC 606**; use IFRS 15 only for IFRS filers.
- Validate jurisdiction and years for EU/UK KAM records before representing them as UK-only.
- Respect chronological publication dates and prevent training leakage; do not imply fitted Jev or TimesFM models exist.
- **Security:** historical notebooks were reported to contain hardcoded HF tokens. Rotate/revoke any potentially exposed tokens before enabling a new upload route. Do not paste tokens into chat, issues, PRs, notebooks, or the public website.
- For a Trusted Publisher, keep GitHub `main` protected and require human review before merges. This is an intentionally human-controlled publication gate.

## 6. Completion criteria

- [ ] Public Static HTML Space created under `SADHON`.
- [ ] Trusted Publisher scoped to `Saehon/Saeid-Homayoun`, `main`, `publish-hf-audit-library.yml`.
- [ ] GitHub PR merged following review.
- [ ] Manual GitHub Action succeeds with OIDC; no `HF_TOKEN` stored.
- [ ] Space files and website successfully read back on Hugging Face.
- [ ] Read-only ChatGPT connector still works.
- [ ] Each of the four future model repos remains marked planned until independently created/verified.
- [ ] No licensed source material or secrets leaked; no paid resources activated.

## Official documentation

- [HF Trusted Publishers](https://huggingface.co/docs/hub/trusted-publishers)
- [HF Static HTML Spaces](https://huggingface.co/docs/hub/spaces-sdks-static)
- [HF OAuth supported scopes](https://huggingface.co/docs/hub/oauth)
- [HF CLI upload](https://huggingface.co/docs/huggingface_hub/guides/upload)
- [HF GitHub Actions](https://huggingface.co/docs/hub/repositories-github-actions)
