from unittest import TestCase

from nba_data.data.player import Player
from nba_data.data.team import Team


class TestPlayer(TestCase):
    def test_instantiation(self):
        player = Player("bae jadley", Team.boston_celtics, 1)
        self.assertEqual(player.name, "bae jadley")
        self.assertEqual(player.team, Team.boston_celtics)
        self.assertEqual(player.nba_id, 1)

    def test_get_query_parameter_name(self):
        self.assertEqual(Player.get_query_parameter_name(), "PlayerId")

    def test_create(self):
        player = Player.create("bae jadley", Team.get_id(Team.boston_celtics), 1)
        self.assertEqual(player.name, "bae jadley")
        self.assertEqual(player.team, Team.boston_celtics)
        self.assertEqual(player.nba_id, 1)

        undefined_team_player = Player.create("jae bradley", 1, 2)
        self.assertEqual(undefined_team_player.name, "jae bradley")
        self.assertIsNone(undefined_team_player.team)
        self.assertEqual(undefined_team_player.nba_id, 2)

    def test_create_assertions(self):
        self.assertRaises(AssertionError, Player.create, name=0, team_id=1, nba_id=2)
        self.assertRaises(AssertionError, Player.create, name="foo", team_id="bar", nba_id=2)
        self.assertRaises(AssertionError, Player.create, name="foo", team_id=1, nba_id="bar")
