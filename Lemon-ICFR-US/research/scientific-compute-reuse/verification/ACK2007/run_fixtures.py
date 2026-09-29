import csv
import hashlib
import json
from math import isfinite
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL_DIR = HERE.parent.parent / "executable-models" / "ACK2007"
sys.path.insert(0, str(MODEL_DIR))
from ack2007 import (
    COEFFICIENTS,
    INTERCEPT,
    REQUIRED,
    logistic,
    validate_compiler_input,
)


def payload_sha256(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def file_sha256(path: Path | str) -> str:
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_payload_checksum(payload: str, expected_sha: str) -> None:
    actual = payload_sha256(payload)
    if actual != expected_sha:
        raise ValueError(
            f"ACK2007 fixture checksum mismatch: expected={expected_sha}, actual={actual}"
        )


def verify_fixture_input_checksum(path: Path | str, expected_sha: str) -> None:
    actual = file_sha256(path)
    if actual != expected_sha:
        raise ValueError(
            "ACK2007 frozen-fixture input checksum mismatch: "
            f"expected={expected_sha}, actual={actual}"
        )


def _evaluate_regression_pin_fixture(x):
    """Fixture-only arithmetic for the unverified regression pin.

    This function is intentionally local to the verification runner. It is not
    a public model prediction API and carries no raw-construction admission.
    """
    validate_compiler_input(x)
    z = INTERCEPT + sum(COEFFICIENTS[k] * float(x[k]) for k in REQUIRED)
    if not isfinite(z):
        raise ValueError("ACK2007 fixture linear predictor must be finite")
    return z, logistic(z)


def execute_fixtures(
    csv_path: Path | str = HERE / "frozen-fixtures.csv",
    out_dir: Path | str = MODEL_DIR,
):
    csv_path = Path(csv_path)
    out_dir = Path(out_dir)
    rows = []
    seen_case_ids = set()
    input_sha = file_sha256(csv_path)

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
                f"expected={expected}, actual={fieldnames}, "
                f"missing={missing}, unknown={unknown}"
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
            z, p = _evaluate_regression_pin_fixture(x)
            rows.append(
                {
                    "case_id": case_id,
                    "z": f"{z:.12f}",
                    "p": f"{p:.12f}",
                }
            )

    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "fixture-results.json").write_text(payload, encoding="utf-8")
    output_sha = payload_sha256(payload)
    (out_dir / "fixture-results.sha256").write_text(
        output_sha + "  fixture-results.json\n", encoding="utf-8"
    )
    (out_dir / "fixture-input.sha256").write_text(
        input_sha + "  frozen-fixtures.csv\n", encoding="utf-8"
    )
    return payload, output_sha


def main():
    payload, output_sha = execute_fixtures()
    print(payload, end="")
    print("INPUT_SHA256", file_sha256(HERE / "frozen-fixtures.csv"))
    print("OUTPUT_SHA256", output_sha)


if __name__ == "__main__":
    main()
