#!/usr/bin/env python3
"""Offline checks for FT50/AJG2024 research registry (no external downloads)."""
import csv
from pathlib import Path
from urllib.parse import urlparse
ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "FT50_AI_2021_2026"
PAPERS = SUB / "ft50_ai_llm_agentic_papers_2021_2026.csv"
COVERAGE = SUB / "ft50_journal_coverage_2026.csv"

def load(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def check():
    papers = load(PAPERS)
    coverage = load(COVERAGE)
    errs = []
    ids = set()
    journals = set()
    for i, p in enumerate(papers, 2):
        pid = p.get("paper_id", "")
        if not pid or pid in ids: errs.append(f"Paper {i}: duplicate/blank ID {pid}")
        ids.add(pid)
        journals.add(p.get("journal", ""))
        for field in ("topic","title","technology","free_code","free_data","replication_limitation"):
            if not p.get(field, "").strip(): errs.append(f"Paper {i}: missing {field}")
        if p.get("ajg2024") not in {"4", "4*"}: errs.append(f"Paper {i}: AJG grade missing")
        if p.get("ft50_2026") != "Yes": errs.append(f"Paper {i}: FT50 flag missing")
        try:
            year = int(p["year"])
            if not (2021 <= year <= 2026): errs.append(f"Paper {i}: year out of range")
        except (KeyError, ValueError): errs.append(f"Paper {i}: bad year")
        url = urlparse(p.get("article_url",""))
        if url.scheme != "https" or not url.netloc: errs.append(f"Paper {i}: article URL invalid")
        art = p.get("artifact_url", "").strip()
        if art:
            url = urlparse(art)
            if url.scheme != "https" or not url.netloc: errs.append(f"Paper {i}: artifact URL invalid")
    cj = [r.get("journal", "") for r in coverage]
    if len(coverage) != 50 or len(set(cj)) != 50:
        errs.append(f"FT50 coverage matrix should have 50 distinct journals; got {len(coverage)} rows")
    for j in journals:
        if j not in set(cj): errs.append(f"Paper journal missing from FT50 matrix: {j}")
    for r in coverage:
        count = sum(p["journal"] == r["journal"] for p in papers)
        try: recorded = int(r["curated_papers"])
        except (ValueError, KeyError): recorded = -1
        if count != recorded: errs.append(f"Journal count mismatch: {r.get('journal')}, CSV={recorded}, papers={count}")
        if not r.get("coverage_status",""): errs.append(f"Journal coverage status missing: {r.get('journal')}")
    if len(papers) < 40: errs.append("Fewer than 40 entries unexpectedly; check accidental deletion")
    if errs:
        print("\n".join(errs));return 1
    print(f"PASS: {len(papers)} papers, {len(journals)} represented journals, {len(coverage)} tracked FT50 journals.")
    print("This checks METADATA only and DOES NOT establish exhaustive search or reproduction.")
    return 0

if __name__ == "__main__":
    raise SystemExit(check())
