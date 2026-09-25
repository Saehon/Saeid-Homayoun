#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-core}"
ROOT="${2:-external-open-source}"

CORE_REPOS=(
  "https://github.com/microsoft/FinanceBenchmark.git"
  "https://github.com/microsoft/finance-advanced-analytics.git"
  "https://github.com/microsoft/CopilotStudioSamples.git"
  "https://github.com/pnp/copilot-pro-dev-samples.git"
  "https://github.com/IBM/AML-Data.git"
  "https://github.com/IBM/AMLSim.git"
  "https://github.com/ibm-client-engineering/output-drift-financial-llms.git"
  "https://github.com/Arelle/Arelle.git"
  "https://github.com/jadchaar/sec-edgar-downloader.git"
  "https://github.com/westland/auditanalytics.git"
  "https://github.com/ProsusAI/finBERT.git"
  "https://github.com/AI4Finance-Foundation/FinGPT.git"
  "https://github.com/adoptai/cpa-skills.git"
  "https://github.com/GAJETOso/financeskills.git"
  "https://github.com/esploro-group/closegate.git"
  "https://github.com/docling-project/docling-mcp.git"
  "https://github.com/stefanoamorelli/sec-edgar-mcp.git"
  "https://github.com/microsoft/agent-framework.git"
)

OPTIONAL_REPOS=(
  "https://github.com/microsoft/dstoolkit-corporate-financial-forecasting.git"
  "https://github.com/microsoft/qlib.git"
  "https://github.com/IBM/TabFormer.git"
  "https://github.com/IBM/ai-on-z-fraud-detection.git"
  "https://github.com/IBM/watsonx-ai-samples.git"
  "https://github.com/IBM/watsonx-developer-hub.git"
  "https://github.com/IBM/ai-agent-for-loan-risk.git"
  "https://github.com/GitiHubi/deepPaper.git"
  "https://github.com/google/adk-python.git"
)

mkdir -p "$ROOT"

clone_one () {
  local url="$1"
  local name
  name="$(basename "$url" .git)"
  if [ -d "$ROOT/$name/.git" ]; then
    echo "SKIP $name (already cloned)"
  else
    echo "CLONE $name"
    git clone --depth 1 "$url" "$ROOT/$name"
  fi
}

for url in "${CORE_REPOS[@]}"; do clone_one "$url"; done

if [ "$MODE" = "all" ]; then
  for url in "${OPTIONAL_REPOS[@]}"; do clone_one "$url"; done
elif [ "$MODE" != "core" ]; then
  echo "Usage: $0 [core|all] [destination]"
  exit 2
fi

echo
echo "Clone complete. No third-party installer or cloud deployment was executed."
echo "Review each upstream LICENSE/README before running code."
