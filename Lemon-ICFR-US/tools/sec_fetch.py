"""P04 — SEC EDGAR evidence acquisition for Microsoft (CIK 0000789019).

  PYTHONPATH=src python tools/sec_fetch.py --email you@example.com

Fair access: User-Agent with contact email (required), ≤ 10 requests/second, and a
cache by URL+hash — a file whose manifest hash verifies is never re-downloaded.
Stores raw files AND a deterministic derived text version (spans refer to the text).
"""
from __future__ import annotations

import argparse
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

from _common import ROOT, dump_json, sha256_bytes
from lemon_icfr.assurance.extract import html_to_text

CIK = "0000789019"
OUT = ROOT / "organized" / "evidence" / "msft"
SUBMISSIONS = f"https://data.sec.gov/submissions/CIK{CIK}.json"
COMPANYFACTS = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"


class EdgarClient:
    def __init__(self, user_agent: str, fetch_fn: Optional[Callable[[str, dict], bytes]] = None,
                 min_interval: float = 0.15, clock=time.monotonic, sleep=time.sleep):
        if "@" not in user_agent:
            raise ValueError("SEC requires a User-Agent with a contact email")
        self.ua, self._fetch, self.min_interval = user_agent, fetch_fn or self._urllib, min_interval
        self._clock, self._sleep, self._last, self.requests = clock, sleep, None, 0

    @staticmethod
    def _urllib(url: str, headers: dict) -> bytes:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
            return r.read()

    def get(self, url: str) -> bytes:
        now = self._clock()
        if self._last is not None and now - self._last < self.min_interval:
            self._sleep(self.min_interval - (now - self._last))
        self._last = self._clock()
        self.requests += 1
        return self._fetch(url, {"User-Agent": self.ua, "Accept-Encoding": "identity"})


def _load_manifest(out: Path) -> list[dict]:
    m = out / "manifest.json"
    return json.loads(m.read_text()) if m.exists() else []


def _cached(manifest: list[dict], url: str, out: Path) -> Optional[dict]:
    for e in manifest:
        if e["url"] == url and e.get("kind") != "derived_text":
            p = out / e["path"]
            if p.exists() and sha256_bytes(p.read_bytes()) == e["sha256"]:
                return e
    return None


def _store(manifest, out, *, url, data, rel, evidence_id, kind, form, accession, period_end, filed_date, tier,
           derived_from=""):
    p = out / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    e = {"evidence_id": evidence_id, "url": url, "path": rel, "kind": kind, "form": form, "accession": accession,
         "period_end": period_end, "filed_date": filed_date, "tier": tier, "rights": "SEC public filing",
         "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
         "sha256": sha256_bytes(data), "derived_from": derived_from}
    manifest[:] = [x for x in manifest if x["evidence_id"] != evidence_id] + [e]
    return e


def select_filings(sub: dict) -> list[dict]:
    r = sub["filings"]["recent"]
    rows = [dict(zip(r.keys(), vals)) for vals in zip(*r.values())]
    tenks = sorted([x for x in rows if x["form"] == "10-K"], key=lambda x: x["filingDate"], reverse=True)[:2]
    if not tenks:
        return []
    start = min(x["filingDate"] for x in tenks)
    eightks = [x for x in rows if x["form"] == "8-K" and x["filingDate"] >= start
               and any(i in (x.get("items") or "") for i in ("4.01", "4.02"))]
    return tenks + eightks


def acquire(client: EdgarClient, out: Path = OUT) -> list[dict]:
    manifest = _load_manifest(out)

    def get(url):
        hit = _cached(manifest, url, out)
        return ((out / hit["path"]).read_bytes(), hit) if hit else (client.get(url), None)

    sub_bytes, _ = get(SUBMISSIONS)
    _store(manifest, out, url=SUBMISSIONS, data=sub_bytes, rel="index/submissions.json", evidence_id="MSFT-INDEX",
           kind="index", form="INDEX", accession="", period_end="", filed_date="", tier=5)
    cf, hit = get(COMPANYFACTS)
    if not hit:
        _store(manifest, out, url=COMPANYFACTS, data=cf, rel="xbrl/companyfacts.json", evidence_id="MSFT-XBRL",
               kind="xbrl", form="XBRL", accession="", period_end="", filed_date="", tier=6)
    for f in select_filings(json.loads(sub_bytes)):
        acc = f["accessionNumber"]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/{f['primaryDocument']}"
        data, hit = get(url)
        base = f"MSFT-{f['form']}-{acc}"
        if not hit:
            _store(manifest, out, url=url, data=data, rel=f"raw/{acc}_{f['primaryDocument']}", evidence_id=f"{base}-raw",
                   kind="raw", form=f["form"], accession=acc, period_end=f.get("reportDate", ""),
                   filed_date=f["filingDate"], tier=5)
        raw_sha = sha256_bytes(data)
        text = html_to_text(data.decode("utf-8", errors="replace")).encode("utf-8")
        _store(manifest, out, url=url, data=text, rel=f"text/{acc}.txt", evidence_id=f"{base}-text",
               kind="derived_text", form=f["form"], accession=acc, period_end=f.get("reportDate", ""),
               filed_date=f["filingDate"], tier=5, derived_from=raw_sha)
    dump_json(manifest, out / "manifest.json")
    return manifest


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True)
    a = ap.parse_args()
    m = acquire(EdgarClient(f"LEMON-ICFR research {a.email}"))
    print(f"manifest entries: {len(m)}")
