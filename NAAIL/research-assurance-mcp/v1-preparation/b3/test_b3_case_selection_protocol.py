from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROTOCOL = ROOT / "case_selection_protocol_v1.json"
TEMPLATE = ROOT / "case_selection_record_template_v1.json"
MANIFEST = ROOT / "case_selection_protocol_freeze_manifest_v1.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_b3_protocol_invariants() -> None:
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert protocol["status"] == "FROZEN_BEFORE_SEARCH"
    assert protocol["approval_state"] == "DRAFT_PENDING_CLAUDE_AND_HUMAN"
    exposure = protocol["prior_exposure"]
    assert exposure["candidate_search_conducted_under_this_protocol"] is False
    assert exposure["candidate_data_or_results_seen_under_this_protocol"] is False

    expected = {
        "doi_uniqueness",
        "peer_reviewed_field_fit",
        "public_replication_package",
        "table_to_code_map",
        "executable_stata_or_python_path",
        "public_data_independent_reproduction_path",
        "prior_exposure_declaration",
    }
    actual = {item["criterion"] for item in protocol["candidate_eligibility"] if item["required"]}
    assert actual == expected
    assert protocol["decision_authority"]["automatic_selection_prohibited"] is True
    assert protocol["poc_complete"] is False
    assert protocol["v1_complete"] is False

    assert template["record_status"] == "BLANK_TEMPLATE_NOT_A_CANDIDATE"
    assert template["candidate_id"] is None
    assert template["normalized_doi"] is None
    assert template["execution_path"]["allowed_values"] == ["Stata", "Python"]
    assert template["human_selection"]["decision"] is None
    assert template["assurance_boundaries"]["no_automatic_case_selection"] is True

    frozen = {item["path"]: item["sha256"] for item in manifest["frozen_files"]}
    assert frozen[PROTOCOL.name] == sha256(PROTOCOL)
    assert frozen[TEMPLATE.name] == sha256(TEMPLATE)
    assert manifest["search_or_candidate_data_existed_at_freeze"] is False


if __name__ == "__main__":
    test_b3_protocol_invariants()
    print("B3 case-selection protocol invariants: PASS")
