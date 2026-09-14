from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from econova_poc import generate_demo, run


def test_demo_is_deterministic():
    a, b = generate_demo(), generate_demo()
    assert a.equals(b)
    assert len(a) == 120
    assert a.firm_id.nunique() == 20


def test_poc_blocks_discovery(tmp_path):
    passport = run(None, tmp_path / "results")
    assert passport["discovery_claim_allowed"] is False
    assert passport["human_approval"] is False
    assert (tmp_path / "results" / "table4_main_regressions.csv").exists()
    assert (tmp_path / "results" / "evidence_passport.json").exists()
