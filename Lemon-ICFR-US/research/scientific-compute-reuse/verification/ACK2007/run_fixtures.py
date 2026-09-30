import csv
import hashlib
import json
from math import isfinite
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL_DIR = HERE.parent.parent / "executable-models" / "ACK2007"
CANONICAL_FIXTURE = HERE / "frozen-fixtures.csv"\nCOEFFICIENT_CONTRACT = MODEL_DIR / "coefficient-contract.json"
CANONICAL_FIXTURE_SHA256 = "e41b2536f8e485bfd4d72cc7f91b49f0640afdcd5e4b96231e6914868b884205"
sys.path.insert(0, str(MODEL_DIR))
from ack2007 import COEFFICIENTS, INTERCEPT, REQUIRED, logistic, validate_compiler_input


def payload_sha256(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def file_sha256(path: Path | str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_payload_checksum(payload: str, expected_sha: str) -> None:
    actual = payload_sha256(payload)
    if actual != expected_sha:
        raise ValueError(f"ACK2007 fixture checksum mismatch: expected={expected_sha}, actual={actual}")


def verify_fixture_input_checksum(path: Path | str, expected_sha: str) -> None:
    actual = file_sha256(path)
    if actual != expected_sha:
        raise ValueError(
            "ACK2007 frozen-fixture input checksum mismatch: "
            f"expected={expected_sha}, actual={actual}"
        )


def _evaluate_regression_pin_fixture(x):
    """Fixture-only arithmetic for the unverified regression pin."""
    validate_compiler_input(x)
    z = INTERCEPT + sum(COEFFICIENTS[k] * float(x[k]) for k in REQUIRED)
    if not isfinite(z):
        raise ValueError("ACK2007 fixture linear predictor must be finite")
    return z, logistic(z)


def parse_fixture_rows(csv_path: Path | str):
    """Parse/validate fixture syntax only; performs no model arithmetic."""
    csv_path = Path(csv_path)
    parsed = []
    seen_case_ids = set()
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected = ["case_id", *REQUIRED, "purpose"]
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise ValueError("frozen fixture is missing a header row")
        if len(fieldnames) != len(set(fieldnames)):
            raise ValueError(f"duplicate frozen-fixture headers: {fieldnames}")
        if fieldnames != expected:
            missing = sorted(set(expected) - set(fieldnames))
            unknown = sorted(set(fieldnames) - set(expected))
            raise ValueError(
                "invalid frozen-fixture schema/order; "
                f"expected={expected}, actual={fieldnames}, missing={missing}, unknown={unknown}"
            )
        for row in reader:
            if None in row:
                raise ValueError(f"row has extra unnamed fields: {row[None]}")
            case_id = row.pop("case_id")
            purpose = row.pop("purpose")
            if case_id is None or not case_id.strip():
                raise ValueError("frozen fixture case_id must be non-empty")
            if case_id in seen_case_ids:
                raise ValueError(f"duplicate frozen fixture case_id: {case_id!r}")
            seen_case_ids.add(case_id)
            if purpose is None or not purpose.strip():
                raise ValueError(f"row {case_id!r} has empty purpose")
            if any(row[k] is None or row[k] == "" for k in REQUIRED):
                raise ValueError(f"row {case_id!r} has missing predictor values")
            x = {k: float(row[k]) for k in REQUIRED}
            validate_compiler_input(x)
            parsed.append((case_id, purpose, x))
    return parsed


def _require_canonical_fixture(csv_path: Path | str) -> Path:
    """Attest that arithmetic is only run on the committed byte-pinned fixture."""
    path = Path(csv_path)
    if path.resolve() != CANONICAL_FIXTURE.resolve():
        raise ValueError("ACK2007 arithmetic is restricted to the committed canonical frozen fixture")
    verify_fixture_input_checksum(path, CANONICAL_FIXTURE_SHA256)
    return path


def execute_fixtures(csv_path: Path | str = CANONICAL_FIXTURE, out_dir: Path | str = MODEL_DIR):
    csv_path = _require_canonical_fixture(csv_path)
    out_dir = Path(out_dir)
    input_sha = file_sha256(csv_path)
    rows = []
    for case_id, _purpose, x in parse_fixture_rows(csv_path):
        z, p = _evaluate_regression_pin_fixture(x)
        rows.append({"case_id": case_id, "z": f"{z:.12f}", "p": f"{p:.12f}"})

    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "fixture-results.json").write_text(payload, encoding="utf-8")
    output_sha = payload_sha256(payload)
    (out_dir / "fixture-results.sha256").write_text(output_sha + "  fixture-results.json\n", encoding="utf-8")
    (out_dir / "fixture-input.sha256").write_text(input_sha + "  frozen-fixtures.csv\n", encoding="utf-8")
    return payload, output_sha


def main():
    payload, output_sha = execute_fixtures()
    print(payload, end="")
    print("INPUT_SHA256", file_sha256(CANONICAL_FIXTURE))
    print("OUTPUT_SHA256", output_sha)


if __name__ == "__main__":
    main()
