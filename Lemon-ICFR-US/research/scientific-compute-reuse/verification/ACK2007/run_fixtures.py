import csv, hashlib, json
from pathlib import Path
from ack2007 import predict, REQUIRED

FIXTURES={
"ZERO":{k:0.0 for k in REQUIRED},
"AUDITOR_RESIGN_ONLY":{**{k:0.0 for k in REQUIRED},"AUDITOR_RESIGN":1.0},
"SCHEMA_VALID":{"SEGMENTS":2,"FOREIGN_SALES":1,"M&A":0,"RESTRUCTURE":0,"RGROWTH":5,"INVENTORY":0.10,"SIZE":8,"%LOSS":0.33,"RZSCORE":4,"AUDITOR_RESIGN":0,"AUDITOR":1,"RESTATEMENT":0,"INST_CON":0.20,"LITIGATION":0}}
rows=[]
for name,x in FIXTURES.items():
 y=predict(x); rows.append({"case_id":name,"z":f"{y.linear_predictor:.12f}","p":f"{y.probability:.12f}"})
payload=json.dumps(rows,sort_keys=True,separators=(",",":"))+"\n"
Path("fixture-results.json").write_text(payload,encoding="utf-8")
sha=hashlib.sha256(payload.encode()).hexdigest()
Path("fixture-results.sha256").write_text(sha+"  fixture-results.json\n",encoding="utf-8")
print(payload,end=""); print("SHA256",sha)
