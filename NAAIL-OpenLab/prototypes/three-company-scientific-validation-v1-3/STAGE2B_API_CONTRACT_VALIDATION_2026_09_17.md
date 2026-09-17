# NAAIL OpenLab™ — Stage 2B Provider API Contract Validation

**Date:** 2026-09-17  
**Control status:** `EXECUTED_VALIDATED`  
**Scientific benchmark:** `REGISTERED_NOT_EXECUTED`  
**Provider calls:** `NOT_EXECUTED`  
**Credentials loaded:** `FALSE`  
**Stage 2C:** `LOCKED`

## Purpose

Validate that the public Stage 2B runner matches the current official provider request contracts before any private credential is introduced. This control is static and non-secret: it does not load the private 21-task packet, gold key, API keys or provider outputs.

## Official contract anchors checked

- OpenAI Responses API: `gpt-6-astra`, `reasoning.effort`, `instructions`, `store`, and no-tools operation are supported by the current Responses API reference.
  - https://developers.openai.com/api/reference/cli/resources/responses/methods/create
- Google Gemini Interactions API: `system_instruction`, `generation_config.thinking_level`, and `store=false` are supported; `gemini-3.8-flash` is shown in current official examples.
  - https://ai.google.dev/gemini-api/docs/text-generation
  - https://ai.google.dev/gemini-api/docs/interactions-overview
- Anthropic Claude Fable 5: adaptive thinking is always on; manual `budget_tokens` thinking is not used; `output_config={"effort":"high"}` is the current migration pattern.
  - https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

## Runner hardening applied

1. OpenAI now uses `instructions=SYSTEM_CONTRACT`, `input=prompt`, `store=False`, `tools=[]`, and `reasoning={"effort":"high"}`.
2. Google uses `system_instruction=SYSTEM_CONTRACT`, `store=False`, `tools=[]`, and `generation_config` with high thinking.
3. Anthropic uses `system=SYSTEM_CONTRACT`, `tools=[]`, and `output_config={"effort":"high"}`; no manual thinking budget is sent for Fable 5.
4. A new AST-based checker fails if state-carrying parameters such as `previous_response_id`, `conversation`, `previous_interaction_id`, or background execution are introduced into the frozen provider calls.

## Executed validation

- Python compile check: PASS
- Existing Stage 2B hardening tests: **2 passed**
- New provider API contract checker: **PASS**
- Patched runner SHA-256: `f14a11a571e94f8988c00a084a7075279c0bcbe15b311c7c9a60be2698f37dd9`

Contract checker result:

```json
{
  "runner": "stage2b_runner.py",
  "runner_sha256": "f14a11a571e94f8988c00a084a7075279c0bcbe15b311c7c9a60be2698f37dd9",
  "status": "PASS",
  "checks": [
    "candidate model IDs match frozen roster",
    "OpenAI request is stateless, no-tools, store=false, high-reasoning",
    "Google request is stateless, no-tools, store=false, high-thinking",
    "Anthropic request is no-tools and uses Fable 5 high effort without manual thinking budget"
  ],
  "errors": [],
  "provider_calls_executed": false,
  "credentials_loaded": false,
  "scoring_opened": false
}
```

## Boundary

This validates request construction and blind-run controls only. It is not a provider runtime test and does not constitute a candidate-model execution. GitHub Actions runtime validation remains `BLOCKED_CI_RUN_NOT_OBSERVED` until an actual Actions run or another independent runtime executes the pinned SDK environment.
