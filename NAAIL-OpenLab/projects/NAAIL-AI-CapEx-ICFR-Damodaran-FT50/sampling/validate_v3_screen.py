"""Validate frozen public sample-screen counts; not a historical SEC cohort."""
import csv
from pathlib import Path

BASE=Path(__file__).parent
NAMES={
    "screen":"INITIAL_424_NONFINANCIAL_FIRMS_2026-10-09.csv",
    "excluded":"EXCLUDED_76_FINANCIAL_FIRMS_2026-10-09.csv",
    "priority":"V2_PRIORITY_119_TECH_SUPPLY_CANDIDATES.csv",
    "comparators":"V2_COMPARATOR_244_GENERAL_NONFINANCIAL.csv",
    "special":"V2_SPECIAL_61_UTILITIES_REAL_ESTATE.csv",
}
def load(key):
    with (BASE/NAMES[key]).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))
def verify():
    rows={k:load(k) for k in NAMES}
    expected={"screen":424,"excluded":76,"priority":119,"comparators":244,"special":61}
    for k,n in expected.items():
        assert len(rows[k])==n,(k,len(rows[k]),n)
        assert len(set(x["cik"] for x in rows[k]))==n,("duplicate CIK",k)
    selected={x["cik"] for x in rows["screen"]}
    excluded={x["cik"] for x in rows["excluded"]}
    assert selected.isdisjoint(excluded)
    sets=[{x["cik"] for x in rows[k]} for k in ("priority","comparators","special")]
    assert all(not sets[i].intersection(sets[j]) for i in range(3) for j in range(i+1,3))
    assert set.union(*sets)==selected
    assert sum(x["priority"]=="P0_10_FIRMS" for x in rows["screen"])==10
    assert sum(x["sector"]=="Utilities" for x in rows["special"])==31
    assert sum(x["sector"]=="Real Estate" for x in rows["special"])==30
    assert sum(x["sec_10k_2019_2025_verified"]=="NO" and x["ai_capex_verified"]=="NO" for x in rows["screen"])==424
    print("PASS: 424 unique CIK screen, 76 exclusions, 119+244+61 exact split; history/AI CapEx still unverified")
if __name__=="__main__":
    verify()
