import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from validate_panel import validate
BASE=dict(firm_id='SYNTHETIC-001',fiscal_year='2022',domain='inventory',industry='Manufacturing',
cutoff_date='2023-03-01',evidence_available_date='2023-02-15',cam_present='0',eligible='1',
risk_probability='0.75',outcome_event='1',outcome_observed_date='2024-02-01',icfr_status='unknown',accounting_standard='US_GAAP')
class TestContract(unittest.TestCase):
 def test_valid(self):self.assertEqual(validate([BASE.copy()])['rows_validated'],1)
 def test_duplicate(self):
  with self.assertRaisesRegex(ValueError,'duplicate'):validate([BASE.copy(),BASE.copy()])
 def test_lookahead(self):
  with self.assertRaisesRegex(ValueError,'LOOKAHEAD'):validate([dict(BASE,evidence_available_date='2023-04-01')])
 def test_future_outcome(self):
  with self.assertRaisesRegex(ValueError,'future'):validate([dict(BASE,outcome_observed_date='2023-02-01')])
 def test_unknown_outcome(self):self.assertEqual(validate([dict(BASE,outcome_event='',outcome_observed_date='')])['rows_validated'],1)
 def test_uncalibrated_invalid_probability(self):
  with self.assertRaisesRegex(ValueError,'score'):validate([dict(BASE,risk_probability='1.5')])
if __name__=='__main__':unittest.main()
