import csv
import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "ack2007_run_fixtures", HERE / "run_fixtures.py"
)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)

EXPECTED = ["case_id", *runner.REQUIRED, "purpose"]
EXPECTED_OUTPUT_SHA = "c420891c605066edc1fe0e895ab5412decd65b648d25a42a1ceaeeb96113dda6"
EXPECTED_INPUT_SHA = "e41b2536f8e485bfd4d72cc7f91b49f0640afdcd5e4b96231e6914868b884205"


def _base_row(case_id="CASE", purpose="test"):
    row = {name: "0" for name in runner.REQUIRED}
    row["case_id"] = case_id
    row["purpose"] = purpose
    return row


def _write_csv(path, fieldnames, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def test_committed_fixture_input_bytes_are_pinned():
    path = HERE / "frozen-fixtures.csv"
    assert runner.file_sha256(path) == EXPECTED_INPUT_SHA
    runner.verify_fixture_input_checksum(path, EXPECTED_INPUT_SHA)


def test_committed_fixture_is_deterministic_across_two_clean_runs(tmp_path):
    payload1, sha1 = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv", tmp_path / "clean-run-1"
    )
    payload2, sha2 = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv", tmp_path / "clean-run-2"
    )
    assert payload1 == payload2
    assert sha1 == sha2 == EXPECTED_OUTPUT_SHA
    assert (tmp_path / "clean-run-1" / "fixture-input.sha256").read_text().startswith(EXPECTED_INPUT_SHA)
    assert (tmp_path / "clean-run-2" / "fixture-input.sha256").read_text().startswith(EXPECTED_INPUT_SHA)


def test_fixture_input_mutation_is_detected_even_if_outputs_would_round_same(tmp_path):
    original = (HERE / "frozen-fixtures.csv").read_bytes()
    mutated = tmp_path / "mutated.csv"
    mutated.write_bytes(
        original.replace(b"intercept_arithmetic_only", b"changed_purpose_only")
    )
    assert runner.file_sha256(mutated) != EXPECTED_INPUT_SHA
    with pytest.raises(ValueError, match="input checksum mismatch"):
        runner.verify_fixture_input_checksum(mutated, EXPECTED_INPUT_SHA)


def test_output_checksum_mutation_is_detected(tmp_path):
    payload, sha = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv", tmp_path / "clean"
    )
    runner.verify_payload_checksum(payload, sha)
    with pytest.raises(ValueError, match="checksum mismatch"):
        runner.verify_payload_checksum(payload + "mutation", sha)


def test_fixture_evaluator_exception_is_not_silently_swallowed(tmp_path, monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("fixture evaluator failure")

    monkeypatch.setattr(runner, "_evaluate_regression_pin_fixture", boom)
    with pytest.raises(RuntimeError, match="fixture evaluator failure"):
        runner.execute_fixtures(
            HERE / "frozen-fixtures.csv", tmp_path / "out"
        )


def test_unknown_fixture_column_is_rejected(tmp_path):
    path = tmp_path / "unknown.csv"
    _write_csv(path, [*EXPECTED, "UNKNOWN"], [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_reordered_fixture_columns_are_rejected(tmp_path):
    path = tmp_path / "reordered.csv"
    reordered = ["purpose", *EXPECTED[:-1]]
    _write_csv(path, reordered, [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_missing_fixture_predictor_is_rejected(tmp_path):
    path = tmp_path / "missing.csv"
    missing_fields = [name for name in EXPECTED if name != "SIZE"]
    _write_csv(path, missing_fields, [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_duplicate_fixture_header_is_rejected(tmp_path):
    path = tmp_path / "duplicate-header.csv"
    header = ["case_id", *runner.REQUIRED, "SIZE", "purpose"]
    values = ["CASE", *(["0"] * len(runner.REQUIRED)), "0", "test"]
    path.write_text(
        ",".join(header) + "\n" + ",".join(values) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate frozen-fixture headers"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_duplicate_case_id_is_rejected(tmp_path):
    path = tmp_path / "duplicate-case.csv"
    _write_csv(path, EXPECTED, [_base_row("DUP"), _base_row("DUP")])
    with pytest.raises(ValueError, match="duplicate frozen fixture case_id"):
        runner.execute_fixtures(path, tmp_path / "out")


@pytest.mark.parametrize("value", ["nan", "inf", "-inf"])
def test_nonfinite_fixture_value_is_rejected(tmp_path, value):
    path = tmp_path / f"nonfinite-{value}.csv"
    row = _base_row()
    row["SIZE"] = value
    _write_csv(path, EXPECTED, [row])
    with pytest.raises(ValueError, match="finite numeric"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_empty_case_id_is_rejected(tmp_path):
    path = tmp_path / "empty-case.csv"
    _write_csv(path, EXPECTED, [_base_row(case_id="")])
    with pytest.raises(ValueError, match="case_id must be non-empty"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_empty_purpose_is_rejected(tmp_path):
    path = tmp_path / "empty-purpose.csv"
    _write_csv(path, EXPECTED, [_base_row(purpose="")])
    with pytest.raises(ValueError, match="empty purpose"):
        runner.execute_fixtures(path, tmp_path / "out")
