# OpenCloud Model Router

Provider-neutral routing layer for NAAIL/OpenLab projects.

## Policy
1. LOCAL_FIRST: prefer open/local models for routine work.
2. ESCALATE_ON_FAILURE: escalate when quality, confidence, tests, or task risk require it.
3. PROVIDER_NEUTRAL: no product depends on one model vendor.
4. HUMAN_GATE: consequential accounting/audit judgments require human approval.
5. NO_SECRETS: never commit credentials.

Providers: Ollama/IBM Granite, approved open-weight models, Gemini, Claude, OpenAI/Codex.
Consumers: LEMON, MANGO, KIWI, POMELO and future engines.

GitHub is the source of truth; Hugging Face and Kaggle consume versioned releases/benchmarks.
