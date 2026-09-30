"""Generate E01-E10 one-error-at-a-time fixtures and benchmark deterministic detector."""
import json, copy
from detector import detect, score

with open("benchmark/fixtures/gold_fixture.json",encoding="utf8") as f: obj=json.load(f)
g=obj["gold"]
mutations={
"E01":("beta",0.214),"E02":("p_value",0.040),"E03":("significance",""),
"E04":("n",5021),"E05":("cluster","industry"),"E06":("variable_definition","ALTERED synthetic definition"),
"E07":("fixed_effects",["gvkey"]),"E08":("future_information",True),
"E09":("pipeline_steps",["load","clean","estimate","export"]),
"E10":("manuscript_claim","Post causes EADelay in this synthetic benchmark fixture.")
}
rows=[]
for eid,(key,val) in mutations.items():
    c=copy.deepcopy(g); c[key]=val
    found=detect(g,c); s=score([eid],found)
    rows.append({"mutation":eid,"expected":[eid],"detected":found,**s})
summary={"case":"MNSC-2023-4670","fixture":obj["fixture_id"],"synthetic":True,
         "n_mutations":len(rows),"all_detected":all(r["recall"]==1 for r in rows),
         "macro_precision":sum(r["precision"] for r in rows)/len(rows),
         "macro_recall":sum(r["recall"] for r in rows)/len(rows),
         "results":rows,
         "caveat":"Engineering unit benchmark only; not evidence of performance on real manuscripts or author data."}
print(json.dumps(summary,indent=2))
