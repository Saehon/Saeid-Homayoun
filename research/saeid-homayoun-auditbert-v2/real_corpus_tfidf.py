#!/usr/bin/env python3
"""Private CAM/KAM TF-IDF benchmark. Dr. Saeid Homayoun, AuditBERT-USUK.

Source datasets remain PRIVATE in Google Drive. This program emits only
aggregate metrics, hashes and class-level statistics, not raw disclosure text.
Read the research plan and gates in README.md before running.
UK cohort is HEADQUARTERS=GB proxy only, not verified ISA (UK) auditor regime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report, f1_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

FIELDS = {
    "us_cam": dict(topic="TOPIC_NAME", issuer="COMPANY_FKEY",
                   matter="CRITICAL_AUDIT_MATTER_KEY", extra=[]),
    "uk_hq_kam": dict(topic="TOPIC", issuer="ENTITY_MAP_FKEY",
                      matter="AO_KEY_AUDIT_MATTER_KEY", extra=["HEADQUARTER_COUNTRY_CODE"]),
    "eu_kam": dict(topic="TOPIC", issuer="ENTITY_MAP_FKEY",
                   matter="AO_KEY_AUDIT_MATTER_KEY", extra=[]),
}


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for b in iter(lambda: fh.read(4 * 1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().casefold())


def load_clean(path: Path, source: str):
    schema = FIELDS[source]
    cols = ["TITLE", "DESCRIPTION", "AUDIT_OPINION_FKEY",
            schema["topic"], schema["issuer"], schema["matter"]] + schema["extra"]
    d = pd.read_csv(path, usecols=cols, dtype="string", low_memory=False, encoding="utf-8-sig")
    input_rows = len(d)
    if source == "uk_hq_kam":
        d = d[d["HEADQUARTER_COUNTRY_CODE"].fillna("").str.upper().eq("GB")].copy()
    subset_rows = len(d)
    required = ["DESCRIPTION", schema["topic"], schema["issuer"],
                schema["matter"], "AUDIT_OPINION_FKEY"]
    d = d.dropna(subset=required).copy()
    for col in ["TITLE"] + required:
        d[col] = d[col].fillna("").str.strip()
    d = d[(d["DESCRIPTION"].str.len() >= 30)
          & (d[schema["topic"]] != "") & (d[schema["issuer"]] != "")
          & (d[schema["matter"]] != "")].copy()
    after_text_filter = len(d)
    d["text"] = d["TITLE"] + " [SEP] " + d["DESCRIPTION"]
    d["text_hash"] = d["text"].map(lambda x: hashlib.sha256(
        normalize(x).encode("utf-8")).hexdigest())
    duplicated_matter_keys = int(d[schema["matter"]].duplicated().sum())
    duplicates_all = int(d["text_hash"].duplicated().sum())
    label_nunique = d.groupby("text_hash")[schema["topic"]].nunique()
    conflicts = set(label_nunique[label_nunique > 1].index)
    conflict_rows = int(d["text_hash"].isin(conflicts).sum())
    d = d[~d["text_hash"].isin(conflicts)].drop_duplicates("text_hash").copy()
    if len(d) < 100:
        raise ValueError("Insufficient eligible matter texts for a robust benchmark.")
    facts = {
        "input_rows": input_rows, "cohort_rows": subset_rows,
        "rows_after_text_filter": after_text_filter,
        "duplicate_text_rows_before_conflict_filter": duplicates_all,
        "conflicting_identical_text_label_clusters": len(conflicts),
        "all_rows_removed_from_conflicting_label_clusters": conflict_rows,
        "duplicate_matter_keys_before_cleaning": duplicated_matter_keys,
        "eligible_rows_after_cleaning": len(d),
        "issuer_count": int(d[schema["issuer"]].nunique()),
        "original_source_topic_count": int(d[schema["topic"]].nunique()),
    }
    return d, schema, facts


def group_split(d, issuer, seed):
    splitter = GroupShuffleSplit(n_splits=1, test_size=.15, random_state=seed)
    a, test = next(splitter.split(d, groups=d[issuer]))
    remain, heldout = d.iloc[a].copy(), d.iloc[test].copy()
    splitter2 = GroupShuffleSplit(
        n_splits=1, test_size=.15/.85, random_state=seed+1)
    train, val = next(splitter2.split(remain, groups=remain[issuer]))
    parts = (remain.iloc[train].copy(), remain.iloc[val].copy(), heldout)
    issuers = [set(x[issuer]) for x in parts]
    hashes = [set(x["text_hash"]) for x in parts]
    for groups in (issuers, hashes):
        if groups[0] & groups[1] or groups[0] & groups[2] or groups[1] & groups[2]:
            raise AssertionError("Issuer or exact-text contamination across splits.")
    return parts


def execute(path: Path, source: str, output: Path,
            seed=42, min_train_support=100, max_features=50000,
            save_private_pipeline: Path | None = None, text_mode="title_plus_description"):
    start = time.monotonic()
    d, schema, facts = load_clean(path, source)
    if text_mode == "description_only":
        # IMPORTANT: global cleaning/dedup has already used TITLE+DESCRIPTION.
        # Retains identical issuer splits; description-only exact/near overlap
        # requires an additional validation before publication.
        d["text"] = d["DESCRIPTION"].copy()
    elif text_mode != "title_plus_description":
        raise ValueError("Unsupported text_mode")
    train, val, test = group_split(d, schema["issuer"], seed)
    counts = train[schema["topic"]].value_counts()
    frequent = set(counts[counts >= min_train_support].index)
    if len(frequent) < 2:
        raise ValueError("At least two common topic classes are necessary.")
    def labels(frame):
        return frame[schema["topic"]].where(
            frame[schema["topic"]].isin(frequent), other="OTHER_RARE").astype(str)
    yt, yv, ys = labels(train), labels(val), labels(test)
    names = sorted(set(yt) | set(yv) | set(ys))
    clf = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2,
                                  max_df=.97, max_features=max_features,
                                  sublinear_tf=True, strip_accents="unicode",
                                  dtype=np.float32)),
        ("classifier", LinearSVC(class_weight="balanced",
                                random_state=seed, max_iter=2500, dual="auto")),
    ])
    clf.fit(train["text"].astype(str).tolist(), yt.tolist())
    vp = clf.predict(val["text"].astype(str).tolist())
    sp = clf.predict(test["text"].astype(str).tolist())
    report = classification_report(ys, sp, labels=names,
                                   zero_division=0, output_dict=True)
    metrics = {
        "accuracy": float(accuracy_score(ys, sp)),
        "macro_f1": float(f1_score(ys, sp, labels=names,
                                   average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(ys, sp, labels=names,
                                      average="weighted", zero_division=0)),
        "balanced_accuracy": float(balanced_accuracy_score(ys, sp)),
        "validation_macro_f1": float(f1_score(yv, vp, labels=names,
                                              average="macro", zero_division=0)),
        "other_rare_f1": float(report.get("OTHER_RARE", {}).get("f1-score", 0)),
    }
    splitnames = ("train", "validation", "test")
    facts.update({
        "status": "REAL_PRIVATE_TFIDF_SVM_TRAINED_NOT_FINBERT",
        "source": source,
        "input_text_mode": text_mode,
        "description_only_split_text_leakage_verified": False,
        "source_sha256": sha256_file(path),
        "python": sys.version.split()[0],
        "sklearn": sklearn.__version__,
        "seed": seed,
        "min_training_class_support": min_train_support,
        "common_training_topic_classes": len(frequent),
        "classes_with_other_rare": len(names),
        "split_rows": {n: len(x) for n, x in zip(splitnames, (train, val, test))},
        "split_issuers": {
            n: int(x[schema["issuer"]].nunique())
            for n, x in zip(splitnames, (train, val, test))},
        "split_issuer_set_sha256": {
            n: hashlib.sha256("\n".join(sorted(x[schema["issuer"]].astype(str).unique())).encode()).hexdigest()
            for n, x in zip(splitnames, (train, val, test))},
        "other_rare_counts": {
            n: int((labels(x) == "OTHER_RARE").sum())
            for n, x in zip(splitnames, (train, val, test))},
        "metrics": metrics,
        "per_class_test_metrics": {
            n: {k: (int(v) if k == "support" else float(v))
                for k, v in cls.items()}
            for n, cls in report.items() if isinstance(cls, dict)},
        "elapsed_seconds": round(time.monotonic() - start, 2),
        "date_join_verified": False,
        "jurisdiction_verified_as_UK_audit_standard": False,
        "issuer_disjoint": True,
        "exact_text_disjoint": True,
        "semantic_near_duplicate_leakage_checked": False,
        "status_note": ("UK cohort is headquartered-GB proxy; no report-year or formal "
                        "UK audit-jurisdiction verification. Internal unreviewed research "
                        "baseline; no neural model has been trained."),
    })
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding="utf-8")
    if save_private_pipeline is not None:
        # Only use an access-controlled user-approved private Drive location:
        import joblib
        save_private_pipeline.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(clf, save_private_pipeline, compress=3)
    print(json.dumps({
        "source": source, "status": facts["status"],
        "cleaned_rows": facts["eligible_rows_after_cleaning"],
        "splits": facts["split_rows"], "metrics": metrics
    }, indent=2))
    return facts


def self_test():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp:
        p = Path(tmp) / "CAM.csv"
        rows = []
        for i in range(140):
            rows.append({
                "TITLE": "Goodwill" if i % 2 == 0 else "Inventory",
                "DESCRIPTION": f"Audit {i} discusses " +
                    ("impairment and discounted goodwill value" if i % 2 == 0
                     else "inventory obsolescence valuation allowances"),
                "TOPIC_NAME": "Goodwill" if i % 2 == 0 else "Inventory",
                "COMPANY_FKEY": f"{i:010d}",
                "CRITICAL_AUDIT_MATTER_KEY": str(i),
                "AUDIT_OPINION_FKEY": str(i),
            })
        pd.DataFrame(rows).to_csv(p, index=False)
        f = execute(p, "us_cam", Path(tmp)/"report.json",
                    min_train_support=1, max_features=300)
        assert f["issuer_disjoint"] and f["exact_text_disjoint"]
        assert f["metrics"]["macro_f1"] >= 0
        g = execute(p, "us_cam", Path(tmp)/"description_only.json",
                    min_train_support=1, max_features=300,
                    text_mode="description_only")
        assert g["input_text_mode"] == "description_only"
        print("PASS: fully synthetic, no private data.")


def main():
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument("--input", type=Path)
    a.add_argument("--source", choices=FIELDS)
    a.add_argument("--output", type=Path)
    a.add_argument("--seed", type=int, default=42)
    a.add_argument("--min-train-support", type=int, default=100)
    a.add_argument("--max-features", type=int, default=50000)
    a.add_argument("--text-mode", choices=("title_plus_description", "description_only"),
                   default="title_plus_description")
    a.add_argument("--save-private-pipeline", type=Path,
                   help="Optional PRIVATE Drive path, never public GitHub or Hub")
    a.add_argument("--self-test", action="store_true")
    x = a.parse_args()
    if x.self_test:
        self_test()
        return
    if x.input is None or x.source is None or x.output is None:
        a.error("--input, --source and --output are required")
    execute(x.input, x.source, x.output, x.seed, x.min_train_support,
            x.max_features, x.save_private_pipeline, x.text_mode)


if __name__ == "__main__":
    main()
