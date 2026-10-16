"""No-dependency smoke tests: python -m unittest discover -s SPACE_DIR."""
import unittest
from topic_screening import JURISDICTIONS, screen

class TopicScreeningTests(unittest.TestCase):
    def test_revenue_us(self):
        hits=screen("Revenue recognition, revenue and variable consideration.", JURISDICTIONS[0])
        self.assertEqual(hits[0]["topic"], "Revenue recognition")
        self.assertEqual(hits[0]["illustrative_reference"], "ASC 606")
    def test_revenue_ifrs(self):
        self.assertEqual(screen("Revenue recognition and variable consideration.", JURISDICTIONS[1])[0]["illustrative_reference"],"IFRS 15")
    def test_empty_and_unmatched(self):
        self.assertEqual(screen(""), [])
        self.assertEqual(screen("This excerpt lacks mapped terminology."), [])
    def test_refuse_unknown_market(self):
        with self.assertRaises(ValueError):
            screen("revenue", "Unknown")
    def test_no_leaked_confidence(self):
        output=screen("Goodwill impairment and discount rate.", JURISDICTIONS[1])
        self.assertEqual(output[0]["topic"], "Goodwill and impairment")
        self.assertNotIn("probability", output[0])
        self.assertNotIn("accuracy", output[0])

if __name__ == "__main__":
    unittest.main()
