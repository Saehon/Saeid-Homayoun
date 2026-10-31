"""Fail-closed local academic evidence integrity gates.

Checks authored Harvard page against exact structured records and enforces
explicitly bounded claim-to-literature mappings. Offline stdlib only.
Not an online DOI verification, peer review, or official journal-rating audit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from research.literature.harvard_crossref import (
    validate_registry, harvard_authors,
)

ROOT = Path(__file__).resolve().parent
PAGE = ROOT.parent / "LLM_FINE_TUNING_AGENTIC_AI_HARVARD_REFERENCES.md"
REGISTRY = ROOT / "llm_agentic_ai_seed_registry.json"
LEDGER = ROOT / "project_evidence_ledger.json"
# Match exact reference rows only, excluding prose, DOI context/footnotes.
REFERENCE = re.compile(
    r"^- \*\*(?P<key>[\w-]+):\*\* (?P<body>.+?)"
    r"\[DOI\]\(https://doi\.org/(?P<doi>[^)]+)\)\.",
    re.M,
)
ALLOWED_RELATIONSHIPS = {
    "context_and_method", "methodological_motivation", "direct_methods",
    "construct_measurement_caution", "indirect_domain_context",
    "conceptual_and_methodological", "indirect_context", "methods_and_caution",
}
PROJECT_NAMES = ("PCAOB", "IFRS", "ISSB", "KIWI", "NAAIL", "POMELO", "DARWIN")


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def audit(registry, ledger, markdown):
    records = validate_registry(registry)
    if not isinstance(markdown, str):
        raise ValueError("expected markdown text")
    by_key = {r["key"]: r for r in records}
    if len(by_key) != len(records):
        raise ValueError("duplicate key")
    refs = list(REFERENCE.finditer(markdown))
    if len(refs) != len(records):
        raise ValueError("bibliography reference-row count differs from registry")
    observed = set()
    for match in refs:
        key = match.group("key")
        doi = match.group("doi").lower()
        if key not in by_key or key in observed:
            raise ValueError("unknown or duplicate reference key: " + key)
        observed.add(key)
        record = by_key[key]
        if doi != record["doi"].lower():
            raise ValueError("DOI drift: " + key)
        body = match.group("body")
        authors = harvard_authors(record["authors"])
        if not body.startswith(authors + " (" + str(record["year"]) + ")"):
            raise ValueError("Harvard author/year drift: " + key)
        if "‘" + record["title"] + "’" not in body:
            raise ValueError("article-title drift: " + key)
        if "*" + record["journal"] + "*" not in body:
            raise ValueError("journal-title drift: " + key)
        if record["tier"].startswith("AJG grade pending") and "pending" not in markdown.lower():
            raise ValueError("unresolved AJG grade must remain visibly pending")
    if observed != set(by_key):
        raise ValueError("missing bibliographic keys")
    if not isinstance(ledger, dict) or ledger.get("schema_version") != "1.0":
        raise ValueError("invalid claim ledger")
    claims = ledger.get("project_claims")
    if not isinstance(claims, list) or not claims:
        raise ValueError("missing project evidence ledger")
    seen = set()
    mapped = set()
    for row in claims:
        if not isinstance(row, dict):
            raise ValueError("invalid claim mapping")
        ident = row.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("missing or duplicate claim identifier")
        seen.add(ident)
        project = row.get("project", "")
        if not any(x.lower() in project.lower() for x in PROJECT_NAMES):
            raise ValueError("unknown research programme: " + ident)
        for key in ("claim", "uncertainty"):
            if not isinstance(row.get(key), str) or len(row[key].strip()) < 25:
                raise ValueError("missing substantive " + key + ": " + ident)
        if row.get("empirical_status") != "NOT_TESTED_IN_THIS_REPOSITORY":
            raise ValueError("unverified experimental claim: " + ident)
        if row.get("relationship") not in ALLOWED_RELATIONSHIPS:
            raise ValueError("unsupported relationship claim: " + ident)
        evidence = row.get("evidence_keys")
        if not isinstance(evidence, list) or not evidence or len(evidence) != len(set(evidence)):
            raise ValueError("invalid evidence keys: " + ident)
        unknown = set(evidence) - set(by_key)
        if unknown:
            raise ValueError("unregistered academic reference in " + ident + ": " + str(sorted(unknown)))
        mapped.update(evidence)
    required_phrases = (
        "non-exhaustive", "private", "Google Drive", "do not",
        "Crossref", "not",
    )
    for phrase in required_phrases:
        if phrase.lower() not in markdown.lower():
            raise ValueError("missing key scientific qualification: " + phrase)
    return {
        "validation_scope": "OFFLINE_STRUCTURE_AND_CLAIM_GATES_ONLY",
        "bibliographic_metadata_verified_against_publisher_api": False,
        "official_ajg_ranking_verified": False,
        "all_project_hypotheses_empirically_supported": False,
        "nonexhaustive_literature": True,
        "bibliographic_records": len(records),
        "public_harvard_references": len(refs),
        "tracked_project_claims": len(claims),
        "unique_cited_sources_in_claim_ledger": len(mapped),
        "unmapped_sources_do_not_imply_empirical_failure": True,
        "limitations": [
            "Does not contact publisher, Crossref, Scopus, Web of Science or official CABS.",
            "DOI syntactic validity does not establish genuine bibliographic metadata.",
            "A registered citation may be theoretically relevant but cannot validate untested methods.",
            "Independent human evaluation, full text assessment and complete journal coverage remain outstanding.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--markdown", type=Path, default=PAGE)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = audit(
        load_json(args.registry),
        load_json(args.ledger),
        args.markdown.read_text(encoding="utf-8"),
    )
    result = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result, encoding="utf-8")
        print("Evidence gates passed:", report["bibliographic_records"], "references;",
              report["tracked_project_claims"], "bounded claims")
    else:
        print(result)


if __name__ == "__main__":
    main()
