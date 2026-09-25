$ErrorActionPreference = "Stop"

Write-Host "NAAIL OpenLab - Kaggle + Hugging Face installer"
Write-Host ""

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python is required for the Kaggle CLI. Install Python 3.11 or later first."
}

Write-Host "Installing/updating Kaggle CLI..."
python -m pip install --upgrade kaggle

Write-Host ""
Write-Host "Installing/updating Hugging Face CLI..."
powershell -ExecutionPolicy ByPass -Command "irm https://hf.co/cli/install.ps1 | iex"

Write-Host ""
Write-Host "Verification:"
foreach ($cmd in @("kaggle", "hf")) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        Write-Host "  [OK] $cmd -> $($found.Source)"
    } else {
        Write-Warning "$cmd is not currently visible on PATH. Restart PowerShell and check again."
    }
}

Write-Host ""
Write-Host "Authentication is intentionally separate."
Write-Host "Kaggle: configure Kaggle authentication/API token."
Write-Host "Hugging Face: run 'hf auth login'."
Write-Host "Never commit credentials to GitHub."
