#!/usr/bin/env python3
"""Validate metadata of the FT50 research source registry, not empirical results."""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

CATALOG = Path(__file__).with_name("sources.json")
def verify(online=False):
    entries = json.loads(CATALOG.read_text(encoding="utf-8"))["sources"]
    assert len(entries) == 14, "Expected 14 source records"
    assert len(set(e["id"] for e in entries)) == len(entries), "Duplicate IDs"
    assert len(set(e["upstream_repository"] for e in entries)) == len(entries), "Duplicate URLs"
    for item in entries:
        assert item["status"] == "CATALOGUED_ONLY_NO_EMPIRICAL_EXECUTION"
        assert item["upstream_repository"].startswith("https://github.com/")
        assert item["paper_url"].startswith("https://")
        assert item["research_mapping"] and item["topic"]
        if online:
            url = item["upstream_repository"].replace("https://github.com/", "https://api.github.com/repos/")
            req = Request(url, headers={"User-Agent": "NAAIL-research-registry", "Accept": "application/vnd.github+json"})
            with urlopen(req, timeout=15) as response:
                info = json.load(response)
            assert info.get("full_name"), "Unresolved GitHub repository " + url
            print(item["id"] + ": " + info["full_name"])
    print(f"PASS: {len(entries)} catalog records (structural validation only)")
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--online", action="store_true")
    verify(p.parse_args().online)
