from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORD = ROOT / "duplicate_case_002_correction_v1.json"


def test_correction_invariants() -> None:
    data = json.loads(RECORD.read_text(encoding="utf-8"))
    assert data["status"] == "DRAFT_ADDITIVE_CORRECTION"
    assert data["canonical_case_001"]["normalized_doi"] == "10.1287/mnsc.2023.4670"
    assert [item["run_id"] for item in data["affected_records"]] == ["RUN-021", "RUN-022"]
    assert data["v1_valid_additional_cases_from_runs_021_022"] == 0
    assert data["case_002_slot"] == "UNASSIGNED_PENDING_HUMAN_SELECTION"
    assert data["historical_records_modified"] is False
    assert data["scientific_claim_created"] is False
    assert data["poc_complete"] is False
    assert data["v1_complete"] is False
    for evidence in data["affected_records"] + data["prior_additive_evidence"]:
        assert len(evidence["git_blob"]) == 40
        int(evidence["git_blob"], 16)


if __name__ == "__main__":
    test_correction_invariants()
    print("B2 duplicate-case correction invariants: PASS")
