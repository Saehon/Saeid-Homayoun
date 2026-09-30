"""Minimal NAAIL Stata log parser: V0.1. No external dependencies."""
import re
from dataclasses import dataclass, asdict

@dataclass
class StataSpec:
    command: str
    dependent_variable: str|None=None
    regressors: list|None=None
    absorb: list|None=None
    cluster: str|None=None
    n: int|None=None

def parse_reghdfe_command(line: str) -> StataSpec|None:
    m=re.search(r"reghdfe\s+(\w+)\s+(.+)", line, re.I)
    if not m: return None
    dv, tail=m.groups()
    opts=tail.split(",",1)
    regs=opts[0].strip().split()
    option_text=opts[1] if len(opts)>1 else ""
    a=re.search(r"(?:a|absorb)\(([^)]+)\)", option_text,re.I)
    c=re.search(r"cluster\(([^)]+)\)", option_text,re.I)
    return StataSpec(line.strip(),dv,regs,a.group(1).split() if a else [],c.group(1).strip() if c else None)

def parse_n(text: str):
    patterns=[r"Number of obs\s*=\s*([\d,]+)",r"Observations\s+([\d,]+)"]
    for p in patterns:
        m=re.search(p,text,re.I)
        if m:return int(m.group(1).replace(",",""))
    return None

def parse(text: str):
    specs=[asdict(s) for line in text.splitlines() if (s:=parse_reghdfe_command(line))]
    return {"software":"Stata","specifications":specs,"n":parse_n(text)}
