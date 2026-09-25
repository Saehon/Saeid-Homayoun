param(
  [ValidateSet("core","all")]
  [string]$Mode = "core",
  [string]$Root = "external-open-source"
)

$ErrorActionPreference = "Stop"

$coreRepos = @(
  "https://github.com/microsoft/FinanceBenchmark.git",
  "https://github.com/microsoft/finance-advanced-analytics.git",
  "https://github.com/microsoft/CopilotStudioSamples.git",
  "https://github.com/pnp/copilot-pro-dev-samples.git",
  "https://github.com/IBM/AML-Data.git",
  "https://github.com/IBM/AMLSim.git",
  "https://github.com/ibm-client-engineering/output-drift-financial-llms.git",
  "https://github.com/Arelle/Arelle.git",
  "https://github.com/jadchaar/sec-edgar-downloader.git",
  "https://github.com/westland/auditanalytics.git",
  "https://github.com/ProsusAI/finBERT.git",
  "https://github.com/AI4Finance-Foundation/FinGPT.git"
)

$optionalRepos = @(
  "https://github.com/microsoft/dstoolkit-corporate-financial-forecasting.git",
  "https://github.com/microsoft/qlib.git",
  "https://github.com/IBM/TabFormer.git",
  "https://github.com/IBM/ai-on-z-fraud-detection.git",
  "https://github.com/IBM/watsonx-ai-samples.git",
  "https://github.com/IBM/watsonx-developer-hub.git",
  "https://github.com/IBM/ai-agent-for-loan-risk.git",
  "https://github.com/GitiHubi/deepPaper.git"
)

New-Item -ItemType Directory -Path $Root -Force | Out-Null

function Clone-One([string]$Url) {
  $name = [System.IO.Path]::GetFileNameWithoutExtension($Url)
  $dest = Join-Path $Root $name
  if (Test-Path (Join-Path $dest ".git")) {
    Write-Host "SKIP $name (already cloned)"
  } else {
    Write-Host "CLONE $name"
    git clone --depth 1 $Url $dest
  }
}

$coreRepos | ForEach-Object { Clone-One $_ }
if ($Mode -eq "all") {
  $optionalRepos | ForEach-Object { Clone-One $_ }
}

Write-Host ""
Write-Host "Clone complete. No third-party installer or cloud deployment was executed."
Write-Host "Review each upstream LICENSE/README before running code."
