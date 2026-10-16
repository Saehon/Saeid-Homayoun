#!/usr/bin/env python3
"""Train an independent FinBERT CAM/KAM topic classifier on AUTHORIZED private data.

Research owner: Prof. Saeid Homayoun. Neither the checkpoint nor any evaluated
metric is created by this source file alone. Do not publish raw licensed data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import GroupShuffleSplit

ALIASES = {
    "kam_title": "title", "cam_title": "title",
    "kam_description": "description", "cam_description": "description",
    "audit_matter_topic": "topic", "issuer": "company",
    "firm": "company", "report_year": "fiscal_year",
}


def prepare_table(path: Path):
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    else:
        raise ValueError("Expected a CSV or Excel file.")
    raw_rows = len(df)
    df.columns = [str(x).strip().lower().replace(" ", "_") for x in df.columns]
    for old, new in ALIASES.items():
        if old in df and new not in df:
            df = df.rename(columns={old: new})
    needed = {"title", "description", "topic"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Required CAM/KAM columns not found: {sorted(missing)}")
    df = df.dropna(subset=sorted(needed)).copy()
    for col in needed:
        df[col] = df[col].astype(str).str.strip()
    df = df[(df["title"] != "") & (df["description"] != "") & (df["topic"] != "")]
    df["text"] = df["title"] + " [SEP] " + df["description"]
    if "company" in df:
        df["company"] = df["company"].astype("string").str.strip()
    if "fiscal_year" in df:
        df["fiscal_year"] = pd.to_numeric(df["fiscal_year"], errors="coerce")
    df = df.reset_index(drop=True)
    classes = sorted(df["topic"].unique().tolist())
    if not classes:
        raise ValueError("No valid labeled observations.")
    report = {
        "raw_rows": int(raw_rows),
        "cleaned_rows": int(len(df)),
        "topics": classes,
        "topic_count": len(classes),
        "sample_is_trained": False,
        "duplicate_text_count": int(df["text"].duplicated().sum()),
        "missing_company_count": int(df["company"].isna().sum()) if "company" in df else None,
        "missing_year_count": int(df["fiscal_year"].isna().sum()) if "fiscal_year" in df else None,
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    return df, report


def holdouts(df, mode, cutoff, seed):
    if mode == "company":
        if "company" not in df or df["company"].isna().any() or (df["company"] == "").any():
            raise ValueError("Complete company identifiers are REQUIRED for company-disjoint split.")
        if df["company"].nunique() < 5:
            raise ValueError("At least 5 independent company IDs required for company holdout.")
        splitter = GroupShuffleSplit(n_splits=1, test_size=0.15, random_state=seed)
        remain_i, test_i = next(splitter.split(df, groups=df["company"]))
        remain = df.iloc[remain_i]
        test = df.iloc[test_i]
        splitter2 = GroupShuffleSplit(n_splits=1, test_size=0.15 / 0.85,
                                      random_state=seed + 1)
        train_i, val_i = next(splitter2.split(remain, groups=remain["company"]))
        train, val = remain.iloc[train_i], remain.iloc[val_i]
        sets = [set(x["company"]) for x in (train, val, test)]
        assert not (sets[0] & sets[1] or sets[0] & sets[2] or sets[1] & sets[2])
    else:
        if cutoff is None:
            raise ValueError("Provide --cutoff YEAR for forward-year validation.")
        if "fiscal_year" not in df or df["fiscal_year"].isna().any():
            raise ValueError("Every observation needs fiscal_year for forward-time split.")
        train = df[df["fiscal_year"] < cutoff]
        val = df[df["fiscal_year"] == cutoff]
        test = df[df["fiscal_year"] > cutoff]
    if min(map(len, (train, val, test))) == 0:
        raise ValueError("Empty train/validation/test group. Increase data or adjust cutoff.")
    train_topics = set(train["topic"])
    absent = sorted((set(val["topic"]) | set(test["topic"])) - train_topics)
    if absent:
        raise ValueError(f"Holdout contains labels absent from training: {absent}. "
                         "Define a documented rare-topic protocol before proceeding.")
    return train.reset_index(drop=True), val.reset_index(drop=True), test.reset_index(drop=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("private_auditbert_v2"))
    p.add_argument("--base-model", default="yiyanghkust/finbert-tone")
    p.add_argument("--split", choices=["company", "year"], default="company")
    p.add_argument("--cutoff", type=int)
    p.add_argument("--epochs", type=float, default=3.0)
    p.add_argument("--batch-size", type=int, default=8)
    p.add_argument("--max-length", type=int, default=256)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    df, report = prepare_table(args.input)
    if args.dry_run:
        report["status"] = "SCHEMA_ONLY_NO_TRAINING"
        print(json.dumps(report, indent=2))
        return

    train, val, test = holdouts(df, args.split, args.cutoff, args.seed)
    classes = report["topics"]
    label2id = {label: i for i, label in enumerate(classes)}
    id2label = {i: label for label, i in label2id.items()}
    for split in (train, val, test):
        split["label"] = split["topic"].map(label2id).astype(int)
    report.update({
        "split": args.split, "cutoff": args.cutoff, "seed": args.seed,
        "split_rows": {"train": len(train), "validation": len(val), "test": len(test)},
        "split_company_counts": {
            name: int(part["company"].nunique()) if "company" in part else None
            for name, part in zip(("train", "validation", "test"), (train, val, test))
        }
    })

    import torch
    from transformers import (
        AutoModelForSequenceClassification, AutoTokenizer, Trainer,
        TrainingArguments, DataCollatorWithPadding, set_seed,
    )
    set_seed(args.seed)
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)

    class TopicDataset(torch.utils.data.Dataset):
        def __init__(self, frame):
            self.examples = tokenizer(
                frame["text"].tolist(), truncation=True,
                max_length=args.max_length
            )
            self.labels = frame["label"].tolist()

        def __len__(self):
            return len(self.labels)

        def __getitem__(self, idx):
            return {**{k: v[idx] for k, v in self.examples.items()},
                    "labels": self.labels[idx]}

    def compute_metrics(pred):
        predicted = np.argmax(pred.predictions, axis=-1)
        return {
            "accuracy": accuracy_score(pred.label_ids, predicted),
            "macro_f1": f1_score(pred.label_ids, predicted, average="macro", zero_division=0),
            "micro_f1": f1_score(pred.label_ids, predicted, average="micro", zero_division=0),
            "weighted_f1": f1_score(pred.label_ids, predicted, average="weighted", zero_division=0),
        }

    model = AutoModelForSequenceClassification.from_pretrained(
        args.base_model, num_labels=len(classes),
        label2id=label2id, id2label=id2label, ignore_mismatched_sizes=True,
    )
    args.output.mkdir(parents=True, exist_ok=True)
    config = TrainingArguments(
        output_dir=str(args.output / "checkpoints"),
        num_train_epochs=args.epochs,
        learning_rate=2e-5,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        eval_strategy="epoch", save_strategy="epoch",
        load_best_model_at_end=True, metric_for_best_model="macro_f1",
        greater_is_better=True, save_total_limit=2,
        weight_decay=0.01, seed=args.seed, report_to="none",
    )
    trainer = Trainer(
        model=model, args=config, train_dataset=TopicDataset(train),
        eval_dataset=TopicDataset(val), processing_class=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=compute_metrics,
    )
    trainer.train()
    heldout = trainer.predict(TopicDataset(test))
    predicted = np.argmax(heldout.predictions, axis=-1)
    target_names = [id2label[i] for i in range(len(classes))]
    by_topic = classification_report(
        test["label"], predicted, labels=list(range(len(classes))),
        target_names=target_names, zero_division=0, output_dict=True,
    )
    report["status"] = "TRAINED_AND_EVALUATED"
    report["sample_is_trained"] = True
    report["test_results"] = {
        k: float(v) for k, v in heldout.metrics.items()
        if isinstance(v, (int, float, np.integer, np.floating))
    }
    report["per_topic_test_results"] = by_topic
    trainer.save_model(str(args.output / "model"))
    tokenizer.save_pretrained(str(args.output / "model"))
    (args.output / "experiment_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps({"status": report["status"],
                      "test_results": report["test_results"]}, indent=2))


if __name__ == "__main__":
    main()
