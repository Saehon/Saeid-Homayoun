import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "erp_open_source_registry.json"
DOC = ROOT / "ERP_DIGITAL_TWIN_LAB.md"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_registry_and_doc_exist():
    assert REGISTRY.exists()
    assert DOC.exists()


def test_core_boundary_is_protected():
    data = load_registry()
    boundary = data["boundary"]
    assert boundary["erp_belongs_to_technology_or_simulation_layer"] is True
    assert boundary["erp_may_modify_knowledge_rag_core"] is False
    assert boundary["erp_output_is_authoritative_without_validation"] is False
    assert boundary["adapter_first_required"] is True
    assert boundary["human_gate_required"] is True


def test_priority_projects_present():
    data = load_registry()
    names = {p["name"] for p in data["priority_projects"]}
    assert {"ERPNext", "Odoo Community", "Apache OFBiz", "LedgerSMB", "iDempiere"}.issubset(names)


def test_no_third_party_code_is_claimed_as_naail_owned():
    data = load_registry()
    assert data["invariants"]["third_party_code_is_naail_owned"] is False
    for project in data["priority_projects"]:
        assert project["third_party_code_vendored"] is False


def test_required_process_domains():
    data = load_registry()
    domains = set(data["process_domains"])
    required = {"order_to_cash", "purchase_to_pay", "record_to_report", "inventory", "journal_entries", "internal_controls"}
    assert required.issubset(domains)


def test_human_gate_and_provenance_required():
    data = load_registry()
    gates = set(data["promotion_gates"])
    assert "erp_event_and_ledger_provenance" in gates
    assert "knowledge_rag_core_boundary_test" in gates
    assert "human_architecture_gate" in gates
    assert data["invariants"]["erp_output_is_audit_evidence_without_provenance"] is False
    assert data["invariants"]["human_gate_required"] is True
