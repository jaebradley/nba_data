import json
import os
from unittest import TestCase

from stats.client.deserializers.advanced_box_score_deserializer import AdvancedBoxScoreDeserializer
from tests.config import ROOT_DIRECTORY


class TestAdvancedBoxScorePlayerStatsDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(AdvancedBoxScoreDeserializer())

    def deserialize_advanced_box_score(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoreadvanced.json')) as data_file:
            data = json.load(data_file)
            advanced_box_score = AdvancedBoxScoreDeserializer.deserialize_advanced_box_score(data)
            self.assertEqual(advanced_box_score.game_id, "0021501205")
