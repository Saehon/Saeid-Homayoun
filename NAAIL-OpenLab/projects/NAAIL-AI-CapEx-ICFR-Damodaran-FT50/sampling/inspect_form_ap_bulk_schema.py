"""Probe complete PCAOB Form AP AuditorSearch downloadable repository before joining to SEC."""
import argparse,csv,io,json,zipfile
from pathlib import Path
from datetime import datetime,timezone
def main(fzip,out):
 out.mkdir(parents=True,exist_ok=True)
 manifest={"source_url":"https://assets.pcaobus.org/firm-filings/FirmFilings.zip",
  "source_page":"https://pcaobus.org/resources/auditorsearch",
  "retrieved_utc":datetime.now(timezone.utc).isoformat(),"members":[]}
 with zipfile.ZipFile(fzip) as z:
  for member in z.infolist():
   rec={"name":member.filename,"uncompressed_size":member.file_size,
        "compressed_size":member.compress_size}
   if member.is_dir():continue
   with z.open(member) as f:chunk=f.read(15000)
   rec["first_120_chars"]=repr(chunk[:120])
   enc=("utf-16" if chunk[:2] in (bytes([255,254]),bytes([254,255]))
        else "utf-16-le" if len(chunk)>8 and chunk[1]==0
        else "utf-8-sig")
   rec["encoding_candidate"]=enc
   if member.filename.lower().endswith((".csv",".txt",".tsv")):
    sample=chunk.decode(enc,errors="replace").splitlines()
    rec["first_lines"]=sample[:3]
    rec["delimiter_candidates"]={k:sample[0].count(k) if sample else 0 for k in [",","\t","|"]}
   manifest["members"].append(rec)
 (out/"FORM_AP_SOURCE_FILE_SCHEMA_PROBE.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
 print(json.dumps(manifest,indent=2))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--zip",required=True,type=Path);p.add_argument("--out",required=True,type=Path);a=p.parse_args();main(a.zip,a.out)
