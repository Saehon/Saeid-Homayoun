#!/usr/bin/env python3
"""Read-only CAM/KAM large-corpus quality gate.

Dr. Saeid Homayoun | AuditBERT-USUK-DARWIN V1.
This script does NOT train models, infer report-year, create output datasets,
upload raw records or access Hugging Face. It reports only aggregate metadata.
Run after private Google Drive has been mounted within an approved Colab session.

Example:
  python large_corpus_preflight.py --cam "/content/drive/MyDrive/.../CAM.csv" \
      --kam "/content/drive/MyDrive/.../KAM.csv"

To COUNT only UK-HEADQUARTER candidates (not true UK audit jurisdiction),
pass --kam-country-column EXACT_ORIGINAL_COLUMN_NAME.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from collections import Counter
from pathlib import Path

SOURCE_FIELDS = {
    "US_CAM": {
        "topic": "TOPIC_NAME",
        "text": "DESCRIPTION",
        "matter_key": "CRITICAL_AUDIT_MATTER_KEY",
        "opinion_key": "AUDIT_OPINION_FKEY",
        "issuer": "COMPANY_FKEY",
    },
    "EU_KAM": {
        "topic": "TOPIC",
        "text": "DESCRIPTION",
        "matter_key": "AO_KEY_AUDIT_MATTER_KEY",
        "opinion_key": "AUDIT_OPINION_FKEY",
        "issuer": "ENTITY_MAP_FKEY",
    },
}

# Strict country LABEL only (a true UK KAM cohort requires report-jurisdiction evidence).
UK_HQ_VALUES = {"united kingdom", "uk", "gbr", "gb", "great britain"}

def source_sha256(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(4 * 1024 * 1024), b""):
            sha.update(block)
    return sha.hexdigest()

def normal_hash(text: str) -> str:
    text = re.sub(r"\s+", " ", text.casefold()).strip()
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def audit(path: Path, source: str, country_column: str | None = None,
          chunk_size: int = 5000, include_sha: bool = True) -> dict:
    import pandas as pd
    if source not in SOURCE_FIELDS:
        raise ValueError(f"Unknown source {source}")
    if not path.is_file() or path.suffix.lower() != ".csv":
        raise ValueError("Provide a readable original CSV file.")
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive.")

    header = list(pd.read_csv(path, nrows=0, encoding="utf-8-sig").columns)
    available = {str(h).upper(): h for h in header}
    required = SOURCE_FIELDS[source]
    missing = [v for v in required.values() if v not in available]
    if missing:
        raise ValueError(f"Required original {source} headers are missing: {missing}")

    # Fail closed rather than silently interpreting HQ as audit jurisdiction.
    if country_column and (source != "EU_KAM" or country_column not in header):
        raise ValueError("UK candidate HQ column must be an EXACT KAM.csv header name.")

    selected = [available[v] for v in required.values()]
    if country_column:
        selected.append(country_column)

    counts = Counter()
    topics = Counter()
    unique_issuers = set()
    unique_opinions = set()
    unique_matter_ids = set()
    duplicate_matter_keys = 0
    unique_text_hashes = set()
    duplicate_texts = 0

    for frame in pd.read_csv(
        path, chunksize=chunk_size, usecols=selected, dtype="string",
        encoding="utf-8-sig", low_memory=False
    ):
        counts["rows"] += len(frame)
        topic_col = required["topic"]
        desc_col = required["text"]
        opinion_col = required["opinion_key"]
        issuer_col = required["issuer"]
        matter_col = required["matter_key"]

        for row in frame.itertuples(index=False, name=None):
            # Map by frame.columns to avoid reliance on pandas' tuple-field sanitization.
            values = dict(zip(frame.columns, row))
            def safe(key: str) -> str:
                value = values.get(key)
                return "" if pd.isna(value) else str(value).strip()
            topic = safe(topic_col)
            description = safe(desc_col)
            issuer = safe(issuer_col)
            opinion = safe(opinion_col)
            matter = safe(matter_col)

            if description:
                counts["nonempty_descriptions"] += 1
                digest = normal_hash(description)
                if digest in unique_text_hashes:
                    duplicate_texts += 1
                else:
                    unique_text_hashes.add(digest)
            if topic:
                topics[topic] += 1
            else:
                counts["missing_topics"] += 1
            if issuer:
                unique_issuers.add(issuer)
            else:
                counts["missing_issuer_ids"] += 1
            if opinion:
                unique_opinions.add(opinion)
            else:
                counts["missing_opinion_ids"] += 1
            if matter:
                if matter in unique_matter_ids:
                    duplicate_matter_keys += 1
                else:
                    unique_matter_ids.add(matter)
            else:
                counts["missing_matter_keys"] += 1
            if country_column:
                if safe(country_column).casefold() in UK_HQ_VALUES:
                    counts["uk_headquarters_only_candidates"] += 1

    result = {
        "status": "READ_ONLY_CORPUS_AUDIT_NOT_TRAINED",
        "source": source,
        "file_basename": path.name,
        "size_bytes": path.stat().st_size,
        "source_sha256": source_sha256(path) if include_sha else None,
        "rows": counts["rows"],
        "nonempty_descriptions": counts["nonempty_descriptions"],
        "missing_topics": counts["missing_topics"],
        "missing_issuer_ids": counts["missing_issuer_ids"],
        "missing_opinion_ids": counts["missing_opinion_ids"],
        "missing_matter_keys": counts["missing_matter_keys"],
        "distinct_issuers": len(unique_issuers),
        "distinct_opinions": len(unique_opinions),
        "distinct_matter_ids": len(unique_matter_ids),
        "repeated_matter_keys": duplicate_matter_keys,
        "duplicate_description_hashes": duplicate_texts,
        "distinct_vendor_topics": len(topics),
        "topic_counts": dict(sorted(topics.items())),
        "country_column_inspected": country_column,
        "uk_headquarters_only_candidates": (
            counts["uk_headquarters_only_candidates"] if country_column else None
        ),
        "uk_audit_reporting_regime_verified": False,
        "audit_opinion_year_verified": False,
        "country_header_candidates": [
            c for c in header if "COUNTRY" in c.upper() or "HQ_" in c.upper()
        ],
        "science_gates": {
            "source_use_rights": "UNVERIFIED_BY_SCRIPT",
            "old_embedded_tokens_rotated": "UNVERIFIED_BY_SCRIPT",
            "true_uk_kam_jurisdiction": "UNVERIFIED_BY_SCRIPT",
            "original_report_year": "UNVERIFIED_BY_SCRIPT",
            "near_duplicate_cross_split_leakage": "UNVERIFIED_BY_SCRIPT",
        },
    }
    return result

def self_test():
    import pandas as pd
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        us = base / "CAM.csv"
        kam = base / "KAM.csv"
        pd.DataFrame([
            {"TOPIC_NAME": "Goodwill", "DESCRIPTION": "Goodwill impairment",
             "CRITICAL_AUDIT_MATTER_KEY": "1", "AUDIT_OPINION_FKEY": "10",
             "COMPANY_FKEY": "0000001000"},
            {"TOPIC_NAME": "Goodwill", "DESCRIPTION": "Goodwill   impairment",
             "CRITICAL_AUDIT_MATTER_KEY": "2", "AUDIT_OPINION_FKEY": "10",
             "COMPANY_FKEY": "0000001000"},
        ]).to_csv(us, index=False)
        pd.DataFrame([
            {"TOPIC": "Inventory", "DESCRIPTION": "Inventory obsolescence",
             "AO_KEY_AUDIT_MATTER_KEY": "3", "AUDIT_OPINION_FKEY": "11",
             "ENTITY_MAP_FKEY": "2000", "HQ_COUNTRY": "United Kingdom"},
            {"TOPIC": "Going concern", "DESCRIPTION": "Going concern",
             "AO_KEY_AUDIT_MATTER_KEY": "4", "AUDIT_OPINION_FKEY": "12",
             "ENTITY_MAP_FKEY": "2001", "HQ_COUNTRY": "France"},
        ]).to_csv(kam, index=False)
        a = audit(us, "US_CAM", include_sha=False)
        b = audit(kam, "EU_KAM", country_column="HQ_COUNTRY", include_sha=False)
        assert a["rows"] == 2 and a["distinct_issuers"] == 1
        assert a["duplicate_description_hashes"] == 1
        assert b["rows"] == 2 and b["uk_headquarters_only_candidates"] == 1
        assert not a["audit_opinion_year_verified"]
        assert not b["uk_audit_reporting_regime_verified"]
        assert a["status"] == "READ_ONLY_CORPUS_AUDIT_NOT_TRAINED"
    print(json.dumps({"synthetic_self_test": "PASS", "real_data_read": False}))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cam", type=Path)
    parser.add_argument("--kam", type=Path)
    parser.add_argument("--kam-country-column", type=str,
                        help="EXACT existing HQ country column name; only counts UK HQ candidates")
    parser.add_argument("--chunk-size", type=int, default=5000)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.cam and not args.kam:
        parser.error("At least one of --cam / --kam is required")
    out = {"research_developer": "Dr. Saeid Homayoun",
           "training_status": "NOT_STARTED", "note":
           "Aggregate read-only audit only. No country regime or report date inferred.",
           "sources": []}
    if args.cam:
        out["sources"].append(audit(args.cam, "US_CAM", chunk_size=args.chunk_size))
    if args.kam:
        out["sources"].append(audit(args.kam, "EU_KAM",
            country_column=args.kam_country_column, chunk_size=args.chunk_size))
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
