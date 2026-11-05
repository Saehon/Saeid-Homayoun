"""NOMOS V6: data provenance, schema and chronology validation only.

Never fits or evaluates a financial decision policy. 2026 snapshot is retrospectively
compiled and NOT point-in-time for historical 2021-25 investment decisions.
"""
from __future__ import annotations
import argparse, hashlib, io, json, os, re, zipfile
from pathlib import Path
from urllib.parse import quote
import numpy as np
import pandas as pd
import requests

OPENAP_REPO='OpenSourceAP/CrossSection'
REV26='dd1054254c4501776432caa6d7ce5ecd9586f6a9'  # Data-Release-2026.10
REV21='2ef566a3a35fc075ceaf5f6fd01b58d39b25e1b6'  # 2021.03
TIDY_REV='31887641d9df6aeeeb901c985edf3fe370dc59f7'
GRID_REV='54da7bfaef55bdfb566849be56e9f1d5826798ea'
OP26='Portfolios/Full Sets OP/PredictorLSretWide.parquet'
OP21='Portfolios/Full_Sets_Main/PredictorLSretWide.parquet'
FF_URL='https://mba.tuck.dartmouth.edu/pages/Faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip'
SIGNAL_MAP={'Accruals':'accruals','AssetGrowth':'assetgrowth','BM':'bm','Mom12m':'mom12m',
            'GP':'gp','Investment':'investment','EP':'ep','STreversal':'streversal'}
FF5=['Mkt-RF','SMB','HML','RMW','CMA','RF']


def file_url(repo,rev,path):
    return f'https://huggingface.co/datasets/{repo}/resolve/{rev}/{quote(path,safe="/")}'

def download(url, max_bytes=70_000_000):
    with requests.get(url,timeout=75,stream=True,headers={'User-Agent':'NOMOS-V6-Scientific-Data-Quality/1.0'}) as resp:
        resp.raise_for_status();parts=[];size=0
        for chunk in resp.iter_content(2**20):
            size+=len(chunk)
            if size>max_bytes:raise ValueError('Download exceeded bounded per-file allowance')
            parts.append(chunk)
    return b''.join(parts)

def read_snapshot(blob,signals=SIGNAL_MAP):
    p=pd.read_parquet(io.BytesIO(blob))
    assert 'date' in p and all(c in p for c in signals),'Expected OpenAP columns absent'
    dates=pd.to_datetime(p['date'],errors='raise').dt.to_period('M').dt.to_timestamp()
    out=p[list(signals)].apply(pd.to_numeric,errors='coerce')/100.0  # OpenAP LS file quoted in PERCENT
    out.index=pd.DatetimeIndex(dates.to_numpy());out.index.name='date'
    if out.index.has_duplicates:raise ValueError('Duplicated OpenAP months')
    out=out.sort_index()
    if (out.abs().max().max()>10):raise ValueError('Unreasonable monthly return or unit mismatch')
    return out

def read_ff5(blob):
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        names=[x for x in z.namelist() if x.lower().endswith('.csv')]
        if len(names)!=1:raise ValueError('Ambiguous FF5 archive')
        lines=z.read(names[0]).decode('utf-8-sig',errors='replace').splitlines()
    header=next((i for i,x in enumerate(lines) if x.strip().startswith(',Mkt-RF,')),None)
    if header is None:raise ValueError('No FF5 monthly header')
    rows=[]
    for x in lines[header+1:]:
        bits=[q.strip() for q in x.split(',')]
        if len(bits)!=7 or not re.fullmatch(r'\d{6}',bits[0]):break
        rows.append([pd.to_datetime(bits[0],format='%Y%m')]+[float(q)/100.0 for q in bits[1:]])
    df=pd.DataFrame(rows,columns=['date']+FF5).set_index('date').sort_index()
    if df.index.has_duplicates or not len(df):raise ValueError('Bad FF5 time index')
    return df

def select_spec(grid):
    """Precommitted, return-independent choice using only grid metadata.
    This Tidy specification is NOT identical to OpenAP original paper returns.
    """
    keep=grid[(grid['sorting_method']=='univariate')&(grid['weighting_scheme']=='VW')&
              (grid['rebalancing']=='monthly')&(grid['breakpoints_exchanges']=='NYSE')].copy()
    if keep.empty:raise ValueError('No deterministic Tidy benchmark specification')
    keep['rank_lag']=keep.sorting_variable_lag.map({'ff':0,'6m':1,'3m':2,'1m':3}).fillna(4)
    keep['rank_n']=abs(pd.to_numeric(keep['n_portfolios_main'])-5)
    keep['rank_sz']=keep['min_size_quantile'].notna().astype(int)
    keep['rank_excl']=keep[['exclude_financials','exclude_utilities','exclude_negative_book_equity','exclude_negative_earnings']].fillna(False).sum(axis=1)
    keep=keep.sort_values(['rank_lag','rank_n','rank_sz','rank_excl','id'])
    return keep.iloc[0].drop(labels=['rank_lag','rank_n','rank_sz','rank_excl']).to_dict()

