from __future__ import annotations

import argparse
from pathlib import Path

from .orchestrator import DEFAULT_SAMPLE, run


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="FRANKENSTEIN evidence-governed accounting, audit and assurance prototype.")
    p.add_argument("--csv", default=str(DEFAULT_SAMPLE))
    p.add_argument("--objective", default=(
        "Assess finance, accounting, internal-control, forensic, operations, sustainability, "
        "cost/FinOps and AI/data-governance risks using evidence-grounded specialist review."
    ))
    p.add_argument("--offline", action="store_true", help="Run deterministic evidence without a Claude API call.")
    return p


def main() -> None:
    args = parser().parse_args()
    report = run(args.objective, Path(args.csv), use_claude=not args.offline)
    print(report.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
