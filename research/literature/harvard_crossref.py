"""Harvard references + conservative Crossref DOI metadata audit (stdlib only).

Default is OFFLINE: renders reviewed seed data and does not claim API verification.
--online checks DOI metadata via Crossref with backoff, outputs mismatch reports,
and NEVER silently overwrites reviewer-approved bibliography metadata.
"""
from __future__ import annotations

import argparse
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
DEFAULT_REGISTRY = ROOT / "llm_agentic_ai_seed_registry.json"
DOI_RX = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$", re.IGNORECASE)


def safe_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("expected nonempty text")
    return value.strip()


def validate_registry(data):
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise ValueError("unsupported bibliography schema version")
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("empty bibliography")
    identifiers = set()
    dois = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("each record must be an object")
        for field in ("key", "title", "journal", "doi", "tier", "theme", "projects", "nature", "directness"):
            safe_text(record.get(field))
        if not isinstance(record.get("year"), int) or not 1900 <= record["year"] <= 2027:
            raise ValueError("invalid bibliographic year")
        authors = record.get("authors")
        if not isinstance(authors, list) or not authors or not all(
                isinstance(a, str) and a.strip() for a in authors):
            raise ValueError("missing authors")
        doi = record["doi"].lower()
        if not DOI_RX.fullmatch(doi):
            raise ValueError("invalid DOI: " + doi)
        if record["key"] in identifiers or doi in dois:
            raise ValueError("duplicate DOI or record key")
        identifiers.add(record["key"])
        dois.add(doi)
        # Tiers are journal metadata, never scientific proof. A "1" grade
        # can be a contextual AI disclosure paper rather than an LLM study.
        if record["tier"].startswith("AJG 1") and "not" in record["directness"].lower():
            pass
    return records


def harvard_name(name):
    name = safe_text(name)
    parts = name.split()
    if len(parts) == 1:
        return parts[0]
    return parts[-1] + ", " + " ".join(p[0] + "." for p in parts[:-1])


def harvard_authors(names):
    names = [harvard_name(x) for x in names]
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]


def citation(record):
    return (f'{harvard_authors(record["authors"])} ({record["year"]}) '
            f'‘{record["title"]}’, *{record["journal"]}*. '
            f'https://doi.org/{record["doi"]}.')


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def top_title(item):
    value = item.get("title") or []
    return value[0] if isinstance(value, list) and value else ""


def year_from_metadata(item):
    for date_key in ("published", "published-online", "issued", "published-print"):
        parts = (item.get(date_key) or {}).get("date-parts") or []
        if parts and parts[0]:
            return parts[0][0]
    return None


def compare_metadata(record, item):
    """An automated flag, not human verification of scientific findings."""
    title = top_title(item)
    journal = (item.get("container-title") or [""])[0]
    crossref_year = year_from_metadata(item)
    title_sim = SequenceMatcher(None, norm(record["title"]), norm(title)).ratio()
    journal_sim = SequenceMatcher(None, norm(record["journal"]), norm(journal)).ratio()
    names = item.get("author") or []
    first_surname = record["authors"][0].split()[-1].lower()
    first_match = bool(names) and (names[0].get("family", "").lower() == first_surname)
    return {
        "key": record["key"], "doi": record["doi"],
        "metadata_queried": True,
        "crossref_title": title, "crossref_journal": journal,
        "crossref_year": crossref_year,
        "crossref_author_count": len(names),
        "title_similarity": round(title_sim, 4),
        "journal_similarity": round(journal_sim, 4),
        "first_author_family_matches": first_match,
        "metadata_needs_manual_review": (
            title_sim < 0.90 or journal_sim < 0.84 or
            not first_match or crossref_year is None or
            abs(crossref_year - record["year"]) > 1
        ),
        "tier_verified_by_crossref": False,
        "research_conclusion_verified_by_crossref": False,
        "notes": "Crossref cannot certify AJG/FT50 tiers, article content, theory validity or private data."
    }


def retrieve_crossref(doi, email=None):
    if not DOI_RX.fullmatch(doi):
        raise ValueError("refusing invalid DOI")
    url = "https://api.crossref.org/works/" + quote(doi, safe="/")
    agent = "NAAILAcademicBibliography/1.0 (open academic metadata checks)"
    if email:
        safe_text(email)
        if "\r" in email or "\n" in email:
            raise ValueError("invalid email")
        url += "?mailto=" + quote(email, safe="")
        agent += "; mailto:" + email
    req = Request(url, headers={"User-Agent": agent, "Accept": "application/json"})
    with urlopen(req, timeout=20) as response:
        obj = json.load(response)
    if obj.get("status") != "ok" or not isinstance(obj.get("message"), dict):
        raise ValueError("unexpected Crossref response")
    return obj["message"]


def build(data, online=False, email=None, delay=1.0):
    records = validate_registry(data)
    result = {
        "mode": "crossref_metadata_check" if online else "offline_reviewed_seed_only",
        "crossref_api_accessed": bool(online),
        "no_claim_of_exhaustiveness": True,
        "tiers_not_verified_by_api": True,
        "records_total": len(records),
        "records": []
    }
    for i, rec in enumerate(records):
        item = {"key": rec["key"], "harvard_reference": citation(rec),
                "source_tier_label": rec["tier"],
                "metadata_api_verified": False,
                "requires_scholarly_content_review": True}
        if online:
            if i:
                time.sleep(max(delay, 0))
            try:
                check = compare_metadata(rec, retrieve_crossref(rec["doi"], email))
                item.update(check)
                item["metadata_api_verified"] = not check["metadata_needs_manual_review"]
            except (HTTPError, URLError, OSError, ValueError, TimeoutError) as exc:
                item["metadata_error"] = type(exc).__name__ + ": " + str(exc)[:200]
        result["records"].append(item)
    result["api_metadata_match_count"] = sum(
        bool(item["metadata_api_verified"]) for item in result["records"]
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--online", action="store_true", help="Opt-in Crossref API DOI metadata checks")
    parser.add_argument("--email", help="Optional contact for Crossref polite pool")
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()
    if args.delay < 0:
        parser.error("--delay must be nonnegative")
    data = json.loads(args.registry.read_text(encoding="utf-8"))
    report = build(data, online=args.online, email=args.email, delay=args.delay)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
        print(f"Wrote {report['records_total']} references to {args.out} ({report['mode']})")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
