#!/usr/bin/env python3
"""Build a provenance-logged code-only ZIP from two verified-licence projects.
Does not execute third-party Python code or include survey/persona/raw datasets.
"""
import hashlib, json, subprocess, tempfile
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "archives" / "dist"
SOURCES = [
    ("MacAma", "https://github.com/YilinYuan/MacAma.git", "MIT", "MIT License"),
    ("Twin-2K-500", "https://github.com/tianyipeng-lab/Digital-Twin-Simulation.git", "Apache-2.0", "Apache License")
]
EXCLUDED = {".git","data","raw","dataset","datasets","cache","personas","text_personas","text_questions","text_simulation_input","text_simulation_output","surveys","survey","notebooks","results","outputs","participants","responses","images","assets",".github",
    "meta_env","venv",".venv","site-packages","lib","node_modules","vendor","third_party","__pycache__","dist","build"}
CODE_TYPES = {".py",".sh",".toml",".yml",".yaml"}

def keep(file, base):
    parts = file.relative_to(base).parts
    if any(x.lower() in EXCLUDED or x.startswith(".") for x in parts[:-1]):
        return False
    if file.name in {"LICENSE","LICENSE.md","NOTICE","NOTICE.md","README.md"}: return True
    return file.suffix.lower() in CODE_TYPES and not file.name.startswith(".")

def main():
    DEST.mkdir(parents=True,exist_ok=True)
    out = DEST / "DATASETFREE_open_licensed_code_ONLY.zip"
    ledger = {"status":"CODE ONLY SUBSET; NO EMPIRICAL DATA","sources":[],"files":[],"omitted_oversize_or_cap":[]}
    total = 0
    with tempfile.TemporaryDirectory() as temp, ZipFile(out,"w",compression=ZIP_DEFLATED) as z:
        for label,url,lic,license_marker in SOURCES:
            base = Path(temp)/label
            subprocess.run(["git","clone","--depth","1",url,str(base)],check=True,timeout=90)
            lfile=base/"LICENSE"
            if not lfile.exists() or license_marker not in lfile.read_text(encoding="utf-8",errors="replace")[:1000]:
                raise RuntimeError("Expected license absent: "+url)
            sha=subprocess.check_output(["git","-C",str(base),"rev-parse","HEAD"],text=True).strip()
            ledger["sources"].append({"repository":url,"licence":lic,"commit":sha})
            for file in sorted(base.rglob("*")):
                if not file.is_file() or not keep(file,base): continue
                blob=file.read_bytes()
                if len(blob)>900000 or total+len(blob)>12000000:
                    ledger["omitted_oversize_or_cap"].append(str(file.relative_to(base)))
                    continue
                total+=len(blob)
                name=label+"/"+file.relative_to(base).as_posix()
                z.writestr(name,blob)
                ledger["files"].append({"name":name,"sha256":hashlib.sha256(blob).hexdigest(),"bytes":len(blob)})
        z.writestr("PROVENANCE.json",json.dumps(ledger,indent=2))
        z.writestr("README.txt","Source code ONLY; MacAma MIT and Twin-2K-500 Apache-2.0. No original empirical data or paper replication.\n")
    print("Archive:",out,"size:",out.stat().st_size,"files:",len(ledger["files"]))
    print("SHA256:",hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=="__main__": main()
