"""Research-safe, standard-library bridge from licensed JKP factor CSVs to NAAIL.

This estimates retrospective factor exposures, not future returns or audit risk.
No third-party raw dataset is bundled or fetched.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path


def parse_date(raw: str) -> str:
    value = str(raw).strip()
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%Y%m"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {value!r}")


def read_csv(path: Path, required: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f"Missing or duplicate CSV header in {path.name}")
        absent = set(required) - set(reader.fieldnames)
        if absent:
            raise ValueError(f"Missing required columns in {path.name}: {sorted(absent)}")
        return list(reader)


def number(raw: str, unit: str) -> float:
    if raw is None or not str(raw).strip():
        raise ValueError("Missing numeric value")
    value = float(raw)
    if not math.isfinite(value):
        raise ValueError("Nonfinite numeric value")
    return value / 100.0 if unit == "percent" else value


def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    aug = [matrix[i][:] + [vector[i]] for i in range(n)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(aug[i][k]))
        if abs(aug[pivot][k]) < 1e-12:
            raise ValueError("Singular design matrix: insufficient factor variation")
        aug[k], aug[pivot] = aug[pivot], aug[k]
        scale = aug[k][k]
        aug[k] = [x / scale for x in aug[k]]
        for i in range(n):
            if i == k:
                continue
            weight = aug[i][k]
            aug[i] = [a - weight * b for a, b in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def regress(y: list[float], xs: list[list[float]]) -> tuple[list[float], float]:
    p = len(xs[0]) + 1
    if len(y) < p + 3:
        raise ValueError(f"Insufficient matched periods: need at least {p + 3}")
    design = [[1.0] + row for row in xs]
    xtx = [[sum(row[i] * row[j] for row in design) for j in range(p)] for i in range(p)]
    xty = [sum(row[i] * val for row, val in zip(design, y)) for i in range(p)]
    coefficients = solve(xtx, xty)
    residuals = [val - sum(a * b for a, b in zip(row, coefficients)) for val, row in zip(y, design)]
    rmse = math.sqrt(sum(e * e for e in residuals) / (len(y) - p))
    return coefficients, rmse


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*, factors: Path, returns: Path, output_dir: Path, factor_cols: list[str],
        factor_unit: str, return_unit: str, source_version: str, universe: str,
        license_confirmed: bool, synthetic: bool = False) -> dict:
    """Require rights attestation, date matching, uniqueness and enough observations."""
    if not synthetic and not license_confirmed:
        raise ValueError("Licensed/rights-cleared input attestation required")
    if not factor_cols or len(factor_cols) != len(set(factor_cols)):
        raise ValueError("Factor columns must be a nonempty unique list")
    if factor_unit not in {"decimal", "percent"} or return_unit not in {"decimal", "percent"}:
        raise ValueError("Declare each input unit as decimal or percent")
    if not source_version.strip() or not universe.strip():
        raise ValueError("Specify JKP source version and geographic universe")
    factor_rows = read_csv(factors, ["date", *factor_cols])
    return_rows = read_csv(returns, ["date", "entity_id", "excess_return"])
    indexed = {}
    for row in factor_rows:
        dt = parse_date(row["date"])
        if dt in indexed:
            raise ValueError(f"Duplicate factor date: {dt}")
        indexed[dt] = [number(row[c], factor_unit) for c in factor_cols]
    entities: dict[str, list[tuple[str, float, list[float]]]] = defaultdict(list)
    seen = set()
    unmatched = 0
    for row in return_rows:
        dt = parse_date(row["date"])
        entity = row["entity_id"].strip()
        if not entity:
            raise ValueError("Empty entity_id")
        key = (entity, dt)
        if key in seen:
            raise ValueError(f"Duplicate entity-date: {key}")
        seen.add(key)
        if dt not in indexed:
            unmatched += 1
            continue
        entities[entity].append((dt, number(row["excess_return"], return_unit), indexed[dt]))
    estimates = []
    excluded = []
    for entity, observations in sorted(entities.items()):
        observations.sort(key=lambda row: row[0])
        try:
            coefficients, rmse = regress([row[1] for row in observations], [row[2] for row in observations])
        except ValueError as error:
            excluded.append({"entity_id": entity, "n_matched": len(observations), "reason": str(error)})
            continue
        estimates.append({"entity_id": entity, "start_date": observations[0][0],
                          "end_date": observations[-1][0], "n_matched": len(observations),
                          "alpha_decimal_per_period": coefficients[0],
                          "betas": dict(zip(factor_cols, coefficients[1:])),
                          "residual_rmse_decimal": rmse,
                          "status": "ESTIMATED_REVIEW_REQUIRED"})
    manifest = {
        "schema_version": "jkp-naail-bridge-1.0", "execution_utc": datetime.now(timezone.utc).isoformat(),
        "source_repository": "https://github.com/bkelly-lab/jkp-data",
        "source_version_user_declared": source_version, "universe_user_declared": universe,
        "input_file_digests_sha256": {"factors": sha256(factors), "returns": sha256(returns)},
        "factor_columns": factor_cols, "factor_unit_input": factor_unit,
        "returns_unit_input": return_unit, "return_type": "already_excess_return",
        "licensed_data_attested": bool(license_confirmed), "synthetic_fixture": bool(synthetic),
        "n_factor_periods": len(indexed), "n_return_rows": len(return_rows),
        "n_unmatched_returns": unmatched, "n_estimated_entities": len(estimates),
        "n_excluded_entities": len(excluded), "excluded_entities": excluded,
        "temporal_contract": "Exact contemporaneous date match; retrospective exposure only; no prediction or causal identification",
        "scientific_status": "SIMULATED" if synthetic else "UNVERIFIED_RESEARCH_OUTPUT",
        "human_gate": "REQUIRED", "jev_decision": "REQUEST_REVIEW_AND_EXTERNAL_EVIDENCE",
        "cam_risk_inference": "NOT_SUPPORTED_BY_MARKET_FACTORS_ALONE",
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "factor_exposures.json").write_text(json.dumps(estimates, indent=2) + "\n", encoding="utf-8")
    (output_dir / "evidence_passport.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factors", required=True, type=Path)
    parser.add_argument("--returns", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--factor-cols", required=True, help="Comma-separated wide-format factor names")
    parser.add_argument("--factor-unit", required=True, choices=["decimal", "percent"])
    parser.add_argument("--return-unit", required=True, choices=["decimal", "percent"])
    parser.add_argument("--source-version", required=True)
    parser.add_argument("--universe", required=True)
    parser.add_argument("--license-confirmed", action="store_true")
    parser.add_argument("--synthetic", action="store_true")
    args = parser.parse_args()
    out = run(factors=args.factors, returns=args.returns, output_dir=args.output_dir,
              factor_cols=[x.strip() for x in args.factor_cols.split(",")],
              factor_unit=args.factor_unit, return_unit=args.return_unit,
              source_version=args.source_version, universe=args.universe,
              license_confirmed=args.license_confirmed, synthetic=args.synthetic)
    print(json.dumps({k: out[k] for k in ("scientific_status", "n_estimated_entities", "n_excluded_entities", "human_gate")}, indent=2))


if __name__ == "__main__":
    main()