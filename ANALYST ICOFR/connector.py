#!/usr/bin/env python3
"""Read-only service connectors; private inputs and outputs stay outside this repo."""
from __future__ import annotations

import argparse
import contextlib
import csv
import importlib
import importlib.util
import json
import logging
import math
import os
from pathlib import Path
import re
import sys
import tempfile

REPO = Path(__file__).resolve().parent
MODEL_FILES = ["*.safetensors", "config.json", "tokenizer.json", "tokenizer_config.json",
               "special_tokens_map.json", "vocab.*", "merges.txt", "*.model",
               "added_tokens.json", "*.safetensors.index.json", "LICENSE*", "README.md"]


class ConnectorError(Exception):
    """Only fixed, non-sensitive messages may be used here."""


class PrivateArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ConnectorError("Invalid command arguments; consult --help without including credentials.")


def dependency(name: str):
    try:
        return importlib.import_module(name)
    except ImportError:
        raise ConnectorError("Missing dependency; install the documented requirements.") from None


@contextlib.contextmanager
def quiet_service():
    # Third-party progress bars and HTTP exceptions can contain IDs or credentials.
    previous_level = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        with open(os.devnull, "w", encoding="utf-8") as sink:
            with contextlib.redirect_stdout(sink), contextlib.redirect_stderr(sink):
                yield
    finally:
        logging.disable(previous_level)


def private_root(value: str) -> Path:
    root = Path(value).expanduser().resolve()
    if root == REPO or REPO in root.parents or root in REPO.parents:
        raise ConnectorError("Local root must be separate from the code repository.")
    if any((parent / ".git").exists() for parent in (root, *root.parents)):
        raise ConnectorError("Local root must be outside every Git working tree.")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    if os.name == "posix" and root.stat().st_mode & 0o077:
        raise ConnectorError("Local root needs owner-only permissions; apply chmod 700 before use.")
    return root


def local_path(root: Path, value: str, *, must_exist: bool = False) -> Path:
    candidate = Path(value).expanduser()
    path = (candidate if candidate.is_absolute() else root / candidate).resolve()
    if path == root or root not in path.parents:
        raise ConnectorError("Path must be inside the private local root.")
    if must_exist and not path.exists():
        raise ConnectorError("Required local input is missing.")
    if not must_exist and path.exists():
        raise ConnectorError("Destination already exists; choose a new destination.")
    return path


def hf_token() -> str:
    value = os.environ.get("HF_TOKEN", "").strip()
    if not value:
        raise ConnectorError("Set HF_TOKEN in your environment or secret manager.")
    return value


def hf_identity() -> None:
    hub = dependency("huggingface_hub")
    token = hf_token()
    with quiet_service():
        identity = hub.HfApi(token=token).whoami()
    if not isinstance(identity, dict) or not identity.get("name"):
        raise ConnectorError("Hugging Face identity could not be verified.")


def kaggle_api():
    modern = bool(os.environ.get("KAGGLE_API_TOKEN", "").strip())
    legacy = all(os.environ.get(key, "").strip() for key in ("KAGGLE_USERNAME", "KAGGLE_KEY"))
    if not (modern or legacy):
        raise ConnectorError("Set KAGGLE_API_TOKEN or both KAGGLE_USERNAME and KAGGLE_KEY.")
    with quiet_service():
        module = dependency("kaggle.api.kaggle_api_extended")
        api = module.KaggleApi()
        api.authenticate()
    return api


def kaggle_identity() -> None:
    # authenticate() alone loads configuration; this remote read verifies authorization.
    api = kaggle_api()
    with quiet_service():
        api.dataset_list(mine=True, page_size=1)


def check(args) -> None:
    providers = ("hf", "kaggle") if args.provider == "all" else (args.provider,)
    for provider in providers:
        (hf_identity if provider == "hf" else kaggle_identity)()
        print(json.dumps({"provider": provider, "authenticated": True}))


def download_hf(args) -> None:
    if not re.fullmatch(r"[a-fA-F0-9]{40}", args.revision):
        raise ConnectorError("Revision must be the full immutable commit SHA.")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo_id):
        raise ConnectorError("Use an explicit namespace/repository identifier.")
    root = private_root(args.local_root)
    destination = local_path(root, args.destination)
    hub = dependency("huggingface_hub")
    token = hf_token()
    with quiet_service():
        api = hub.HfApi(token=token)
        info = api.repo_info(args.repo_id, repo_type=args.kind, revision=args.revision)
    if str(info.sha).lower() != args.revision.lower():
        raise ConnectorError("Requested revision did not resolve to the expected commit.")
    card = info.card_data
    license_value = card.get("license") if card is not None else None
    licenses = license_value if isinstance(license_value, list) else [license_value]
    if args.accept_license not in licenses or args.accept_license == "other":
        raise ConnectorError("Review the repository license; an exact documented license is required.")
    destination.mkdir(parents=True, mode=0o700)
    with quiet_service():
        hub.snapshot_download(repo_id=args.repo_id, repo_type=args.kind,
                              revision=args.revision, token=token, local_dir=destination,
                              cache_dir=root / ".hf-cache", allow_patterns=MODEL_FILES if args.kind == "model" else None,
                              ignore_patterns=["*.py", "*.pkl", "*.pickle", "*.bin", "*.pt", "*.pth"])
    # Only the private download receives provenance; nothing is written to the code repo.
    metadata = {"provider": "hf", "kind": args.kind, "repo_id": args.repo_id,
                "revision": args.revision, "license": args.accept_license}
    with (destination / ".connector-download.json").open("x", encoding="utf-8") as stream:
        json.dump(metadata, stream)
    print(json.dumps({"downloaded": True, "destination": "private-local-directory"}))


