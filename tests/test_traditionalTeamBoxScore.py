from unittest import TestCase

from stats.data.team import Team
from stats.data.traditional_team_box_score import TraditionalTeamBoxScore


class TestTraditionalTeamBoxScore(TestCase):
    def test_create(self):
        test_team_id = 1610612738
        box_score = TraditionalTeamBoxScore.create(team_id=test_team_id, seconds_played=1,
                                                   field_goals_made=2, field_goal_attempts=3,
                                                   three_point_field_goals_made=4,
                                                   three_point_field_goal_attempts=5, free_throws_made=6,
                                                   free_throws_attempts=7,
                                                   offensive_rebounds=8, defensive_rebounds=9, steals=10, blocks=11,
                                                   turnovers=12, personal_fouls=13, assists=14)

        self.assertIsNotNone(box_score)
        self.assertEqual(box_score.team, Team.boston_celtics)
        self.assertEqual(box_score.seconds_played, 1)
        self.assertEqual(box_score.field_goals_made, 2)
        self.assertEqual(box_score.field_goal_attempts, 3)
        self.assertEqual(box_score.three_point_field_goals_made, 4)
        self.assertEqual(box_score.three_point_field_goal_attempts, 5)
        self.assertEqual(box_score.free_throws_made, 6)
        self.assertEqual(box_score.free_throws_attempts, 7)
        self.assertEqual(box_score.offensive_rebounds, 8)
        self.assertEqual(box_score.defensive_rebounds, 9)
        self.assertEqual(box_score.steals, 10)
        self.assertEqual(box_score.blocks, 11)
        self.assertEqual(box_score.turnovers, 12)
        self.assertEqual(box_score.personal_fouls, 13)
        self.assertEqual(box_score.assists, 14)
