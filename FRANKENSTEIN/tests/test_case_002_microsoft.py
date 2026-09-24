import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"phase4_benchmark"
case=json.loads((ROOT/"case_002_microsoft_sec_2026.json").read_text(encoding="utf-8"))
assert case["filing"]["accession_number"]=="0001193125-26-323660"
assert case["gold_standard"]["revenue_growth_pct"]==17.79
assert case["gold_standard"]["gross_margin_pct"]==67.94
assert case["gold_standard"]["operating_margin_pct"]==46.78
assert case["gold_standard"]["net_margin_pct"]==40.31

out=subprocess.check_output([sys.executable,str(ROOT/"validate_case_002_microsoft.py")],text=True)
result=json.loads(out)
assert result["score"]["passed"] is True
assert result["score"]["accuracy"]==1.0
print("Microsoft SEC Case 002 deterministic validation passed.")
