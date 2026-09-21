from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from .agent import ALL_DOMAINS, run_frankenstein_audit
from .analytics import result_as_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="FRANKENSTEIN evidence-grounded Finance & Operations Audit System."
    )
    parser.add_argument(
        "--csv",
        default="sample_data/transactions.csv",
        help="Repo-local CSV path relative to frankenstein_finops/.",
    )
    parser.add_argument(
        "--objective",
        default=(
            "Assess financial-process and operational risks, test key transaction controls, "
            "identify forensic indicators, challenge the evidence, and recommend prioritized follow-up."
        ),
    )
    parser.add_argument(
        "--deterministic-only",
        action="store_true",
        help="Run transparent transaction tests only; no model/API call.",
    )
    parser.add_argument(
        "--domains",
        default="all",
        help=(
            "Comma-separated specialist domains or 'all'. Valid values: "
            + ", ".join(ALL_DOMAINS)
        ),
    )
    return parser


def _parse_domains(value: str) -> list[str] | None:
    if value.strip().lower() == "all":
        return None
    return [part.strip() for part in value.split(",") if part.strip()]


async def _main() -> None:
    args = build_parser().parse_args()

    if args.deterministic_only or not os.getenv("OPENAI_API_KEY"):
        csv_path = Path(args.csv)
        if not csv_path.is_absolute():
            csv_path = Path(__file__).resolve().parent / csv_path
        print(result_as_json(csv_path))
        if not args.deterministic_only and not os.getenv("OPENAI_API_KEY"):
            print(
                "\nOPENAI_API_KEY is not set, so only deterministic tests were run. "
                "Set the key to enable the full specialist + challenge + synthesis workflow."
            )
        return

    report = await run_frankenstein_audit(
        objective=args.objective,
        csv_path=args.csv,
        domains=_parse_domains(args.domains),
    )
    print(report.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(_main())
