"""NAAIL controlled-mutation detector V0.1. Synthetic benchmark only."""
def detect(gold, candidate):
    flags=[]
    exact=[("E01","beta"),("E02","p_value"),("E04","n"),("E05","cluster"),
           ("E06","variable_definition"),("E10","manuscript_claim")]
    for eid,k in exact:
        if candidate.get(k)!=gold.get(k): flags.append(eid)
    # E03: significance representation is derived from p-value and explicit stars
    expected="***" if gold["p_value"]<.01 else ("**" if gold["p_value"]<.05 else ("*" if gold["p_value"]<.10 else ""))
    if candidate.get("significance",expected)!=expected: flags.append("E03")
    if candidate.get("fixed_effects")!=gold.get("fixed_effects"): flags.append("E07")
    if bool(candidate.get("future_information",False))!=bool(gold.get("future_information",False)): flags.append("E08")
    if candidate.get("pipeline_steps")!=gold.get("pipeline_steps"): flags.append("E09")
    return sorted(set(flags))

def score(expected, detected):
    e,d=set(expected),set(detected)
    tp=len(e&d); fp=len(d-e); fn=len(e-d)
    precision=tp/(tp+fp) if tp+fp else 1.0
    recall=tp/(tp+fn) if tp+fn else 1.0
    fpr=fp/max(1,10-len(e))
    return {"tp":tp,"fp":fp,"fn":fn,"precision":precision,"recall":recall,"false_positive_rate":fpr}
