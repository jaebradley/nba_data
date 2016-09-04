from unittest import TestCase

from stats.data.outcome import Outcome, outcome_abbreviation_to_outcome_map


class TestOutcome(TestCase):
    def test_get_outcome_from_abbreviation(self):
        self.assertEqual(Outcome.get_outcome_from_abbreviation("w"), Outcome.win)
        self.assertEqual(Outcome.get_outcome_from_abbreviation("W"), Outcome.win)
        self.assertRaises(ValueError, Outcome.get_outcome_from_abbreviation, "jae")
        self.assertEqual(outcome_abbreviation_to_outcome_map,
                         {
                             "W": Outcome.win,
                             "L": Outcome.loss,
                         })
