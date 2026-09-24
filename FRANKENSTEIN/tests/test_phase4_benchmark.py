import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "phase4_benchmark"

case = json.loads((ROOT / "case_001_bank_reconciliation.json").read_text(encoding="utf-8"))
providers = json.loads((ROOT / "providers.json").read_text(encoding="utf-8"))

assert case["gold_standard"]["adjusted_bank_balance"] == 100500
assert case["gold_standard"]["adjusted_book_balance"] == 100500
assert len(providers["providers"]) == 6

out = subprocess.check_output(
    [sys.executable, str(ROOT / "benchmark.py"), "--mode", "score-mock"],
    cwd=str(ROOT),
    text=True,
)
scored = json.loads(out)
assert scored["score"]["accuracy"] == 1.0
assert scored["score"]["passed"] is True

dry = subprocess.check_output(
    [sys.executable, str(ROOT / "benchmark.py"), "--mode", "dry-run"],
    cwd=str(ROOT),
    text=True,
)
dry_result = json.loads(dry)
assert len(dry_result["providers"]) == 6
assert "CASE BANK-REC-001" in dry_result["prompt"]

print("Phase 4 benchmark validation passed.")
