from pathlib import Path
import csv, json

ROOT=Path(__file__).parent
EXPECTED={"Revenue":331839,"OperatingIncome":155237,"NetIncome":133749,"NetCashFromOperations":182935,
"AccountsReceivableNet":80876,"Inventory":1397,"Goodwill":119651,"TotalAssets":758376,"LongTermDebt":31067}

def score(candidate):
    matched=0
    unsupported=0
    for k,v in candidate.items():
        if k not in EXPECTED: unsupported+=1; continue
        if abs(float(v)-EXPECTED[k]) <= max(1, abs(EXPECTED[k])*1e-6): matched+=1
    return {"numeric_accuracy":matched/len(EXPECTED),
            "completeness":len(set(candidate)&set(EXPECTED))/len(EXPECTED),
            "unsupported_claim_rate":unsupported/max(1,len(candidate))}

if __name__=="__main__":
    p=ROOT/"candidate.json"
    if not p.exists():
        print("NO CANDIDATE: baseline/reference created; external engines remain NOT_RUN.")
    else:
        print(json.dumps(score(json.loads(p.read_text())),indent=2))
