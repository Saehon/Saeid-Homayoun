#!/usr/bin/env python3
"""Build publication-ready cross-platform catalogues from the canonical YAML registries."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml


def read_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="open-source/accounting-finance-audit")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    root = Path(args.root)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    repos_doc = read_yaml(root / "repos.yml")
    data_doc = read_yaml(root / "data" / "data_sources.yml")

    program_rows = []
    for r in repos_doc["repositories"]:
        program_rows.append({
            "record_type": "program",
            "provider": r.get("provider", ""),
            "platform": "github",
            "handle": r.get("repo", ""),
            "url": r.get("url", ""),
            "domains": "|".join(r.get("domains", [])),
            "tier": r.get("tier", ""),
            "free_assets": "|".join(r.get("free_assets", [])),
            "licence": r.get("licence", "verify upstream"),
            "notes": r.get("runtime_note", ""),
        })

    data_rows = []
    for d in data_doc["sources"]:
        platform = d.get("platform", "")
        handle = d.get("handle", "")
        if platform == "huggingface":
            url = f"https://huggingface.co/datasets/{handle}"
        elif platform == "kaggle":
            url = f"https://www.kaggle.com/datasets/{handle}"
        elif platform == "github":
            url = f"https://github.com/{handle}"
        else:
            url = ""
        data_rows.append({
            "record_type": "data",
            "provider": "",
            "platform": platform,
            "handle": handle,
            "url": url,
            "domains": "|".join(d.get("domains", [])),
            "tier": "",
            "free_assets": d.get("kind", ""),
            "licence": d.get("licence", ""),
            "notes": d.get("size_note", ""),
        })

    fields = [
        "record_type","provider","platform","handle","url","domains",
        "tier","free_assets","licence","notes"
    ]
    write_csv(out / "program_catalog.csv", program_rows, fields)
    write_csv(out / "data_catalog.csv", data_rows, fields)
    write_csv(out / "combined_catalog.csv", program_rows + data_rows, fields)

    # Preserve canonical machine-readable source registries.
    (out / "repos.yml").write_text((root / "repos.yml").read_text(encoding="utf-8"), encoding="utf-8")
    (out / "data_sources.yml").write_text((root / "data" / "data_sources.yml").read_text(encoding="utf-8"), encoding="utf-8")

    manifest = {
        "title": "Accounting Finance Audit Open Data and Program Registry",
        "canonical_github": "https://github.com/Saehon/Saeid-Homayoun/tree/main/open-source/accounting-finance-audit",
        "huggingface_target": "https://huggingface.co/datasets/SADHON/accounting-finance-audit-open-registry",
        "kaggle_target": "https://www.kaggle.com/datasets/sadhon/accounting-finance-audit-open-registry",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "program_records": len(program_rows),
        "data_records": len(data_rows),
        "policy": {
            "metadata_links_only": True,
            "vendor_third_party_source": False,
            "redistribute_third_party_large_data": False,
            "verify_upstream_licence_before_use": True,
        },
    }
    (out / "REGISTRY_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    hashes = {}
    for p in sorted(out.iterdir()):
        if p.is_file():
            hashes[p.name] = sha256(p)
    (out / "SHA256SUMS.json").write_text(
        json.dumps(hashes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
