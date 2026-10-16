"""Minimal CAM topic risk pilot with synthetic observations only.

No third-party Jev model is installed or invoked. This validates the verified
Google Drive CAM schema and the existing benchmark.py interface.
"""
import csv
import tempfile
from pathlib import Path
from benchmark import evaluate

# Mirrors columns verified in the canonical CAM Google Sheet:
# CAM_YEAR, TOPIC_NAME, CAM_PRESENT, VALIDATION_STATUS (CAM_TOPIC_YEAR);
# TOPIC_CODE, CHOICE_SET_INCLUDED, EXPOSURE_ELIGIBILITY_STATUS,
# CAM_PRESENT, R_SCREENING_AVAILABLE, RELATIVE_RISK_STATUS (CANDIDATE_TOPIC_GRID_5CO).
# All observations below are SYNTHETIC, not copied from Google Drive.
synthetic = [
    dict(variant="synthetic_baseline", industry="Manufacturing", domain="revenue",
         icfr_status="unknown", label="1", p_event="0.70"),
    dict(variant="synthetic_baseline", industry="Manufacturing", domain="inventory",
         icfr_status="effective", label="0", p_event="0.20"),
    dict(variant="synthetic_baseline", industry="Services", domain="goodwill",
         icfr_status="unknown", label="", p_event="0.40"),
]
if __name__ == "__main__":
    result = evaluate(synthetic)
    assert len(result) == 2
    assert all(item["n"] == 1 for item in result)
    print("Synthetic smoke test passed; 2 known outcomes, 1 excluded unknown outcome.")
    print(result)
    print("No Jev/OpenJev model run; no real CAM/ICFR findings.")


def test_common_risk_engine_synthetic():
    """FT50 risk engine is feature-only; never returns fictional fitted probabilities."""
    from common_risk_engine import build_features, classification_scope
    base = dict(firm_id="SYNTHETIC-CIK", fiscal_year="2024", industry="Manufacturing",
                domain="revenue", accounting_standard="US_GAAP", icfr_status="unknown",
                cutoff_date="2025-03-01", evidence_available_date="2025-02-15",
                assets=100, assets_prior=90, net_income=8, operating_cash_flow=5,
                receivables=20, receivables_prior=16, revenue=120, revenue_prior=100,
                inventory=12, inventory_prior=10, goodwill=10, liabilities=45,
                segment_count=3, cam_present=True, pcaob_deficiency=True)
    features = build_features(base)
    assert "cam_present" not in features and "pcaob_deficiency" not in features
    assert "icfr_status" not in features
    assert len(features) == 8 and features["accrual_intensity"] > 0
    scope = classification_scope(base)
    assert scope["revenue_standard"] == "ASC 606"
    assert scope["risk_probability"] is None and scope["risk_model_status"] == "UNTRAINED"
    try:
        build_features(dict(base, evidence_available_date="2025-04-01"))
        raise AssertionError("Future-data leakage was accepted")
    except ValueError as exc:
        assert "Leakage" in str(exc)
    assert build_features(dict(base, revenue_prior=0))["revenue_growth"] is None
    print("FT50 common risk engine: synthetic feature and leakage tests passed.")

if __name__ == "__main__":
    test_common_risk_engine_synthetic()
