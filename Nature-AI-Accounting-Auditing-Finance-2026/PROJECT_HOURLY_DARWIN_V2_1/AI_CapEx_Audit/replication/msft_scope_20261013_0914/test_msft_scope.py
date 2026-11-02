#!/usr/bin/env python3
"""Deterministic tests for hand-transcribed public MSFT ICFR scope evidence.
Not a raw-source extraction or independent replication.
Usage: python test_msft_scope.py [path/to/msft_scope_asof.json]
"""
import datetime as dt
import json
import sys
from pathlib import Path

p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('msft_scope_asof.json')
data=json.loads(p.read_text(encoding='utf-8'))
rows=data['firm_years']
checks=[]
def check(name, condition):
    checks.append((name,bool(condition)))

check('exactly_two_public_firm_years',len(rows)==2)
check('unique_years',len({r['fiscal_year'] for r in rows})==2)
check('years_2024_2025',{r['fiscal_year'] for r in rows}=={2024,2025})
check('cik_is_10_digit',data['cik10']=='0000789019')
check('original_transcription_not_raw_bytes',data['data_class'].startswith('MANUALLY_TRANSCRIBED'))
check('no_raw_source_sha_claim',all(r['source_byte_sha256'] is None for r in rows))
check('official_report_sources',all(r['report_url'].startswith('https://www.microsoft.com/investor/reports/ar') for r in rows))
check('sec_source_accessions',all('sec.gov/Archives/edgar/data/789019/' in r['sec_10k_url'] for r in rows))
check('date_order_asof',all(dt.date.fromisoformat(r['sec_filing_date'])>=dt.date.fromisoformat(r['fiscal_year_end']) for r in rows))
check('fiscal_year_matches_end',all(dt.date.fromisoformat(r['fiscal_year_end']).year==r['fiscal_year'] for r in rows))
check('effective_management_both',all(r['management_icfr']=='EFFECTIVE' for r in rows))
check('effective_auditor_both',all(r['auditor_icfr']=='EFFECTIVE' for r in rows))
r24,r25=sorted(rows,key=lambda r:r['fiscal_year'])
check('2024_explicit_exclusion',r24['scope_exclusion_explicitly_disclosed']==1)
check('2024_acquisition_identified',r24['scope_exclusion_name']=='Activision Blizzard, Inc.')
check('2024_asset_share_strict_lt_one',r24['scope_exclusion_asset_share_upper_bound_pct']==1 and r24['scope_exclusion_asset_share_is_strict_less_than'])
check('2024_revenue_share_two',r24['scope_exclusion_revenue_share_pct']==2)
check('2025_no_exclusion_disclosed',r25['scope_exclusion_explicitly_disclosed']==0 and r25['scope_exclusion_name'] is None)
check('2025_no_invented_exclusion_pct',r25['scope_exclusion_asset_share_upper_bound_pct'] is None and r25['scope_exclusion_revenue_share_pct'] is None)
check('ai_specific_capex_not_imputed',data['ai_specific_capex_usd_m'] is None)
check('no_causal_claim',data['causal_model']=='NOT_RUN')
check('no_independent_replication_claim',data['independent_source_byte_replication']=='NOT_RUN')
check('coding_limitation_explicit','does not certify' in data['coding_note'])
for name,ok in checks:print(('PASS' if ok else 'FAIL')+' '+name)
print(f'TOTAL {sum(ok for _,ok in checks)}/{len(checks)}')
print(f'FIRM_YEARS {len(rows)} | EXPLICIT_EXCLUSIONS {sum(r["scope_exclusion_explicitly_disclosed"] for r in rows)} | UNIQUE_COMPANIES 1')
sys.exit(0 if all(ok for _,ok in checks) else 1)
