import os
from pathlib import Path
from huggingface_hub import HfApi

TOKEN = os.environ.get("HF_TOKEN")
if not TOKEN:
    raise SystemExit("HF_TOKEN is required.")

REPO_ID = os.environ.get("HF_SPACE_REPO", "SADHON/ibm-granite-accounting-audit")
SOURCE = Path("open-source/ibm-granite/huggingface-space")

api = HfApi(token=TOKEN)
api.create_repo(
    repo_id=REPO_ID,
    repo_type="space",
    space_sdk="gradio",
    private=False,
    exist_ok=True,
)
api.upload_folder(
    repo_id=REPO_ID,
    repo_type="space",
    folder_path=str(SOURCE),
    commit_message="Sync IBM Granite Accounting & Audit Lab from GitHub",
)
print(f"Synced to https://huggingface.co/spaces/{REPO_ID}")
