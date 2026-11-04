import unittest
import numpy as np
from digital_twin_power import generate,fit,simulation

class TestPower(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(simulation(50,3,4,11), simulation(50,3,4,11))
    def test_null_is_not_injected_alternative(self):
        d=generate(np.random.default_rng(44),60,3,(0,0,0))
        self.assertEqual(len(d),180)
        self.assertTrue(all(isinstance(x["p_value"],float) for x in fit(d).values()))
    def test_no_false_real_outcome_claim(self):
        self.assertIn("SIMULATED",simulation(50,3,2)["label"])
if __name__=="__main__":
    unittest.main()
