#!/usr/bin/env python3
"""Provider-neutral, offline ICFR model comparison reference.

Feeds separately adjudicated event labels to an expanding-time logistic model,
then calibrates only on later VALIDATION events and evaluates on TEST events.
Do NOT mistake demonstration synthetic fixtures for actual audited firm evidence.

Usage:
  python temporal_icfr_baseline.py --features features.csv --labels gold.csv \
       --train-before 2022-12-31 --valid-before 2023-12-31 --out result.json
"""
from __future__ import annotations
import argparse, json, re
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import average_precision_score,brier_score_loss,roc_auc_score

KEYS = ['event_id','cik','public_utc','available_utc']
DENY = ('future','outcome','label','target','post_','return','realized','next_','hindsight')

def verified_inputs(features:pd.DataFrame, labels:pd.DataFrame, train_before:str, valid_before:str):
    if any(key not in features for key in KEYS) or not {'event_id','mw_verified'} <= set(labels.columns):
        raise ValueError('Missing source keys or independently reviewed gold')
    xcols = [c for c in features if c.startswith('feat_')]
    if len(xcols)<2 or any(any(b in col.lower() for b in DENY) for col in xcols):
        raise ValueError('No valid prespecified predictors or likely target leakage')
    if len(features)!=features.event_id.nunique() or len(labels)!=labels.event_id.nunique():
        raise ValueError('Duplicate event IDs')
    if features[xcols].select_dtypes(include='object').shape[1]:
        raise ValueError('Numeric pre-event features only; first build text embeddings offline')
    f=features.copy(); f['public_utc']=pd.to_datetime(f.public_utc,utc=True,errors='raise')
    f['available_utc']=pd.to_datetime(f.available_utc,utc=True,errors='raise')
    if f['public_utc'].isna().any() or f['available_utc'].isna().any():
        raise ValueError('Missing timestamps')
    if (f['available_utc']>f['public_utc']).any():
        raise ValueError('FUTURE_DATA_LEAKAGE: feature not yet public')
    v=f.merge(labels[['event_id','mw_verified']],on='event_id',how='left',validate='one_to_one')
    if v['mw_verified'].isna().any() or not set(v.mw_verified.unique()) <= {0,1}:
        raise ValueError('Unverified/partial outcomes must not silently become controls')
    t=pd.Timestamp(train_before,tz='UTC'); vv=pd.Timestamp(valid_before,tz='UTC')
    if vv<=t: raise ValueError('Validation cutoff must follow train cutoff')
    v['split']=np.where(v.public_utc <= t,'train',np.where(v.public_utc<=vv,'validation','test'))
    return v,xcols

def train_predict(v:pd.DataFrame, xcols:list[str]):
    subsets={s:v.loc[v['split']==s] for s in ('train','validation','test')}
    if any(len(part)<10 or part.mw_verified.nunique()<2 for part in subsets.values()):
        raise ValueError('Need >=10 events and both classes in every split')
    a,b,c=(subsets[s] for s in ('train','validation','test'))
    model=make_pipeline(SimpleImputer(strategy='median'), StandardScaler(),
                        LogisticRegression(max_iter=500,class_weight='balanced',random_state=271828))
    model.fit(a[xcols],a.mw_verified.astype(int))
    pvalid=model.predict_proba(b[xcols])[:,1]
    # Crucial: no test-set adaptation, calibration fit on validation labels only.
    calib=IsotonicRegression(y_min=0.,y_max=1.,out_of_bounds='clip')
    calib.fit(pvalid,b.mw_verified.astype(int))
    raw=model.predict_proba(c[xcols])[:,1]
    pred=np.asarray(calib.predict(raw),dtype=float)
    y=c.mw_verified.astype(int).to_numpy()
    metrics={
      'test_n':len(c),'test_positive_n':int(sum(y)),
      'roc_auc':float(roc_auc_score(y,pred)),
      'pr_auc':float(average_precision_score(y,pred)),
      'brier':float(brier_score_loss(y,pred)),
      'raw_brier':float(brier_score_loss(y,raw)),
      'train_n':len(a),'validation_n':len(b),
    }
    cases=[{'event_id':str(e),'predicted_prob':round(float(p),6),'gold':int(actual)}
           for e,p,actual in zip(c.event_id,pred,y)]
    return {'status':'EXECUTED_ON_USER_SUPPLIED_DATA','method':'logistic + out-of-time isotonic calibration',
            'metrics':metrics,'predictions':cases,
            'disclaimer':'Do not publish as a real finance result unless labels, source rights and provenance have been independently validated.'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--features',required=True)
    p.add_argument('--labels',required=True)
    p.add_argument('--train-before',required=True)
    p.add_argument('--valid-before',required=True)
    p.add_argument('--out',required=True)
    z=p.parse_args()
    features=pd.read_csv(z.features); labels=pd.read_csv(z.labels)
    v,cols=verified_inputs(features,labels,z.train_before,z.valid_before)
    result=train_predict(v,cols)
    with open(z.out,'w',encoding='utf-8') as f: json.dump(result,f,indent=2)
    print(json.dumps(result['metrics'],indent=2))
if __name__=='__main__': main()
