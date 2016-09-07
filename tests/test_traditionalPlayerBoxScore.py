from unittest import TestCase

from stats.data.team import Team
from stats.data.traditional_player_box_score import TraditionalPlayerBoxScore


class TestTraditionalPlayerBoxScore(TestCase):
    def test_create(self):
        test_player_name = "jae"
        test_player_nba_id = 1
        test_team_nba_id = 1610612738

        box_score = TraditionalPlayerBoxScore.create(player_name=test_player_name, player_nba_id=test_player_nba_id,
                                                     team_id=test_team_nba_id, comment="boo", seconds_played=100,
                                                     field_goals_attempts=1, field_goals_made=2,
                                                     three_point_field_goals_made=3, three_point_field_goals_attempts=4,
                                                     free_throws_made=5, free_throws_attempts=6, offensive_rebounds=7,
                                                     defensive_rebounds=8, assists=9, steals=10, blocks=11, turnovers=12,
                                                     personal_fouls=13, plus_minus=14)

        self.assertIsNotNone(box_score)
        self.assertEqual(box_score.player.name, test_player_name)
        self.assertEqual(box_score.player.nba_id, test_player_nba_id)
        self.assertEqual(box_score.player.team, Team.boston_celtics)
        self.assertEqual(box_score.comment, "boo")
        self.assertEqual(box_score.seconds_played, 100)
        self.assertEqual(box_score.field_goals_attempts, 1)
        self.assertEqual(box_score.field_goals_made, 2)
        self.assertEqual(box_score.three_point_field_goals_made, 3)
        self.assertEqual(box_score.three_point_field_goals_attempts, 4)
        self.assertEqual(box_score.free_throws_made, 5)
        self.assertEqual(box_score.free_throws_attempts, 6)
        self.assertEqual(box_score.offensive_rebounds, 7)
        self.assertEqual(box_score.defensive_rebounds, 8)
        self.assertEqual(box_score.assists, 9)
        self.assertEqual(box_score.steals, 10)
        self.assertEqual(box_score.blocks, 11)
        self.assertEqual(box_score.turnovers, 12)
        self.assertEqual(box_score.personal_fouls, 13)
        self.assertEqual(box_score.plus_minus, 14)