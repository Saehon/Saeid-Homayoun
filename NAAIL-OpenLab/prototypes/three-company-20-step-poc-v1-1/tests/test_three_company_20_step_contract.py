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


def test_exactly_60_company_step_rows():
    rows = load_rows()
    assert len(rows) == 60


def test_exactly_three_companies():
    rows = load_rows()
    assert {r["ticker"] for r in rows} == EXPECTED


def test_each_company_has_steps_1_to_20_once():
    rows = load_rows()
    for ticker in EXPECTED:
        steps = [int(r["step_id"]) for r in rows if r["ticker"] == ticker]
        assert sorted(steps) == list(range(1, 21))


def test_status_vocabulary_is_controlled():
    rows = load_rows()
    assert all(r["status"] in ALLOWED_STATUSES for r in rows)


def test_source_access_is_verified_for_starting_cohort():
    rows = load_rows()
    assert all(r["source_access"] == "VERIFIED" for r in rows)


def test_walmart_and_jpm_are_not_falsely_promoted():
    rows = load_rows()
    for ticker in {"WMT", "JPM"}:
        statuses = {r["status"] for r in rows if r["ticker"] == ticker}
        assert statuses == {"REGISTERED_NOT_EXECUTED"}


def test_microsoft_retains_open_scientific_gates():
    rows = load_rows()
    msft = {int(r["step_id"]): r["status"] for r in rows if r["ticker"] == "MSFT"}
    assert msft[7] == "REGISTERED_NOT_EXECUTED"   # Fama–French
    assert msft[10] == "REGISTERED_NOT_EXECUTED"  # professional AI benchmark
    assert msft[11] == "REGISTERED_NOT_EXECUTED"  # cost per verified professional output
    assert msft[15] == "DESIGN_ONLY"              # participant experiment
    assert msft[20] == "REGISTERED_NOT_EXECUTED"  # independent replication


def test_microsoft_bounded_validation_is_preserved():
    rows = load_rows()
    msft = {int(r["step_id"]): r["status"] for r in rows if r["ticker"] == "MSFT"}
    assert msft[17] == "EXECUTED_VALIDATED"
