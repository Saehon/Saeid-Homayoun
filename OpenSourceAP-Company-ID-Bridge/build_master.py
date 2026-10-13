#!/usr/bin/env python3
import json, re, zipfile, hashlib
from pathlib import Path
import pandas as pd
import requests

ROOT=Path(__file__).resolve().parent
WORK=ROOT/"work"; OUT=ROOT/"output"
WORK.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

OSAP_ZIP=WORK/"signed_predictors_dl_wide.zip"
OSAP_FILE_ID="1avFIMjz_7LoF3p3nO26eqLW5KdRTOdhW"
GVKEY_PERM_URL="https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/main/other/gvkey_permco_permno.pq"
CIK_GVKEY_URL="https://raw.githubusercontent.com/Wenzhi-Ding/Std_Security_Code/main/other/cik_gvkey.pq"
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

def download(url,dest):
    with requests.get(url,stream=True,timeout=120) as r:
        r.raise_for_status()
        with open(dest,"wb") as f:
            for chunk in r.iter_content(8*1024*1024):
                if chunk: f.write(chunk)

def ensure_osap():
    if OSAP_ZIP.exists() and OSAP_ZIP.stat().st_size>100_000_000: return
    import gdown
    out=gdown.download(id=OSAP_FILE_ID,output=str(OSAP_ZIP),quiet=False)
    if not out or not OSAP_ZIP.exists(): raise RuntimeError("OpenSourceAP download failed")

def csv_member(zf):
    members=[m for m in zf.namelist() if m.lower().endswith(".csv") and not m.endswith("/")]
    if not members: raise RuntimeError("No CSV in OpenSourceAP ZIP")
    return max(members,key=lambda m:zf.getinfo(m).file_size)

def extract_december():
    ensure_osap()
    tmp=OUT/"osap_december_2019_2024.csv"
    if tmp.exists(): tmp.unlink()
    total=kept=0; first=True
    with zipfile.ZipFile(OSAP_ZIP) as zf:
        member=csv_member(zf)
        with zf.open(member) as fh:
            for chunk in pd.read_csv(fh,chunksize=50000,low_memory=False):
                total+=len(chunk)
                p=pick(chunk.columns,["permno"])
                ym=pick(chunk.columns,["yyyymm","date","month"])
                if not p or not ym:
                    raise RuntimeError(f"PERMNO/YYYYMM not found. First cols: {list(chunk.columns)[:30]}")
                nym=pd.to_numeric(chunk[ym],errors="coerce")
                mask=(nym//100).isin(YEARS) & ((nym%100)==12)
                sub=chunk.loc[mask].copy()
                if sub.empty: continue
                sub.rename(columns={p:"permno",ym:"yyyymm"},inplace=True)
                sub["permno"]=pd.to_numeric(sub["permno"],errors="coerce").astype("Int64")
                sub["yyyymm"]=pd.to_numeric(sub["yyyymm"],errors="coerce").astype("Int64")
                sub["year"]=(sub["yyyymm"]//100).astype("Int64")
                sub.to_csv(tmp,index=False,mode="a",header=first)
                first=False; kept+=len(sub)
    return tmp,total,kept,member

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
        primary_gv=gvs[0] if gvs else None
        ca=ciks.get(primary_gv,[]) if primary_gv else []
        status=("AMBIGUOUS_GVKEY" if len(gvs)>1 else
                "NO_CIK" if not ca else
                "AMBIGUOUS_CIK" if len(ca)>1 else "UNIQUE_STATIC_MAP")
        rows.append({
            "permno":int(permno),
            "permco_primary":pcs[0] if pcs else pd.NA,
            "permco_all":"|".join(map(str,pcs)),
            "n_permco":len(pcs),
            "gvkey_primary":primary_gv if primary_gv is not None else pd.NA,
            "gvkey_all":"|".join(map(str,gvs)),
            "n_gvkey":len(gvs),
            "cik_primary":ca[0] if ca else pd.NA,
            "cik10_primary":f"{ca[0]:010d}" if ca else "",
            "cik_all":"|".join(map(str,ca)),
            "n_cik":len(ca),
            "id_map_status":status,
        })
    return pd.DataFrame(rows)

def main():
    tmp,total,kept,member=extract_december()
    d=pd.read_csv(tmp,low_memory=False)
    d["permno"]=pd.to_numeric(d["permno"],errors="coerce").astype("Int64")
    m=d.merge(id_map(),on="permno",how="left",validate="m:1")
    m["osap_release"]="202510_v2.0.0"
    m["osap_public_characteristics"]="209_wide_file"
    m["id_bridge_source"]="Wenzhi-Ding/Std_Security_Code_static_snapshot"
    m["publication_link_verification_required"]=1
    m["id_map_status"]=m["id_map_status"].fillna("NO_STATIC_MAP")
    m=m.sort_values(["year","permno"]).drop_duplicates(["year","permno"],keep="last")

    ids=["permno","permco_primary","permco_all","n_permco","gvkey_primary","gvkey_all","n_gvkey",
         "cik_primary","cik10_primary","cik_all","n_cik","id_map_status","yyyymm","year",
         "osap_release","osap_public_characteristics","id_bridge_source",
         "publication_link_verification_required"]
    m=m[[c for c in ids if c in m.columns]+[c for c in m.columns if c not in ids]]

    csv=OUT/"osap_company_id_master_2019_2024.csv"
    gz=OUT/"osap_company_id_master_2019_2024.csv.gz"
    m.to_csv(csv,index=False); m.to_csv(gz,index=False,compression="gzip")
    m.head(100).to_csv(OUT/"sample_100_rows.csv",index=False)

    report={
      "source_rows_scanned":int(total),"december_rows_selected_premerge":int(kept),
      "master_rows":int(len(m)),"master_columns":int(len(m.columns)),
      "year_counts":{str(k):int(v) for k,v in m.groupby("year").size().to_dict().items()},
      "mapping_status_counts":{str(k):int(v) for k,v in m["id_map_status"].value_counts().to_dict().items()},
      "osap_zip_bytes":OSAP_ZIP.stat().st_size,"osap_zip_sha256":sha256(OSAP_ZIP),
      "osap_csv_member":member,"csv_bytes":csv.stat().st_size,"csv_gz_bytes":gz.stat().st_size,
      "csv_sha256":sha256(csv),"coverage_years":[2019,2020,2021,2022,2023,2024],
      "warnings":[
        "Static Std_Security_Code mappings require independent historical verification before publication.",
        "Public OpenSourceAP wide file has 209 characteristics and omits Price, Size, and STreversal.",
        "Annual rows use December observations; temporally align to audit dates before causal or ex-ante tests."
      ]
    }
    (OUT/"validation_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
