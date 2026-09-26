"""Bounded filing-text feature calculator.
The repository does not redistribute filing sections; pass legally retrieved text into feature_row().
"""
import re, hashlib

UNCERTAINTY={"may","could","risk","uncertain","uncertainty","possible","potential"}
MODAL={"may","could","might","should","would","can"}
INNOVATION={"innovation","innovative","ai","technology","research","development","product"}

def _syllables(word):
    word=re.sub(r"[^a-z]","",word.lower())
    if not word: return 0
    groups=re.findall(r"[aeiouy]+",word)
    n=len(groups)
    if word.endswith("e") and n>1: n-=1
    return max(1,n)

def feature_row(text):
    words=re.findall(r"\b[A-Za-z][A-Za-z\-']*\b", text.lower())
    sents=[s for s in re.split(r"[.!?]+", text) if s.strip()]
    wc=len(words); sc=max(1,len(sents)); syll=sum(_syllables(w) for w in words)
    return {
        "word_count": wc,
        "sentence_count": len(sents),
        "avg_sentence_length": wc/sc if wc else 0,
        "flesch_reading_ease": 206.835-1.015*(wc/sc)-84.6*(syll/wc) if wc else None,
        "uncertainty_count": sum(w in UNCERTAINTY for w in words),
        "modal_count": sum(w in MODAL for w in words),
        "innovation_count": sum(w in INNOVATION for w in words),
        "sample_sha256": hashlib.sha256(text.encode()).hexdigest(),
    }
