"""Offline, strictly synthetic human-judgment calibration protocol.

Two simulated reviewers annotate answer-evidence support. This measures the
annotation *software contract*, not actual expert independence or model quality.
Requires stdlib Python 3.11+. No network or external data.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

from research.ai_evidence_evaluation.compare_runs import resolve_case_path
from research.ai_evidence_evaluation.evaluate import index_records, load_jsonl

LABELS = ("supported", "contradicted", "insufficient_evidence")
SOURCE_CLASS = "synthetic_fixture"
DEFAULT_FILES = Path(__file__).resolve().parent / "examples"


def text_field(obj, name):
    value = obj.get(name)
    if not isinstance(value, str) or not value.strip() or len(value) > 1000:
        raise ValueError(f"{name}: missing, empty, or too long")
    return value


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_panel(config):
    if not isinstance(config, dict) or config.get("schema_version") != "1.0":
        raise ValueError("unsupported annotation manifest")
    if config.get("evaluation_class") != SOURCE_CLASS:
        raise ValueError("only synthetic fixture records supported")
    for field in ("gold_path", "annotations_path", "resolutions_path",
                  "rights_statement"):
        text_field(config, field)
    if config["rights_statement"] != "original_synthetic_data":
        raise ValueError("public demo rights must be original_synthetic_data")
    people = config.get("reviewers")
    adjudicator = config.get("adjudicator")
    if (not isinstance(people, list) or len(people) != 2
            or not isinstance(adjudicator, dict)):
        raise ValueError("exactly two simulated reviewers and an adjudicator are required")
    ids = []
    for reviewer in people + [adjudicator]:
        if not isinstance(reviewer, dict):
            raise ValueError("invalid reviewer entry")
        ids.append(text_field(reviewer, "reviewer_id"))
        if reviewer.get("source_type") != SOURCE_CLASS:
            raise ValueError("cannot claim independently validated human reviewers")
    if len(set(ids)) != 3:
        raise ValueError("reviewer and adjudicator IDs must be distinct")
    return tuple(ids)


def validate_annotations(rows, case_ids, reviewer_ids, gold):
    expected = {(case, reviewer) for case in case_ids for reviewer in reviewer_ids}
    observed = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("annotation must be an object")
        case = text_field(row, "case_id")
        reviewer = text_field(row, "reviewer_id")
        if (case, reviewer) not in expected:
            raise ValueError("unknown case or reviewer")
        if (case, reviewer) in observed:
            raise ValueError("duplicate (case, reviewer) annotation")
        if row.get("support_label") not in LABELS:
            raise ValueError("invalid evidence-support label")
        text_field(row, "rationale")
        evidence = row.get("evaluated_evidence_ids")
        allowed = gold[case]["evidence_ids"]
        if not isinstance(evidence, list) or not all(
            isinstance(x, str) and x in allowed for x in evidence
        ) or len(set(evidence)) != len(evidence):
            raise ValueError("evidence IDs must be unique and from gold reference")
        observed[(case, reviewer)] = row
    if set(observed) != expected:
        raise ValueError("incomplete two-reviewer annotation panel")
    return observed


def validate_resolutions(rows, disagreements, adjudicator_id):
    resolutions = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("resolution must be an object")
        case = text_field(row, "case_id")
        if case in resolutions or case not in disagreements:
            raise ValueError("resolution duplicate or case not disputed")
        if row.get("adjudicator_id") != adjudicator_id:
            raise ValueError("invalid adjudicator")
        if row.get("final_support_label") not in LABELS:
            raise ValueError("invalid adjudicated label")
        text_field(row, "adjudication_reason")
        resolutions[case] = row
    if set(resolutions) != disagreements:
        raise ValueError("all and only disputed cases require an adjudication")
    return resolutions


def agreement_metrics(rows, case_ids, a_id, b_id):
    n = len(case_ids)
    if n < 1:
        raise ValueError("empty panel")
    counts_a = {k: 0 for k in LABELS}
    counts_b = {k: 0 for k in LABELS}
    matrix = {k: {other: 0 for other in LABELS} for k in LABELS}
    agreements = 0
    conflicts = []
    for case in case_ids:
        label_a = rows[(case, a_id)]["support_label"]
        label_b = rows[(case, b_id)]["support_label"]
        counts_a[label_a] += 1
        counts_b[label_b] += 1
        matrix[label_a][label_b] += 1
        agreements += int(label_a == label_b)
        if label_a != label_b:
            conflicts.append(case)
    observed = agreements / n
    chance = sum(counts_a[label] * counts_b[label] for label in LABELS) / (n * n)
    kappa = None if chance == 1 else round((observed - chance) / (1 - chance), 6)
    return {
        "n_cases": n, "n_reviewer_records": 2 * n,
        "n_agreements": agreements,
        "raw_agreement": round(observed, 6),
        "cohens_kappa": kappa,
        "kappa_limitation": "undefined if expected agreement equals one" if kappa is None else None,
        "reviewer_a_label_counts": counts_a, "reviewer_b_label_counts": counts_b,
        "confusion_matrix_a_by_b": matrix,
        "disputed_case_ids": sorted(conflicts),
    }


def audit(manifest, base):
    a_id, b_id, adj_id = validate_panel(manifest)
    root = Path(base)
    gold_file = resolve_case_path(root, manifest["gold_path"])
    annotations_file = resolve_case_path(root, manifest["annotations_path"])
    resolution_file = resolve_case_path(root, manifest["resolutions_path"])
    gold_rows = load_jsonl(gold_file)
    gold = index_records(gold_rows, "gold")
    for case in gold.values():
        if case.get("source_rights") != "original_synthetic_data":
            raise ValueError("only original synthetic references permitted")
    annotations = validate_annotations(
        load_jsonl(annotations_file), list(gold), (a_id, b_id), gold
    )
    metrics = agreement_metrics(annotations, list(gold), a_id, b_id)
    resolutions = validate_resolutions(
        load_jsonl(resolution_file), set(metrics["disputed_case_ids"]), adj_id
    ) if metrics["disputed_case_ids"] else {}
    if not metrics["disputed_case_ids"] and resolution_file.read_text(encoding="utf-8").strip():
        raise ValueError("no resolutions allowed without disagreements")
    metrics["n_adjudicated"] = len(resolutions)
    metrics["adjudication_coverage_of_disagreements"] = (
        1.0 if not metrics["disputed_case_ids"]
        else round(len(resolutions) / len(metrics["disputed_case_ids"]), 6)
    )
    metrics["final_label_counts"] = {label: 0 for label in LABELS}
    for case in gold:
        label = (resolutions[case]["final_support_label"] if case in resolutions
                 else annotations[(case, a_id)]["support_label"])
        metrics["final_label_counts"][label] += 1
    return {
        "evaluation_class": "SYNTHETIC_ANNOTATION_CONTRACT_ONLY",
        "actual_independent_human_review_verified": False,
        "model_evaluation_completed": False,
        "source_document_entailment_independently_verified": False,
        "source_files_sha256": {
            "gold": digest(gold_file), "annotations": digest(annotations_file),
            "adjudications": digest(resolution_file),
        },
        "summary": metrics,
        "limitations": [
            "Reviewers are simulated identifiers, not independent human experts.",
            "Synthetic adjudication demonstrates software control flow, not scientific validation.",
            "Cohen kappa is descriptive on a five-case constructed toy set; do not generalize.",
            "Evidence ID validation checks membership only, never factual entailment.",
            "No real GPT, Claude, Gemini, or other model was called.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(DEFAULT_FILES / "annotation_manifest.json"))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    report = audit(manifest, manifest_path.resolve().parent)
    report["manifest_sha256"] = digest(manifest_path)
    result = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result, encoding="utf-8")
        print("Wrote simulated annotation audit to", output)
    else:
        print(result)


if __name__ == "__main__":
    main()
