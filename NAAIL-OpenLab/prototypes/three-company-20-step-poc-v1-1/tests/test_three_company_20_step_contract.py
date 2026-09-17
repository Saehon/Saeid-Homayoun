from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "three_company_60_step_execution_matrix.csv"

ALLOWED_STATUSES = {
    "EXECUTED_VALIDATED",
    "RESEARCH_PROTOTYPE",
    "EXECUTED",
    "DERIVED_EXECUTED",
    "SYNTHETIC_EXECUTED",
    "DESIGN_ONLY",
    "REGISTERED_NOT_EXECUTED",
    "PATENT_HOLD_NON_ENABLING",
}
EXPECTED = {"MSFT", "WMT", "JPM"}


def load_rows():
    with MATRIX.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def status_map(ticker):
    return {int(r["step_id"]): r["status"] for r in load_rows() if r["ticker"] == ticker}


def test_exactly_60_company_step_rows():
    assert len(load_rows()) == 60


def test_exactly_three_companies():
    assert {r["ticker"] for r in load_rows()} == EXPECTED


def test_each_company_has_steps_1_to_20_once():
    rows = load_rows()
    for ticker in EXPECTED:
        steps = [int(r["step_id"]) for r in rows if r["ticker"] == ticker]
        assert sorted(steps) == list(range(1, 21))


def test_status_vocabulary_is_controlled():
    assert all(r["status"] in ALLOWED_STATUSES for r in load_rows())


def test_source_access_is_verified_for_starting_cohort():
    assert all(r["source_access"] == "VERIFIED" for r in load_rows())


def test_walmart_and_jpm_core_bounded_execution_is_recorded():
    for ticker in {"WMT", "JPM"}:
        s = status_map(ticker)
        assert s[1] == "EXECUTED"
        assert s[2] == "EXECUTED"
        assert s[3] == "DERIVED_EXECUTED"
        assert s[4] == "EXECUTED"
        assert s[5] == "DERIVED_EXECUTED"
        assert s[6] == "EXECUTED"
        assert s[9] == "SYNTHETIC_EXECUTED"
        assert s[12] == "RESEARCH_PROTOTYPE"
        assert s[13] == "EXECUTED"
        assert s[14] == "RESEARCH_PROTOTYPE"
        assert s[15] == "DESIGN_ONLY"
        assert s[17] == "EXECUTED_VALIDATED"
        assert s[18] == "RESEARCH_PROTOTYPE"
        assert s[19] == "RESEARCH_PROTOTYPE"


def test_walmart_and_jpm_open_scientific_gates_stay_open():
    for ticker in {"WMT", "JPM"}:
        s = status_map(ticker)
        for step_id in {7, 8, 10, 11, 16, 20}:
            assert s[step_id] == "REGISTERED_NOT_EXECUTED"


def test_microsoft_retains_open_scientific_gates():
    s = status_map("MSFT")
    assert s[7] == "REGISTERED_NOT_EXECUTED"
    assert s[10] == "REGISTERED_NOT_EXECUTED"
    assert s[11] == "REGISTERED_NOT_EXECUTED"
    assert s[15] == "DESIGN_ONLY"
    assert s[20] == "REGISTERED_NOT_EXECUTED"


def test_bounded_validation_is_preserved_for_all_three():
    for ticker in EXPECTED:
        assert status_map(ticker)[17] == "EXECUTED_VALIDATED"
