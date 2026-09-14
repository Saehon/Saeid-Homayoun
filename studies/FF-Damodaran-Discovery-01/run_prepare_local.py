from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STEPS = [
    [sys.executable, "src/download_sources.py"],
    [sys.executable, "src/build_ff49_annual.py"],
    [sys.executable, "src/build_factor_exposures.py"],
    [sys.executable, "src/build_damodaran_panel.py"],
    [sys.executable, "src/suggest_crosswalk.py"],
    [sys.executable, "src/make_data_passport.py"],
    [sys.executable, "tests/test_contract.py"],
    [sys.executable, "tests/test_synthetic_pipeline.py"],
]


def run(cmd: list[str]) -> None:
    print("\n>>> " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> None:
    for cmd in STEPS:
        run(cmd)

    candidate = ROOT / "crosswalk" / "candidate_crosswalk.csv"
    passport = ROOT / "evidence" / "data_passport.json"
    manifest = ROOT / "evidence" / "download_manifest.json"

    print("\nECONOVA-S preparation completed.")
    print(f"Candidate crosswalk: {candidate}")
    print(f"Data Passport:      {passport}")
    print(f"Download manifest:  {manifest}")
    print("\nScientific gate: DO NOT run the full baseline until candidate_crosswalk.csv has been reviewed and approved into reviewed_crosswalk.csv.")


if __name__ == "__main__":
    main()
