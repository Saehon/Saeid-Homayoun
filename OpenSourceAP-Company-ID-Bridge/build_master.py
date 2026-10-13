#!/usr/bin/env python3
import json, re, hashlib, time
from pathlib import Path

import pandas as pd
import requests
from openassetpricing.gdrive_parse import _get_readable_link, _get_name_id_map
from openassetpricing.urls import release202510_url

ROOT=Path(__file__).resolve().parent
WORK=ROOT/"work"; OUT=ROOT/"output"
WORK.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

GVKEY_PERM_URL="https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/main/other/gvkey_permco_permno.pq"
CIK_GVKEY_URL="https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/main/other/cik_gvkey.pq"\nSIGNALDOC_URL="https://raw.githubusercontent.com/OpenSourceAP/CrossSection/master/SignalDoc.csv"
YEARS=set(range(2019,2025))

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
    with requests.get(url,stream=True,timeout=180,allow_redirects=True) as r:
        r.raise_for_status()
        ctype=(r.headers.get("content-type") or "").lower()
        if "text/html" in ctype:
            raise RuntimeError("HTML_RESPONSE")
        with open(dest,"wb") as f:
            for chunk in r.iter_content(4*1024*1024):
                if chunk: f.write(chunk)

def drive_download(url,dest,retries=4):
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
            time.sleep(2*(attempt+1))
    raise RuntimeError(f"Drive download failed after {retries} tries: {last}")

