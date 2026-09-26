#!/usr/bin/env python3
"""NAAIL SEC EDGAR Education Lab — CompanyFacts starter.

Educational/research use only. This script retrieves first-party SEC CompanyFacts
JSON and converts one selected US-GAAP tag into a chronology-aware pandas table.

Before use, replace USER_AGENT with an identifying SEC-compliant user agent that
contains your name/organization and contact email. Respect SEC fair-access rules.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

USER_AGENT = "NAAIL-OpenLab/education replace-with-your-email@example.com"
BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


def normalize_cik(cik: str) -> str:
    digits = "".join(ch for ch in str(cik) if ch.isdigit())
    if not digits:
        raise ValueError("CIK must contain digits.")
    return digits.zfill(10)


def get_companyfacts(cik: str) -> tuple[dict, bytes]:
    cik10 = normalize_cik(cik)
    url = BASE_URL.format(cik=cik10)
    response = requests.get(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Encoding": "gzip, deflate",
            "Host": "data.sec.gov",
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json(), response.content


def tag_to_frame(payload: dict, tag: str, taxonomy: str = "us-gaap") -> pd.DataFrame:
    facts = payload.get("facts", {}).get(taxonomy, {})
    if tag not in facts:
        available = sorted(facts.keys())[:25]
        raise KeyError(
            f"Tag {tag!r} not found under {taxonomy!r}. "
            f"Example available tags: {available}"
        )

    concept = facts[tag]
    rows: list[dict] = []
    for unit, observations in concept.get("units", {}).items():
        for obs in observations:
            rows.append(
                {
                    "entity": payload.get("entityName"),
                    "cik": str(payload.get("cik", "")).zfill(10),
                    "taxonomy": taxonomy,
                    "tag": tag,
                    "label": concept.get("label"),
                    "unit": unit,
                    "val": obs.get("val"),
                    "start": obs.get("start"),
                    "end": obs.get("end"),
                    "filed": obs.get("filed"),
                    "form": obs.get("form"),
                    "fy": obs.get("fy"),
                    "fp": obs.get("fp"),
                    "frame": obs.get("frame"),
                    "accn": obs.get("accn"),
                }
            )

    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame

    for col in ("start", "end", "filed"):
        frame[col] = pd.to_datetime(frame[col], errors="coerce")

    return frame.sort_values(["filed", "end", "accn"], na_position="last").reset_index(drop=True)


def save_evidence(payload: dict, raw: bytes, frame: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    sha256 = hashlib.sha256(raw).hexdigest()
    retrieved_at = datetime.now(timezone.utc).isoformat()

    (output_dir / "companyfacts.json").write_bytes(raw)
    frame.to_csv(output_dir / "selected_tag.csv", index=False)

    manifest = {
        "source": "U.S. SEC data.sec.gov CompanyFacts API",
        "entity": payload.get("entityName"),
        "cik": str(payload.get("cik", "")).zfill(10),
        "retrieved_at_utc": retrieved_at,
        "sha256_companyfacts_json": sha256,
        "row_count_selected_tag": int(len(frame)),
        "human_gate_required": True,
        "ai_output_is_source_evidence": False,
    }
    (output_dir / "evidence_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cik", required=True, help="SEC CIK; zero-padding is automatic")
    parser.add_argument("--tag", default="Revenues", help="US-GAAP concept/tag")
    parser.add_argument("--taxonomy", default="us-gaap")
    parser.add_argument("--output", default="outputs/sec_companyfacts")
    args = parser.parse_args()

    if "replace-with-your-email" in USER_AGENT:
        raise RuntimeError(
            "Edit USER_AGENT before running. SEC automated access should identify the requester."
        )

    payload, raw = get_companyfacts(args.cik)
    frame = tag_to_frame(payload, args.tag, args.taxonomy)
    save_evidence(payload, raw, frame, Path(args.output))

    print(f"Entity: {payload.get('entityName')}")
    print(f"Rows: {len(frame)}")
    if not frame.empty:
        print(frame.tail(10).to_string(index=False))


if __name__ == "__main__":
    main()
