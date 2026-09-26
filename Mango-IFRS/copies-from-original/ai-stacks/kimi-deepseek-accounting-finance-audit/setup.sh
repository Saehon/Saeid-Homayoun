#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo
echo "Setup complete."
echo "Lightweight datasets: python download_assets.py --datasets"
echo "Kaggle datasets:      python download_assets.py --kaggle"
echo "DeepSeek 7B:          python download_assets.py --deepseek-7b"
echo "Kimi VL:              python download_assets.py --kimi-vl"
