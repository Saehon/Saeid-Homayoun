#!/usr/bin/env python3
"""Archive the MIT-labelled synthetic candidate-matching benchmark from Hugging Face.
Select three small training Parquet files; do not copy embeddings or real user resumes.
"""
import hashlib
import io
import json
from pathlib import Path
import urllib.request
from zipfile import ZipFile, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/"archives"/"dist"
BASE="https://huggingface.co/datasets/michaelozon/candidate-matching-synthetic/resolve/main/"
FILES=[
  "jobs/train-00000-of-00001.parquet",
  "matches/train-00000-of-00001.parquet",
  "resumes/train-00000-of-00001.parquet",
  "README.md",
]
MAX_FILE=2_000_000
def main():
    DEST.mkdir(parents=True,exist_ok=True)
    output=DEST/"DATASETFREE_synthetic_resume_benchmark_MIT.zip"
    ledger={"upstream":"https://huggingface.co/datasets/michaelozon/candidate-matching-synthetic",
            "licence_label":"MIT as stated on source data card",
            "content":"Synthetic LLM-generated candidate and job matching; NOT real Cognism/hiring profiles",
            "files":[]}
    with ZipFile(output,"w",ZIP_DEFLATED) as z:
        for path in FILES:
            url=BASE+path
            request=urllib.request.Request(url,headers={"User-Agent":"DATASETFREE-academic-code-provenance/1.0"})
            with urllib.request.urlopen(request,timeout=40) as response:
                blob=response.read(MAX_FILE+1)
            if len(blob)>MAX_FILE or len(blob)==0:
                raise RuntimeError("Invalid or oversized source file: "+path)
            z.writestr(path,blob)
            ledger["files"].append({"path":path,"url":url,"bytes":len(blob),
                                    "sha256":hashlib.sha256(blob).hexdigest()})
        z.writestr("PROVENANCE.json",json.dumps(ledger,indent=2))
        z.writestr("CITATION_AND_RIGHTS.txt",
          "Derived archive of upstream MIT-labelled synthetic research data.\n"
          "Source: https://huggingface.co/datasets/michaelozon/candidate-matching-synthetic\n"
          "Licensing must still be reviewed before public redistribution. The sample is NOT real workforce data.\n")
    print("Downloaded source files:",len(FILES),"ZIP size:",output.stat().st_size)
    print("SHA256:",hashlib.sha256(output.read_bytes()).hexdigest())
if __name__=="__main__":main()
