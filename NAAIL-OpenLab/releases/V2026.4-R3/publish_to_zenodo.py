#!/usr/bin/env python3
"""Publish NAAIL OpenLab V2026.4-R3 to Zenodo.

Requires ZENODO_TOKEN with deposit:write and deposit:actions scopes.
The script is intentionally idempotent for the exact release title/version:
it reuses an existing matching Zenodo deposition when one is visible to the token.
"""

import json
import os
import pathlib
import sys
import requests

API = "https://zenodo.org/api"
TITLE = "NAAIL OpenLab™ V2026.4-R3: Zenodo-Ready Archival Release"
VERSION = "V2026.4-R3"
ASSET = pathlib.Path("NAAIL-OpenLab-V2026.4-R3-Zenodo.zip")
RELEASE_URL = "https://github.com/Saehon/Saeid-Homayoun/releases/tag/V2026.4-R3"

token = os.environ.get("ZENODO_TOKEN", "").strip()
if not token:
    raise SystemExit(
        "ZENODO_TOKEN is missing. Add it as a GitHub Actions repository secret; "
        "the token needs Zenodo deposit:write and deposit:actions scopes."
    )
if not ASSET.exists():
    raise SystemExit(f"Missing archival asset: {ASSET}")

headers = {"Authorization": f"Bearer {token}"}
json_headers = {**headers, "Content-Type": "application/json"}

metadata = {
    "title": TITLE,
    "upload_type": "software",
    "publication_date": "2026-09-24",
    "description": (
        "Zenodo-ready public archival release of NAAIL OpenLab research "
        "infrastructure for evidence-governed accounting, auditing, assurance, "
        "finance, sustainability, CAM/KAM, open-agent tooling, reproducible "
        "cross-platform research packaging, provenance, independent review, "
        "and human approval. This release does not claim independent scientific "
        "validation of all registered experiments or integrations."
    ),
    "creators": [
        {
            "name": "Homayoun, Saeid",
            "orcid": "0000-0002-2536-0446",
        }
    ],
    "version": VERSION,
    "keywords": [
        "accounting",
        "auditing",
        "assurance",
        "artificial intelligence",
        "multi-agent systems",
        "digital twin",
        "CAM",
        "KAM",
        "internal control",
        "sustainability",
        "evidence governance",
        "reproducibility",
        "provenance",
        "research software",
    ],
    "access_right": "open",
    "notes": (
        "GitHub release: " + RELEASE_URL +
        ". Validated historical executable checkpoint remains NAAIL OpenLab "
        "v0.2.3 / Audit Workspace V0.4 / Prototype 003."
    ),
}


def check(resp, expected):
    if resp.status_code not in expected:
        body = resp.text[:3000]
        raise RuntimeError(
            f"Zenodo API error {resp.status_code} for {resp.request.method} "
            f"{resp.url}: {body}"
        )
    return resp


# Find a prior exact-title/version deposit to avoid duplicate publication on reruns.
resp = check(
    requests.get(
        f"{API}/deposit/depositions",
        params={"size": 100, "all_versions": "true"},
        headers=headers,
        timeout=60,
    ),
    {200},
)
deposits = resp.json()
dep = None
for item in deposits:
    md = item.get("metadata") or {}
    if md.get("title") == TITLE and md.get("version") == VERSION:
        dep = item
        break

if dep and dep.get("doi"):
    published = dep
else:
    if dep is None:
        resp = check(
            requests.post(
                f"{API}/deposit/depositions",
                json={},
                headers=json_headers,
                timeout=60,
            ),
            {201},
        )
        dep = resp.json()

    dep_id = dep["id"]
    bucket = dep["links"]["bucket"]

    # Upload the archive only if it is not already present.
    existing_names = {f.get("filename") for f in dep.get("files", [])}
    if ASSET.name not in existing_names:
        with ASSET.open("rb") as fh:
            resp = check(
                requests.put(
                    f"{bucket}/{ASSET.name}",
                    data=fh,
                    headers={**headers, "Content-Type": "application/octet-stream"},
                    timeout=300,
                ),
                {200, 201},
            )

    # Refresh metadata after file upload.
    resp = check(
        requests.put(
            f"{API}/deposit/depositions/{dep_id}",
            json={"metadata": metadata},
            headers=json_headers,
            timeout=60,
        ),
        {200},
    )
    dep = resp.json()

    # Publish only if still unpublished.
    if dep.get("doi"):
        published = dep
    else:
        resp = check(
            requests.post(
                f"{API}/deposit/depositions/{dep_id}/actions/publish",
                headers=headers,
                timeout=120,
            ),
            {202},
        )
        published = resp.json()

doi = published.get("doi")
doi_url = published.get("doi_url") or (f"https://doi.org/{doi}" if doi else None)
record_id = published.get("record_id")
conceptrecid = published.get("conceptrecid")
links = published.get("links") or {}

if not doi:
    raise RuntimeError("Zenodo returned a published response without a DOI.")

result = {
    "title": TITLE,
    "version": VERSION,
    "doi": doi,
    "doi_url": doi_url,
    "record_id": record_id,
    "conceptrecid": conceptrecid,
    "record_url": links.get("record_html") or links.get("html"),
    "github_release": RELEASE_URL,
}
pathlib.Path("zenodo-published.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
print(json.dumps(result, indent=2, ensure_ascii=False))

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
    with open(github_output, "a", encoding="utf-8") as fh:
        fh.write(f"doi={doi}\n")
        fh.write(f"doi_url={doi_url}\n")
        if record_id is not None:
            fh.write(f"record_id={record_id}\n")
