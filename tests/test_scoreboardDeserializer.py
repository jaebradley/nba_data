import json
import os
from unittest import TestCase

from nba_data.deserializers.scoreboard import ScoreboardDeserializer
from tests.config import ROOT_DIRECTORY


# TODO: @jbradley in future make test more robust


class TestScoreboardDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(ScoreboardDeserializer())

    def test_deserialize(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/scoreboard.json')) as data_file:
            data = json.load(data_file)
            scoreboard_games = ScoreboardDeserializer.deserialize(data=data)
            self.assertIsNotNone(scoreboard_games)
            self.assertEqual(len(scoreboard_games), 9)

    def test_deserialize_future_game(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/scoreboardfuturegames.json')) as data_file:
            data = json.load(data_file)
            scoreboard_games = ScoreboardDeserializer.deserialize(data=data)
            self.assertIsNotNone(scoreboard_games)
            self.assertEqual(len(scoreboard_games), 4)
