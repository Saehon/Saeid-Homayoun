import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark import run_benchmark

def test_seeded_customer_zero_benchmark():
    result = run_benchmark()
    assert result["cases"] >= 3
    assert result["pass_rate"] == 1.0
