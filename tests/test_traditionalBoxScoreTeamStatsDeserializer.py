import json
import os
from unittest import TestCase

from stats.client.deserializers.traditional_team_box_score_deserializer import TraditionalBoxScoreTeamStatsDeserializer
from stats.data.traditional_team_box_score import TraditionalTeamBoxScore
from stats.data.team import Team
from tests.config import ROOT_DIRECTORY


class TestTraditionalBoxScoreTeamStatsDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(TraditionalBoxScoreTeamStatsDeserializer())

    def test_deserialize_traditional_box_score_player_stats(self):
         with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoretraditionalteamstats.json')) as data_file:
            data = json.load(data_file)
            team_box_scores = TraditionalBoxScoreTeamStatsDeserializer.deserialize_traditional_box_score_team_stats(data)

            self.assertIsNotNone(team_box_scores)
            self.assertEqual(len(team_box_scores), 4)

            spurs_starters = team_box_scores[0]
            self.assertIsInstance(spurs_starters, TraditionalTeamBoxScore)
            self.assertEqual(spurs_starters.team, Team.san_antonio_spurs)
            self.assertEqual(spurs_starters.seconds_played, 8474)
            self.assertEqual(spurs_starters.field_goals_made, 33)
            self.assertEqual(spurs_starters.field_goal_attempts, 51)
            self.assertEqual(spurs_starters.three_point_field_goals_made, 2)
            self.assertEqual(spurs_starters.three_point_field_goal_attempts, 7)
            self.assertEqual(spurs_starters.free_throws_made, 16)
            self.assertEqual(spurs_starters.free_throws_attempts, 17)
            self.assertEqual(spurs_starters.offensive_rebounds, 3)
            self.assertEqual(spurs_starters.defensive_rebounds, 20)
            self.assertEqual(spurs_starters.assists, 17)
            self.assertEqual(spurs_starters.steals, 7)
            self.assertEqual(spurs_starters.blocks, 7)
            self.assertEqual(spurs_starters.turnovers, 3)
            self.assertEqual(spurs_starters.personal_fouls, 8)

