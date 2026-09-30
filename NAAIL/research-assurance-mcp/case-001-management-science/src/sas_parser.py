"""Minimal NAAIL SAS log/parser V0.1."""
import re

def procedures(text:str):
    return [m.group(1).upper() for m in re.finditer(r"\bproc\s+(\w+)",text,re.I)]

def datasets(text:str):
    found=[]
    for p in [r"\bset\s+([\w.]+)",r"\bdata\s*=\s*([\w.]+)"]:
        found += re.findall(p,text,re.I)
    return sorted(set(found))

def warnings(text:str):
    return [line.strip() for line in text.splitlines()
            if re.match(r"\s*(ERROR|WARNING):",line,re.I)]

def parse(text:str):
    return {"software":"SAS","procedures":procedures(text),
            "datasets":datasets(text),"warnings":warnings(text)}
