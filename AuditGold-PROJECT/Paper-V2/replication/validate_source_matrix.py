#!/usr/bin/env python3
"""Validate the public evidence registry only; does not fetch or run upstream research archives."""
import csv,sys,collections,json,urllib.parse
from pathlib import Path
if len(sys.argv)<2: raise SystemExit('Usage: python validate_source_matrix.py matrix.csv')
with Path(sys.argv[1]).open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
assert len(rows)>=10,'Expected >=10 sources'
assert len({r['source_id'] for r in rows})==len(rows),'Duplicate source identifiers'
for r in rows:
    assert r['journal'] and r['ranking'] and r['source_evidence_tier']
    for col in ('primary_paper_link','replication_asset_link'):
        v=r[col].strip()
        if v: assert urllib.parse.urlparse(v).scheme=='https',f'Non-HTTPS: {v}'
print(json.dumps({'sources':len(rows),'rankings':dict(collections.Counter(r['ranking'] for r in rows)),
 'evidence_tiers':dict(collections.Counter(r['source_evidence_tier'].split(':')[0] for r in rows)),
 'warning':'Metadata-only validation, not independent replication'},indent=2))
