"""Optional live SEC CompanyFacts fetch for Microsoft CIK 0000789019.
Not required for offline unit tests.
"""
import json, urllib.request
URL='https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json'

def fetch(user_agent: str):
    if '@' not in user_agent:
        raise ValueError('Use an SEC-compliant User-Agent including contact information.')
    req=urllib.request.Request(URL, headers={'User-Agent':user_agent,'Accept-Encoding':'gzip, deflate'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
