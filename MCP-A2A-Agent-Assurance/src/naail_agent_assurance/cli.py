"""Command-line validator for NAAIL Evidence Passports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .evidence import compute_content_hash, validate_passport


def main() -> int:
    parser = argparse.ArgumentParser(prog="naail-assurance")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="validate an Evidence Passport")
    validate.add_argument("path", type=Path)

    digest = sub.add_parser("hash", help="compute the canonical Evidence Passport hash")
    digest.add_argument("path", type=Path)

    args = parser.parse_args()
    data = json.loads(args.path.read_text(encoding="utf-8"))

    if args.command == "hash":
        print(compute_content_hash(data))
        return 0

    errors = validate_passport(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("PASS: Evidence Passport minimum contract validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
