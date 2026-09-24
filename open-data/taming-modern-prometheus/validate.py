from __future__ import annotations

import csv
from pathlib import Path

EXPECTED_COLUMNS = {
    "case_id",
    "domain",
    "entity_or_scope",
    "source_type",
    "source_anchor",
    "claim_or_event",
    "benchmark_label",
    "expected_gate",
    "required_evidence",
    "red_team_challenge",
    "target_assertion",
    "synthetic_flag",
}
EXPECTED_IDS = {
    "FA-001", "FA-002", "FA-003",
    "AUD-001", "AUD-002",
    "ICFR-001", "ICFR-002",
    "CAM-001",
    "ESG-001", "ESG-002",
    "GOV-001", "RED-001", "REP-001",
}
ALLOWED_LABELS = {"pass", "review", "fail"}


def main() -> None:
    path = Path(__file__).with_name("agentic_assurance_benchmark.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert rows, "dataset is empty"
    assert set(rows[0]) == EXPECTED_COLUMNS, "unexpected columns"
    assert {row["case_id"] for row in rows} == EXPECTED_IDS, "stable IDs do not match"
    assert len(rows) == 13, f"expected 13 rows, got {len(rows)}"
    assert all(row["benchmark_label"] in ALLOWED_LABELS for row in rows)
    assert all(row["source_type"] in {"public_derived", "synthetic"} for row in rows)
    assert sum(row["synthetic_flag"] == "0" for row in rows) == 3
    assert sum(row["synthetic_flag"] == "1" for row in rows) == 10
    assert all(all(value.strip() for value in row.values()) for row in rows)

    print("PASS: Taming the Modern Prometheus benchmark")
    print(f"rows={len(rows)} public_derived=3 synthetic=10")
    for label in sorted(ALLOWED_LABELS):
        print(f"{label}={sum(row['benchmark_label'] == label for row in rows)}")


if __name__ == "__main__":
    main()
