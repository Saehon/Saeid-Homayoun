from __future__ import annotations

import hashlib
import json
from pathlib import Path

import openai_finops


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = PACKAGE_ROOT / "cases" / "CASE_001_SYNTHETIC_FINOPS"
SAMPLE = PACKAGE_ROOT / "sample_data" / "transactions.csv"


def test_package_import_and_version():
    assert openai_finops.__version__ == "0.2.0"


def test_case_001_provenance_matches_current_sample_data():
    manifest = json.loads((CASE_ROOT / "RUN_MANIFEST.json").read_text())
    report = json.loads((CASE_ROOT / "deterministic_report.json").read_text())

    digest = hashlib.sha256(SAMPLE.read_bytes()).hexdigest()

    assert digest == manifest["source"]["sample_data_sha256"]
    assert digest == report["source_sha256"]
    assert manifest["result_summary"]["row_count"] == report["row_count"] == 12
    assert manifest["result_summary"]["finding_count"] == len(report["findings"]) == 7
    assert manifest["result_summary"]["deterministic_risk_score"] == report["risk_score"] == 91
