# OpenCloud — Lemon ICFR multi-provider prototype

OpenCloud is a provider-neutral orchestration **prototype** for Lemon-ICFR-US. It standardizes requests through a Unified Request Contract (URC) and supports a primary/challenger pattern across GPT, Claude, Gemini, and future local/open models.

## Boundaries
- Technology is replaceable.
- ICFR knowledge/evidence remains outside provider-specific adapters.
- Human approval remains authoritative.
- This public repository contains only a safe reference skeleton.
- Private Frankenstein prompts, benchmark gold labels, routing thresholds, customer data, credentials, and commercial decision logic remain private.
- Provider calls in `opencloud_core.py` are mocks; real API adapters are not enabled here.

## Existing OpenCloud.ai bridge
See `integrations/opencloud/README.md` for the separate OpenCloud.ai MCP/CLI bridge for GPT/Codex and Claude.

## Security
Never commit API keys, OAuth tokens, credentials, private benchmark data, or private prompts.
