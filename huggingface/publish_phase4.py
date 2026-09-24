from huggingface_hub import HfApi
import os

token=os.environ.get("HF_TOKEN")
if not token:
    print("HF_TOKEN is not configured; skipping Hugging Face publication.")
    raise SystemExit(0)

repo_id="SADHON/frankenstein-phase4-accounting-audit-benchmark"
api=HfApi(token=token)
api.create_repo(repo_id=repo_id, repo_type="dataset", private=False, exist_ok=True)
api.upload_folder(
    folder_path="huggingface/frankenstein-phase4-accounting-audit-benchmark",
    repo_id=repo_id,
    repo_type="dataset",
)
print(f"Published https://huggingface.co/datasets/{repo_id}")
