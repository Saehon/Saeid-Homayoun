#!/usr/bin/env python3
"""DARWIN–AuditBERT: gated release of verified private FinBERT weights to SADHON.

NO automatic publishing. The default is local dry-run and requires no HF token.
Only independently trained, frozen issuer-split final checkpoints can pass the
preflight. Never copy licensed CAM/KAM text, original KAM notebooks, identifiers,
dataset CSV/Parquet/SQLite or token files to Hugging Face.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path

MODEL_FILES = {
    "config.json", "generation_config.json", "model.safetensors",
    "pytorch_model.bin", "tokenizer.json", "tokenizer_config.json",
    "special_tokens_map.json", "vocab.txt", "merges.txt",
    "sentencepiece.bpe.model", "added_tokens.json",
}
TARGETS = {
    "us_cam": "SADHON/saeid-finbert-cam-v2",
    "uk_hq_kam": "SADHON/saeid-finbert-kam-v2",
    # Independently trained CAM and UK-HQ KAM checkpoints NEVER share a Hub repo.
}
EXPECTED_STATUSES = {"TRAINED_AND_HELDOUT_EVALUATED"}


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for part in iter(lambda: fp.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()


def verify_private_checkpoint(root: Path, cohort: str):
    if cohort not in TARGETS:
        raise ValueError("Cohort has no independently approved private model target.")
    report_path = root / "experiment_report.json"
    weights = root / "model"
    if not report_path.is_file() or not weights.is_dir():
        raise FileNotFoundError("Missing final training report or model directory")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if (report.get("status") not in EXPECTED_STATUSES
            or report.get("evaluation_mode") != "heldout_test"
            or report.get("split") != "frozen"
            or not report.get("issuer_disjoint_for_frozen")
            or not report.get("sample_is_trained")
            or int(report.get("train_limit", 0)) != 0
            or not isinstance(report.get("test_results"), dict)
            or not report["test_results"]):
        raise ValueError("Only full, frozen issuer-disjoint models with measured "
                         "heldout results pass. No pilot/model-card placeholders.")
    if not (weights / "config.json").is_file():
        raise ValueError("Missing model config.json")
    found = [p for p in weights.iterdir() if p.is_file()]
    if not found:
        raise ValueError("Empty model directory")
    disallowed = [p.name for p in found if p.name not in MODEL_FILES]
    # Explicit strict allowlist: do not blindly upload arbitrary files.
    if disallowed:
        raise ValueError("Unexpected private checkpoint artifacts: " + ", ".join(sorted(disallowed)))
    viable_weights = [p for p in found if p.name in {"model.safetensors", "pytorch_model.bin"}]
    if len(viable_weights) != 1 or viable_weights[0].stat().st_size < 1024:
        raise ValueError("Expected exactly one nonempty model weight file")
    digest = sha256_file(viable_weights[0])
    return {
        "repo_id": TARGETS[cohort], "model_dir": str(weights),
        "file_names": sorted(p.name for p in found),
        "weight_sha256": digest,
        "status": "LOCAL_VALIDATION_ONLY_NOT_UPLOADED",
        "training_status": report["status"], "split": report["split"],
        "trained_records": report["split_rows"].get("train"),
        "test_records": report["split_rows"].get("test"),
        "source_licensed_data_uploaded": False,
    }


def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as temp:
        p = Path(temp)
        (p / "model").mkdir()
        (p / "model" / "config.json").write_text('{"model_type":"bert"}')
        (p / "model" / "model.safetensors").write_bytes(b"0" * 2048)
        good = {
            "status": "TRAINED_AND_HELDOUT_EVALUATED", "split": "frozen",
            "evaluation_mode": "heldout_test", "issuer_disjoint_for_frozen": True,
            "sample_is_trained": True, "train_limit": 0,
            "split_rows": {"train": 100, "validation": 20, "test": 20},
            "test_results": {"test_macro_f1": 0.5}
        }
        (p / "experiment_report.json").write_text(json.dumps(good))
        assert verify_private_checkpoint(p, "us_cam")["repo_id"] == TARGETS["us_cam"]
        (p / "model" / "CAM.csv").write_text("private data")
        try:
            verify_private_checkpoint(p, "us_cam")
        except ValueError:
            pass
        else:
            raise AssertionError("Unsafe file guard FAILED")
        (p / "model" / "CAM.csv").unlink()
        good["status"] = "PILOT_TRAINED_VALIDATION_ONLY"
        (p / "experiment_report.json").write_text(json.dumps(good))
        try:
            verify_private_checkpoint(p, "us_cam")
        except ValueError:
            pass
        else:
            raise AssertionError("Pilot release gate FAILED")
        print("PASS: fully synthetic Hugging Face checkpoint gates; no internet, token or upload.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path)
    p.add_argument("--cohort", choices=sorted(TARGETS), default="us_cam")
    p.add_argument("--rights-attested", action="store_true",
                   help="Explicitly attest legal authorization for derivative weights release")
    p.add_argument("--approve-private-upload", action="store_true",
                   help="Explicit external private Hugging Face weight transfer approval")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return
    if args.checkpoint is None:
        p.error("--checkpoint private/final/model-parent is required")
    manifest = verify_private_checkpoint(args.checkpoint, args.cohort)
    if not (args.rights_attested and args.approve_private_upload):
        print(json.dumps(manifest, indent=2))
        print("DRY RUN ONLY: to upload independently trained derived weights, supply "
              "BOTH rights and private-upload attestations after owner review.")
        return
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise PermissionError("Missing HF_TOKEN in runtime secret environment. "
                              "Never paste secret values into notebook cells.")
    from huggingface_hub import HfApi
    api = HfApi(token=token)
    name = api.whoami().get("name", "")
    if name.lower() != "sadhon":
        raise PermissionError("HF_TOKEN is not for SADHON.")
    details = api.repo_info(repo_id=manifest["repo_id"], repo_type="model")
    if not details.private:
        raise PermissionError("Destination Hugging Face repository is NOT private. Abort.")
    model_dir = Path(manifest["model_dir"])
    api.upload_folder(
        repo_id=manifest["repo_id"], repo_type="model",
        folder_path=str(model_dir),
        allow_patterns=manifest["file_names"],
        commit_message="DARWIN-AuditBERT: verified independently trained US CAM checkpoint",
    )
    actual = set(api.list_repo_files(repo_id=manifest["repo_id"], repo_type="model"))
    if not {"config.json", "model.safetensors"}.issubset(actual) and not {
        "config.json", "pytorch_model.bin"}.issubset(actual):
        raise RuntimeError("Hub readback missing required trained checkpoint files")
    print(json.dumps({
        "status": "PRIVATE_HF_MODEL_UPLOAD_VERIFIED",
        "hub": "https://huggingface.co/" + manifest["repo_id"],
        "uploaded_files": manifest["file_names"],
        "source_private_disclosures_included": False,
    }, indent=2))


if __name__ == "__main__":
    main()
