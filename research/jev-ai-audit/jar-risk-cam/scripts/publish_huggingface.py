"""Publish the permission-cleared synthetic Risk-CAM starter to Hugging Face.

Requires HF_TOKEN with repository write permission. This script reads only files
already committed to the public GitHub publication package. It never reads
Google Drive or private research data.
"""
import os
import pathlib
from huggingface_hub import HfApi

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ID = os.environ.get("HF_REPO_ID", "SADHON/darwin-jev-risk-cam-synthetic-replication")
token = os.environ.get("HF_TOKEN", "").strip()
if not token:
    raise SystemExit("HF_TOKEN is missing. Add a write-enabled Hugging Face token as a GitHub Actions secret.")

api = HfApi(token=token)
api.create_repo(REPO_ID, repo_type="dataset", exist_ok=True, private=False)

uploads = {
    ROOT / "data" / "SYNTHETIC_demo.csv": "SYNTHETIC_demo.csv",
    ROOT / "distribution" / "huggingface" / "README.md": "README.md",
    ROOT / "src" / "validate_panel.py": "code/validate_panel.py",
    ROOT / "tests" / "test_contract.py": "code/test_contract.py",
    ROOT / "JAR_Risk_CAM_Replication_Starter_2026-10-16.zip": "replication/JAR_Risk_CAM_Replication_Starter_2026-10-16.zip",
    ROOT / "PUBLIC_DISTRIBUTION_MANIFEST.md": "PUBLIC_DISTRIBUTION_MANIFEST.md",
}
for source, destination in uploads.items():
    if not source.is_file():
        raise SystemExit(f"Missing public package file: {source}")
    api.upload_file(
        path_or_fileobj=str(source),
        path_in_repo=destination,
        repo_id=REPO_ID,
        repo_type="dataset",
        commit_message=f"Sync {destination} from DARWIN-JEV Risk-CAM publication package",
    )

print(f"Published synthetic-only package to https://huggingface.co/datasets/{REPO_ID}")
