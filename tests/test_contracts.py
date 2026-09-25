"""Bootstrap checks only; no scientific-performance claims."""

import unittest

from textileroute import Decision, make_review_result


class ContractChecks(unittest.TestCase):
    def test_no_model_requires_review(self):
        result = make_review_result("synthetic-001")
        self.assertEqual(result.decision, Decision.REVIEW)
        self.assertIsNone(result.profile_id)
        self.assertIsNone(result.evidence_source)

    def test_empty_identifier_rejected(self):
        with self.assertRaises(ValueError):
            make_review_result("  ")


if __name__ == "__main__":
    unittest.main()
