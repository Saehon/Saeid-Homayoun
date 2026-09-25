$ErrorActionPreference = "Stop"

Write-Host "Creating Python virtual environment..."
python -m venv .venv

Write-Host "Activating environment..."
& .\.venv\Scripts\Activate.ps1

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing free/open-source research stack..."
python -m pip install -r requirements.txt

Write-Host ""
Write-Host "Setup complete."
Write-Host "Lightweight datasets: python download_assets.py --datasets"
Write-Host "Kaggle datasets:      python download_assets.py --kaggle"
Write-Host "DeepSeek 7B:          python download_assets.py --deepseek-7b"
Write-Host "Kimi VL:              python download_assets.py --kimi-vl"
