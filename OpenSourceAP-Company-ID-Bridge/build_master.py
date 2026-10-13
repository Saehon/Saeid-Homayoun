#!/usr/bin/env python3
import json, re, hashlib, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import pandas as pd
import requests
from openassetpricing.gdrive_parse import _get_readable_link, _get_name_id_map
from openassetpricing.urls import release202510_url

ROOT=Path(__file__).resolve().parent
WORK=ROOT/"work"; OUT=ROOT/"output"
WORK.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

STD_COMMIT="472825305c986d241ee04ce882a037d5118f733b"
OSAP_SIGNALDOC_COMMIT="8db892442c2c3a3779b0f1eac4370d3655be15a1"
GVKEY_PERM_URL=f"https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/{STD_COMMIT}/other/gvkey_permco_permno.pq"
CIK_GVKEY_URL=f"https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/{STD_COMMIT}/other/cik_gvkey.pq"
SIGNALDOC_URL=f"https://raw.githubusercontent.com/OpenSourceAP/CrossSection/{OSAP_SIGNALDOC_COMMIT}/SignalDoc.csv"
YEARS=set(range(2019,2025))
MAX_WORKERS=6

def norm(c): return re.sub(r"[^a-z0-9]+","",str(c).lower())

def pick(cols,cands):
    m={norm(c):c for c in cols}
    for x in cands:
        if norm(x) in m: return m[norm(x)]
    return None

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(2**20),b""): h.update(b)
    return h.hexdigest()

def stream_download(url,dest):
    with requests.get(url,stream=True,timeout=120,allow_redirects=True) as r:
        r.raise_for_status()
        ctype=(r.headers.get("content-type") or "").lower()
        if "text/html" in ctype:
            raise RuntimeError("HTML_RESPONSE")
        with open(dest,"wb") as f:
            for chunk in r.iter_content(4*1024*1024):
                if chunk: f.write(chunk)

def drive_download(url,dest,retries=5):
    last=None
    for attempt in range(retries):
        try:
            try:
                stream_download(url,dest)
            except RuntimeError as e:
                if str(e)!="HTML_RESPONSE": raise
                readable=_get_readable_link(url)
                stream_download(readable,dest)
            if dest.exists() and dest.stat().st_size>20:
                return
        except Exception as e:
            last=e
            if dest.exists(): dest.unlink()
            time.sleep(min(20,2*(attempt+1)))
    raise RuntimeError(f"Drive download failed after {retries} tries: {last}")

def _empty_signal_frame(signal):
    idx=pd.MultiIndex.from_arrays([[],[]],names=["permno","yyyymm"])
    return pd.DataFrame(index=idx,columns=[signal],dtype=float)

