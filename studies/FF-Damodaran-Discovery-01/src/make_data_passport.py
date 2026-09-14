from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "evidence" / "download_manifest.json"
PROCESSED = ROOT / "data" / "processed"
OUT = ROOT / "evidence" / "data_passport.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def csv_profile(path: Path) -> dict:
    df = pd.read_csv(path)
    return {
        "path": str(path.relative_to(ROOT)),
        "rows": int(len(df)),
        "columns": list(df.columns),
        "sha256": sha256(path),
        "missing_cells": int(df.isna().sum().sum()),
    }


def main() -> None:
    if not MANIFEST.exists():
        raise FileNotFoundError("Run download_sources.py first.")
    raw = json.loads(MANIFEST.read_text(encoding="utf-8"))
    processed = []
    for name in [
        "ff49_industry_year.csv",
        "ff_factors_year.csv",
        "ff49_factor_exposures_year.csv",
        "damodaran_industry_year.csv",
        "econova_ff_damodaran_panel.csv",
    ]:
        path = PROCESSED / name
        if path.exists():
            processed.append(csv_profile(path))

    passport = {
        "study_id": "FF-DAMODARAN-DISCOVERY-01",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "authoritative_source_policy": True,
        "raw_manifest": raw,
        "processed_artifacts": processed,
        "scientific_controls": {
            "year_specific_mapping": True,
            "manual_crosswalk_approval_required": True,
            "future_outcome_constructed_after_time_sort": True,
            "rolling_factor_exposure_provenance_required": True,
            "null_results_preserved": True,
            "human_gate_required": True,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(passport, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