def tidy_chunk(idnum,folder=''):
    lo=((int(idnum)-1)//1000)*1000+1;hi=lo+999
    return folder+f'id_{lo:07d}-{hi:07d}.parquet'

def no_future_features(panel,columns=None):
    """Feature in month t MUST use at most finalized month t-1.
    Does not itself prove historical publication-time vintage availability.
    """
    cols=list(columns or panel.columns)
    out=pd.DataFrame(index=panel.index)
    for c in cols:out['lag1_'+c]=panel[c].shift(1)
    return out

def audit(panel,series_cols,period_start='2021-01-01',period_end='2025-12-01'):
    if panel.index.has_duplicates or not panel.index.is_monotonic_increasing:raise ValueError('Nonunique or unsorted panel index')
    expected=pd.date_range(period_start,period_end,freq='MS')
    ix=panel.loc[period_start:period_end]
    return {'months_expected':len(expected),'months_present':len(ix),
            'missing_months':len(expected.difference(ix.index)),
            'start':str(ix.index.min().date()) if len(ix) else None,
            'end':str(ix.index.max().date()) if len(ix) else None,
            'duplicate_dates':int(panel.index.duplicated().sum()),
            'na_rate_by_signal':{k:round(float(ix[k].isna().mean()),6) for k in series_cols},
            'nonfinite_by_signal':{k:int(np.isinf(ix[k].to_numpy(dtype=float)).sum()) for k in series_cols}}

def build(out_dir='reports',enable_tidy=True):
    out_dir=Path(out_dir);out_dir.mkdir(parents=True,exist_ok=True)
    evidence={'phase':'V6 Phase 1 — Data Validation','status':'RESEARCH_DATA_AUDIT',
              'evidence_type':'public_revised_historical_data','point_in_time_verified':False,
              'notes':['No decision policy is trained or tested in this phase',
                       'OpenAP 2026 release retrospective: historical publication-time not proven',
                       'Tidy portfolio specifications may differ from OpenAP original methods',
                       'No inference-cost estimation or trading-profits claim'],
              'sources':{},'tidy':{'specs':{},'coverage':{},'errors':[]}}
    cache={}
    def get(label,url):
        if url in cache:return cache[url]
        b=download(url);cache[url]=b
        evidence['sources'][label]={'url':url,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
        return b
    new=read_snapshot(get('OpenAP_2026',file_url(OPENAP_REPO,REV26,OP26)))
    old=read_snapshot(get('OpenAP_2021',file_url(OPENAP_REPO,REV21,OP21)))
    ff=read_ff5(get('French_FF5',FF_URL))
    # Avoid date column type mismatch. This is a research PANEL, NOT a historical PIT investment universe.
    merged=new.join(ff,how='inner',validate='one_to_one')
    merged=merged.loc['2021-01-01':'2025-12-01']
    cols=list(SIGNAL_MAP)
    # The 2026 snapshot is in percentage units and all series here are converted to decimal monthly returns.
    qa=audit(merged,cols)
    ix=merged.index
    qa['french_missing_by_factor']={x:round(float(merged[x].isna().mean()),6) for x in FF5}
    qa['openap_2026_full_start']=str(new.index.min().date());qa['openap_2026_full_end']=str(new.index.max().date())
    qa['openap_2021_full_start']=str(old.index.min().date());qa['openap_2021_full_end']=str(old.index.max().date())
    qa['french_full_end']=str(ff.index.max().date())
    overlap=new.join(old,lsuffix='_v26',rsuffix='_v21',how='inner')
    qa['vintage_months_overlap']=len(overlap)
    qa['historical_revision_by_signal']={s:{'common_n':int(overlap[[s+'_v26',s+'_v21']].dropna().shape[0]),
          'mean_abs_difference_pct_points':float((overlap[s+'_v26']-overlap[s+'_v21']).abs().mean()*100)} for s in cols}
    # Pre-decision signals based on previous month's published *realization*, but release vintage still not PIT.
    all_eligible=new.join(ff,how='inner',validate='one_to_one')
    lag=no_future_features(all_eligible,cols+FF5).loc['2021-01-01':'2025-12-01']
    full=merged.join(lag,validate='one_to_one')
    qa['lag1_feature_na_rate']={c:round(float(full['lag1_'+c].isna().mean()),6) for c in cols+FF5}
    full.insert(0,'historical_pit_verified',False)
    full.insert(1,'data_release','OpenAP_2026.10_revised')
    full.to_csv(out_dir/'v6_revised_openap_ff5_2021_2025.csv',float_format='%.10g')
    evidence['core_quality']=qa
    if enable_tidy:
      tidy_frames=[]
      for signal,slug in SIGNAL_MAP.items():
       try:
        gridblob=get('TidyGrid_'+signal,file_url('tidy-finance/factor-library-grid',GRID_REV,'portfolio_sort_grid/'+slug+'.parquet'))
        grd=pd.read_parquet(io.BytesIO(gridblob));spec=select_spec(grd)
        idn=int(spec['id']);evidence['tidy']['specs'][signal]={k:(None if pd.isna(v) else v.item() if isinstance(v,np.generic) else v) for k,v in spec.items()}
        re_path=tidy_chunk(idn);co_path=tidy_chunk(idn,'costs/')
        returns=pd.read_parquet(io.BytesIO(get('TidyReturns_'+signal,file_url('tidy-finance/factor-library',TIDY_REV,re_path))))
        costs=pd.read_parquet(io.BytesIO(get('TidyCosts_'+signal,file_url('tidy-finance/factor-library',TIDY_REV,co_path))))
        if 'id' not in returns.columns or 'id' not in costs.columns:raise ValueError('Missing Tidy id column')
        ret=returns[returns.id==idn].copy();cost=costs[costs.id==idn].copy()
        keys=['id'];
        if 'date' in returns and 'date' in costs:keys+=['date']
        if 'ret_type' in returns and 'ret_type' in costs:keys+=['ret_type']
        # Match VW construction and explicit dates, fail rather than infer unknown cost grain.
        if 'ret_type' in ret:ret=ret[ret.ret_type=='vw'];cost=cost[cost.ret_type=='vw']
        if 'date' not in ret:raise ValueError('Tidy return date missing')
        ret['month']=pd.to_datetime(ret.date).dt.to_period('M').dt.to_timestamp()
        cost['month']=pd.to_datetime(cost.date).dt.to_period('M').dt.to_timestamp() if 'date' in cost else pd.NaT
        if ret.month.duplicated().any() or cost.month.duplicated().any():raise ValueError('Duplicate Tidy monthly series')
        rc=ret.merge(cost.drop(columns=['id','date','ret_type'],errors='ignore'),on='month',how='left',validate='one_to_one',suffixes=('','_cost'))
        fields=['month']+[v for v in rc if v not in ['id','date','ret_type','sorting_variable','sorting_variable_lag','month']]
        use=rc[fields].copy()
        rename={c:'tidy_'+signal+'_'+c for c in use.columns if c!='month'}
        use=use.rename(columns=rename).set_index('month')
        use=use.loc['2021-01-01':'2024-12-01']
        evidence['tidy']['coverage'][signal]={'id':idn,'rows_2021_2024':len(use),'observed_min':str(use.index.min().date()) if len(use) else None,
          'observed_max':str(use.index.max().date()) if len(use) else None,
          'null_rates':{x:round(float(use[x].isna().mean()),5) for x in use.columns}}
        tidy_frames.append(use)
        print('TIDY_OK',signal,idn,'months',len(use),'fields',list(use.columns),flush=True)
       except Exception as e:
        evidence['tidy']['errors'].append({'signal':signal,'error':repr(e)})
        print('TIDY_ERROR',signal,repr(e),flush=True)
      if tidy_frames:
        dt=pd.concat(tidy_frames,axis=1)
        joined=merged.join(dt,how='inner',validate='one_to_one')
        joined.index.name='date'
        joined.to_csv(out_dir/'v6_auxiliary_tidy_costs_2021_2024.csv',float_format='%.10g')
        evidence['tidy']['joined_months']=len(joined)
        evidence['tidy']['joined_months_start']=str(joined.index.min().date()) if len(joined) else None
        evidence['tidy']['joined_months_end']=str(joined.index.max().date()) if len(joined) else None
    evidence['quality_gate']={'structural_integrity':'PASS' if qa['duplicate_dates']==0 and qa['missing_months']==0 and all(v==0 for v in qa['nonfinite_by_signal'].values()) else 'FAIL',
        'publication_time_vintage':'FAIL_NOT_ESTABLISHED',
        'all_8_tidy_cost_series':'PASS' if len(evidence['tidy']['coverage'])==8 and all(e['rows_2021_2024']>=36 for e in evidence['tidy']['coverage'].values()) else 'PARTIAL_OR_FAIL',
        'trading_cost_equivalence_to_openap':'NOT_ESTABLISHED',
        'ready_for_prospective_V6_finance_backtest':False}
    with open(out_dir/'v6_quality_report.json','w') as f:json.dump(evidence,f,indent=2,default=str)
    print('NOMOS_V6_PHASE1_RESULT',json.dumps({'quality':qa,'tidy_coverage':evidence['tidy']['coverage'],
       'tidy_errors':evidence['tidy']['errors'],'gates':evidence['quality_gate']},default=str)[:17000],flush=True)
    return evidence

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',default='reports');p.add_argument('--no-tidy',action='store_true')
    args=p.parse_args();build(args.out,not args.no_tidy)
