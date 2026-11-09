"""Synthetic feasibility experiment; NOT firm-level empirical evidence."""
import numpy as np
import pandas as pd
from pathlib import Path
rng=np.random.default_rng(20261011)
n=400
risk=rng.binomial(1,.35,n)
provenance=rng.binomial(1,.82,n)
rights=rng.binomial(1,.92,n)
coso=rng.binomial(1,.88,n)
support=rng.binomial(1,.76,n)
review=rng.binomial(1,.86,n)
falsification=rng.binomial(1,.81,n)
repro=rng.binomial(1,.90,n)
human=np.zeros(n,dtype=int)
all_auto=provenance*rights*coso*support*review*falsification*repro
unsafe=1-provenance*rights*coso*support
baseline=np.ones(n,dtype=int)
gated=all_auto*human
out=pd.DataFrame(dict(case_id=np.arange(n),risk=risk,provenance=provenance,rights=rights,coso=coso,support=support,review=review,falsification=falsification,reproducibility=repro,human_approval=human,unsafe=unsafe,baseline_auto_pass=baseline,gated_auto_pass=gated,awaiting_human=all_auto))
p=Path(__file__).parent
out.to_csv(p/'synthetic_cases.csv',index=False)
summary={'n':n,'unsafe_cases':int(unsafe.sum()),'baseline_unsafe_auto_pass':int((unsafe*baseline).sum()),'gated_unsafe_auto_pass':int((unsafe*gated).sum()),'awaiting_human':int(all_auto.sum()),'gated_auto_approvals':int(gated.sum())}
(p/'synthetic_results.txt').write_text('\n'.join(f'{k}: {v}' for k,v in summary.items())+'\n')
print(summary)
