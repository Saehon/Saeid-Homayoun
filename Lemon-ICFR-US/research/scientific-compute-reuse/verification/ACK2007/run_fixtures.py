import csv, hashlib, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
MODEL_DIR=HERE.parent.parent/"executable-models"/"ACK2007"
sys.path.insert(0,str(MODEL_DIR))
from ack2007 import predict, REQUIRED

csv_path=HERE/"frozen-fixtures.csv"
rows=[]
with csv_path.open(newline="",encoding="utf-8") as f:
    for row in csv.DictReader(f):
        case_id=row.pop("case_id"); row.pop("purpose",None)
        x={k:float(row[k]) for k in REQUIRED}
        y=predict(x)
        rows.append({"case_id":case_id,"z":f"{y.linear_predictor:.12f}","p":f"{y.probability:.12f}"})
payload=json.dumps(rows,sort_keys=True,separators=(",",":"))+"\n"
out_dir=MODEL_DIR
(out_dir/"fixture-results.json").write_text(payload,encoding="utf-8")
sha=hashlib.sha256(payload.encode()).hexdigest()
(out_dir/"fixture-results.sha256").write_text(sha+"  fixture-results.json\n",encoding="utf-8")
print(payload,end=""); print("SHA256",sha)
