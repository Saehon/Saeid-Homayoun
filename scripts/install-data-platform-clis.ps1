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
if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Host "Installing/updating Databricks CLI with WinGet..."
    $existing = winget list --id Databricks.DatabricksCLI --exact --accept-source-agreements 2>$null
    if ($LASTEXITCODE -eq 0) {
        winget upgrade --id Databricks.DatabricksCLI --exact --accept-source-agreements --accept-package-agreements
    } else {
        winget install --id Databricks.DatabricksCLI --exact --accept-source-agreements --accept-package-agreements
    }
} elseif (Get-Command choco -ErrorAction SilentlyContinue) {
    Write-Host "WinGet was not found. Installing Databricks CLI with Chocolatey..."
    choco upgrade databricks-cli -y
} else {
    Write-Warning "Databricks CLI was not installed because neither WinGet nor Chocolatey is available."
    Write-Warning "Install WinGet or follow Databricks' official Windows installation instructions."
}

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
