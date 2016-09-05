from decimal import Decimal
import os
import json
from unittest import TestCase

from tests.config import ROOT_DIRECTORY
from stats.data.team import Team
from stats.client.deserializers.advanced_team_box_score_deserializer import AdvancedBoxScoreTeamStatsDeserializer


class TestAdvancedBoxScoreTeamStatsDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(AdvancedBoxScoreTeamStatsDeserializer())

    def test_deserialize_advanced_box_score_player_stats(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoreadvancedteamstats.json')) as data_file:
            data = json.load(data_file)
            team_box_score = AdvancedBoxScoreTeamStatsDeserializer.deserialize_advanced_box_score_team_stats(data)
            self.assertEqual(len(team_box_score), 2)

            charlotte_hornets_box_score = team_box_score[0]
            self.assertEqual(charlotte_hornets_box_score.team, Team.charlotte_hornets)
            self.assertEqual(charlotte_hornets_box_score.seconds_played, 14400)
            self.assertEqual(charlotte_hornets_box_score.offensive_rating, Decimal("116.7"))
            self.assertEqual(charlotte_hornets_box_score.defensive_rating, Decimal("99.2"))
            self.assertEqual(charlotte_hornets_box_score.teammate_assist_percentage, Decimal("56.1"))
            self.assertEqual(charlotte_hornets_box_score.assist_to_turnover_ratio, Decimal("1.6"))
            self.assertEqual(charlotte_hornets_box_score.assists_per_100_possessions, Decimal("18.0"))
            self.assertEqual(charlotte_hornets_box_score.offensive_rebound_percentage, Decimal("17.5"))
            self.assertEqual(charlotte_hornets_box_score.defensive_rebound_percentage, Decimal("74.0"))
            self.assertEqual(charlotte_hornets_box_score.turnovers_per_100_possessions, Decimal("14.3"))
            self.assertEqual(charlotte_hornets_box_score.effective_field_goal_percentage, Decimal("59.3"))
            self.assertEqual(charlotte_hornets_box_score.true_shooting_percentage, Decimal("62.9"))
