# Unified AI Coding Workspace

This repository is configured so the same project can be used with four major coding assistants:

| Provider | CLI / Agent | Repository instruction file |
|---|---|---|
| OpenAI | Codex CLI | `AGENTS.md` |
| Anthropic | Claude Code | `CLAUDE.md` → imports `AGENTS.md` |
| Google | Gemini CLI | `GEMINI.md` → imports `AGENTS.md` |
| GitHub / Microsoft | Copilot CLI and GitHub Copilot | `.github/copilot-instructions.md` and `AGENTS.md` |

## One-command installation

### Windows PowerShell

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-ai-clis.ps1
```

### macOS / Linux

```bash
bash scripts/install-ai-clis.sh
```

The scripts require Node.js 22 or later and install:

```text
@openai/codex
@anthropic-ai/claude-code
@google/gemini-cli
@github/copilot
```

## Start each assistant

```text
codex
claude
gemini
copilot
```

Authentication is intentionally not stored in this repository.

- **Codex:** start `codex` and sign in with ChatGPT, or configure an OpenAI API key outside the repository.
- **Claude Code:** start `claude` and authenticate with an eligible Claude account or Anthropic API configuration.
- **Gemini CLI:** start `gemini` and complete Google authentication.
- **Copilot CLI:** start `copilot`, then use `/login` if prompted.

## Security rule

Never commit credentials to GitHub. Use provider login flows, local environment configuration, or GitHub Actions secrets when a workflow specifically requires an API key.

## Shared operating model

All assistants should work from the same repository evidence and follow the same governance principles:

**Evidence → Analysis / Code → Tests → Falsification / Review → Reproducibility → Human Approval**

Provider-specific instruction files should remain thin wrappers around the canonical `AGENTS.md` so that Codex, Claude, Gemini, and Copilot do not drift into conflicting project rules.

## Official documentation

- OpenAI Codex: https://github.com/openai/codex
- Anthropic Claude Code: https://docs.anthropic.com/en/docs/claude-code/getting-started
- Google Gemini CLI: https://google-gemini.github.io/gemini-cli/
- GitHub Copilot CLI: https://docs.github.com/en/copilot/get-started/cli-quickstart
