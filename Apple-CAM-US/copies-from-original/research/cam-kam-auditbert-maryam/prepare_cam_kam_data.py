"""Prepare authorized CAM/KAM data for AuditBERT-style topic classification.

This script does not download or redistribute proprietary data.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

REQUIRED = ["title", "description", "topic"]


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(c).strip().lower() for c in df.columns]
    aliases = {
        "kam_title": "title",
        "cam_title": "title",
        "kam_description": "description",
        "cam_description": "description",
        "audit_matter_topic": "topic",
        "audit_matter_topic_fkey": "topic_fkey",
    }
    return df.rename(columns={k: v for k, v in aliases.items() if k in df.columns})


def prepare(input_path: Path, output_dir: Path, test_size: float, seed: int) -> None:
    if input_path.suffix.lower() == ".csv":
        df = pd.read_csv(input_path)
    elif input_path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(input_path)
    else:
        raise ValueError("Input must be CSV, XLSX, or XLS.")

    df = normalize_columns(df)

    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=REQUIRED).copy()
    df["title"] = df["title"].astype(str).str.strip()
    df["description"] = df["description"].astype(str).str.strip()
    df["topic"] = df["topic"].astype(str).str.strip()
    df = df[(df["title"] != "") & (df["description"] != "") & (df["topic"] != "")]

    df["text"] = df["title"] + " [SEP] " + df["description"]

    encoder = LabelEncoder()
    df["topic_label"] = encoder.fit_transform(df["topic"])

    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        random_state=seed,
        stratify=df["topic_label"] if df["topic_label"].value_counts().min() >= 2 else None,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(output_dir / "train.csv", index=False)
    test_df.to_csv(output_dir / "test.csv", index=False)

    metadata = {
        "rows_after_cleaning": int(len(df)),
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "topic_count": int(len(encoder.classes_)),
        "topics": encoder.classes_.tolist(),
        "seed": seed,
        "test_size": test_size,
    }
    (output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", default=Path("prepared_cam_kam"), type=Path)
    parser.add_argument("--test-size", default=0.20, type=float)
    parser.add_argument("--seed", default=42, type=int)
    args = parser.parse_args()
    prepare(args.input, args.output, args.test_size, args.seed)