def _process_signal(args):
    i,signal,url,sg=args
    safe=re.sub(r"[^A-Za-z0-9_.-]+","_",signal)[:80]
    tmp=WORK/f"_signal_{i}_{safe}.csv"
    try:
        drive_download(url,tmp)
        parts=[]
        for ch in pd.read_csv(tmp,chunksize=250_000,low_memory=False):
            p=pick(ch.columns,["permno"])
            ym=pick(ch.columns,["yyyymm","date","month"])
            val=pick(ch.columns,[signal])
            if val is None:
                other=[c for c in ch.columns if c not in {p,ym}]
                if len(other)==1: val=other[0]
            if not p or not ym or not val:
                raise RuntimeError(f"Schema not recognized for {signal}: {list(ch.columns)}")
            nym=pd.to_numeric(ch[ym],errors="coerce")
            mask=(nym//100).isin(YEARS) & ((nym%100)==12)
            sub=ch.loc[mask,[p,ym,val]].copy()
            if sub.empty: continue
            sub.columns=["permno","yyyymm",signal]
            sub["permno"]=pd.to_numeric(sub["permno"],errors="coerce").astype("Int64")
            sub["yyyymm"]=pd.to_numeric(sub["yyyymm"],errors="coerce").astype("Int64")
            sub[signal]=pd.to_numeric(sub[signal],errors="coerce")
            parts.append(sub)
        if not parts:
            return signal,_empty_signal_frame(signal),0,None
        s=pd.concat(parts,ignore_index=True).drop_duplicates(["permno","yyyymm"],keep="last")
        if pd.notna(sg):
            s[signal]=s[signal]*float(sg)
        s=s.set_index(["permno","yyyymm"])
        return signal,s,len(s),None
    except Exception as e:
        return signal,None,0,str(e)[:700]
    finally:
        if tmp.exists(): tmp.unlink()

def load_december_signals():
    _,imap_pl=_get_name_id_map(release202510_url)
    imap=imap_pl.to_pandas()
    smap=pd.read_csv(SIGNALDOC_URL,usecols=["Acronym","Sign"])
    sign_map={str(r["Acronym"]):r["Sign"] for _,r in smap.iterrows()}

    signal_col=pick(imap.columns,["signal"])
    url_col=pick(imap.columns,["file_id","url"])
    if not signal_col or not url_col:
        raise RuntimeError(f"Unexpected individual-signal map schema: {list(imap.columns)}")

    tasks=[]
    for i,row in imap.iterrows():
        signal=str(row[signal_col])
        tasks.append((i,signal,str(row[url_col]),sign_map.get(signal)))

    frames={}
    failures=[]
    total_selected=0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures={ex.submit(_process_signal,t):t[1] for t in tasks}
        done=0
        for fut in as_completed(futures):
            signal,frame,nrows,err=fut.result()
            done+=1
            if err:
                failures.append({"signal":signal,"error":err})
                print(f"[{done}/{len(tasks)}] FAIL {signal}: {err}",flush=True)
            else:
                frames[signal]=frame
                total_selected+=nrows
                print(f"[{done}/{len(tasks)}] OK {signal}: {nrows} December rows",flush=True)

    ordered=[]
    for _,row in imap.iterrows():
        signal=str(row[signal_col])
        if signal in frames:
            ordered.append(frames[signal])
    if not ordered:
        raise RuntimeError("No OpenSourceAP individual signals could be downloaded")

    base=pd.concat(ordered,axis=1,join="outer")
    out=base.reset_index()
    out["year"]=(out["yyyymm"]//100).astype("Int64")
    wide=OUT/"osap_december_2019_2024.csv"
    out.to_csv(wide,index=False)

    meta={
      "source_mode":"individual_public_signal_files",
      "signals_attempted":int(len(tasks)),
      "signals_loaded":int(len(frames)),
      "signals_failed":int(len(failures)),
      "loaded_signals":[str(row[signal_col]) for _,row in imap.iterrows() if str(row[signal_col]) in frames],
      "failed_signals":failures,
      "december_key_rows":int(len(out)),
      "signal_row_fragments_selected":int(total_selected)
    }
    (OUT/"signal_download_report.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    return wide,meta

def download(url,dest):
    with requests.get(url,stream=True,timeout=180) as r:
        r.raise_for_status()
        with open(dest,"wb") as f:
            for chunk in r.iter_content(4*1024*1024):
                if chunk: f.write(chunk)

def _fmt(v):
    return "" if pd.isna(v) else str(int(v))

def id_map():
    p1=WORK/"gvkey_permco_permno.pq"; p2=WORK/"cik_gvkey.pq"
    if not p1.exists(): download(GVKEY_PERM_URL,p1)
    if not p2.exists(): download(CIK_GVKEY_URL,p2)
    bridge_meta={
      "std_security_code_commit":STD_COMMIT,
      "gvkey_permco_permno_sha256":sha256(p1),
      "cik_gvkey_sha256":sha256(p2),
      "bridge_retrieved_utc":datetime.now(timezone.utc).isoformat()
    }

    gp=pd.read_parquet(p1); cg=pd.read_parquet(p2)
    pc=pick(gp.columns,["permno","lpermno"])
    pcc=pick(gp.columns,["permco","lpermco"])
    gc=pick(gp.columns,["gvkey"])
    cgc=pick(cg.columns,["gvkey"]); cc=pick(cg.columns,["cik"])
    if not pc or not gc: raise RuntimeError(f"Bad GVKEY-PERMNO schema: {list(gp.columns)}")
    if not cgc or not cc: raise RuntimeError(f"Bad CIK-GVKEY schema: {list(cg.columns)}")

    gp=gp[[pc]+([pcc] if pcc else [])+[gc]].copy()
    gp.columns=["permno"]+(["permco"] if pcc else [])+["gvkey"]
    if "permco" not in gp: gp["permco"]=pd.NA
    for c in ["permno","permco","gvkey"]:
        gp[c]=pd.to_numeric(gp[c],errors="coerce").astype("Int64")
    gp=gp.dropna(subset=["permno","gvkey"]).drop_duplicates()

    cg=cg[[cgc,cc]].copy(); cg.columns=["gvkey","cik"]
    for c in ["gvkey","cik"]:
        cg[c]=pd.to_numeric(cg[c],errors="coerce").astype("Int64")
    cg=cg.dropna(subset=["gvkey"]).drop_duplicates()

    bridge=gp.merge(cg,on="gvkey",how="left",validate="m:m").drop_duplicates()
    rows=[]
    for permno,g in bridge.groupby("permno"):
        tuples=sorted({
          (_fmt(r.permco),_fmt(r.gvkey),_fmt(r.cik))
          for r in g.itertuples(index=False)
        })
        pcs=sorted({x[0] for x in tuples if x[0]})
        gvs=sorted({x[1] for x in tuples if x[1]})
        ciks=sorted({x[2] for x in tuples if x[2]})
        unique=(len(tuples)==1 and bool(tuples[0][1]))
        if unique:
            pc0,gv0,cik0=tuples[0]
        else:
            pc0=gv0=cik0=""
        if not tuples:
            status="NO_STATIC_MAP"
        elif len(tuples)>1:
            status="AMBIGUOUS_STATIC_MAP"
        elif not tuples[0][2]:
            status="NO_CIK"
        else:
            status="UNIQUE_STATIC_MAP"
        rows.append({
          "permno":int(permno),
          "permco_primary":int(pc0) if pc0 else pd.NA,
          "permco_all":"|".join(pcs),"n_permco":len(pcs),
          "gvkey_primary":int(gv0) if gv0 else pd.NA,
          "gvkey_all":"|".join(gvs),"n_gvkey":len(gvs),
          "cik_primary":int(cik0) if cik0 else pd.NA,
          "cik10_primary":f"{int(cik0):010d}" if cik0 else "",
          "cik_all":"|".join(ciks),"n_cik":len(ciks),
          "n_link_tuples":len(tuples),
          "link_tuples":";".join("|".join(x) for x in tuples),
          "id_map_status":status
        })
    return pd.DataFrame(rows),bridge_meta

def main():
    wide,srcmeta=load_december_signals()
    d=pd.read_csv(wide,low_memory=False)
    d["permno"]=pd.to_numeric(d["permno"],errors="coerce").astype("Int64")
    ids,bridge_meta=id_map()
    m=d.merge(ids,on="permno",how="left",validate="m:1")
    m["osap_release"]="202510_v2.0.0"
    m["osap_public_characteristics_expected"]=209
    m["id_bridge_source"]=f"Wenzhi-Ding/Std_Security_Code@{STD_COMMIT}"
    m["publication_link_verification_required"]=1
    m["id_map_status"]=m["id_map_status"].fillna("NO_STATIC_MAP")
    m=m.sort_values(["year","permno"]).drop_duplicates(["year","permno"],keep="last")

    idcols=[
      "permno","permco_primary","permco_all","n_permco",
      "gvkey_primary","gvkey_all","n_gvkey",
      "cik_primary","cik10_primary","cik_all","n_cik",
      "n_link_tuples","link_tuples","id_map_status","yyyymm","year",
      "osap_release","osap_public_characteristics_expected",
      "id_bridge_source","publication_link_verification_required"
    ]
    m=m[[c for c in idcols if c in m.columns]+[c for c in m.columns if c not in idcols]]

    csv=OUT/"osap_company_id_master_2019_2024.csv"
    gz=OUT/"osap_company_id_master_2019_2024.csv.gz"
    m.to_csv(csv,index=False)
    m.to_csv(gz,index=False,compression="gzip")
    m.head(100).to_csv(OUT/"sample_100_rows.csv",index=False)

    observed_years=sorted(int(x) for x in m["year"].dropna().unique())
    characteristic_cols=[c for c in m.columns if c not in idcols]
    report={
      **{k:v for k,v in srcmeta.items() if k not in {"loaded_signals","failed_signals"}},
      **bridge_meta,
      "open_source_ap_signal_doc_commit":OSAP_SIGNALDOC_COMMIT,
      "build_utc":datetime.now(timezone.utc).isoformat(),
      "master_rows":int(len(m)),
      "master_columns":int(len(m.columns)),
      "characteristic_columns":int(len(characteristic_cols)),
      "year_counts":{str(k):int(v) for k,v in m.groupby("year").size().to_dict().items()},
      "mapping_status_counts":{str(k):int(v) for k,v in m["id_map_status"].value_counts().to_dict().items()},
      "csv_bytes":csv.stat().st_size,
      "csv_gz_bytes":gz.stat().st_size,
      "csv_sha256":sha256(csv),
      "coverage_years":observed_years,
      "requested_years":sorted(YEARS),
      "failed_signals":srcmeta["failed_signals"],
      "warnings":[
        "Std_Security_Code mappings are static snapshots and require independent historical verification before publication.",
        "Ambiguous static mappings deliberately leave primary identifier fields blank and preserve all source link tuples.",
        "Public OpenSourceAP characteristics exclude CRSP-only Price, Size, and STreversal.",
        "Annual rows use December observations; align predictors to audit-report dates before ex-ante or causal tests."
      ]
    }
    (OUT/"validation_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

    if observed_years != sorted(YEARS):
        raise RuntimeError(f"Incomplete year coverage: observed {observed_years}, expected {sorted(YEARS)}")
    if srcmeta["signals_failed"] != 0:
        raise RuntimeError(f"Incomplete signal build: {srcmeta['signals_failed']} downloads failed")
    if len(characteristic_cols) < 209:
        raise RuntimeError(f"Expected at least 209 public characteristics, found {len(characteristic_cols)}")

if __name__=="__main__":
    main()
