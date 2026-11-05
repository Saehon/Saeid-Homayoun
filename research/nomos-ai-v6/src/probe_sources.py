"""Bounded HTTP metadata probe. No credentials or CRSP/Compustat raw data."""
from __future__ import annotations
import json, datetime, requests, os, sys
from urllib.parse import quote
R=requests.Session();R.headers.update({'User-Agent':'NOMOS-V6-Academic-Data-Validation/1.0'})
BASE='https://huggingface.co/api/datasets'
def jget(url, timeout=50):
    r=R.get(url,timeout=timeout);r.raise_for_status();return r.json()
def tree(repo,revision='main',path='',limit=300):
    url=f'{BASE}/{repo}/tree/{quote(revision,safe="")}'
    if path: url+='/'+quote(path,safe='/')
    obj=jget(url,60)
    return [{'path':z.get('path'),'type':z.get('type'),'size':z.get('size')} for z in obj[:limit]]
def meta(repo,rev='main'):
    o=jget(f'{BASE}/{repo}/revision/{quote(rev,safe="")}')
    return {'sha':o.get('sha'),'lastModified':o.get('lastModified'),'license':((o.get('cardData') or {}).get('license')),'siblings_n':len(o.get('siblings') or []),'siblings_sample':[(z.get('rfilename'),z.get('size')) for z in (o.get('siblings') or [])[:9]]}
def run():
    out={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':{},'errors':[]}
    sources=[('OpenAP_main','OpenSourceAP/CrossSection','main'),('OpenAP_2026','OpenSourceAP/CrossSection','Data-Release-2026.10'),('OpenAP_2021','OpenSourceAP/CrossSection','2021.03'),('Tidy_Returns','tidy-finance/factor-library','main'),('Tidy_Grid','tidy-finance/factor-library-grid','main'),('Tidy_Costs','tidy-finance/factor-library-costs','main')]
    for label,repo,rev in sources:
      x={'repo':repo,'revision':rev}
      for what in ['meta','tree']:
        try:x[what]=(meta(repo,rev) if what=='meta' else tree(repo,rev))
        except Exception as e:x[what+'_error']=repr(e);out['errors'].append({'label':label,'what':what,'error':repr(e)})
      out['sources'][label]=x
      print('SOURCE_PROBE',label,json.dumps(x,ensure_ascii=False)[:10000],flush=True)
    # Enumerate release branch and tag names from Hub refs API; essential for PIT assessment.
    try:
      refs=jget(BASE+'/OpenSourceAP/CrossSection/refs')
      out['openap_refs']={k:[{'name':q.get('name'),'targetCommit':q.get('targetCommit')} for q in v[:40]] for k,v in refs.items() if isinstance(v,list)}
      print('OPENAP_REFS',json.dumps(out['openap_refs'])[:10000],flush=True)
    except Exception as e:out['openap_refs_error']=repr(e)
    # Probe OpenAP root directories selectively; bounded, fail individually.
    for rev in ('main','Data-Release-2026.10','2021.03'):
      for path in ('Portfolios','Portfolios/Full Sets OP','Portfolios/Full Sets Alt','Portfolios/Full_Sets_Main','Portfolios/Full_Sets_Extended'):
        try:
            x=tree('OpenSourceAP/CrossSection',rev,path,50)
            if x:
              out.setdefault('OpenAP_subdirectories',{})[rev+'/'+path]=x
              print('OPENAP_DIR',rev,path,json.dumps(x)[:7000],flush=True)
        except Exception: pass
    
    for repo, path in [('tidy-finance/factor-library','costs'),('tidy-finance/factor-library-grid','portfolio_sort_grid')]:
      try:
        z=tree(repo,'main',path,100)
        out.setdefault('tidy_subdirectories',{})[repo+'/'+path]=z
        print('TIDY_DIR',repo,path,json.dumps(z[:50])[:7000],flush=True)
      except Exception as e:out.setdefault('tidy_errors',[]).append(repr(e))
    with open('reports/source_probe.json','w') as f:json.dump(out,f,indent=2)
    print('SOURCE_PROBE_DONE',len(out['sources']),len(out['errors']))
if __name__=='__main__':run()
