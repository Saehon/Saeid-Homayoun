import json
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[1] / "architecture" / "audit_analytics_open_source_registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_audit_analytics_boundary_is_read_only():
    data = load_registry()
    boundary = data["boundary"]
    assert boundary["external_repo_is_authoritative_audit_truth"] is False
    assert boundary["external_repo_may_modify_knowledge_rag_core"] is False
    assert boundary["proprietary_audit_analytics_data_is_included"] is False
    assert boundary["adapter_first_required"] is True
    assert boundary["human_gate_required"] is True


def test_no_third_party_code_is_vendored():
    data = load_registry()
    assert data["projects"]
    assert all(project["third_party_code_vendored"] is False for project in data["projects"])


def test_unlicensed_reference_is_not_adopted_for_copy():
    data = load_registry()
    westland = next(p for p in data["projects"] if p["name"] == "Westland Audit Analytics")
    assert westland["license"] == "UNVERIFIED_NO_REPOSITORY_LICENSE_FILE"
    assert westland["state"] == "REFERENCE_ONLY_NO_CODE_COPY"


def test_agpl_project_is_isolated():
    data = load_registry()
    xbrlkit = next(p for p in data["projects"] if p["name"] == "xbrlkit")
    assert xbrlkit["license"] == "AGPL-3.0"
    assert xbrlkit["state"] == "REFERENCE_ISOLATED_AGPL"


def test_core_audit_domains_present():
    data = load_registry()
    required = {
        "journal_entry_testing",
        "segregation_of_duties",
        "icfr_deficiency_classification",
        "xbrl_validation",
        "cam_kam_alignment",
        "evidence_coverage_and_traceability",
    }
    assert required.issubset(set(data["audit_analytics_domains"]))
