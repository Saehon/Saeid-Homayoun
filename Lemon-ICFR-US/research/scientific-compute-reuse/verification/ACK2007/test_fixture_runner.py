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
EXPECTED_OUTPUT_SHA = "84fd60074500b523cd78e0e159796cf7edf0717df847ec631577075e1f4b3cde"
EXPECTED_INPUT_SHA = "fcec3365f05b4787a9adc151f0a21404d939fc44263ac51a87c8a2133894cace"


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


def test_pre_attestation_evaluator_is_not_exposed():
    assert not hasattr(runner, "_evaluate_regression_pin_fixture")



def test_unknown_fixture_column_is_rejected(tmp_path):
    path = tmp_path / "unknown.csv"
    _write_csv(path, [*EXPECTED, "UNKNOWN"], [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.parse_fixture_rows(path)


def test_reordered_fixture_columns_are_rejected(tmp_path):
    path = tmp_path / "reordered.csv"
    reordered = ["purpose", *EXPECTED[:-1]]
    _write_csv(path, reordered, [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.parse_fixture_rows(path)


def test_missing_fixture_predictor_is_rejected(tmp_path):
    path = tmp_path / "missing.csv"
    missing_fields = [name for name in EXPECTED if name != "SIZE"]
    _write_csv(path, missing_fields, [_base_row()])
    with pytest.raises(ValueError, match="schema/order"):
        runner.parse_fixture_rows(path)


def test_duplicate_fixture_header_is_rejected(tmp_path):
    path = tmp_path / "duplicate-header.csv"
    header = ["case_id", *runner.REQUIRED, "SIZE", "purpose"]
    values = ["CASE", *(["0"] * len(runner.REQUIRED)), "0", "test"]
    path.write_text(
        ",".join(header) + "\n" + ",".join(values) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate frozen-fixture headers"):
        runner.parse_fixture_rows(path)


def test_duplicate_case_id_is_rejected(tmp_path):
    path = tmp_path / "duplicate-case.csv"
    _write_csv(path, EXPECTED, [_base_row("DUP"), _base_row("DUP")])
    with pytest.raises(ValueError, match="duplicate frozen fixture case_id"):
        runner.parse_fixture_rows(path)


@pytest.mark.parametrize("value", ["nan", "inf", "-inf"])
def test_nonfinite_fixture_value_is_rejected(tmp_path, value):
    path = tmp_path / f"nonfinite-{value}.csv"
    row = _base_row()
    row["SIZE"] = value
    _write_csv(path, EXPECTED, [row])
    with pytest.raises(ValueError, match="finite numeric"):
        runner.parse_fixture_rows(path)


def test_empty_case_id_is_rejected(tmp_path):
    path = tmp_path / "empty-case.csv"
    _write_csv(path, EXPECTED, [_base_row(case_id="")])
    with pytest.raises(ValueError, match="case_id must be non-empty"):
        runner.parse_fixture_rows(path)


def test_empty_purpose_is_rejected(tmp_path):
    path = tmp_path / "empty-purpose.csv"
    _write_csv(path, EXPECTED, [_base_row(purpose="")])
    with pytest.raises(ValueError, match="empty purpose"):
        runner.parse_fixture_rows(path)


def test_arithmetic_rejects_noncanonical_fixture_even_when_schema_valid(tmp_path):
    path = tmp_path / "schema-valid.csv"
    _write_csv(path, EXPECTED, [_base_row()])
    with pytest.raises(ValueError, match="committed canonical frozen fixture"):
        runner.execute_fixtures(path, tmp_path / "out")


def test_provenance_manifest_binds_fixture_contract_output_and_commit(tmp_path):
    payload, output_sha = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv", tmp_path / "provenance-run"
    )
    import json
    provenance = json.loads(
        (tmp_path / "provenance-run" / "fixture-provenance.json").read_text(encoding="utf-8")
    )
    assert provenance["model_id"] == "ACK2007"
    assert provenance["scientific_status"] == "HOLD"
    assert provenance["fixture_input_sha256"] == EXPECTED_INPUT_SHA
    assert provenance["fixture_output_sha256"] == output_sha
    assert provenance["coefficient_contract_sha256"] == runner.file_sha256(
        runner.COEFFICIENT_CONTRACT
    )
    assert provenance["producing_git_commit"]
    assert provenance["producing_git_commit"] != "UNAVAILABLE"


def test_coefficient_contract_covers_every_required_predictor():
    assert list(runner.COEFFICIENTS) == list(runner.REQUIRED)
    assert len(runner.COEFFICIENTS) == 14
    for predictor in runner.REQUIRED:
        assert predictor in runner.COEFFICIENTS


@pytest.mark.parametrize("predictor", runner.REQUIRED)
def test_every_coefficient_changes_attested_arithmetic_when_observable(tmp_path, predictor):
    """Falsify each term through the canonical-attested execution path."""
    baseline_payload, _ = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv", tmp_path / "baseline"
    )
    mutated = dict(runner.COEFFICIENTS)
    mutated[predictor] = mutated[predictor] + 1.0
    mutated_payload, _ = runner.execute_fixtures(
        HERE / "frozen-fixtures.csv",
        tmp_path / f"mutated-{predictor.replace('/', '_')}",
        _test_coefficient_override=mutated,
    )
    canonical_rows = [x for _, _, x in runner.parse_fixture_rows(HERE / "frozen-fixtures.csv")]
    observable = any(float(row[predictor]) != 0.0 for row in canonical_rows)
    if observable:
        assert mutated_payload != baseline_payload
    else:
        pytest.fail(f"{predictor} is not observable in any canonical attested fixture row")
