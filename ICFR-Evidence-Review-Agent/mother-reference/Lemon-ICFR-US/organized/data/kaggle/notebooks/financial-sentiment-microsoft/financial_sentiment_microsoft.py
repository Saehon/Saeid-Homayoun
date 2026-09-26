"""Reproducible finance sentiment baseline with a Microsoft SEC demonstration.

The labeled finance-text CSVs belong to the authors credited in the linked
reference repository. This script does not republish their source sentences.
"""

import hashlib
import io
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

import joblib
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.pipeline import make_pipeline


REFERENCE_REPO = "Saehon/Financial-Sentiment-Analysis-and-Classification-Deep-Learning-Models"
REFERENCE_COMMIT = "0654984510e6a8ed15e89dd901b8328836cd7930"
MICROSOFT_REPO = "Saehon/Saeid-Homayoun"
MICROSOFT_SHA256 = "b0fc573642135624b8f87fc4fb25cea6ce6992d617f0d36301ec2b51f7c20631"
DATA_SHA256 = {
    "train": "c529274ec7e458968c9d17638379b638ae4eb8b74691045975549800b2a7cfa3",
    "validation": "21f847c0338ca1749f6ce2b22086e07a56e9059beb22413c3380bf0a11c5dc21",
    "test": "e644aa70bec487dcfb4cb06d7158efed22f9f79eadd1f4c2e6f0c0f3928c4db9",
}
LABELS = ["negative", "neutral", "positive"]


def verified_csv(name: str) -> pd.DataFrame:
    """Load a pinned GitHub reference CSV or an identical local copy."""
    filename = f"{name}_set.csv"
    local_dir = os.environ.get("FINANCE_DATA_DIR")
    if local_dir:
        content = (Path(local_dir) / filename).read_bytes()
    else:
        url = (
            "https://raw.githubusercontent.com/"
            f"{REFERENCE_REPO}/{REFERENCE_COMMIT}/Datasets/{filename}"
        )
        request = Request(url, headers={"User-Agent": "research-replication/1.0"})
        with urlopen(request, timeout=45) as response:
            content = response.read()
    digest = hashlib.sha256(content).hexdigest()
    if digest != DATA_SHA256[name]:
        raise ValueError(f"Checksum mismatch for {filename}; expected pinned source")
    frame = pd.read_csv(io.BytesIO(content), usecols=["id", "Sentence", "Sentiment"])
    frame = frame.dropna(subset=["Sentence", "Sentiment"]).copy()
    frame = frame[frame["Sentiment"].isin(LABELS)].copy()
    frame["text_key"] = (
        frame["Sentence"].str.lower().str.replace(r"\s+", " ", regex=True).str.strip()
    )
    return frame[frame["text_key"].ne("")].copy()


def clean_splits(frames: dict[str, pd.DataFrame]):
    """Keep one label per text, with disjoint evaluation text across splits."""
    cleaned = {}
    counts = {}
    seen = set()
    for name in ("train", "validation", "test"):
        raw = frames[name]
        label_count = raw.groupby("text_key")["Sentiment"].nunique()
        conflicts = set(label_count[label_count > 1].index)
        without_conflicts = raw[~raw["text_key"].isin(conflicts)]
        without_overlap = without_conflicts[~without_conflicts["text_key"].isin(seen)]
        clean = without_overlap.drop_duplicates("text_key").copy()
        counts[name] = {
            "raw_rows": len(raw),
            "contradictory_text_keys_within_split": len(conflicts),
            "rows_removed_for_conflict": len(raw) - len(without_conflicts),
            "rows_removed_for_earlier_split_overlap": len(without_conflicts) - len(without_overlap),
            "rows_removed_for_duplicate_text": len(without_overlap) - len(clean),
            "clean_rows": len(clean),
            "class_counts": {label: int((clean["Sentiment"] == label).sum()) for label in LABELS},
        }
        if not set(LABELS).issubset(set(clean["Sentiment"])):
            raise ValueError(f"Clean {name} split lacks at least one class")
        cleaned[name] = clean
        # Reserve even excluded contradictory texts, preventing any evaluation
        # of a text seen in an earlier split.
        seen.update(raw["text_key"])
    return cleaned, counts


