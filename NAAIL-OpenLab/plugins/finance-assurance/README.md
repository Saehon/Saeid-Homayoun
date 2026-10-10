# NAAIL Finance & Assurance Plugin

**Status:** Research Prototype v0.1.0 — no live ERP/SEC access; no claims of audit effectiveness or regulatory compliance.  
**Maintainer:** Saeid Homayoun · [NAAIL OpenLab](../../README.md)  
**Reference inspiration:** [Anthropic Finance & Accounting Plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance); this is original, independently authored project code, not an Anthropic product or endorsement.

## What this is
A provider-neutral, evidence-governed skill-and-workpaper package for accounting, finance, management accounting, ICFR and SOX research. It translates routine finance procedures into reproducible tasks and imposes an **Evidence Passport / Human Approval** boundary. The **stable knowledge core** contains accounting, audit and scientific methodology; the **replaceable technology core** can later integrate OpenAI, Claude, Gemini, ERP, SEC EDGAR, Kaggle or Hugging Face using reviewed adapters. There is no third permanent core.

## Workflows
| Skill path | Task | Executable local check |
|---|---|---|
| `skills/journal-entry/SKILL.md` | Balanced, supported proposed journal entries | `journal-entry` |
| `skills/reconciliation/SKILL.md` | Bank/GL and subledger reconciliation | `reconciliation` |
| `skills/income-statement/SKILL.md` | Revenue/expense comparative workpaper | `income-statement` |
| `skills/variance-analysis/SKILL.md` | Actual vs. comparator analysis | `variance-analysis` |
| `skills/sox-testing/SKILL.md` | Deterministic sample and exception triage | `sox-testing` |
| `skills/close-management/SKILL.md` | Close checklist and evidence dependencies | prompt only |
| `skills/icfr-risk/SKILL.md` | Public-source risk and control mapping | prompt only |
| `skills/research-design/SKILL.md` | Multi-agent research benchmarking | prompt only |

## Offline quickstart (Python 3.10+, standard library only)
Run from this folder:
```bash
python -m unittest discover -s tests -v
python src/naail_finance.py journal-entry examples/journal-entry.json
python src/naail_finance.py reconciliation examples/reconciliation.json
python src/naail_finance.py income-statement examples/income-statement.json
python src/naail_finance.py variance-analysis examples/variance-analysis.json
python src/naail_finance.py sox-testing examples/sox-testing.json
```
All example records are **synthetic**. Outputs are JSON DRAFT workpapers that require professional review; they do not post to ledgers, select statistically representative audit samples or sign off financial statements.

## Claude-compatible skill packaging
The `.claude-plugin/plugin.json` manifest and `skills/*/SKILL.md` follow the conventions of Claude plugin skill folders. Load locally only after verifying Claude's currently supported installation procedure. They are not claimed to be published in any provider's marketplace. This project is also readable independently of Claude, ChatGPT, Gemini and local LLM platforms.

## Cross-platform links
- **Project master Google Drive folder:** https://drive.google.com/drive/folders/1cYPf2LARtKpEdFNWJ7AO4RXGK0rgU5eQ
- **GitHub portfolio:** https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab
- **Existing Kaggle NAAIL mirror (not yet this plugin):** https://www.kaggle.com/datasets/sadhon/naail-openlab
- **Existing Hugging Face NAAIL mirror (not yet this plugin):** https://huggingface.co/datasets/SADHON/NAAIL-OpenLab
- **Existing evidence-oriented ICFR module:** [Lemon-ICFR-US](../../../Lemon-ICFR-US/README.md)
- **Separate private control plane:** POMELO (integration subject to explicit authorization; no private content is copied here)

## Governance, evaluation, limitations
- Immutable source links, run ID, input SHA-256, calculation and exception trail are the intended Evidence Passport fields; the CLI emits an input hash and named evidence references.
- Every workpaper returns `DRAFT_REQUIRES_HUMAN_REVIEW`. No automated ledger posting, regulatory assurance, audit conclusion, approval, file upload or external system mutations.
- Do not load client files, unreleased manuscripts, private benchmarks or account credentials into public repositories. Use only synthetic or licensed public inputs.
- Simple rule checks are not statistical validation, professional audit sampling or independent replication. See [RESEARCH_PROTOCOL.md](RESEARCH_PROTOCOL.md), [CONNECTORS.md](CONNECTORS.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [SECURITY.md](SECURITY.md).
- Patent-sensitive and private implementations remain outside this open-source demo; project licensing and IP must be approved before standalone distribution.

**Provenance:** Independently authored for NAAIL; Anthropic's linked finance plugin is a format and workflow reference. Neither Anthropic nor OpenAI is affiliated with this project.
