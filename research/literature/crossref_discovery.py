"""Bounded, opt-in Crossref candidate harvesting by journal ISSN and keyword.

A discovery queue is NOT a systematic or exhaustive literature review.
No official AJG data, private papers or restricted full text are downloaded.
Standard-library Python 3.11+. Run only with explicit --online.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parent
ISSN = re.compile(r"^\d{4}-[\dXx]{4}$")
DOI = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$", re.I)


def validate_scope(scope):
    if not isinstance(scope, dict) or scope.get("schema_version") != "1.0":
        raise ValueError("unsupported journal search scope")
    journals = scope.get("journal_candidates")
    keywords = scope.get("search_terms")
    if not isinstance(journals, list) or not journals:
        raise ValueError("no journals")
    if not isinstance(keywords, list) or not keywords:
        raise ValueError("no keywords")
    for j in journals:
        if not isinstance(j, dict) or not ISSN.fullmatch(j.get("issn", "")):
            raise ValueError("invalid ISSN")
        if not isinstance(j.get("journal"), str) or not j["journal"].strip():
            raise ValueError("missing journal title")
    for term in keywords:
        if not isinstance(term, str) or not term.strip() or len(term) > 100:
            raise ValueError("invalid term")
    if len({j["issn"] for j in journals}) != len(journals):
        raise ValueError("duplicate ISSN")


def request_url(issn, keyword, rows, email=None):
    if not ISSN.fullmatch(issn):
        raise ValueError("invalid ISSN")
    if not 1 <= rows <= 100:
        raise ValueError("rows must be 1..100")
    parameters = {
        "query": keyword,
        "filter": "from-pub-date:2023-01-01,until-pub-date:2026-10-31",
        "rows": str(rows),
        "select": "DOI,title,author,published,container-title,abstract",
    }
    if email:
        if "\r" in email or "\n" in email or "@" not in email:
            raise ValueError("invalid email")
        parameters["mailto"] = email
    return "https://api.crossref.org/journals/" + issn + "/works?" + urlencode(parameters)


def result_to_candidate(item, journal, keyword):
    doi = item.get("DOI", "")
    if not isinstance(doi, str) or not DOI.fullmatch(doi):
        return None
    title = item.get("title") or []
    title = title[0] if isinstance(title, list) and title else ""
    if not title:
        return None
    year = None
    parts = (item.get("published") or {}).get("date-parts") or []
    if parts and parts[0]:
        year = parts[0][0]
    return {
        "doi": doi.lower(), "title_deposited": title,
        "journal_scoped": journal["journal"], "issn_scoped": journal["issn"],
        "year_deposited": year,
        "search_term": keyword,
        "ft50_candidate_journal": journal["ft50"],
        "ajg_2024_secondary_candidate": journal["ajg_2024_secondary"],
        "manual_inclusion_review": "PENDING",
        "rank_not_authenticated_by_crossref": True
    }


def collect(items, journal, keyword, destination):
    for item in items:
        c = result_to_candidate(item, journal, keyword)
        if c is None:
            continue
        doi = c["doi"]
        if doi in destination:
            old = destination[doi]
            terms = old["search_terms_matched"]
            if keyword not in terms:
                terms.append(keyword)
        else:
            c["search_terms_matched"] = [keyword]
            del c["search_term"]
            destination[doi] = c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scope", type=Path, default=BASE/"crossref_journal_search_scope.json")
    p.add_argument("--online", action="store_true", help="Explicit network opt-in")
    p.add_argument("--out", type=Path)
    p.add_argument("--rows", type=int, default=20)
    p.add_argument("--delay", type=float, default=1.0)
    p.add_argument("--email")
    args = p.parse_args()
    scope = json.loads(args.scope.read_text("utf-8"))
    validate_scope(scope)
    if not args.online:
        p.error("discovery requires --online (not run in GitHub CI)")
    if args.delay < 0 or not 1 <= args.rows <= 100:
        p.error("invalid delay/rows")
    queue = {}
    requests = 0
    failures = []
    for journal in scope["journal_candidates"]:
        for term in scope["search_terms"]:
            if requests:
                time.sleep(args.delay)
            requests += 1
            url = request_url(journal["issn"], term, args.rows, args.email)
            try:
                headers = {"User-Agent": "NAAILResearchDiscovery/1.0",
                           "Accept":"application/json"}
                with urlopen(Request(url, headers=headers), timeout=25) as response:
                    obj = json.load(response)
                if obj.get("status") != "ok" or not isinstance(obj.get("message"), dict):
                    raise ValueError("unexpected Crossref response")
                items = obj["message"].get("items") or []
                collect(items, journal, term, queue)
            except Exception as exc:
                failures.append({"journal":journal["journal"],"term":term,
                                 "error":type(exc).__name__ + ": " + str(exc)[:180]})
    result = {
        "scope": "bounded_API_search_candidates_not_exhaustive",
        "crossref_requests": requests,
        "failed_queries": failures,
        "unique_candidates": len(queue),
        "all_items_require_manual_screening": True,
        "ajg_issued_by_crossref": False,
        "entries": sorted(queue.values(), key=lambda d: d["doi"])
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
        print("Candidate queue written:", args.out, "records:", len(queue))
    else:
        print(rendered)


if __name__ == "__main__":
    main()
