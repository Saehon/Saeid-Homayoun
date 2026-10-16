"""Installable, local synthetic CAM + MLflow smoke test. No real Drive data."""
import argparse
import tempfile
from pathlib import Path
import numpy as np
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss
from sklearn.model_selection import train_test_split

def run(tracking_dir=None):
    rng = np.random.default_rng(20261015)
    n = 240
    risk = rng.normal(size=n)
    industry = rng.integers(0, 3, n)
    domain = rng.integers(0, 3, n)
    p = 1 / (1 + np.exp(-(-0.7 + .8*risk + .2*(industry == 1) + .3*(domain == 2))))
    y = rng.binomial(1, p)
    x = np.column_stack([risk, industry == 1, industry == 2, domain == 1, domain == 2])
    xtr, xte, ytr, yte = train_test_split(x, y, test_size=.3, random_state=42, stratify=y)
    model = LogisticRegression(max_iter=1000).fit(xtr, ytr)
    pred = model.predict_proba(xte)[:, 1]
    metrics = {"brier": float(brier_score_loss(yte, pred)),
               "pr_auc": float(average_precision_score(yte, pred))}
    root = Path(tracking_dir) if tracking_dir else Path(tempfile.mkdtemp(prefix="jev_cam_mlflow_"))
    root.mkdir(parents=True, exist_ok=True)
    # MLflow 3.17+ defaults away from the legacy filesystem store.
    # Use a local SQLite backend so the synthetic run works on current CI.
    mlflow.set_tracking_uri('sqlite:///' + (root / 'mlflow.db').resolve().as_posix())
    mlflow.set_experiment("synthetic_cam_pipeline_only")
    with mlflow.start_run(run_name="rad_cam_baseline_smoke"):
        mlflow.log_params({"model":"logistic_regression","dataset":"SYNTHETIC",
                           "stage":"CAM","seed":20261015})
        mlflow.log_metrics(metrics)
    print("SYNTHETIC ONLY:", metrics)
    print("MLflow tracking:", root)
    return metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracking-dir", default=None)
    args = parser.parse_args()
    assert all(0 <= v <= 1 for v in run(args.tracking_dir).values())
