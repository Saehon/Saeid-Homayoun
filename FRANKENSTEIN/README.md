# FRANKENSTEIN™ — Evidence-Governed Accounting, Audit & Assurance Research Architecture

**Professional research scaffold · provider-neutral · open-data aware · human-gated**

FRANKENSTEIN connects **GitHub, Hugging Face, Kaggle and Google Drive** through a reproducible data registry, then routes evidence into deterministic accounting/audit tools and specialist agents.

## Simple view

```text
Hugging Face ─┐
Kaggle ───────┼──> Data Registry / Provenance ──> Accounting & Audit Tools
Google Drive ─┘                                      ↓
                                                 Specialist Agents
                                                      ↓
                                              Independent Review
                                                      ↓
                                               Human Approval
```

### Platform roles

- **GitHub:** code, architecture, manifests, tests, small samples and reproducible experiments.
- **Hugging Face:** public datasets and models.
- **Kaggle:** benchmark datasets and notebooks.
- **Google Drive:** controlled research files, drafts and larger working documents.
- **Free/open agents:** reusable accounting, audit, evidence, control, governance and ESG capabilities.

## Current status: Phase 4 benchmark harness active

The first live example has now been extended into a four-platform fabric:

**Hugging Face FinancialPhraseBank → GitHub provenance/sample → Kaggle private dataset → Google Drive controlled registry → bounded specialist accounting/audit agents.**

No paid API and no Hugging Face secret are required.

Files:
- [5-phase roadmap](ROADMAP_5_PHASES.md)
- [architecture](ARCHITECTURE.md)
- [Phase-1 connector](connectors/huggingface_public_example.py)
- [data registry](data_registry/README.md)
- [Phase-2 four-platform registry](data_registry/phase2_data_fabric/README.md)
- [Phase-3 specialist agent layer](phase3_agents/README.md)
- [Phase-3 integration map](phase3_agents/INTEGRATIONS.md)
- [Phase-4 benchmark harness](phase4_benchmark/README.md)
- [Phase-4 provider setup](phase4_benchmark/PROVIDER_SETUP.md)
- [Phase-4 current status](phase4_benchmark/status.json)
- [GitHub Action](../.github/workflows/frankenstein_phase1_huggingface.yml)

Run locally:

```bash
python FRANKENSTEIN/connectors/huggingface_public_example.py
```

Or run the GitHub Action manually from **Actions → FRANKENSTEIN Phase 1 - Hugging Face Public Data**.

## Five phases

| Phase | Scope | Complexity |
|---|---|---|
| 1 | One public Hugging Face connection + provenance | Simple |
| 2 | Hugging Face + Kaggle + Google Drive registered data fabric | Moderate |
| 3 | Free/open specialist accounting and audit agents — **ACTIVE** | Advanced |
| 4 | GPT/Claude/Gemini/Microsoft-Azure/Kimi/DeepSeek cross-model benchmark — **HARNESS ACTIVE** | Hard |
| 5 | Evidence-governed multi-agent research platform | Sophisticated |

## Professional design principle

Do **not** copy every dataset into GitHub. A professional research repository keeps code and provenance in GitHub while the source platforms retain the authoritative/large data. This improves licensing clarity, reproducibility and maintainability.

## Research boundary

FRANKENSTEIN is for education and academic research. It does not issue an audit opinion, declare IFRS compliance, conclude fraud, declare a material weakness or replace qualified professional judgment.

**Evidence before narrative. Human authority remains final.**


## Phase 4 execution status

The benchmark harness and deterministic scorer are validated. A controlled GitHub Actions attempt was also executed:
https://github.com/Saehon/Saeid-Homayoun/actions/runs/35991057487

All six proprietary-provider calls were **skipped because the corresponding GitHub secrets/model variables are not configured**. This is the intended safe behavior. No model ranking or provider-performance result is claimed yet.