def load_december_signals():
    _, imap_pl=_get_name_id_map(release202510_url)
    imap=imap_pl.to_pandas()
    smap=pd.read_csv(SIGNALDOC_URL,usecols=["Acronym","Sign"])
    sign_map={str(r["Acronym"]):r["Sign"] for _,r in smap.iterrows()}

    signal_col=pick(imap.columns,["signal"])
    url_col=pick(imap.columns,["file_id","url"])
    if not signal_col or not url_col:
        raise RuntimeError(f"Unexpected individual-signal map schema: {list(imap.columns)}")

    base=None
    failures=[]
    loaded=[]
    total_selected=0
    for i,row in imap.iterrows():
        signal=str(row[signal_col])
        url=str(row[url_col])
        tmp=WORK/f"_signal_{i}.csv"
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
            if parts:
                s=pd.concat(parts,ignore_index=True).drop_duplicates(["permno","yyyymm"],keep="last")
                sg=sign_map.get(signal)
                if pd.notna(sg):
                    s[signal]=s[signal]*float(sg)
                s=s.set_index(["permno","yyyymm"])
                base=s if base is None else base.join(s,how="outer")
                total_selected += len(s)
            loaded.append(signal)
        except Exception as e:
            failures.append({"signal":signal,"error":str(e)[:500]})
        finally:
            if tmp.exists(): tmp.unlink()

    if base is None:
        raise RuntimeError("No OpenSourceAP individual signals could be downloaded")

    out=base.reset_index()
    out["year"]=(out["yyyymm"]//100).astype("Int64")
    wide=OUT/"osap_december_2019_2024.csv"
    out.to_csv(wide,index=False)
    meta={
        "source_mode":"individual_public_signal_files",
        "signals_attempted":int(len(imap)),
        "signals_loaded":int(len(loaded)),
        "signals_failed":int(len(failures)),
        "loaded_signals":loaded,
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

def id_map():
    p1=WORK/"gvkey_permco_permno.pq"; p2=WORK/"cik_gvkey.pq"
    if not p1.exists(): download(GVKEY_PERM_URL,p1)
    if not p2.exists(): download(CIK_GVKEY_URL,p2)
    gp=pd.read_parquet(p1); cg=pd.read_parquet(p2)

    pc=pick(gp.columns,["permno","lpermno"]); pcc=pick(gp.columns,["permco","lpermco"]); gc=pick(gp.columns,["gvkey"])
    cgc=pick(cg.columns,["gvkey"]); cc=pick(cg.columns,["cik"])
    if not pc or not gc: raise RuntimeError(f"Bad GVKEY-PERMNO schema: {list(gp.columns)}")
    if not cgc or not cc: raise RuntimeError(f"Bad CIK-GVKEY schema: {list(cg.columns)}")

    gp=gp[[pc]+([pcc] if pcc else [])+[gc]].copy()
    gp.columns=["permno"]+(["permco"] if pcc else [])+["gvkey"]
    for c in ["permno","gvkey"]+(["permco"] if "permco" in gp else []):
        gp[c]=pd.to_numeric(gp[c],errors="coerce").astype("Int64")
    gp=gp.dropna(subset=["permno","gvkey"]).drop_duplicates()

    cg=cg[[cgc,cc]].copy(); cg.columns=["gvkey","cik"]
    for c in ["gvkey","cik"]: cg[c]=pd.to_numeric(cg[c],errors="coerce").astype("Int64")
    cg=cg.dropna().drop_duplicates()
    ciks={int(k):sorted({int(x) for x in g["cik"].dropna()}) for k,g in cg.groupby("gvkey")}

    rows=[]
    for permno,g in gp.groupby("permno"):
        gvs=sorted({int(x) for x in g["gvkey"].dropna()})
        pcs=sorted({int(x) for x in g["permco"].dropna()}) if "permco" in g else []
        gv=gvs[0] if gvs else None
        ca=ciks.get(gv,[]) if gv else []
        status=("AMBIGUOUS_GVKEY" if len(gvs)>1 else "NO_CIK" if not ca else
                "AMBIGUOUS_CIK" if len(ca)>1 else "UNIQUE_STATIC_MAP")
        rows.append({
          "permno":int(permno),"permco_primary":pcs[0] if pcs else pd.NA,
          "permco_all":"|".join(map(str,pcs)),"n_permco":len(pcs),
          "gvkey_primary":gv if gv else pd.NA,"gvkey_all":"|".join(map(str,gvs)),"n_gvkey":len(gvs),
          "cik_primary":ca[0] if ca else pd.NA,"cik10_primary":f"{ca[0]:010d}" if ca else "",
          "cik_all":"|".join(map(str,ca)),"n_cik":len(ca),"id_map_status":status
        })
    return pd.DataFrame(rows)

def main():
    wide,srcmeta=load_december_signals()
    d=pd.read_csv(wide,low_memory=False)
    d["permno"]=pd.to_numeric(d["permno"],errors="coerce").astype("Int64")
    m=d.merge(id_map(),on="permno",how="left",validate="m:1")
    m["osap_release"]="202510_v2.0.0"
    m["osap_public_characteristics_expected"]=209
    m["id_bridge_source"]="Wenzhi-Ding/Std_Security_Code_static_snapshot"
    m["publication_link_verification_required"]=1
    m["id_map_status"]=m["id_map_status"].fillna("NO_STATIC_MAP")
    m=m.sort_values(["year","permno"]).drop_duplicates(["year","permno"],keep="last")

    ids=["permno","permco_primary","permco_all","n_permco","gvkey_primary","gvkey_all","n_gvkey",
         "cik_primary","cik10_primary","cik_all","n_cik","id_map_status","yyyymm","year",
         "osap_release","osap_public_characteristics_expected","id_bridge_source",
         "publication_link_verification_required"]
    m=m[[c for c in ids if c in m.columns]+[c for c in m.columns if c not in ids]]

    csv=OUT/"osap_company_id_master_2019_2024.csv"
    gz=OUT/"osap_company_id_master_2019_2024.csv.gz"
    m.to_csv(csv,index=False); m.to_csv(gz,index=False,compression="gzip")
    m.head(100).to_csv(OUT/"sample_100_rows.csv",index=False)

    report={
      **{k:v for k,v in srcmeta.items() if k not in {"loaded_signals","failed_signals"}},
      "master_rows":int(len(m)),"master_columns":int(len(m.columns)),
      "characteristic_columns":int(len([c for c in m.columns if c not in ids])),
      "year_counts":{str(k):int(v) for k,v in m.groupby("year").size().to_dict().items()},
      "mapping_status_counts":{str(k):int(v) for k,v in m["id_map_status"].value_counts().to_dict().items()},
      "csv_bytes":csv.stat().st_size,"csv_gz_bytes":gz.stat().st_size,
      "csv_sha256":sha256(csv),"coverage_years":[2019,2020,2021,2022,2023,2024],
      "failed_signals":srcmeta["failed_signals"],
      "warnings":[
        "Static Std_Security_Code mappings require independent historical verification before publication.",
        "Public OpenSourceAP characteristics exclude CRSP-only Price, Size, and STreversal.",
        "Annual rows use December observations; align predictors to audit-report dates before ex-ante or causal tests."
      ]
    }
    (OUT/"validation_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
