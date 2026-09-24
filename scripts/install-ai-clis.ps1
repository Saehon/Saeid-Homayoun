$ErrorActionPreference = "Stop"

Write-Host "NAAIL OpenLab - Unified AI CLI installer"
Write-Host "Checking prerequisites..."

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    throw "Node.js is not installed. Install Node.js 22 or later, then run this script again."
}

$nodeVersion = (node --version).TrimStart("v")
$nodeMajor = [int]($nodeVersion.Split(".")[0])
if ($nodeMajor -lt 22) {
    throw "Node.js 22 or later is required. Current version: $nodeVersion"
}

if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    throw "npm is not available. Reinstall Node.js with npm enabled."
}

Write-Host "Installing OpenAI Codex, Claude Code, Gemini CLI, and GitHub Copilot CLI..."

npm install -g @openai/codex @anthropic-ai/claude-code @google/gemini-cli @github/copilot

Write-Host ""
Write-Host "Installed commands:"
foreach ($cmd in @("codex", "claude", "gemini", "copilot")) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        Write-Host "  [OK] $cmd -> $($found.Source)"
    } else {
        Write-Warning "$cmd was installed but is not currently visible on PATH. Restart PowerShell and try again."
    }
}

Write-Host ""
Write-Host "Next: from this repository, run codex, claude, gemini, or copilot and complete each provider's login."
Write-Host "Never paste API keys into repository files."
