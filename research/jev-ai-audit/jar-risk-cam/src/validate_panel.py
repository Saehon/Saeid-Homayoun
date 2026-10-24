"""Fail-closed QA for prepared firm-year-account-domain risk/CAM panel.
No training, no regression, no predictions generated. Source: Dr Saeid Homayoun, 2026.
"""
import csv,datetime,math,sys
from pathlib import Path
REQUIRED=('firm_id','fiscal_year','domain','industry','cutoff_date','evidence_available_date',
'cam_present','eligible','risk_probability','outcome_event','outcome_observed_date','icfr_status','accounting_standard')
ICFR={'effective','ineffective','unknown'}
def iso(x):
    return datetime.date.fromisoformat(x)
def validate(rows):
    keys=set(); inspected=0
    for row in rows:
        inspected+=1
        for col in REQUIRED:
            if col not in row:raise ValueError('missing column: '+col)
        k=(row['firm_id'].strip(),row['fiscal_year'],row['domain'].lower().strip())
        if not all(k) or k in keys:raise ValueError('empty or duplicate firm×year×domain key')
        keys.add(k)
        if row['icfr_status'].lower() not in ICFR:raise ValueError('bad icfr status')
        if row['accounting_standard'] not in {'US_GAAP','IFRS','other'}:raise ValueError('bad accounting standard')
        if row['cam_present'] not in {'0','1',''}:raise ValueError('CAM label must be 0,1 or unknown blank')
        if row['eligible'] not in {'0','1'}:raise ValueError('eligible must be 0 or 1')
        c=iso(row['cutoff_date']);e=iso(row['evidence_available_date'])
        if e>c:raise ValueError('LOOKAHEAD: predictor evidence later than cutoff')
        if row['outcome_event'] not in {'0','1',''}:raise ValueError('outcome must be 0,1 or unknown blank')
        if row['outcome_event']!='':
            if not row['outcome_observed_date'] or iso(row['outcome_observed_date'])<=c:
                raise ValueError('future outcome date missing or <= cutoff')
        if row['risk_probability']:
            x=float(row['risk_probability'])
            if not math.isfinite(x) or not 0<=x<=1:raise ValueError('risk score must be finite [0,1]')
    return {'rows_validated':inspected,'keys_unique':len(keys),'mode':'SCHEMA_ONLY','empirical_validity':'NOT_EVALUATED'}
def main(path):
    with open(path,newline='',encoding='utf-8') as f:res=validate(csv.DictReader(f))
    print(res)
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python src/validate_panel.py path/to/prepared.csv')
    main(sys.argv[1])
