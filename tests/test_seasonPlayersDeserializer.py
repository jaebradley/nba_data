import json
import os
from unittest import TestCase

from nba_data.deserializers.season_players import SeasonPlayersDeserializer
from tests.config import ROOT_DIRECTORY


class TestSeasonPlayersDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(SeasonPlayersDeserializer())

    def test_deserialize(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/players.json')) as data_file:
            data = json.load(data_file)
            players = SeasonPlayersDeserializer.deserialize(data=data)
            self.assertIsNotNone(players)
            self.assertEqual(len(players), 778)
