"""Run baseline on locally obtained CUAD SQuAD JSON. No data are bundled."""
import argparse,csv,json,re,hashlib,pathlib,collections
PATTERNS={
"termination":r"\bterminat(?:e|ion|ed|ing)\b",
"warranty":r"\bwarrant(?:y|ies)\b",
"indemnification":r"\bindemnif(?:y|ication|ied)\b",
"audit_rights":r"\b(?:audit rights?|right to audit|inspect(?:ion)?)\b",
"intellectual_property":r"\b(?:intellectual property|patents?|trademarks?|copyrights?)\b",
"minimum_commitment":r"\b(?:minimum purchase|minimum commitment|take.or.pay)\b",
"revenue_pricing":r"\b(?:royalt(?:y|ies)|rebates?|discounts?|variable consideration)\b",
"confidentiality":r"\b(?:confidential(?:ity)?|non.disclosure)\b",
"assignment":r"\bassign(?:ment|ed)?\b",
"liability":r"\b(?:liabilit(?:y|ies)|limitation of liability)\b",
"governing_law":r"\bgoverning law\b",
"exclusivity":r"\bexclusiv(?:e|ity)\b"
}
def run(src,out,n):
 raw=pathlib.Path(src).read_bytes();data=json.loads(raw)
 docs={}
 for article in data["data"]:
  title=article.get("title","unknown")
  docs.setdefault(title,[])
  for paragraph in article.get("paragraphs",[]):
   docs[title].append(paragraph["context"])
 selected=sorted(docs)[:n];rows=[];counts=collections.Counter()
 for doc in selected:
  text="\n".join(dict.fromkeys(docs[doc]))
  for category,pattern in PATTERNS.items():
   matches=list(re.finditer(pattern,text,re.I));counts[category]+=int(bool(matches))
   evidence=text[max(0,matches[0].start()-80):matches[0].end()+80].replace("\n"," ") if matches else ""
   rows.append(dict(document=doc,category=category,keyword_detected=int(bool(matches)),match_count=len(matches),first_evidence=evidence))
 dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=True)
 with (dest/"clause_screen.csv").open("w",newline="",encoding="utf-8") as f:
  writer=csv.DictWriter(f,fieldnames=["document","category","keyword_detected","match_count","first_evidence"]);writer.writeheader();writer.writerows(rows)
 summary=dict(status="keyword_baseline_only",sha256=hashlib.sha256(raw).hexdigest(),unique_source_documents=len(docs),selected_documents=len(selected),categories=len(PATTERNS),flagged_documents_by_category=dict(counts),caution="Keyword hits are not validated clauses or empirical accounting results.")
 (dest/"pilot_summary.json").write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--out",default="results");p.add_argument("--n",type=int,default=120);a=p.parse_args();run(a.input,a.out,a.n)
