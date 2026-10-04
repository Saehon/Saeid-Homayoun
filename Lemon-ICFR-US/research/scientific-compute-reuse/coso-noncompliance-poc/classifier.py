import re
def classify_noncompliance(text):
    if not isinstance(text, str) or not text.strip(): return None
    a=bool(re.search(r"Integrated Framework\s*\(\s*1992\s*\)",text,re.I))
    b=bool(re.search(r"Integrated Framework\s*\(\s*2013\s*\)",text,re.I))
    if a==b: return None
    return 1 if a else 0
