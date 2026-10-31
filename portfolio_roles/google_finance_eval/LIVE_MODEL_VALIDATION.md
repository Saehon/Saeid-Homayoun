# Real API model benchmark — access-controlled protocol

**Status: implemented and unit tested. Not executed on GPT, Gemini or Claude without a credential and explicit dataset-transfer authorization. No claims of actual model accuracy are made.**

This is an independent academic research portfolio, **not** a job assessment supplied or endorsed by OpenAI, Google DeepMind or Anthropic.

## Providers and official APIs

- OpenAI Responses API — https://platform.openai.com/docs/api-reference/responses
- Google Gemini generateContent — https://ai.google.dev/api/generate-content
- Anthropic Messages — https://platform.claude.com/docs/en/api/messages

Credentials are read exclusively from environment variables: `OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`. They are never displayed, checked into git, or written to reports.

## Run plan, with **zero network calls**

Use Python 3.9+ and a separate local JSONL file that the operator is authorized to use.

```bash
python -m portfolio_roles.google_finance_eval.live_provider_eval  --cases /path/to/private/synthetic_cases.jsonl --schema synthetic  --provider openai --model YOUR_MODEL_ID  --max-cases 2 --max-output-tokens 200  --input-usd-per-million 1 --output-usd-per-million 2  --price-source "https://openai.com/api/pricing checked YYYY-MM-DD"  --max-usd 0.25 --out /private/dry_run_report.json
```

The prices above are **example inputs, NOT current provider prices**. Verify published pricing and supply actual model-specific prices before proceeding.

## Real calls: opt-in only

Set a provider key in the **local environment** or an approved secret store; then append `--execute --authorize-data-transfer` to the command above.

- This transmits case question and evidence text to the selected model provider. Confirm license, retention, DPA and security approval first.
- The script will attempt at most ten cases, defaults to two, and caps each output at 1024 tokens. It rejects missing credentials.
- The `--max-usd` value is a **best-effort usage-cost estimate**, *not* a hard charge guarantee. Fees for cached/thinking tokens, provider billing differences, failures, retries outside this code, and any platform overhead can differ. A project-level spend limit is advised.
- Generation is **strictly opt-in**: neither normal GitHub Actions tests nor Pull Request updates issue API calls or incur model API expenses.
- Models must be explicitly selected; the runner never assumes a model name or silently changes versions.
- Reports include provider, model, source SHA-256, usage tokens, estimated expense, duration, abstention and *strict-text* matching with gold.
- **Strict-text match is not expert-correctness**, and small samples cannot support safety, model ranking, or recruitment claims.

## Data governance and independent review

FinanceBench is published by Patronus AI under CC BY-NC 4.0 (public 150-case sample). https://huggingface.co/datasets/PatronusAI/financebench

**Never commit dataset rows, report text, raw evidence or private predictions to a public repository without rights/privacy review.** This repository contains code only.

The benchmark must be run with a licensed copy downloaded separately and, where applicable, permitted for third-party API transfer.

Human evaluators blinded to provider identity should separately adjudicate correctness, evidence grounding and error taxonomy. The evaluators' names, conflicts, gold corrections, and code-review approvals need to be retained **outside the model-generated score file**. A successful CI run is not an independent review.

## Failure analysis

- Count `ERROR` cases and missing usage separately; do not silently remove them from denominators.
- Track hallucinated financial facts, citation fabrication, missing reporting periods, ratio denominator errors, currency / scale confusion and unsupported AI CapEx inference.
- Report by question category, company/year, sector and model, with confidence intervals only when sampling assumptions justify them.
