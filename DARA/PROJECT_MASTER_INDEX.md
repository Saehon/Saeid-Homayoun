# DARA — PROJECT MASTER INDEX
**Version:** 1.0 · **Date:** 2026-10-14

## Authoritative locations
- **Canonical DARA folder (Drive):** https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL
- **GitHub main repository:** https://github.com/Saehon/Saeid-Homayoun
- **DARA versioned code:** https://github.com/Saehon/Saeid-Homayoun/tree/main/DARA
- **Open DARA notebook in Colab:** https://colab.research.google.com/github/Saehon/Saeid-Homayoun/blob/main/DARA/colab/DARA_Integration_Bootstrap.ipynb
- **Google Cloud project ID:** `third-serenity-428705-g2`
- **ChatGPT project link:** Not automatically obtainable from this workflow; record only after user provides a verified URL.

## Master register schema
| Field | Meaning |
|---|---|
| Project ID / name | Canonical existing research project identifier |
| Drive folder URL | Verified canonical source/archive |
| GitHub code URL / commit | If explicitly authorized, applicable code version |
| Colab URL | Runnable notebook with explicit execution authority |
| Data status | Verified / unverified; record coverage and permissions |
| Research stage | Proposal / QA / empirical / drafting / submitted |
| Last verified UTC | Actual run timestamp, not planned date |
| Outputs | Source-grounded result references |
| Next gate | Human approval / data check / compute / replication |

## Initially registered infrastructure
| ID | Drive | GitHub / Code | Status |
|---|---|---|---|
| DARA | https://drive.google.com/drive/folders/1OXZ6v1zB0G7wmlGezLCAvm8I4Egr2UPL | https://github.com/Saehon/Saeid-Homayoun/tree/main/DARA | Structure established, Colab runtime not yet executed |

## Existing projects
Do **not** create duplicate CAM, ICFR, ESG, asset-pricing or valuation folders. Locate their existing Drive folders and add verified links here **in a future explicitly approved registry backfill**. Do not infer undocumented samples, latest empirical results or completion dates.

## Storage and governance
Drive is authoritative for research data and outputs. GitHub is the software and interface spine. Project-specific GitHub synchronization pauses remain effective and are not changed by publishing this DARA infrastructure. GPT can inspect connected Drive and GitHub accounts under their separate authorization, but cannot assume access to Colab sessions.

## Colab verification
The `DARA_Integration_Bootstrap.ipynb` notebook checks local runtime, Drive readback, Google Cloud credential/project selection, GitHub notebook availability, and reports Gemini CLI / Gemini UI separately. It writes only a non-sensitive verification report to DARA's Drive folder after the user authenticates. **No billable Gemini/GPT inference calls are performed.**
