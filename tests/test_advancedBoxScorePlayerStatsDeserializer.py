import json
import os
from decimal import Decimal
from unittest import TestCase

from nba_data.data.team import Team
from nba_data.deserializers.advanced_player_box_score_deserializer import AdvancedBoxScorePlayerStatsDeserializer
from tests.config import ROOT_DIRECTORY


class TestAdvancedBoxScorePlayerStatsDeserializer(TestCase):
    def test_instantiation(self):
        deserializer = AdvancedBoxScorePlayerStatsDeserializer()
        self.assertTrue(deserializer.__dict__ == {})

    def test_deserialize_advanced_box_score_player_stats(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoreadvancedplayerstats.json')) as data_file:
            data = json.load(data_file)
            player_box_scores = AdvancedBoxScorePlayerStatsDeserializer.deserialize_advanced_box_score_player_stats(advanced_box_score_player_stats_json=data)
            self.assertIsNotNone(player_box_scores)
            self.assertEqual(len(player_box_scores), 26)

            nicolas_batum_box_score = player_box_scores[0]
            self.assertEqual(nicolas_batum_box_score.player.nba_id, 201587)
            self.assertEqual(nicolas_batum_box_score.player.name, "Nicolas Batum")
            self.assertEqual(nicolas_batum_box_score.player.team, Team.charlotte_hornets)
            self.assertEqual(nicolas_batum_box_score.seconds_played, 1037)
            self.assertEqual(nicolas_batum_box_score.offensive_rating, Decimal('143.3'))
            self.assertEqual(nicolas_batum_box_score.defensive_rating, Decimal('54.4'))
            self.assertEqual(nicolas_batum_box_score.teammate_assist_percentage, Decimal('35.7'))
            self.assertEqual(nicolas_batum_box_score.assist_to_turnover_ratio, Decimal('5.0'))
            self.assertEqual(nicolas_batum_box_score.assists_per_100_possessions, Decimal('41.7'))
            self.assertEqual(nicolas_batum_box_score.offensive_rebound_percentage, Decimal('0.0'))
            self.assertEqual(nicolas_batum_box_score.defensive_rebound_percentage, Decimal('17.6'))
            self.assertEqual(nicolas_batum_box_score.turnovers_per_100_possessions, Decimal('8.3'))
            self.assertEqual(nicolas_batum_box_score.effective_field_goal_percentage, Decimal('50.0'))
            self.assertEqual(nicolas_batum_box_score.true_shooting_percentage, Decimal('50.0'))
            self.assertEqual(nicolas_batum_box_score.usage_percentage, Decimal('18.1'))
