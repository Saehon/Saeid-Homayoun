"""Offline, provider-neutral comparative evaluation with explicit evidence boundaries.

Uses the existing deterministic financial-evidence scorer. No external API calls.
All scores computed on synthetic fixtures are labelled NON-EMPIRICAL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from research.ai_evidence_evaluation.evaluate import (
    index_records, load_jsonl, run_evaluation, validate_reference
)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require_nonempty(row, keys, context):
    for key in keys:
        if not isinstance(row.get(key), str) or not row[key].strip():
            raise ValueError(f"{context}: missing {key}")


def resolve_case_path(base, name):
    # All paths must remain below the manifest directory. Prevents accidental
    # reading of private files from a public demo command.
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("manifest paths must be nonempty and relative")
    resolved = (base / name).resolve()
    if not resolved.is_relative_to(base.resolve()):
        raise ValueError("manifest path escapes manifest directory")
    if not resolved.is_file():
        raise ValueError(f"missing input file: {name}")
    return resolved


def validate_manifest(manifest):
    if manifest.get("schema_version") != "1.0":
        raise ValueError("unsupported schema_version")
    if manifest.get("evaluation_class") != "synthetic":
        raise ValueError("public example requires evaluation_class=synthetic")
    require_nonempty(manifest, ("reference_path", "rights_statement"), "manifest")
    runs = manifest.get("runs")
    if not isinstance(runs, list) or len(runs) < 2:
        raise ValueError("must compare at least two model/run records")
    seen = set()
    for row in runs:
        if not isinstance(row, dict):
            raise ValueError("run must be an object")
        require_nonempty(
            row, ("run_id", "provider", "model_id", "model_version",
                  "predictions_path", "source_type"), "run"
        )
        if row["run_id"] in seen:
            raise ValueError("duplicate run_id")
        seen.add(row["run_id"])
        if row["source_type"] != "synthetic_fixture":
            raise ValueError("this public demo cannot certify real model outputs")
        if row["provider"] not in ("synthetic", "openai", "anthropic", "google", "other"):
            raise ValueError("unrecognized provider label")


def by_domain(gold, records):
    summary = {}
    for item in records:
        domain = gold[item["case_id"]]["domain"]
        row = summary.setdefault(domain, {"n": 0, "answered": 0,
                                          "correct": 0, "grounded": 0})
        row["n"] += 1
        row["answered"] += int(item["answered"])
        row["correct"] += int(item["answer_correct"])
        row["grounded"] += int(item["grounded_correct"])
    for row in summary.values():
        row["answer_accuracy_all_cases"] = round(row["correct"] / row["n"], 5)
        row["grounded_correct_rate"] = round(row["grounded"] / row["n"], 5)
    return summary


def pairwise(records_a, records_b):
    a = {x["case_id"]: x for x in records_a}
    b = {x["case_id"]: x for x in records_b}
    if set(a) != set(b):
        raise ValueError("different case IDs across runs")
    out = {"a_better_grounded": 0, "b_better_grounded": 0, "tie": 0}
    for key in a:
        x = bool(a[key]["grounded_correct"])
        y = bool(b[key]["grounded_correct"])
        if x and not y:
            out["a_better_grounded"] += 1
        elif y and not x:
            out["b_better_grounded"] += 1
        else:
            out["tie"] += 1
    return out


def compare(manifest, manifest_dir):
    validate_manifest(manifest)
    base = Path(manifest_dir).resolve()
    gold_path = resolve_case_path(base, manifest["reference_path"])
    gold_rows = load_jsonl(gold_path)
    gold = index_records(gold_rows, "gold")
    for row in gold.values():
        validate_reference(row)
        if row.get("source_rights") != "original_synthetic_data":
            raise ValueError("demo uses only original_synthetic_data")
        if row.get("label_provenance", "").startswith("independent"):
            raise ValueError("cannot certify independent labels through fixtures")
    report = {
        "evaluation_class": "SYNTHETIC_CONTRACT_ONLY",
        "empirical_model_benchmark": False,
        "real_model_inference": False,
        "independent_gold_validation": False,
        "human_review_complete": False,
        "reference_sha256": digest(gold_path),
        "reference_count": len(gold_rows),
        "source_rights": manifest["rights_statement"],
        "run_summaries": [],
        "paired": [],
        "interpretation_limitations": [
            "Fixture predictions are handwritten; results are not GPT, Claude or Gemini performance.",
            "Case labels are not blinded; n is insufficient for inference.",
            "Evidence-ID equality is not document entailment or professional assurance.",
            "Model tags are user-provided metadata; this script never authenticates API provenance.",
            "No confidence intervals, significance claims or deployment readiness may be inferred."
        ],
    }
    scored = []
    for run in manifest["runs"]:
        path = resolve_case_path(base, run["predictions_path"])
        predictions = load_jsonl(path)
        results = run_evaluation(gold_rows, predictions)["records"]
        summary = run_evaluation(gold_rows, predictions)["summary"]
        scored.append((run["run_id"], results))
        report["run_summaries"].append({
            "run_id": run["run_id"],
            "provider": run["provider"],
            "model_id": run["model_id"],
            "model_version": run["model_version"],
            "source_type": "synthetic_fixture",
            "predictions_sha256": digest(path),
            "summary": summary,
            "domain_breakdown": by_domain(gold, results),
            "failure_cases": [
                {"case_id": row["case_id"], "status": row["status"]}
                for row in results if row["status"] != "passed_synthetic_contract"
            ],
        })
    for i in range(len(scored)):
        for j in range(i+1, len(scored)):
            label_a, rows_a = scored[i]
            label_b, rows_b = scored[j]
            report["paired"].append({
                "a": label_a, "b": label_b,
                "comparison": pairwise(rows_a, rows_b)
            })
    return report


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(
        here / "examples" / "synthetic_comparison_manifest.json"))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    result = compare(manifest, manifest_path.resolve().parent)
    result["manifest_sha256"] = digest(manifest_path)
    body = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        print(f"Wrote synthetic comparative report to {target}")
    else:
        print(body)


if __name__ == "__main__":
    main()
