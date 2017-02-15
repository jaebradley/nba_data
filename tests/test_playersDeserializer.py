import json
import os
from unittest import TestCase

from nba_data.deserializers.players import PlayersDeserializer
from tests.config import ROOT_DIRECTORY


class TestPlayersDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(PlayersDeserializer())

    def test_deserialize(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/players.json')) as data_file:
            data = json.load(data_file)
            players = PlayersDeserializer.deserialize(players_json=data)
            self.assertIsNotNone(players)
            self.assertEqual(len(players), 778)
