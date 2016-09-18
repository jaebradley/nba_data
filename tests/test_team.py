from unittest import TestCase

from nba_data.data.team import Team


class TestTeam(TestCase):
    def test_assertions(self):
        self.assertRaises(AssertionError, Team.get_team_by_id, "foo")
        self.assertRaises(AssertionError, Team.get_id, "foo")
        self.assertRaises(AssertionError, Team.get_team_by_abbreviation, 1)

    def test_get_query_parameter_name(self):
        self.assertEqual(Team.get_query_parameter_name(), "TeamId")

    def test_get_team_by_id(self):
        self.assertEqual(Team.get_team_by_id(1610612737), Team.atlanta_hawks)
        self.assertEqual(Team.get_team_by_id("jae"), None)

    def test_get_id(self):
        self.assertEqual(Team.get_id(Team.atlanta_hawks), 1610612737)
        self.assertEqual(Team.get_id("jae"), None)

    def test_get_team_by_abbreviation(self):
        self.assertEqual(Team.get_team_by_abbreviation("bos"), Team.boston_celtics)
        self.assertEqual(Team.get_team_by_abbreviation("BOS"), Team.boston_celtics)
        self.assertEqual(Team.get_team_by_abbreviation("jae"), None)
