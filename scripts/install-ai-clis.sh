#!/usr/bin/env bash
set -euo pipefail

echo "NAAIL OpenLab - Unified AI CLI installer"
echo "Checking prerequisites..."

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js is not installed. Install Node.js 22 or later, then run this script again." >&2
  exit 1
fi

NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]')"
if [ "$NODE_MAJOR" -lt 22 ]; then
  echo "Node.js 22 or later is required. Current version: $(node --version)" >&2
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is not available. Reinstall Node.js with npm enabled." >&2
  exit 1
fi

echo "Installing OpenAI Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI..."
npm install -g @openai/codex @anthropic-ai/claude-code @google/gemini-cli @github/copilot

echo
echo "Installed commands:"
for cmd in codex claude gemini copilot; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "  [OK] $cmd -> $(command -v "$cmd")"
  else
    echo "  [WARN] $cmd is not currently visible on PATH. Restart your shell and try again."
  fi
done

echo
echo "Next: from this repository, run codex, claude, gemini, or copilot and complete each provider's login."
echo "Never paste API keys into repository files."
