import json
import os
from unittest import TestCase

from nba_data.data.team import Team
from nba_data.data.traditional_team_box_score import TraditionalTeamBoxScore
from nba_data.deserializers.traditional_team_box_score_deserializer import TraditionalTeamBoxScoresDeserializer
from tests.config import ROOT_DIRECTORY


class TestTraditionalBoxScoreTeamStatsDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(TraditionalTeamBoxScoresDeserializer())

    def test_deserialize_traditional_box_score_player_stats(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoretraditionalteamstats.json')) as data_file:
            data = json.load(data_file)
            team_box_scores = TraditionalTeamBoxScoresDeserializer.deserialize(data)

            self.assertIsNotNone(team_box_scores)
            self.assertEqual(len(team_box_scores), 2)

            spurs = team_box_scores[0]
            self.assertIsInstance(spurs, TraditionalTeamBoxScore)
            self.assertEqual(spurs.team, Team.san_antonio_spurs)
            self.assertEqual(spurs.seconds_played, 14400)
            self.assertEqual(spurs.field_goals_made, 47)
            self.assertEqual(spurs.field_goal_attempts, 85)
            self.assertEqual(spurs.three_point_field_goals_made, 4)
            self.assertEqual(spurs.three_point_field_goal_attempts, 19)
            self.assertEqual(spurs.free_throws_made, 18)
            self.assertEqual(spurs.free_throw_attempts, 19)
            self.assertEqual(spurs.offensive_rebounds, 9)
            self.assertEqual(spurs.defensive_rebounds, 37)
            self.assertEqual(spurs.assists, 28)
            self.assertEqual(spurs.steals, 13)
            self.assertEqual(spurs.blocks, 7)
            self.assertEqual(spurs.turnovers, 9)
            self.assertEqual(spurs.personal_fouls, 16)

