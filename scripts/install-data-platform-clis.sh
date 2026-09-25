#!/usr/bin/env bash
set -euo pipefail

echo "NAAIL OpenLab - Kaggle + Hugging Face installer"
echo

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.11 or later is required for the Kaggle CLI." >&2
  exit 1
fi

echo "Installing/updating Kaggle CLI..."
python3 -m pip install --upgrade --user kaggle

echo
echo "Installing/updating Hugging Face CLI..."
curl -LsSf https://hf.co/cli/install.sh | bash


echo
echo "Verification:"
for cmd in kaggle hf; do
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "  [OK] $cmd -> $(command -v "$cmd")"
  else
    echo "  [WARN] $cmd is not currently visible on PATH. Restart your shell and check again."
  fi
done

echo
echo "Authentication is intentionally separate."
echo "Kaggle: configure Kaggle authentication/API token."
echo "Hugging Face: run 'hf auth login'."
echo "Never commit credentials to GitHub."
