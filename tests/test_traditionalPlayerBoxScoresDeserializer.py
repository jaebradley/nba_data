import json
import os
from unittest import TestCase

from nba_data.data.box_scores import TraditionalPlayerBoxScore
from nba_data.data.player_status import PlayerStatusType
from nba_data.data.team import Team
from nba_data.deserializers.box_scores.traditional import TraditionalPlayerBoxScoresDeserializer
from tests.config import ROOT_DIRECTORY


class TestTraditionalPlayerBoxScoresDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(TraditionalPlayerBoxScoresDeserializer())

    def test_deserialize_traditional_box_score_player_stats(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoretraditionalplayerstats.json')) as data_file:
            data = json.load(data_file)
            player_box_scores = TraditionalPlayerBoxScoresDeserializer.deserialize(data)

            self.assertIsNotNone(player_box_scores)
            self.assertEqual(len(player_box_scores), 25)

            kawhi_leonard_box_score = player_box_scores[0]
            self.assertIsInstance(kawhi_leonard_box_score, TraditionalPlayerBoxScore)
            self.assertEqual(kawhi_leonard_box_score.player.name, "Kawhi Leonard")
            self.assertEqual(kawhi_leonard_box_score.player.team, Team.san_antonio_spurs)
            self.assertEqual(kawhi_leonard_box_score.player.id, 202695)
            self.assertEqual(kawhi_leonard_box_score.player.status.type, PlayerStatusType.active)
            self.assertIsNone(kawhi_leonard_box_score.player.status.comment)
            self.assertEqual(kawhi_leonard_box_score.seconds_played, 1471)
            self.assertEqual(kawhi_leonard_box_score.field_goals_made, 6)
            self.assertEqual(kawhi_leonard_box_score.field_goals_attempted, 12)
            self.assertEqual(kawhi_leonard_box_score.three_point_field_goals_made, 0)
            self.assertEqual(kawhi_leonard_box_score.three_point_field_goals_attempted, 1)
            self.assertEqual(kawhi_leonard_box_score.free_throws_made, 3)
            self.assertEqual(kawhi_leonard_box_score.free_throws_attempted, 3)
            self.assertEqual(kawhi_leonard_box_score.offensive_rebounds, 1)
            self.assertEqual(kawhi_leonard_box_score.defensive_rebounds, 4)
            self.assertEqual(kawhi_leonard_box_score.assists, 2)
            self.assertEqual(kawhi_leonard_box_score.steals, 1)
            self.assertEqual(kawhi_leonard_box_score.blocks, 0)
            self.assertEqual(kawhi_leonard_box_score.turnovers, 0)
            self.assertEqual(kawhi_leonard_box_score.personal_fouls, 1)
            self.assertEqual(kawhi_leonard_box_score.plus_minus, 29)

