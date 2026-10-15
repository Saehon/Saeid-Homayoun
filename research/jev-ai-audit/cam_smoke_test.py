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
