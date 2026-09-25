#!/usr/bin/env python3
"""Download registered public/free research datasets without committing them to Git."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "data_sources.yml"
REPO_ROOT = HERE.parents[2]


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc, {x["id"]: x for x in doc["sources"]}


def sanitize(name: str) -> str:
    return name.replace("/", "__").replace(":", "_")


def write_meta(dest: Path, spec: dict, extra: dict | None = None):
    meta = dict(spec)
    if extra:
        meta.update(extra)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "_SOURCE.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def download_huggingface(spec: dict, root: Path, rows: int | None):
    from datasets import load_dataset

    handle = spec["handle"]
    config = spec.get("config")
    split = spec.get("split", "train")
    streaming = bool(spec.get("streaming", False))
    limit = rows if rows is not None else int(spec.get("default_rows", 1000))

    kwargs = {"split": split, "streaming": streaming}
    if config:
        ds = load_dataset(handle, config, **kwargs)
    else:
        ds = load_dataset(handle, **kwargs)

    dest = root / spec["id"]
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / "sample.jsonl"

    count = 0
    with out.open("w", encoding="utf-8") as f:
        iterator = iter(ds)
        while count < limit:
            try:
                row = next(iterator)
            except StopIteration:
                break
            f.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
            count += 1

    write_meta(dest, spec, {"download_mode": "sample", "rows_written": count})
    print(f"Wrote {count} rows to {out}")


def download_kaggle(spec: dict, root: Path):
    import kagglehub

    handle = spec["handle"]
    cache_path = Path(kagglehub.dataset_download(handle))
    dest = root / spec["id"]
    dest.mkdir(parents=True, exist_ok=True)

    # Preserve the platform-managed cache and record its resolved path instead of
    # duplicating hundreds of MB/GB into Git.
    (dest / "KAGGLE_CACHE_PATH.txt").write_text(str(cache_path) + "\n", encoding="utf-8")
    write_meta(dest, spec, {"download_mode": "kagglehub-cache", "resolved_path": str(cache_path)})
    print(f"Kaggle dataset available at: {cache_path}")
    print(f"Reference recorded in: {dest}")


def clone_github(spec: dict, root: Path):
    handle = spec["handle"]
    dest = root / spec["id"]
    if (dest / ".git").exists():
        print(f"Already cloned: {dest}")
        return
    if dest.exists() and any(dest.iterdir()):
        raise RuntimeError(f"Destination exists and is not empty: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://github.com/{handle}.git"
    subprocess.run(["git", "clone", "--depth", "1", url, str(dest)], check=True)
    print(f"Cloned {handle} to {dest}")


def main():
    doc, sources = load_registry()
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="List registered sources")
    parser.add_argument("--source", help="Source id from data_sources.yml")
    parser.add_argument("--rows", type=int, help="Rows to sample for Hugging Face datasets")
    parser.add_argument("--root", default=doc.get("download_root", "research-data"))
    args = parser.parse_args()

    if args.list:
        for s in sources.values():
            print(f'{s["id"]:<30} {s["platform"]:<12} {s["kind"]:<16} {s["handle"]}')
        return 0

    if not args.source:
        parser.error("Use --list or --source SOURCE_ID")
    if args.source not in sources:
        parser.error(f"Unknown source: {args.source}")

    spec = sources[args.source]
    root = REPO_ROOT / args.root
    root.mkdir(parents=True, exist_ok=True)

    platform = spec["platform"]
    if platform == "huggingface":
        download_huggingface(spec, root, args.rows)
    elif platform == "kaggle":
        download_kaggle(spec, root)
    elif platform == "github":
        clone_github(spec, root)
    else:
        raise RuntimeError(f"Unsupported platform: {platform}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
