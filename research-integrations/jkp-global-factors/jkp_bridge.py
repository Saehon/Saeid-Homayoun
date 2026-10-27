"""Validate researcher-supplied JKP factor tables without redistributing licensed rows.

Supports CSV and Parquet (Parquet requires pandas/pyarrow).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from datetime import date, datetime
from pathlib import Path


def parse_date(value: str) -> date:
    value = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y%m%d", "%Y-%m", "%Y%m"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date value: {value!r}")


def read_rows(path: Path):
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                raise ValueError("Input CSV has no header")
            yield from reader
    elif path.suffix.lower() in (".parquet", ".pq"):
        try:
            import pandas as pd
        except ImportError as exc:
            raise RuntimeError("Parquet input requires pandas and pyarrow") from exc
        for row in pd.read_parquet(path).to_dict(orient="records"):
            yield row
    else:
        raise ValueError("Only .csv and .parquet input are supported")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(
    path: Path,
    *,
    date_column: str,
    factors: list[str],
    keys: list[str] | None = None,
    start: str = "2020-01-01",
    end: str = "2024-12-31",
    frequency: str = "monthly",
) -> dict:
    """Report provenance/quality; reject malformed factor values and duplicate keys.

    No raw observations are included. Factor units are not changed; source
    files may report percentages or decimals and must be documented separately.
    """
    if not factors:
        raise ValueError("Specify at least one factor column")
    if frequency not in ("monthly", "daily"):
        raise ValueError("frequency must be monthly or daily")
    keys = keys or []
    fields = [date_column, *keys, *factors]
    if len(set(fields)) != len(fields):
        raise ValueError("Date, key, and factor column names must not overlap")
    low, high = parse_date(start), parse_date(end)
    if low > high:
        raise ValueError("start must not exceed end")
    path = Path(path)
    seen: set[tuple] = set()
    missing = Counter({f: 0 for f in factors})
    valid = 0
    excluded = 0
    duplicates = 0
    date_min = None
    date_max = None
    for row in read_rows(path):
        absent = [f for f in fields if f not in row]
        if absent:
            raise ValueError(f"Input is missing required columns: {absent}")
        raw_date = row[date_column]
        if raw_date is None:
            raise ValueError("Date cannot be blank")
        d = parse_date(str(raw_date))
        if not low <= d <= high:
            excluded += 1
            continue
        period = date(d.year, d.month, 1) if frequency == "monthly" else d
        keyvals = tuple(str(row[k]).strip() for k in keys)
        if any(not v or v.lower() in ("nan", "none") for v in keyvals):
            raise ValueError("Blank key value encountered")
        grain = (period, *keyvals)
        if grain in seen:
            duplicates += 1
        else:
            seen.add(grain)
        for factor in factors:
            value = row[factor]
            if value is None or str(value).strip().lower() in ("", "nan", "none", "null", "na"):
                missing[factor] += 1
            else:
                try:
                    numeric = float(value)
                except (TypeError, ValueError) as exc:
                    raise ValueError(f"Non-numeric factor in column {factor}") from exc
                if not math.isfinite(numeric):
                    raise ValueError(f"Non-finite factor in column {factor}")
        valid += 1
        date_min = period if date_min is None else min(period, date_min)
        date_max = period if date_max is None else max(period, date_max)
    if valid == 0:
        raise ValueError("No observations fall in the requested sample window")
    if duplicates:
        raise ValueError(f"Found {duplicates} duplicate period/key observation(s)")
    return {
        "status": "VALIDATED_SCHEMA_ONLY",
        "source_basename": path.name,
        "source_sha256": sha256_file(path),
        "license_note": "Check JKP CC BY-NC and upstream WRDS/vendor terms; no redistribution assumed.",
        "frequency": frequency,
        "date_column": date_column,
        "key_columns": keys,
        "factor_columns": factors,
        "start": str(low),
        "end": str(high),
        "first_period": str(date_min),
        "last_period": str(date_max),
        "rows_in_window": valid,
        "rows_outside_window": excluded,
        "missing_by_factor": dict(missing),
        "units": "UNCHANGED_UNVERIFIED",
        "empirical_results": "NOT_RUN",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--date-column", default="date")
    parser.add_argument("--factor-columns", required=True, help="comma-separated input factor names")
    parser.add_argument("--key-columns", default="", help="optional country/region keys, comma-separated")
    parser.add_argument("--start", default="2020-01-01")
    parser.add_argument("--end", default="2024-12-31")
    parser.add_argument("--frequency", choices=("monthly", "daily"), default="monthly")
    parser.add_argument("--report", type=Path, help="local JSON summary path (no data rows)")
    args = parser.parse_args()
    split = lambda text: [x.strip() for x in text.split(",") if x.strip()]
    report = validate(args.input, date_column=args.date_column,
                      factors=split(args.factor_columns), keys=split(args.key_columns),
                      start=args.start, end=args.end, frequency=args.frequency)
    serialized = json.dumps(report, indent=2, sort_keys=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
