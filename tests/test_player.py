from unittest import TestCase

from nba_data.data.players import Player


class TestPlayer(TestCase):
    def test_instantiation(self):
        player = Player("bae jadley", 1)
        self.assertEqual(player.name, "bae jadley")
        self.assertEqual(player.id, 1)

    def test_get_query_parameter_name(self):
        self.assertEqual(Player.get_query_parameter_name(), "PlayerId")
