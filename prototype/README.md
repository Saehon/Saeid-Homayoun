# ECONOVA-S™ GPT-5.6 Sol Product Prototype

A runnable product prototype implementing the **ECONOVA-S™ dual-core scientific economic intelligence architecture** with GPT-5.6 Sol as a replaceable AI backend.

## Product objective

Turn a research question into a governed scientific design without allowing the AI model to approve its own scientific claims.

**Workflow**

`Question → Systems Map/DAG → Hypothesis Tournament → ERA Empirical Design → Independent Red Team → Evidence Passport → Human Gate`

## Architecture

### Stable Economic Knowledge Core™
Encoded as non-negotiable scientific instructions:
- economics and finance theory;
- causal DAG governance;
- construct/Variable DNA discipline;
- identification and replication rules;
- FT50/AJG/ABS 4*/4 relevance-gated benchmarking;
- robustness/falsification/OOS requirements;
- private vs social value and welfare;
- human approval.

### Replaceable Technology Core™
Current default:
- OpenAI `gpt-5.6-sol`;
- Responses API;
- reasoning effort configurable as medium/high/xhigh/max;
- optional public web search.

The model can later be replaced without changing the scientific schema.

## Why three model calls?

1. **Discovery Agent** — systems map, DAG, competing hypotheses and ranking.
2. **Econometric Design Agent** — ERA-style reproducible empirical design.
3. **Independent Red-Team Agent** — attacks constructs, identification, chronology, specification search, external validity and welfare claims.

The **Evidence Passport™ and Human Gate are deterministic application logic**, not a fourth model call. This prevents the model from approving itself.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env  # Windows; use cp on macOS/Linux
# Put your API key in .env

streamlit run app.py
```

## Environment

```text
OPENAI_API_KEY=...
ECONOVA_MODEL=gpt-5.6-sol
ECONOVA_REASONING=high
```

## Scientific status

This prototype generates **research designs**, not empirical discoveries. It does not contain a curated licensed FT50 corpus or a verified empirical database. When web search is enabled, the model may retrieve current public material, but publication-grade work should still use a controlled literature corpus and verified datasets.

No discovery claim is permitted until real-data provenance, construct validation, credible identification, replication/OOS validation, adversarial review, robustness/falsification, economic significance, welfare interpretation, and explicit human approval are complete.

## IP

Governed by the ECONOVA-S™ Research and Non-Commercial License in the parent repository. Commercial use requires prior written permission.

Copyright © 2026 Saeid Homayoun. ORCID: 0000-0002-2536-0446.
