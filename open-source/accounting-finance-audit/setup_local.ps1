param()
$ErrorActionPreference = "Stop"

python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r open-source\accounting-finance-audit\data\requirements-data.txt

powershell -ExecutionPolicy Bypass -File open-source\accounting-finance-audit\bootstrap.ps1 -Mode core

New-Item -ItemType Directory -Path research-data -Force | Out-Null
Write-Host ""
Write-Host "Research stack ready."
Write-Host "List datasets with:"
Write-Host "  .\.venv\Scripts\python.exe open-source\accounting-finance-audit\data\download_data.py --list"
