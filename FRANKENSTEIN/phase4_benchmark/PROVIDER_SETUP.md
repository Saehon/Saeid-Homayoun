# FRANKENSTEIN Phase 4 — Provider Setup

The live benchmark workflow is ready but intentionally does not store credentials or model IDs in the repository.

## GitHub Actions secrets

Add only the providers you want to run:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY`
- `AZURE_OPENAI_API_KEY`
- `MOONSHOT_API_KEY`
- `DEEPSEEK_API_KEY`

## GitHub Actions variables

Record the exact model/version used:

- `OPENAI_MODEL`
- `ANTHROPIC_MODEL`
- `GEMINI_MODEL`
- `AZURE_OPENAI_MODEL`
- `MOONSHOT_MODEL`
- `DEEPSEEK_MODEL`

Endpoint variables:

- `OPENAI_CHAT_COMPLETIONS_URL` — optional; OpenAI default is already configured.
- `ANTHROPIC_MESSAGES_URL` — optional; Anthropic default is already configured.
- `ANTHROPIC_VERSION` — optional API-version header.
- `GEMINI_GENERATE_CONTENT_URL` — required for the exact Gemini model/API version being benchmarked.
- `AZURE_OPENAI_CHAT_COMPLETIONS_URL` — required; include the complete Azure deployment/API-version URL.
- `MOONSHOT_CHAT_COMPLETIONS_URL` — required; use the endpoint for the account/region under test.
- `DEEPSEEK_CHAT_COMPLETIONS_URL` — required.

## Execution

GitHub → Actions → **FRANKENSTEIN Phase 4 - Live Provider Benchmark** → Run workflow.

Missing providers are skipped explicitly. Configured providers are run on the same frozen case, evidence packet and scoring code.

## First controlled attempt

Workflow:
https://github.com/Saehon/Saeid-Homayoun/actions/runs/35991057487

Outcome:
- workflow execution: SUCCESS;
- benchmark harness: SUCCESS;
- OpenAI GPT/Codex: skipped — key/model not configured;
- Claude: skipped — key/model not configured;
- Gemini: skipped — key/model/endpoint not configured;
- Microsoft/Azure: skipped — key/model/endpoint not configured;
- Kimi/Moonshot: skipped — key/model/endpoint not configured;
- DeepSeek: skipped — key/model/endpoint not configured.

No provider result or ranking is claimed from this run.
