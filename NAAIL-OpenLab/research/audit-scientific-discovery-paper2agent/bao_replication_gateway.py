#!/usr/bin/env python3
"""Rights-aware gateway to ORIGINAL Bao et al. (2020) MATLAB author code.

No downloaded proprietary data or author code is redistributed here.
'--inspect' requires neither licensed inputs nor MATLAB; '--execute' requires
explicit rights acknowledgement, a matching original code checkout, and MATLAB.
MATLAB output never becomes a confirmed replication without independent review.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

UPSTREAM="https://github.com/JarFraud/FraudDetection"
EXPECTED_BLOBS={
 "run_RUSBoost.m":"2ae5c04c54ddee2ecd999817e4ab21ad211ecc78",
 "data_reader.m":"de15ae2e5d6af43edabbdfb5bcecc8f2cee743f3",
 "evaluate.m":"10764403e3ca9a7a3eefada9e292b39f0a3fb7ce",
}
DATA_FILE="data_FraudDetection_JAR2020.csv"
FIELDS=("fyear","gvkey","p_aaer","misstate")
def git_blob(data):
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def assess(source_dir):
    source_dir=Path(source_dir)
    checks={}
    for name,expected in EXPECTED_BLOBS.items():
        path=source_dir/name
        current=git_blob(path.read_bytes()) if path.is_file() else None
        checks[name]={"exists":path.is_file(),"expected_git_blob_sha":expected,
                      "actual_git_blob_sha":current,"exact_author_blob":current==expected}
    file=source_dir/DATA_FILE
    csv_meta={"exists":file.is_file(),"rows":None,"columns":None,
              "feature_count_28_confirmed":False,"year_span":None,
              "fraud_positive_count":None,"binary_label_confirmed":False}
    if file.is_file():
        with file.open(newline="",encoding="utf-8-sig") as f:
            reader=csv.reader(f)
            try: header=next(reader)
            except StopIteration: header=[]
            header=[h.strip() for h in header]
            csv_meta["columns"]=header
            # Published author reader assumes first four columns:
            # fyear, gvkey, p_aaer, misstate, then 28 raw features.
            label_index=header.index("misstate") if "misstate" in header else None
            year_index=header.index("fyear") if "fyear" in header else None
            years=[]
            positives=0
            valid_binary=True
            n=0
            for row in reader:
                n+=1
                if label_index is not None and len(row)>label_index:
                    try: label=float(row[label_index])
                    except ValueError: label=float("nan")
                    valid_binary&=(label in (0.0,1.0))
                    positives+=(label==1.0)
                else: valid_binary=False
                if year_index is not None and len(row)>year_index:
                    try: years.append(int(float(row[year_index])))
                    except ValueError: pass
            csv_meta.update(rows=n,feature_count_28_confirmed=len(header)>=32,
                            year_span=[min(years),max(years)] if years else None,
                            fraud_positive_count=positives,binary_label_confirmed=valid_binary)
    return {"publication":"Bao et al. (2020), Journal of Accounting Research",
            "source":UPSTREAM,"correction_doi":"10.1111/1475-679X.12454",
            "code_checks":checks,"author_data_check":csv_meta,
            "matlab_available":bool(shutil.which("matlab")),
            "rights_status":"NOT_VERIFIED_BY_THIS_TOOL",
            "empirical_replication_status":"BLOCKED_PENDING_RIGHTS_ENVIRONMENT_AND_REVIEW",
            "all_original_code_blobs_match":all(x["exact_author_blob"] for x in checks.values())}

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-dir",type=Path,required=True)
    ap.add_argument("--out",type=Path,default=Path("results/bao_replication_gate.json"))
    ap.add_argument("--execute",action="store_true",
                    help="Explicitly run pinned MATLAB source from local code checkout")
    ap.add_argument("--rights-authorized",action="store_true",
                    help="Caller confirms lawful local use of final author dataset")
    ap.add_argument("--timeout",type=int,default=7200)
    args=ap.parse_args(argv)
    report=assess(args.source_dir)
    if args.execute:
        reasons=[]
        if not args.rights_authorized: reasons.append("Explicit data rights acknowledgement required")
        if not report["all_original_code_blobs_match"]: reasons.append("Original author code files missing/modified")
        if not report["author_data_check"]["exists"]: reasons.append("Author final dataset missing")
        if not report["author_data_check"]["binary_label_confirmed"]: reasons.append("Fraud label validity not established")
        if not report["matlab_available"]: reasons.append("MATLAB not available")
        if reasons:
            report["execution"]={"status":"BLOCKED","reasons":reasons}
        else:
            try:
                process=subprocess.run(["matlab","-batch","run_RUSBoost"],
                    cwd=args.source_dir,capture_output=True,text=True,timeout=args.timeout,check=False)
                report["execution"]={"status":"EXECUTED_PENDING_INDEPENDENT_VERIFICATION",
                    "returncode":process.returncode,
                    "stdout_tail":process.stdout[-3000:],
                    "stderr_tail":process.stderr[-1500:],
                    "results_output_exists":(args.source_dir/"results_rusboost.txt").is_file()}
            except subprocess.TimeoutExpired:
                report["execution"]={"status":"TIMEOUT","timeout_seconds":args.timeout}
    else:
        report["execution"]={"status":"DRY_RUN_ONLY"}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Saved author-replication gate to {args.out}: {report['execution']['status']}")
    return report

if __name__=="__main__":
    main()
