import re, hashlib

UNCERTAINTY={"uncertain","uncertainty","risk","risks","estimate","estimates","judgment","may","could"}
MODAL={"may","might","could","would","should","can"}
INNOVATION={"ai","artificial","intelligence","cloud","innovation","research","development","technology"}
NEGATIVE={"risk","loss","adverse","failure","decline","uncertain"}
POSITIVE={"growth","improve","strong","opportunity","benefit"}
LITIGIOUS={"litigation","legal","claim","regulatory","lawsuit"}
HUMAN={"employee","employees","human","talent","skills","workforce"}

def words(text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())

def sentences(text):
    return [s for s in re.split(r"[.!?]+", text) if s.strip()]

def count(dictionary, toks):
    return sum(t in dictionary for t in toks)

def flesch(text):
    toks=words(text); s=max(1,len(sentences(text)))
    def syll(w):
        return max(1,len(re.findall(r"[aeiouy]+", w)))
    syl=sum(syll(w) for w in toks)
    return 206.835 - 1.015*(len(toks)/s) - 84.6*(syl/max(1,len(toks)))

def extract(text):
    toks=words(text); n=max(1,len(toks))
    return {
        "word_count":len(toks),
        "sentence_count":len(sentences(text)),
        "avg_sentence_length":len(toks)/max(1,len(sentences(text))),
        "flesch_reading_ease":flesch(text),
        "sha256":hashlib.sha256(text.encode()).hexdigest(),
        "uncertainty_per_100_words":100*count(UNCERTAINTY,toks)/n,
        "modal_per_100_words":100*count(MODAL,toks)/n,
        "innovation_per_100_words":100*count(INNOVATION,toks)/n,
        "negative_per_100_words":100*count(NEGATIVE,toks)/n,
        "positive_per_100_words":100*count(POSITIVE,toks)/n,
        "litigious_per_100_words":100*count(LITIGIOUS,toks)/n,
        "human_capital_per_100_words":100*count(HUMAN,toks)/n,
    }
