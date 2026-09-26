import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark import run_benchmark


def test_seeded_customer_zero_v2_benchmark():
    result = run_benchmark()
    assert result["benchmark"] == "Customer Zero V2"
    assert result["cases"] >= 20
    assert result["pass_rate"] == 1.0
    assert result["false_positives"] == 0
    assert result["false_negatives"] == 0
    assert result["evidence_lineage_completeness"] == 1.0
