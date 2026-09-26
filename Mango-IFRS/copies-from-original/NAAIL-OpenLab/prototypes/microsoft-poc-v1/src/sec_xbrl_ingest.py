"""Minimal SEC CompanyFacts retrieval for Microsoft.
Run in a networked environment and comply with SEC fair-access guidance.
"""
import json, urllib.request
URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json"
USER_AGENT = "NAAIL-OpenLab research prototype contact: replace-with-project-email"

def fetch_companyfacts(url=URL):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def latest_fy_value(data, concept, unit="USD", fy=2026):
    facts = data["facts"]["us-gaap"][concept]["units"][unit]
    candidates = [x for x in facts if x.get("fy")==fy and x.get("fp")=="FY" and x.get("form")=="10-K"]
    if not candidates:
        raise KeyError((concept, fy))
    return sorted(candidates, key=lambda x: x["filed"])[-1]