def download_kaggle(args) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.dataset):
        raise ConnectorError("Use an explicit owner/dataset identifier.")
    root = private_root(args.local_root)
    destination = local_path(root, args.destination)
    api = kaggle_api()
    destination.mkdir(parents=True, mode=0o700)
    # Keep the archive intact: downloaded archives must not extract paths on this machine.
    with quiet_service():
        api.dataset_download_files(args.dataset, path=str(destination), quiet=True, unzip=False)
    print(json.dumps({"downloaded": True, "destination": "private-local-directory"}))


def classify(args) -> None:
    root = private_root(args.local_root)
    model_dir = local_path(root, args.model_dir, must_exist=True)
    destination = local_path(root, args.output)
    source = Path(args.input_csv).expanduser().resolve(strict=True)
    if not source.is_file() or not model_dir.is_dir():
        raise ConnectorError("CSV and model directory must be existing local inputs.")
    # All model and tokenizer loads stay offline, including dynamic-code and telemetry paths.
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["DO_NOT_TRACK"] = "1"
    with quiet_service():
        transformers = dependency("transformers")
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            str(model_dir), local_files_only=True, trust_remote_code=False)
        model = transformers.AutoModelForSequenceClassification.from_pretrained(
            str(model_dir), local_files_only=True, trust_remote_code=False, use_safetensors=True)
        classifier = transformers.pipeline("text-classification", model=model, tokenizer=tokenizer, device=-1)
    destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temporary = None
    try:
        with source.open(newline="", encoding="utf-8-sig") as reader_stream:
            reader = csv.DictReader(reader_stream)
            fields = reader.fieldnames or []
            if args.text_column not in fields or len(fields) != len(set(fields)):
                raise ConnectorError("CSV requires a unique header and the requested text column.")
            if {"predicted_label", "model_confidence"}.intersection(fields):
                raise ConnectorError("Prediction columns already exist; use a clean input CSV.")
            with tempfile.NamedTemporaryFile(mode="w", newline="", encoding="utf-8", dir=destination.parent,
                                             prefix=".classification-", delete=False) as output_stream:
                temporary = Path(output_stream.name)
                writer = csv.DictWriter(output_stream, fieldnames=fields + ["predicted_label", "model_confidence"])
                writer.writeheader()
                for row in reader:
                    if None in row or any(value is None for value in row.values()) or not row[args.text_column].strip():
                        raise ConnectorError("CSV contains missing, extra, or empty text fields.")
                    with quiet_service():
                        predictions = classifier(row[args.text_column], truncation=True)
                    prediction = predictions[0]
                    confidence = float(prediction["score"])
                    label = prediction["label"]
                    if not isinstance(label, str) or not label or not math.isfinite(confidence) or not 0 <= confidence <= 1:
                        raise ConnectorError("Model returned an invalid label or confidence.")
                    row.update(predicted_label=label, model_confidence=format(confidence, ".8g"))
                    writer.writerow(row)
        # Exclusive link commits a complete file without replacing an existing output.
        os.link(temporary, destination)
        print(json.dumps({"classified": True, "output": "private-local-file"}))
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def parser() -> argparse.ArgumentParser:
    cli = PrivateArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="command", required=True)
    status = commands.add_parser("status", help="Check optional package availability without network access")
    status.set_defaults(handler=lambda args: print(json.dumps({name: importlib.util.find_spec(name) is not None
                                                             for name in ("huggingface_hub", "kaggle", "transformers")})))
    connection = commands.add_parser("check", help="Verify authenticated read access without printing identities")
    connection.add_argument("--provider", choices=("hf", "kaggle", "all"), required=True)
    connection.set_defaults(handler=check)
    hf = commands.add_parser("hf-download", help="Download an explicitly identified repository to private local storage")
    hf.add_argument("--kind", choices=("model", "dataset"), required=True)
    hf.add_argument("--repo-id", required=True)
    hf.add_argument("--revision", required=True)
    hf.add_argument("--accept-license", required=True)
    hf.add_argument("--local-root", required=True)
    hf.add_argument("--destination", required=True)
    hf.set_defaults(handler=download_hf)
    kaggle = commands.add_parser("kaggle-download", help="Download one explicitly named dataset as an unopened archive")
    kaggle.add_argument("--dataset", required=True)
    kaggle.add_argument("--local-root", required=True)
    kaggle.add_argument("--destination", required=True)
    kaggle.set_defaults(handler=download_kaggle)
    local = commands.add_parser("classify-local", help="Run offline classification and write only a private local CSV")
    for argument in ("local-root", "model-dir", "input-csv", "text-column", "output"):
        local.add_argument("--" + argument, required=True)
    local.set_defaults(handler=classify)
    return cli


def main(argv=None) -> int:
    try:
        args = parser().parse_args(argv)
        args.handler(args)
        return 0
    except ConnectorError as error:
        print(str(error), file=sys.stderr)
    except Exception:
        # Do not include external exception details, URLs, paths, IDs, or response bodies.
        print("Operation failed. Check dependency versions, permissions, credentials and the documented setup.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
