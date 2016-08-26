from unittest import TestCase
import json
import os

from tests.config import ROOT_DIRECTORY
from stats.data.player import Player
from stats.data.team import Team


class TestPlayer(TestCase):
    def test_create(self):
        player = Player.create("bae jadley", Team.get_id(Team.boston_celtics), 1)
        self.assertEqual(player.name, "bae jadley")
        self.assertEqual(player.team, Team.boston_celtics)
        self.assertEqual(player.nba_id, 1)

    def test_deserialize_common_all_players(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/commonallplayers.json')) as data_file:
            data = json.load(data_file)
            deserialized_players = Player.deserialize_common_all_players(data)
            quincy_acy = deserialized_players[0]
            quincy_acy.name = "Quincy Acy"
            quincy_acy.id = 203112
            quincy_acy.team = Team.sacramento_kings
