"""Publish only the permission-cleared synthetic Risk-CAM starter to Hugging Face.
Requires HF_TOKEN with write permission. Never reads Google Drive or private data.
"""
import os, pathlib
from huggingface_hub import HfApi
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO_ID=os.environ.get("HF_REPO_ID","SADHON/darwin-jev-risk-cam-synthetic-replication")
token=os.environ["HF_TOKEN"]
api=HfApi(token=token)
api.create_repo(REPO_ID, repo_type="dataset", exist_ok=True, private=False)
api.upload_file(path_or_fileobj=str(ROOT/"data"/"SYNTHETIC_demo.csv"), path_in_repo="SYNTHETIC_demo.csv", repo_id=REPO_ID, repo_type="dataset")
api.upload_file(path_or_fileobj=str(ROOT/"distribution"/"huggingface"/"README.md"), path_in_repo="README.md", repo_id=REPO_ID, repo_type="dataset")
print(f"Published synthetic-only dataset to https://huggingface.co/datasets/{REPO_ID}")
