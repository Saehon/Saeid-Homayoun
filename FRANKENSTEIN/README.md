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

## Today: Phase 1 only

The first live example is intentionally small:

**Hugging Face FinancialPhraseBank → 5-row public sample + provenance manifest → FRANKENSTEIN GitHub data registry.**

No paid API and no Hugging Face secret are required.

Files:
- [5-phase roadmap](ROADMAP_5_PHASES.md)
- [architecture](ARCHITECTURE.md)
- [Phase-1 connector](connectors/huggingface_public_example.py)
- [data registry](data_registry/README.md)
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
| 3 | Free/open specialist accounting and audit agents | Advanced |
| 4 | GPT/Claude/Gemini/Kimi/DeepSeek cross-model benchmark | Hard |
| 5 | Evidence-governed multi-agent research platform | Sophisticated |

## Professional design principle

Do **not** copy every dataset into GitHub. A professional research repository keeps code and provenance in GitHub while the source platforms retain the authoritative/large data. This improves licensing clarity, reproducibility and maintainability.

## Research boundary

FRANKENSTEIN is for education and academic research. It does not issue an audit opinion, declare IFRS compliance, conclude fraud, declare a material weakness or replace qualified professional judgment.

**Evidence before narrative. Human authority remains final.**