def evaluate(model, frame: pd.DataFrame) -> dict:
    true = frame["Sentiment"].to_numpy()
    predicted = model.predict(frame["Sentence"])
    return {
        "accuracy": round(float(accuracy_score(true, predicted)), 4),
        "macro_f1": round(float(f1_score(true, predicted, labels=LABELS, average="macro")), 4),
        "confusion_matrix_rows_true_cols_predicted": confusion_matrix(
            true, predicted, labels=LABELS
        ).tolist(),
    }


def microsoft_examples(model, output_dir: Path) -> None:
    local = os.environ.get("MICROSOFT_CSV")
    source = Path(local) if local else Path(
        "/kaggle/input/microsoft-accounting-demo-sec-10k/microsoft_financials.csv"
    )
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != MICROSOFT_SHA256:
        raise ValueError("Microsoft CSV differs from the canonical GitHub snapshot")
    rows = pd.read_csv(io.BytesIO(data)).sort_values("fiscal_year")
    if len(rows) != 3 or rows["fiscal_year"].tolist() != [2024, 2025, 2026]:
        raise ValueError("Expected the three-year Microsoft SEC demonstration")
    examples = []
    for prior, current in zip(rows.iloc[:-1].itertuples(), rows.iloc[1:].itertuples()):
        growth = 100 * (current.revenue_musd / prior.revenue_musd - 1)
        direction = "increased" if growth >= 0 else "decreased"
        sentence = (
            f"Microsoft revenue {direction} by {abs(growth):.1f} percent in fiscal "
            f"{current.fiscal_year} compared with fiscal {prior.fiscal_year}."
        )
        examples.append({"fiscal_year": current.fiscal_year,
                         "revenue_musd": current.revenue_musd,
                         "revenue_growth_percent": round(growth, 2),
                         "generated_example_text": sentence})
    result = pd.DataFrame(examples)
    result["illustrative_text_prediction"] = model.predict(result["generated_example_text"])
    result.to_csv(output_dir / "microsoft_generated_examples.csv", index=False)
    print("Microsoft examples (generated from the SEC-sourced numbers; not filing quotations):")
    print(result[["fiscal_year", "revenue_growth_percent", "illustrative_text_prediction"]].to_string(index=False))


def main() -> None:
    output_dir = Path(os.environ.get("MODEL_OUTPUT_DIR", "/kaggle/working"))
    output_dir.mkdir(parents=True, exist_ok=True)
    frames = {name: verified_csv(name) for name in ("train", "validation", "test")}
    split, counts = clean_splits(frames)
    train, validation, test = (split[name] for name in ("train", "validation", "test"))

    model = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=20000, sublinear_tf=True),
        LogisticRegression(C=1.0, max_iter=1200, random_state=42),
    )
    model.fit(train["Sentence"], train["Sentiment"])
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(train["Sentence"], train["Sentiment"])
    metrics = {
        "model": "TF-IDF (1-2 grams) + logistic regression; no hyperparameter tuning",
        "labels_order": LABELS,
        "reference_repo": f"https://github.com/{REFERENCE_REPO}/tree/{REFERENCE_COMMIT}",
        "reference_commit": REFERENCE_COMMIT,
        "source_csv_sha256": DATA_SHA256,
        "microsoft_repo": f"https://github.com/{MICROSOFT_REPO}/tree/main/open-data/microsoft-demo-001",
        "microsoft_csv_sha256": MICROSOFT_SHA256,
        "split_counts": counts,
        "validation": {"model": evaluate(model, validation),
                       "majority_baseline": evaluate(baseline, validation)},
        "test": {"model": evaluate(model, test),
                 "majority_baseline": evaluate(baseline, test)},
        "limitations": "No issuer/date identifiers; no company-held-out or chronological test. Source labels sometimes conflict. Microsoft sentences are generated examples, not labeled evaluation data.",
    }
    (output_dir / "model_metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    predictions = pd.DataFrame({"source_id": test["id"], "true_label": test["Sentiment"],
                                "predicted_label": model.predict(test["Sentence"])})
    predictions.to_csv(output_dir / "test_predictions_no_source_text.csv", index=False)
    joblib.dump(model, output_dir / "financial_sentiment_model.joblib")
    microsoft_examples(model, output_dir)
    print("Clean split sizes:", {name: counts[name]["clean_rows"] for name in counts})
    print("Held-out test:", metrics["test"])
    print("Artifacts:", output_dir)


if __name__ == "__main__":
    main()
