"""Download small exact source snapshots; inspect schemas, no model fitting."""
import os,io,json,hashlib,requests,pandas as pd
from urllib.parse import quote
os.makedirs('reports',exist_ok=True)
BASE='https://huggingface.co/datasets/'
SOURCES={
 'OpenAP_2026':('OpenSourceAP/CrossSection','dd1054254c4501776432caa6d7ce5ecd9586f6a9','Portfolios/Full Sets OP/PredictorLSretWide.parquet'),
 'OpenAP_2021':('OpenSourceAP/CrossSection','2ef566a3a35fc075ceaf5f6fd01b58d39b25e1b6','Portfolios/Full_Sets_Main/PredictorLSretWide.parquet')}
GRID_SHA='54da7bfaef55bdfb566849be56e9f1d5826798ea'
for name in ['accruals','assetgrowth','bm','mom12m','gp','investment','ep','streversal']:
  SOURCES['TidyGrid_'+name]=('tidy-finance/factor-library-grid',GRID_SHA,'portfolio_sort_grid/'+name+'.parquet')
res={}
for label,(repo,rev,path) in SOURCES.items():
 url=BASE+repo+'/resolve/'+rev+'/'+quote(path,safe='/')
 try:
  r=requests.get(url,timeout=90,headers={'User-Agent':'NOMOS-V6-Data-Audit/1.0'});r.raise_for_status()
  payload=r.content
  df=pd.read_parquet(io.BytesIO(payload))
  result={'url':url,'sha256':hashlib.sha256(payload).hexdigest(),'bytes':len(payload),'shape':list(df.shape),'columns':df.columns.tolist()[:260],'dtypes':{x:str(df[x].dtype) for x in df.columns[:35]},'head':df.head(2).astype(str).to_dict(orient='records'),'tail':df.tail(2).astype(str).to_dict(orient='records')}
  res[label]=result
  print('DATA_PARQUET',label,'shape',result['shape'],'col',result['columns'][:18],'head',str(result['head'])[:400],flush=True)
 except Exception as e:
  res[label]={'url':url,'error':repr(e)}
  print('DATA_ERROR',label,repr(e),flush=True)
with open('reports/parquet_schema_probe.json','w') as f:json.dump(res,f,indent=2)
