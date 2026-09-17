# NAAIL OpenLab™ — Stage 2B Candidate Assignment & Run Contract

**Date:** 2026-09-17  
**Stage:** `2B — Independent Blind Model Runs`  
**Scientific execution status:** `REGISTERED_NOT_EXECUTED`  
**Candidate-assignment status:** `EXECUTED_VALIDATED` as readiness infrastructure only  
**Maturity:** `RESEARCH_PROTOTYPE`

> **PATENT RIGHTS RESERVED — PATENT APPLICATION PREPARATION IN PROGRESS**

## Purpose

Freeze a provider-diverse, promotion-grade candidate set and a common execution condition before any model sees the private V1.3B benchmark prompts. This artifact does not contain the private prompts or gold key and does not constitute benchmark execution.

## Frozen candidate set

| Candidate | Provider | Model/API identifier | Current provider position | Run status |
|---|---|---|---|---|
| C01 | OpenAI | `gpt-6-astra` | current flagship for hardest end-to-end work | `READY_PROVIDER_CONNECTION_REQUIRED` |
| C02 | Google | `gemini-3.8-flash` | GA stable; current most intelligent Flash model | `READY_PROVIDER_CONNECTION_REQUIRED` |
| C03 | Anthropic | `claude-fable-5` | current Fable 5 API identifier; Fable 5.1 service announced September 2026 | `READY_PROVIDER_CONNECTION_REQUIRED` |

The candidate set intentionally spans three independently operated model families. No same-session self-comparison is eligible.

## Common closed-evidence condition

Every candidate must receive exactly the same frozen V1.3B task order and the same E1–E8 evidence packet. For the primary benchmark condition:

- browsing/search grounding: **disabled**;
- external tools/functions: **disabled**;
- file search beyond the supplied evidence packet: **disabled**;
- prior conversation context: **none**;
- private gold key: **not supplied**;
- candidate outputs: frozen before any scoring;
- failures/refusals/nulls: retained as observations;
- sampling controls such as temperature/top-p: omitted unless required by a provider, because current model APIs differ in their support for those controls;
- reasoning/thinking setting: **high** where a directly comparable provider control exists.

Provider-specific reasoning controls:

- OpenAI `gpt-6-astra`: `reasoning.effort = high`;
- Google `gemini-3.8-flash`: `thinking_level = high`;
- Anthropic `claude-fable-5`: adaptive thinking with `output_config.effort = high`.

## Frozen output envelope

Each candidate must return one machine-parseable record per task in task order with at least:

- `task_id`;
- `response`.

No candidate may receive another candidate's response. The raw provider response must be retained exactly and SHA-256 hashed before normalization or scoring.

## Cost baseline recorded at freeze date

The pricing below is a **run-planning baseline only**. Actual Stage 2D CVPO uses observed run usage and the provider price in force at the execution timestamp.

| Candidate | Input USD / 1M tokens | Output USD / 1M tokens | Freeze-date note |
|---|---:|---:|---|
| C01 OpenAI GPT-6 Astra | 10.00 | 50.00 | OpenAI official API model page, checked 2026-09-17 |
| C02 Gemini 3.8 Flash | 0.75 | 3.75 | introductory paid-tier price through 2026-12-31 |
| C03 Claude Fable 5 / Fable 5.1 service | 10.00 | 50.00 | Anthropic public availability/pricing, checked 2026-09-17 |

Pricing is not used to rank scientific quality and does not substitute for observed CVPO telemetry.

## Evidence and provenance requirements per run

Each run must record provider, exact model identifier returned by the API if available, UTC timestamp, independent session/run ID, packet version, E1–E8 hash set, browsing/tool state, inference settings, raw output, response SHA-256, input/output tokens where exposed, latency, API cost, price source, and run outcome.

## Promotion boundary

This candidate assignment makes Stage 2B **ready to execute**, but it does not change the scientific execution state. Until independently invoked provider runs exist:

- Stage 2B remains `REGISTERED_NOT_EXECUTED`;
- Stage 2C scoring remains locked;
- numeric CVPO remains `NOT_EXECUTED`;
- Phase 2 remains open;
- no Human Gate or independent replication state changes;
- Phase 3 and Phase 4 are not promoted.

## Provider sources used for candidate freeze

- OpenAI model documentation: `https://developers.openai.com/api/docs/models/gpt-6-astra`
- Google Gemini 3.8 Flash documentation: `https://ai.google.dev/gemini-api/docs/latest-model`
- Google Gemini pricing: `https://ai.google.dev/gemini-api/docs/pricing`
- Anthropic current-model/deprecation documentation: `https://docs.anthropic.com/en/docs/about-claude/model-deprecations`
- Anthropic Fable availability/pricing: `https://www.anthropic.com/claude/fable`

The next permitted scientific action is to connect or otherwise obtain independent API execution routes and run C01, C02 and C03 under this frozen contract.
