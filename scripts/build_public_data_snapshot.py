#!/usr/bin/env python3
"""Build a public-safe research-data snapshot from Saehon's public GitHub repositories."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable

DIRECT_DATA_EXTS = {
    ".csv", ".tsv", ".parquet", ".feather", ".arrow",
    ".xlsx", ".xls", ".sav", ".dta", ".sas7bdat",
    ".jsonl", ".ndjson", ".geojson", ".npy", ".npz",
}
CONDITIONAL_TEXT_EXTS = {".json", ".xml", ".txt"}
TEXT_SCAN_EXTS = {
    ".csv", ".tsv", ".json", ".jsonl", ".ndjson",
    ".geojson", ".txt", ".xml", ".yaml", ".yml",
}
DATA_HINTS = {
    "data", "dataset", "datasets", "open-data", "benchmark", "benchmarks",
    "result", "results", "output", "outputs", "registry", "sample", "samples",
    "synthetic", "manifest", "cam", "kam", "icfr", "esg", "sec", "xbrl",
    "ifrs", "audit", "accounting", "finance",
}

KNOWN_EXTERNAL_MIRRORS = {
    "yfinance",
    "openai-agents-python",
    "timesfm",
    "sec-edgar-downloader",
    "openesef",
    "esef-website",
    "github-profile-achievements",
    "desktop-tutorial",
    "ganlab",
    "robosystems",
    "fg-data-synthetic",
    "artificial-analysis-intelligence-index",
    "financial-services",
    "agent-openai-python-banking-assistant",
    "Saeid-Homayoun-Test",
}

SENSITIVE_PATH_PATTERNS = [
    re.compile(r"(^|/)(\.env($|\.)|secrets?($|[._-])|credentials?($|[._-])|passwords?($|[._-]))", re.I),
    re.compile(r"(^|/)(kaggle\.json|service[-_]account|id_rsa|id_ed25519|private[-_]key|api[-_]key|apikey|access[-_]key|oauth)", re.I),
    re.compile(r"(^|/)(token|tokens)\.(json|txt|csv|tsv)$", re.I),
    re.compile(r"(^|/)(applicants?|student[-_]records?|recruitment|resumes?|curriculum[-_]vitae)(/|$)", re.I),
]

SECRET_PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("huggingface-token", re.compile(r"\bhf_[A-Za-z0-9]{20,}\b")),
    ("openai-style-key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    (
        "generic-secret-assignment",
        re.compile(
            r"""(?ix)
            ["']?(?:api[_-]?key|access[_-]?key|secret|token|password)["']?
            \s*[:=]\s*
            ["'][^"'\r\n]{12,}["']
            """
        ),
    ),
]

MAX_FILE_BYTES = 95 * 1024 * 1024
SCAN_ALL_BYTES = 25 * 1024 * 1024
SCAN_EDGE_BYTES = 4 * 1024 * 1024


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, text=True, **kwargs)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_candidate(rel: Path) -> bool:
    ext = rel.suffix.lower()
    if ext in DIRECT_DATA_EXTS:
        return True
    if ext in CONDITIONAL_TEXT_EXTS:
        parts = {p.lower() for p in rel.parts}
        stem_tokens = set(re.split(r"[^a-z0-9]+", rel.stem.lower()))
        return bool((parts | stem_tokens) & DATA_HINTS)
    return False


def sensitive_path(rel: Path) -> str | None:
    normalized = rel.as_posix().lower()
    for rx in SENSITIVE_PATH_PATTERNS:
        if rx.search(normalized):
            return "sensitive-path"
    return None


def is_lfs_pointer(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(256)
        return head.startswith(b"version https://git-lfs.github.com/spec/v1")
    except OSError:
        return False


def read_for_secret_scan(path: Path) -> str:
    size = path.stat().st_size
    with path.open("rb") as f:
        if size <= SCAN_ALL_BYTES:
            raw = f.read()
        else:
            head = f.read(SCAN_EDGE_BYTES)
            f.seek(max(0, size - SCAN_EDGE_BYTES))
            tail = f.read(SCAN_EDGE_BYTES)
            raw = head + b"\n...middle omitted from scan...\n" + tail
    return raw.decode("utf-8", errors="ignore")


def secret_reason(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SCAN_EXTS:
        return None
    text = read_for_secret_scan(path)
    for label, rx in SECRET_PATTERNS:
        if rx.search(text):
            return f"secret-scan:{label}"
    return None


def tracked_files(repo_dir: Path) -> Iterable[Path]:
    cp = subprocess.run(
        ["git", "-C", str(repo_dir), "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    for raw in cp.stdout.split(b"\0"):
        if raw:
            yield Path(raw.decode("utf-8", errors="surrogateescape"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-json", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--owner", default="Saehon")
    args = ap.parse_args()

    repos = json.loads(Path(args.repos_json).read_text(encoding="utf-8"))
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    (out / "repositories").mkdir(parents=True)

    included_rows: list[dict] = []
    excluded_rows: list[dict] = []
    source_rows: list[dict] = []

    eligible = []
    for repo in repos:
        name = repo.get("name", "")
        reason = None
        if repo.get("owner", {}).get("login") != args.owner:
            reason = "not-owned-by-target-account"
        elif repo.get("private"):
            reason = "private-repository"
        elif repo.get("archived"):
            reason = "archived-repository"
        elif repo.get("fork"):
            reason = "forked-repository"
        elif name in KNOWN_EXTERNAL_MIRRORS:
            reason = "known-third-party-or-code-mirror"

        source_rows.append({
            "repository": name,
            "html_url": repo.get("html_url", ""),
            "default_branch": repo.get("default_branch", ""),
            "fork": bool(repo.get("fork")),
            "archived": bool(repo.get("archived")),
            "license": (repo.get("license") or {}).get("spdx_id") or "",
            "included_in_snapshot": reason is None,
            "exclusion_reason": reason or "",
        })
        if reason is None:
            eligible.append(repo)

    with tempfile.TemporaryDirectory(prefix="github-public-data-") as tmp:
        tmp_root = Path(tmp)
        for repo in eligible:
            name = repo["name"]
            clone_url = repo["clone_url"]
            repo_dir = tmp_root / name
            env = os.environ.copy()
            env["GIT_LFS_SKIP_SMUDGE"] = "1"
            print(f"Cloning {name} ...", flush=True)
            try:
                subprocess.run(
                    ["git", "clone", "--depth", "1", "--filter=blob:none", clone_url, str(repo_dir)],
                    check=True,
                    env=env,
                )
            except subprocess.CalledProcessError:
                excluded_rows.append({
                    "repository": name,
                    "source_path": "",
                    "reason": "repository-clone-failed",
                })
                continue

            try:
                commit = run(["git", "-C", str(repo_dir), "rev-parse", "HEAD"], capture_output=True).stdout.strip()
            except subprocess.CalledProcessError:
                commit = ""

            license_id = (repo.get("license") or {}).get("spdx_id") or ""
            for rel in tracked_files(repo_dir):
                if not is_candidate(rel):
                    continue
                src = repo_dir / rel
                if not src.is_file():
                    continue

                reason = sensitive_path(rel)
                if reason:
                    excluded_rows.append({"repository": name, "source_path": rel.as_posix(), "reason": reason})
                    continue

                try:
                    size = src.stat().st_size
                except OSError:
                    excluded_rows.append({"repository": name, "source_path": rel.as_posix(), "reason": "stat-failed"})
                    continue

                if size > MAX_FILE_BYTES:
                    excluded_rows.append({"repository": name, "source_path": rel.as_posix(), "reason": f"file-too-large:{size}"})
                    continue
                if is_lfs_pointer(src):
                    excluded_rows.append({"repository": name, "source_path": rel.as_posix(), "reason": "git-lfs-pointer-not-materialized"})
                    continue

                try:
                    reason = secret_reason(src)
                except OSError:
                    reason = "secret-scan-read-failed"
                if reason:
                    excluded_rows.append({"repository": name, "source_path": rel.as_posix(), "reason": reason})
                    continue

                dst_rel = Path("repositories") / name / rel
                dst = out / dst_rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                digest = sha256(dst)
                included_rows.append({
                    "repository": name,
                    "source_path": rel.as_posix(),
                    "source_url": f"https://github.com/{args.owner}/{name}/blob/{commit}/{rel.as_posix()}",
                    "source_commit": commit,
                    "repository_license": license_id,
                    "bytes": size,
                    "sha256": digest,
                    "mirrored_path": dst_rel.as_posix(),
                })

    included_rows.sort(key=lambda r: (r["repository"].lower(), r["source_path"].lower()))
    excluded_rows.sort(key=lambda r: (r["repository"].lower(), r["source_path"].lower(), r["reason"]))
    source_rows.sort(key=lambda r: r["repository"].lower())

    if not included_rows:
        raise SystemExit("No public-safe data files were found; refusing to publish an empty dataset.")

    def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    write_csv(
        out / "DATA_MANIFEST.csv",
        included_rows,
        ["repository", "source_path", "source_url", "source_commit", "repository_license", "bytes", "sha256", "mirrored_path"],
    )
    write_csv(
        out / "EXCLUSIONS.csv",
        excluded_rows,
        ["repository", "source_path", "reason"],
    )
    write_csv(
        out / "SOURCE_REPOSITORIES.csv",
        source_rows,
        ["repository", "html_url", "default_branch", "fork", "archived", "license", "included_in_snapshot", "exclusion_reason"],
    )

    total_bytes = sum(int(r["bytes"]) for r in included_rows)
    repos_with_data = sorted({r["repository"] for r in included_rows}, key=str.lower)
    metadata = {
        "dataset": "Saeid Homayoun GitHub Public Research Data",
        "canonical_owner": args.owner,
        "generated_by": "Saehon/Saeid-Homayoun GitHub Actions",
        "included_files": len(included_rows),
        "included_repositories": repos_with_data,
        "total_uncompressed_bytes": total_bytes,
        "safety_policy": {
            "public_only": True,
            "non_fork_only": True,
            "known_external_mirrors_excluded": sorted(KNOWN_EXTERNAL_MIRRORS),
            "credential_and_personal_record_paths_excluded": True,
            "text_secret_scan": True,
            "git_lfs_pointers_excluded": True,
        },
        "targets": {
            "kaggle": "https://www.kaggle.com/datasets/sadhon/github-public-research-data",
            "huggingface": "https://huggingface.co/datasets/SADHON/github-public-research-data",
        },
    }
    (out / "SNAPSHOT_METADATA.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    readme = f"""---
license: other
pretty_name: Saeid Homayoun GitHub Public Research Data
tags:
- accounting
- auditing
- finance
- ifrs
- esg
- icfr
- research
---

# Saeid Homayoun GitHub Public Research Data

This is an automated, provenance-preserving mirror of public-safe research data files from original public repositories owned by Saehon.

## Snapshot contents

- Included data files: {len(included_rows)}
- Repositories contributing data: {len(repos_with_data)}
- Uncompressed data size: {total_bytes:,} bytes
- Canonical source: https://github.com/Saehon
- Kaggle mirror: https://www.kaggle.com/datasets/sadhon/github-public-research-data
- Hugging Face mirror: https://huggingface.co/datasets/SADHON/github-public-research-data

## Publication controls

The pipeline includes only public, non-archived, non-fork repositories; excludes known third-party/code mirrors; copies only data-oriented file types; excludes credential-like and personal-record paths; scans text-like data files for high-risk secret patterns; and excludes Git LFS pointer files that are not actually materialized.

DATA_MANIFEST.csv records the original GitHub repository, path, commit, source URL, repository-level license metadata, file size, SHA-256 digest, and mirrored path for every included file. EXCLUSIONS.csv records candidate data files deliberately left out and why. SOURCE_REPOSITORIES.csv documents the account-level repository inclusion decision.

## Rights and licensing

Public availability on GitHub does not itself change copyright or data-use rights. Each source file remains subject to its original applicable license, terms, and provenance. Repository-level license metadata is preserved in the manifest where GitHub exposes it.

## Research-use note

This mirror is designed for reproducibility, discovery, and research workflows in accounting, auditing, finance, IFRS, ESG, ICFR, governance, and related AI applications. Always cite the canonical source repository and inspect the manifest before reuse.
"""
    (out / "README.md").write_text(readme, encoding="utf-8")

    zip_path = out / "github-public-research-data.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for p in sorted((out / "repositories").rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(out).as_posix())
        for name in ["DATA_MANIFEST.csv", "EXCLUSIONS.csv", "SOURCE_REPOSITORIES.csv", "SNAPSHOT_METADATA.json", "README.md"]:
            p = out / name
            zf.write(p, p.relative_to(out).as_posix())

    (out / "SNAPSHOT_SHA256.txt").write_text(
        f"{sha256(zip_path)}  {zip_path.name}\n",
        encoding="utf-8",
    )

    shutil.rmtree(out / "repositories")
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
