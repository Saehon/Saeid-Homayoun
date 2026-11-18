"""CUAD full-dataset baseline. Downloads official GitHub data.zip; does not commit source data."""
import argparse,csv,hashlib,io,json,re,urllib.request,zipfile,pathlib,collections
SOURCE="https://raw.githubusercontent.com/The-Atticus-Project/cuad/main/data.zip"
PATTERNS={"termination":r"\bterminat(?:e|ion|ed|ing)\b","warranty":r"\bwarrant(?:y|ies)\b","indemnification":r"\bindemnif(?:y|ication|ied)\b","audit_rights":r"\b(?:audit rights?|right to audit|inspect(?:ion)?)\b","intellectual_property":r"\b(?:intellectual property|patents?|trademarks?|copyrights?)\b","minimum_commitment":r"\b(?:minimum purchase|minimum commitment|take.or.pay)\b","revenue_pricing":r"\b(?:royalt(?:y|ies)|rebates?|discounts?|variable consideration)\b","confidentiality":r"\b(?:confidential(?:ity)?|non.disclosure)\b","assignment":r"\bassign(?:ment|ed)?\b","liability":r"\b(?:liabilit(?:y|ies)|limitation of liability)\b","governing_law":r"\bgoverning law\b","exclusivity":r"\bexclusiv(?:e|ity)\b"}
def main():
 p=argparse.ArgumentParser();p.add_argument("--zip");p.add_argument("--out",default="results_full");p.add_argument("--limit",type=int,default=0);a=p.parse_args()
 if a.zip: raw=pathlib.Path(a.zip).read_bytes()
 else:
  req=urllib.request.Request(SOURCE,headers={"User-Agent":"Contract-AIVA-academic-research/0.1"})
  with urllib.request.urlopen(req,timeout=120) as response:raw=response.read()
 out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
 z=zipfile.ZipFile(io.BytesIO(raw));names=[x for x in z.namelist() if x.endswith(".json")];print("JSON files:",names)
 candidates=[]
 for name in names:
  try:
   obj=json.loads(z.read(name))
   if isinstance(obj,dict) and isinstance(obj.get("data"),list):candidates.append((name,obj))
  except (UnicodeDecodeError,ValueError):pass
 if not candidates:raise RuntimeError("No SQuAD-compatible CUAD JSON found; inspect archive structure")
 # Prefer original CUAD_v1, never silently merge train/test exports or count duplicated documents.
 candidates.sort(key=lambda x:(0 if pathlib.PurePosixPath(x[0]).name=="CUAD_v1.json" else 1,x[0]))
 source_name,obj=candidates[0];docs={}
 for article in obj["data"]:
  name=article.get("title","unknown");docs.setdefault(name,[])
  for para in article.get("paragraphs",[]):docs[name].append(para.get("context",""))
 keys=sorted(docs);keys=keys[:a.limit] if a.limit else keys
 rows=[];counts=collections.Counter()
 for name in keys:
  text="\n".join(dict.fromkeys(docs[name]))
  for category,regex in PATTERNS.items():
   hits=list(re.finditer(regex,text,re.I));counts[category]+=bool(hits)
   evidence=text[max(0,hits[0].start()-80):hits[0].end()+80].replace("\n"," ") if hits else ""
   rows.append(dict(document=name,category=category,keyword_detected=int(bool(hits)),match_count=len(hits),first_evidence=evidence))
 with (out/"clause_screen.csv").open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["document","category","keyword_detected","match_count","first_evidence"]);w.writeheader();w.writerows(rows)
 summary={"status":"keyword_baseline_not_validated_clause_extraction","source_url":SOURCE if not a.zip else "local_zip","archive_sha256":hashlib.sha256(raw).hexdigest(),"json_file":source_name,"documents_in_source":len(docs),"documents_screened":len(keys),"category_count":len(PATTERNS),"document_flags_by_category":dict(counts),"warning":"No precision/recall, no gold-standard validation, no causal accounting claims."}
 (out/"pilot_summary.json").write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=="__main__":main()
