#!/usr/bin/env python3
"""Validate DATASETFREE's public source registries, offline and without PII."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = (
    (ROOT / "data" / "open_data_sources.csv",
     ("source", "discipline", "url", "data_fields", "license_access", "caveat"), "source"),
    (ROOT / "replication_packages_2026-10-10.csv",
     ("id", "journal", "topic", "url", "replication_status", "primary_caveat"), "id"),
)

def validate(path: Path, required: tuple[str, ...], unique_field: str) -> list[str]:
    """Check metadata structure; never download third-party data."""
    errors: list[str] = []
    try:
        with path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            absent = set(required) - set(reader.fieldnames or ())
            if absent:
                return [f"{path.name}: missing columns {sorted(absent)}"]
            seen: set[str] = set()
            nrows = 0
            for line, row in enumerate(reader, start=2):
                nrows += 1
                for key in required:
                    if not (row.get(key) or "").strip():
                        errors.append(f"{path.name}:{line}: empty {key}")
                primary = (row.get(unique_field) or "").strip().casefold()
                if primary in seen and primary:
                    errors.append(f"{path.name}:{line}: duplicate {unique_field}={primary}")
                seen.add(primary)
                raw_url = (row.get("url") or "").strip()
                parsed = urlparse(raw_url)
                if parsed.scheme != "https" or not parsed.netloc:
                    errors.append(f"{path.name}:{line}: invalid HTTPS url {raw_url!r}")
            if not nrows:
                errors.append(f"{path.name}: registry has no data rows")
    except FileNotFoundError:
        errors.append(f"{path}: not found")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path.name}: unreadable CSV: {exc}")
    return errors

def run() -> int:
    parser = argparse.ArgumentParser(description="Validate public metadata registries")
    parser.add_argument("--source", type=Path, help="Alternative free-source CSV")
    parser.add_argument("--replication", type=Path, help="Alternative replication CSV")
    args = parser.parse_args()
    paths = [
        (args.source or REGISTRIES[0][0], REGISTRIES[0][1], REGISTRIES[0][2]),
        (args.replication or REGISTRIES[1][0], REGISTRIES[1][1], REGISTRIES[1][2]),
    ]
    violations = [err for p, fields, key in paths for err in validate(p, fields, key)]
    if violations:
        print("\n".join(violations))
        return 1
    print("DATASETFREE metadata registry validation PASSED (no data downloaded).")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())
