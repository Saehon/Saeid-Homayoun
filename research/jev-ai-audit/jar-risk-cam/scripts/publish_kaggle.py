"""Publish the permission-cleared synthetic Risk-CAM starter to Kaggle.

Requires KAGGLE_USERNAME and KAGGLE_KEY. This script copies only files already
committed to the public GitHub publication package. It never reads Google Drive
or private research data.
"""
import os
import pathlib
import shutil
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
username = os.environ.get("KAGGLE_USERNAME", "").strip()
key = os.environ.get("KAGGLE_KEY", "").strip()
if not username or not key:
    raise SystemExit("KAGGLE_USERNAME/KAGGLE_KEY missing. Add Kaggle API credentials as GitHub Actions secrets.")

with tempfile.TemporaryDirectory(prefix="riskcam_kaggle_") as td:
    out = pathlib.Path(td)
    copies = {
        ROOT / "data" / "SYNTHETIC_demo.csv": out / "SYNTHETIC_demo.csv",
        ROOT / "distribution" / "kaggle" / "dataset-metadata.json": out / "dataset-metadata.json",
        ROOT / "distribution" / "kaggle" / "README.md": out / "README.md",
        ROOT / "src" / "validate_panel.py": out / "validate_panel.py",
        ROOT / "tests" / "test_contract.py": out / "test_contract.py",
        ROOT / "JAR_Risk_CAM_Replication_Starter_2026-10-16.zip": out / "JAR_Risk_CAM_Replication_Starter_2026-10-16.zip",
        ROOT / "PUBLIC_DISTRIBUTION_MANIFEST.md": out / "PUBLIC_DISTRIBUTION_MANIFEST.md",
    }
    for source, destination in copies.items():
        if not source.is_file():
            raise SystemExit(f"Missing public package file: {source}")
        shutil.copy2(source, destination)

    result = subprocess.run(
        ["kaggle", "datasets", "create", "-p", str(out)],
        text=True,
        capture_output=True,
    )
    # If the slug already exists, publish a new version instead of failing.
    combined = (result.stdout or "") + "\n" + (result.stderr or "")
    if result.returncode != 0 and ("already exists" in combined.lower() or "409" in combined):
        result = subprocess.run(
            ["kaggle", "datasets", "version", "-p", str(out), "-m", "Sync public synthetic Risk-CAM replication package"],
            text=True,
            capture_output=True,
        )
        combined = (result.stdout or "") + "\n" + (result.stderr or "")
    if result.returncode != 0:
        raise SystemExit("Kaggle publication failed: " + combined[-3000:])

print("Kaggle synthetic-only dataset publication completed.")
