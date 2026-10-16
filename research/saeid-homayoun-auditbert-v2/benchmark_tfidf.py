#!/usr/bin/env python3
"""TF–IDF benchmark for independent Saeid Homayoun AuditBERT V2 study.

CPU-only baseline with the SAME split function and topic labels as the FinBERT
track. This is not the original SSRN paper's benchmark and must not be
represented as published results until run on verified authorized data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

from train_finbert_topic import holdouts, prepare_table


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("private_tfidf_v2_report.json"))
    p.add_argument("--split", choices=["company", "year"], default="company")
    p.add_argument("--cutoff", type=int)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    data, manifest = prepare_table(args.input)
    if args.dry_run:
        print(json.dumps({
            "status": "SCHEMA_ONLY_NOT_ESTIMATED",
            "rows": int(len(data)), "topics": manifest["topic_count"]}, indent=2))
        return
    train, val, test = holdouts(data, args.split, args.cutoff, args.seed)
    # Vocabulary learned ONLY from train data; validation and test remain sealed.
    clf = Pipeline([
        ("tfidf", TfidfVectorizer(
            ngram_range=(1, 2), min_df=2, max_df=0.95,
            max_features=50000, sublinear_tf=True,
        )),
        ("svm", LinearSVC(class_weight="balanced", random_state=args.seed)),
    ])
    clf.fit(train["text"], train["topic"])
    val_predictions = clf.predict(val["text"])
    test_predictions = clf.predict(test["text"])
    all_labels = manifest["topics"]
    report = {
        "research_lead": "Prof. Saeid Homayoun",
        "status": "TFIDF_ESTIMATED_ON_PROVIDED_AUTHORIZED_DATA",
        "source_sha256": manifest["source_sha256"],
        "split": args.split, "year_cutoff": args.cutoff, "seed": args.seed,
        "counts": {"train": len(train), "validation": len(val), "test": len(test)},
        "validation_macro_f1": float(f1_score(
            val["topic"], val_predictions, average="macro", labels=all_labels,
            zero_division=0)),
        "test_accuracy": float(accuracy_score(test["topic"], test_predictions)),
        "test_macro_f1": float(f1_score(
            test["topic"], test_predictions, average="macro",
            labels=all_labels, zero_division=0)),
        "test_weighted_f1": float(f1_score(
            test["topic"], test_predictions, average="weighted",
            labels=all_labels, zero_division=0)),
        "test_per_topic": classification_report(
            test["topic"], test_predictions, labels=all_labels,
            output_dict=True, zero_division=0),
        "warning": "Measured on the supplied run only. No CI toy sample is a "
                   "publication-grade empirical benchmark.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in (
        "status", "counts", "test_macro_f1", "test_weighted_f1"
    )}, indent=2))


if __name__ == "__main__":
    main()
