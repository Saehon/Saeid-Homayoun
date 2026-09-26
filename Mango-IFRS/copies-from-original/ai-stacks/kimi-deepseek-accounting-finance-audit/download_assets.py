"""Download selected open accounting/finance/audit assets.

The default behavior is conservative:
- --datasets downloads small/medium Hugging Face benchmark datasets.
- --kaggle downloads selected public Kaggle datasets.
- Model weights are only downloaded when explicitly requested because they can
  require many gigabytes of disk and substantial RAM/VRAM.

Each upstream asset retains its own license.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

HF_DATASETS = {
    "finqa": "bevaya/FinQA",
    "financebench": "PatronusAI/financebench",
}

HF_MODELS = {
    "deepseek_7b": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    "kimi_vl": "moonshotai/Kimi-VL-A3B-Instruct",
}

KAGGLE_DATASETS = {
    "creditcardfraud": "mlg-ulb/creditcardfraud",
    "paysim": "ealaxi/paysim1",
}


def download_hf_datasets() -> None:
    from datasets import load_dataset

    out = ASSETS / "huggingface-datasets"
    out.mkdir(parents=True, exist_ok=True)

    for short_name, repo_id in HF_DATASETS.items():
        print(f"[HF dataset] {repo_id}")
        dataset = load_dataset(repo_id)
        target = out / short_name
        target.mkdir(parents=True, exist_ok=True)
        dataset.save_to_disk(str(target))
        print(f"  saved -> {target}")


def download_hf_model(key: str) -> None:
    from huggingface_hub import snapshot_download

    repo_id = HF_MODELS[key]
    out = ASSETS / "huggingface-models" / key
    out.mkdir(parents=True, exist_ok=True)

    print(f"[HF model] {repo_id}")
    print("WARNING: model downloads can require many GB of disk space.")
    snapshot_download(
        repo_id=repo_id,
        local_dir=str(out),
    )
    print(f"  saved -> {out}")


def download_kaggle() -> None:
    import kagglehub

    out = ASSETS / "kaggle"
    out.mkdir(parents=True, exist_ok=True)

    for short_name, handle in KAGGLE_DATASETS.items():
        print(f"[Kaggle] {handle}")
        try:
            downloaded = kagglehub.dataset_download(handle)
            print(f"  downloaded -> {downloaded}")
        except Exception as exc:
            print(f"  FAILED: {exc}")
            print("  If authentication is required, configure Kaggle credentials and rerun.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasets", action="store_true", help="Download FinQA and FinanceBench from Hugging Face")
    parser.add_argument("--kaggle", action="store_true", help="Download selected public Kaggle fraud datasets")
    parser.add_argument("--deepseek-7b", action="store_true", help="Download DeepSeek R1 Distill Qwen 7B")
    parser.add_argument("--kimi-vl", action="store_true", help="Download Kimi VL A3B Instruct")
    args = parser.parse_args()

    ASSETS.mkdir(parents=True, exist_ok=True)

    if not any((args.datasets, args.kaggle, args.deepseek_7b, args.kimi_vl)):
        parser.print_help()
        return

    if args.datasets:
        download_hf_datasets()
    if args.kaggle:
        download_kaggle()
    if args.deepseek_7b:
        download_hf_model("deepseek_7b")
    if args.kimi_vl:
        download_hf_model("kimi_vl")


if __name__ == "__main__":
    main()
