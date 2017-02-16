import json
import os
from unittest import TestCase

from nba_data.data.game_box_score import GameBoxScore
from nba_data.data.box_scores import TraditionalPlayerBoxScore
from nba_data.data.box_scores import TraditionalTeamBoxScore
from nba_data.deserializers.traditional_box_score_deserializer import TraditionalBoxScoreDeserializer
from tests.config import ROOT_DIRECTORY


class TestTraditionalBoxScoreDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(TraditionalBoxScoreDeserializer())

    def test_deserialize_traditional_box_score(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoretraditional.json')) as data_file:
            data = json.load(data_file)
            box_score = TraditionalBoxScoreDeserializer().deserialize(data=data)
            self.assertIsNotNone(box_score)
            self.assertIsInstance(box_score, GameBoxScore)
            self.assertEqual(box_score.game_id, "0021500945")
            self.assertEqual(len(box_score.player_box_scores), 25)
            self.assertEqual(len(box_score.team_box_scores), 2)
            self.assertIsInstance(box_score.player_box_scores[0], TraditionalPlayerBoxScore)
            self.assertIsInstance(box_score.team_box_scores[0], TraditionalTeamBoxScore)
