import unittest
import numpy as np, pandas as pd
from temporal_icfr_baseline import verified_inputs,train_predict

def data(seed=22):
    rng=np.random.default_rng(seed)
    n=90
    periods=['2021-03-01']*30+['2023-03-01']*30+['2025-03-01']*30
    x=rng.normal(size=n)
    y=(rng.random(n)<(1/(1+np.exp(-x)))).astype(int)
    features=pd.DataFrame({'event_id':['SIM-'+str(i) for i in range(n)],
        'cik':[str(i%15) for i in range(n)],'public_utc':periods,
        'available_utc':periods,'feat_icfr_risk':x,'feat_size':rng.normal(size=n)})
    labels=pd.DataFrame({'event_id':features.event_id,'mw_verified':y})
    return features,labels
class TestModel(unittest.TestCase):
    def test_temporal_holdout_and_calibration(self):
        a,b=data(); v,cols=verified_inputs(a,b,'2022-12-31','2023-12-31')
        out=train_predict(v,cols)
        self.assertEqual(out['metrics']['test_n'],30)
        self.assertTrue(all(0<=k['predicted_prob']<=1 for k in out['predictions']))
    def test_target_leakage_rejected(self):
        a,b=data();a['feat_future_return']=0
        with self.assertRaisesRegex(ValueError,'leakage'):
            verified_inputs(a,b,'2022-12-31','2023-12-31')
    def test_future_timestamp_rejected(self):
        a,b=data(); a.loc[0,'available_utc']='2026-01-01'
        with self.assertRaisesRegex(ValueError,'FUTURE_DATA_LEAKAGE'):
            verified_inputs(a,b,'2022-12-31','2023-12-31')
    def test_unvalidated_gold_rejected(self):
        a,b=data(); b.loc[0,'mw_verified']=np.nan
        with self.assertRaisesRegex(ValueError,'Unverified'):
            verified_inputs(a,b,'2022-12-31','2023-12-31')
if __name__=='__main__': unittest.main()
