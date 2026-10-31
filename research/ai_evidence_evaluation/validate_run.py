"""Offline provenance validation for research LLM run manifests.

This script validates *declared* model metadata and local file integrity.
It cannot attest that a provider executed a model, a reviewer approved the
result, or that a dataset is lawfully reusable.

Standard-library Python 3.11; no API calls, cloud access or package installs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

from research.ai_evidence_evaluation.compare_runs import resolve_case_path
from research.ai_evidence_evaluation.evaluate import load_jsonl, index_records

HEX64 = re.compile(r"^[0-9a-f]{64}$")
PROVIDERS = {"openai", "anthropic", "google", "other", "synthetic"}
SCHEMA_VERSION = "1.0"


def check_sha256(value, label):
    if not isinstance(value, str) or HEX64.fullmatch(value) is None:
        raise ValueError(f"{label}: expected lowercase 64-character SHA-256")


def required_text(obj, name):
    v = obj.get(name)
    if not isinstance(v, str) or not v.strip() or len(v) > 500:
        raise ValueError(f"{name}: missing, empty, or too long")
    return v


def parse_timestamp(value):
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("run_started_utc must be UTC with Z suffix")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("run_started_utc invalid ISO-8601") from exc
    if dt.utcoffset() != timezone.utc.utcoffset(dt):
        raise ValueError("run_started_utc must use UTC")
    return dt


def nonnegative_number(value, label):
    if type(value) is bool or not isinstance(value, (str, int, float)):
        raise ValueError(f"{label}: must be numeric")
    try:
        n = Decimal(str(value))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError(f"{label}: cannot parse") from exc
    if not n.is_finite() or n < 0:
        raise ValueError(f"{label}: must be finite and nonnegative")
    return n


def nonnegative_int(value, label):
    if type(value) is not int or value < 0:
        raise ValueError(f"{label}: must be a nonnegative integer")
    return value


def sha_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_prediction_record(record):
    if record.get("status") not in ("answered", "abstained", "error"):
        raise ValueError("unknown prediction status")
    if record["status"] == "answered":
        if record.get("model_answer") is None:
            raise ValueError("answered record requires model_answer")
        citations = record.get("cited_evidence_ids")
        if not isinstance(citations, list) or not all(
            isinstance(x, str) and x for x in citations
        ):
            raise ValueError("answered record requires evidence-id list")
    if record["status"] == "error" and record.get("model_answer") is not None:
        raise ValueError("failed request cannot report successful answer")


def validate_record(row, base, allow_observed=False):
    for field in ("run_id", "provider", "model_id", "model_version",
                  "run_started_utc", "predictions_path", "data_rights",
                  "model_configuration_id"):
        required_text(row, field)
    if row["provider"] not in PROVIDERS:
        raise ValueError("invalid provider label")
    kind = row.get("source_type")
    if kind not in ("synthetic_fixture", "declared_provider_output"):
        raise ValueError("source_type is invalid")
    if kind == "synthetic_fixture" and row["provider"] != "synthetic":
        raise ValueError("synthetic fixtures must use provider=synthetic")
    if kind == "declared_provider_output":
        if not allow_observed:
            raise ValueError("provider-output inspection is explicitly opt-in")
        if row["provider"] == "synthetic":
            raise ValueError("declared provider output must name a provider")
        if row.get("data_transfer_authorized") is not True:
            raise ValueError("declared output requires data transfer authorization")
    elif row.get("data_transfer_authorized") is True:
        raise ValueError("fixture must not claim data transfer authorization")

    parse_timestamp(row["run_started_utc"])
    for key in ("predictions_sha256", "prompt_template_sha256",
                "reference_sha256"):
        check_sha256(row.get(key), key)
    for field in ("input_tokens", "output_tokens", "latency_ms"):
        nonnegative_int(row.get(field), field)
    usd = nonnegative_number(row.get("estimated_cost_usd"), "estimated_cost_usd")
    required_text(row, "price_assumption")
    path = resolve_case_path(base, row["predictions_path"])
    if sha_file(path) != row["predictions_sha256"]:
        raise ValueError("predictions digest mismatch")
    records = load_jsonl(path)
    index_records(records, "predictions")
    for record in records:
        validate_prediction_record(record)
    return {
        "run_id": row["run_id"],
        "provider_declared": row["provider"],
        "model_id_declared": row["model_id"],
        "model_version_declared": row["model_version"],
        "run_started_utc": row["run_started_utc"],
        "source_type": kind,
        "n_predictions": len(records),
        "n_answered": sum(r["status"] == "answered" for r in records),
        "n_abstained": sum(r["status"] == "abstained" for r in records),
        "n_errors": sum(r["status"] == "error" for r in records),
        "input_tokens_declared": row["input_tokens"],
        "output_tokens_declared": row["output_tokens"],
        "latency_ms_declared": row["latency_ms"],
        "estimated_cost_usd_declared": str(usd),
        "file_sha256_verified_locally": True,
        "provider_execution_independently_attested": False,
        "data_license_independently_verified": False,
        "human_review_independently_verified": False,
    }


def inspect_manifest(manifest, base, allow_observed=False):
    if not isinstance(manifest, dict) or manifest.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported manifest version")
    required_text(manifest, "study_id")
    required_text(manifest, "study_scope")
    rows = manifest.get("runs")
    if not isinstance(rows, list) or not rows:
        raise ValueError("runs must be a nonempty list")
    ids, results = set(), []
    types = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("run must be an object")
        if row.get("run_id") in ids:
            raise ValueError("duplicate run id")
        ids.add(row.get("run_id"))
        result = validate_record(row, base, allow_observed=allow_observed)
        results.append(result)
        types.add(row["source_type"])
    if len(types) != 1:
        raise ValueError("do not mix synthetic fixtures and claimed model outputs")
    counts = [r["n_predictions"] for r in results]
    return {
        "schema_version": SCHEMA_VERSION,
        "study_id": manifest["study_id"],
        "source_type": next(iter(types)),
        "local_file_integrity_checks_passed": True,
        "records_checked": len(results),
        "run_summaries": results,
        "case_counts_comparable_only": len(set(counts)) == 1,
        "model_performance_claim_permitted": False,
        "independent_validation_status": "NOT_VERIFIED",
        "limitations": [
            "Successful hash/metadata checks do not verify an API response came from a named provider.",
            "Matching case counts do not prove identical case IDs or equivalent prompts.",
            "Local files may contain confidential information and must be permissioned externally.",
            "Human validation of source rights, model outputs and reference labels is required.",
            "No live API call, blind review or accuracy benchmark is performed here.",
        ],
    }


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(here / "examples" / "provenance_manifest.json"))
    parser.add_argument("--out")
    parser.add_argument(
        "--inspect-observed", action="store_true",
        help="Opt in to validating metadata of local declared provider outputs; not attestation"
    )
    args = parser.parse_args()
    path = Path(args.manifest)
    result = inspect_manifest(json.loads(path.read_text(encoding="utf-8")),
                              path.resolve().parent, allow_observed=args.inspect_observed)
    result["manifest_sha256"] = sha_file(path)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload, encoding="utf-8")
        print("Metadata validation report:", target)
    else:
        print(payload)


if __name__ == "__main__":
    main()
