from unittest import TestCase

from stats.data.player import Player
from stats.data.team import Team


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
