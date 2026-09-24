from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

CANDIDATES = [
    Path("/kaggle/input/taming-modern-prometheus-assurance/agentic_assurance_benchmark.csv"),
    Path("agentic_assurance_benchmark.csv"),
    Path("../../../open-data/taming-modern-prometheus/agentic_assurance_benchmark.csv"),
]


def locate() -> Path:
    for candidate in CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("agentic_assurance_benchmark.csv not found")


def main() -> None:
    path = locate()
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    counts = Counter(row["benchmark_label"] for row in rows)
    domain_counts = Counter(row["domain"] for row in rows)
    results = {
        "dataset": "taming-modern-prometheus-assurance",
        "rows": len(rows),
        "label_counts": dict(sorted(counts.items())),
        "domain_counts": dict(sorted(domain_counts.items())),
        "public_derived_rows": sum(row["synthetic_flag"] == "0" for row in rows),
        "synthetic_rows": sum(row["synthetic_flag"] == "1" for row in rows),
        "deterministic_checks": {
            "expected_rows": 13,
            "row_count_pass": len(rows) == 13,
            "public_synthetic_split_pass": (
                sum(row["synthetic_flag"] == "0" for row in rows) == 3
                and sum(row["synthetic_flag"] == "1" for row in rows) == 10
            ),
        },
    }
    print(json.dumps(results, indent=2))
    Path("benchmark_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
