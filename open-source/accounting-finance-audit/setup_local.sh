#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r open-source/accounting-finance-audit/data/requirements-data.txt

bash open-source/accounting-finance-audit/bootstrap.sh core

mkdir -p research-data
echo
echo "Research stack ready."
echo "List datasets with:"
echo "  .venv/bin/python open-source/accounting-finance-audit/data/download_data.py --list"
