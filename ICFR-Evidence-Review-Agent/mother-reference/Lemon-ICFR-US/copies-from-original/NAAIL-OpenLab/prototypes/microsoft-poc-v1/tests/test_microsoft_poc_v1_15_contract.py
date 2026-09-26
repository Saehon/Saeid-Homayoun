import csv, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def read_csv(name):
    with (ROOT / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def test_01_sec_xbrl_ingestion():
    twin = read_json("microsoft_digital_twin.json")
    assert twin["company"]["cik"] == "0000789019"
    assert set(twin["accounting"]["xbrl_reports"]) == {"R2", "R4", "R6", "R107"}
    p = twin["evidence_passports"][0]
    assert p["execution_status"] == "EXECUTED"
    assert "SEC" in p["provenance"]["provider"]
    assert p["source_url"].startswith("https://www.sec.gov/")

def test_02_financial_statement_extraction():
    twin = read_json("microsoft_digital_twin.json")
    facts = twin["accounting"]["facts"]
    required = {
        "revenue": 331839,
        "operating_income": 155237,
        "net_income": 133749,
        "total_assets": 758376,
        "total_liabilities": 315989,
        "equity": 442387,
        "operating_cf": 182935,
        "capex": 115948,
    }
    for k, v in required.items():
        assert facts[k] == v
    rows = {r["variable"]: r for r in read_csv("microsoft_financial_features.csv")}
    assert float(rows["revenue_usd_m"]["value"]) == facts["revenue"]
    assert float(rows["total_assets_usd_m"]["value"]) == facts["total_assets"]
    assert float(rows["operating_cash_flow_usd_m"]["value"]) == facts["operating_cf"]

def test_03_variable_dictionary_validation():
    rows = read_csv("microsoft_variable_dictionary.csv")
    assert rows
    expected_columns = {"variable","definition","unit","module","source_id","evidence_class"}
    assert set(rows[0].keys()) == expected_columns
    variables = [r["variable"] for r in rows]
    assert len(variables) == len(set(variables))
    assert all(all((r[c] or "").strip() for c in expected_columns) for r in rows)

    required_variables = {
        "revenue","operating_income","net_income","total_assets","current_ratio",
        "fcf_proxy","msft_fy2026_price_return","dgs10","rd_intensity",
        "github_repo_snapshot","cam_revenue_recognition","cam_uncertain_tax_positions",
        "uncertainty_per_100_words","innovation_per_100_words",
        "tdabc_activity_cost","livebench_cost_success"
    }
    assert required_variables.issubset(set(variables))

    registry = read_json("microsoft_data_source_registry.json")
    registered_ids = {s["id"] for s in registry["sources"]}
    allowed_local_synthetic = {"SYNTHETIC_AI_PROCESS"}
    for r in rows:
        assert r["source_id"] in registered_ids | allowed_local_synthetic

def test_04_evidence_passport_generation():
    twin = read_json("microsoft_digital_twin.json")
    schema = read_json("microsoft_evidence_passport_schema.json")
    p = twin["evidence_passports"][0]
    for field in schema["required"]:
        assert field in p
        assert p[field] not in ("", None)
    assert p["rights_gate"] in schema["properties"]["rights_gate"]["enum"]
    assert p["human_review_status"] in schema["properties"]["human_review_status"]["enum"]
    assert p["transformation"]["derived"] is True

def test_05_cam_audit_risk_mapping():
    twin = read_json("microsoft_digital_twin.json")
    audit = twin["audit"]
    assert audit["auditor"] == "Deloitte & Touche LLP"
    assert audit["icfr_opinion"] == "UNQUALIFIED"
    assert {c["topic"] for c in audit["cams"]} == {
        "Revenue Recognition", "Income Taxes — Uncertain Tax Positions"
    }
    for cam in audit["cams"]:
        assert cam["account"]
        assert cam["assertions"]
        assert cam["risk"]
        assert cam["procedures"]
        assert cam["evidence"]
        assert cam["judgment"]

def test_06_text_analytics():
    rows = read_csv("microsoft_text_features.csv")
    assert len(rows) == 2
    for r in rows:
        assert r["execution_status"] == "EXECUTED_ON_BOUNDED_SOURCE_SAMPLE"
        assert int(r["word_count"]) > 0
        assert int(r["sentence_count"]) > 0
        assert len(r["sample_sha256"]) == 64
        int(r["sample_sha256"], 16)
        assert r["source_url"].startswith("https://www.sec.gov/")

def test_07_finance_calculation():
    twin = read_json("microsoft_digital_twin.json")
    facts = twin["accounting"]["facts"]
    finance = twin["finance"]
    assert math.isclose(facts["fcf"], facts["operating_cf"] - facts["capex"], rel_tol=0, abs_tol=1e-9)
    assert math.isclose(
        finance["market_data"]["simple_price_return"],
        finance["market_data"]["last_close"] / finance["market_data"]["first_close"] - 1,
        rel_tol=1e-12
    )
    rows = {r["variable"]: r for r in read_csv("microsoft_financial_features.csv")}
    assert math.isclose(float(rows["current_ratio"]["value"]), facts["current_assets"]/facts["current_liabilities"], rel_tol=1e-12)
    assert float(rows["fred_dgs10_2026_06_30"]["value"]) == 4.44

def test_08_innovation_measure():
    rows = {r["measure"]: r for r in read_csv("microsoft_innovation_features.csv")}
    assert math.isclose(float(rows["rd_intensity"]["value"]), 35562/331839, rel_tol=1e-12)
    assert rows["rd_intensity"]["status"] == "EXECUTED"
    assert int(rows["microsoft_github_public_repositories_snapshot"]["value"]) > 0
    assert rows["microsoft_github_public_repositories_snapshot"]["status"] == "EXECUTED_SNAPSHOT"
    assert rows["patent_activity"]["status"] == "NOT_EXECUTED"

def test_09_abc_calculation():
    twin = read_json("microsoft_digital_twin.json")
    ma = twin["management_accounting"]
    assert ma["status"] == "SYNTHETIC_EXECUTED"
    activities = ma["activities"]
    assert {a["activity"] for a in activities} >= {
        "document_retrieval","financial_analysis","audit_agent_analysis",
        "report_generation","human_review"
    }
    assert math.isclose(sum(a["tool_cost_usd"] for a in activities), ma["tool_cost_usd"], abs_tol=1e-12)

def test_10_tdabc_calculation():
    twin = read_json("microsoft_digital_twin.json")
    ma = twin["management_accounting"]
    rate = ma["capacity_cost_rate_usd_per_min"]
    for a in ma["activities"]:
        expected = rate * a["human_minutes"]
        assert math.isclose(a["tdabc_human_cost_usd"], expected, abs_tol=0.0001)
    assert math.isclose(
        sum(a["tdabc_human_cost_usd"] for a in ma["activities"]),
        ma["total_human_tdabc_cost_usd"],
        abs_tol=0.0001
    )

def test_11_ai_token_cost_calculation():
    twin = read_json("microsoft_digital_twin.json")
    ma = twin["management_accounting"]
    total_tokens = sum(a["input_tokens"] + a["output_tokens"] for a in ma["activities"])
    assert total_tokens == ma["total_tokens"]
    assert total_tokens == 23550
    assert math.isclose(sum(a["tool_cost_usd"] for a in ma["activities"]), 0.05, abs_tol=1e-12)

def test_12_model_benchmark():
    rows = read_csv("ai_cost_benchmark.csv")
    assert len(rows) >= 3
    for r in rows:
        assert r["benchmark_release"] == "LiveBench-2026-06-25"
        assert float(r["overall_score"]) > 0
        assert float(r["cost_per_successful_task_usd"]) > 0
        assert r["cost_metric_status"] == "EXTERNAL_COST_PER_SUCCESSFUL_TASK"
        assert r["task_fit"] == "general objective benchmark"

def test_13_human_ai_experiment_structure():
    twin = read_json("microsoft_digital_twin.json")
    design = (ROOT / "human_ai_experiment_design.md").read_text(encoding="utf-8")
    assert twin["human_ai_experiment"]["status"] == "DESIGN_COMPLETE_NOT_EXECUTED"
    for condition in ["T0 Human only", "T1 Human + AI recommendation",
                      "T2 Human + AI recommendation + explanation",
                      "T3 Human + AI recommendation + contradictory evidence"]:
        assert condition in design
    assert "No participant data have been collected." in design

def test_14_dashboard_data_load():
    twin = read_json("microsoft_digital_twin.json")
    facts = twin["accounting"]["facts"]
    html = (ROOT / "dashboard.html").read_text(encoding="utf-8")
    expected_strings = [
        f"${facts['revenue']:,}m",
        f"{facts['operating_income']/facts['revenue']*100:.1f}%",
        f"{facts['net_income']/facts['revenue']*100:.1f}%",
        f"{facts['rd']/facts['revenue']*100:.1f}%",
        f"${facts['fcf']:,}m",
        f"{twin['finance']['market_data']['simple_price_return']*100:.1f}%",
        "RESEARCH_PROTOTYPE",
        "2 permanent cores"
    ]
    for value in expected_strings:
        assert value in html

def test_15_human_gate_decision():
    twin = read_json("microsoft_digital_twin.json")
    gate = twin["human_gate"]
    assert gate["decision"] == "APPROVE_RESEARCH_PROTOTYPE_FOR_PUBLICATION_WITH_LIMITATIONS"
    assert gate["production_approval"] == "NO"
    assert gate["scientific_validation"] == "PENDING_INDEPENDENT_REPLICATION"
    assert twin["maturity"] == "RESEARCH_PROTOTYPE"
