import json
import os
from unittest import TestCase

from nba_data.data.box_scores import GameBoxScore, TraditionalPlayerBoxScore, TraditionalTeamBoxScore
from nba_data.deserializers.box_scores.game import TraditionalGameBoxScoreDeserializer
from tests.config import ROOT_DIRECTORY


class TestTraditionalBoxScoreDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(TraditionalGameBoxScoreDeserializer())

    def test_deserialize_traditional_box_score(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoretraditional.json')) as data_file:
            data = json.load(data_file)
            box_score = TraditionalGameBoxScoreDeserializer().deserialize(data=data)
            self.assertIsNotNone(box_score)
            self.assertIsInstance(box_score, GameBoxScore)
            self.assertEqual(box_score.game_id, "0021500945")
            self.assertEqual(len(box_score.player_box_scores), 25)
            self.assertEqual(len(box_score.team_box_scores), 2)
            self.assertIsInstance(box_score.player_box_scores[0], TraditionalPlayerBoxScore)
            self.assertIsInstance(box_score.team_box_scores[0], TraditionalTeamBoxScore)
