from decimal import Decimal
from unittest import TestCase

from nba_data.data.advanced_team_box_score import AdvancedTeamBoxScore
from nba_data.data.team import Team


class TestAdvancedTeamBoxScore(TestCase):
    def test_assertions(self):
        self.assertRaises(AssertionError, AdvancedTeamBoxScore.create, team_id=0, seconds_played=1, offensive_rating=Decimal("123.4"),
                          defensive_rating=Decimal("567.8"), teammate_assist_percentage=Decimal("111.1"), assist_to_turnover_ratio=Decimal("222.2"),
                          assists_per_100_possessions=Decimal("333.3"), offensive_rebound_percentage=Decimal("444.4"),
                          defensive_rebound_percentage=Decimal("555.5"), turnovers_per_100_possessions=Decimal("666.6"),
                          effective_field_goal_percentage=Decimal("777.7"), true_shooting_percentage=Decimal("888.8"))
        self.assertRaises(AssertionError, AdvancedTeamBoxScore, team=0, seconds_played=1, offensive_rating=Decimal("123.4"),
                          defensive_rating=Decimal("567.8"), teammate_assist_percentage=Decimal("111.1"),
                          assist_to_turnover_ratio=Decimal("222.2"), assists_per_100_possessions=Decimal("333.3"),
                          offensive_rebound_percentage=Decimal("444.4"), defensive_rebound_percentage=Decimal("555.5"),
                          turnovers_per_100_possessions=Decimal("666.6"), effective_field_goal_percentage=Decimal("777.7"),
                          true_shooting_percentage=Decimal("888.8"))

    def test_create(self):
        test_team_id = 1610612738
        box_score = AdvancedTeamBoxScore.create(team_id=test_team_id,
                                                seconds_played=100,
                                                offensive_rating=Decimal("123.4"),
                                                defensive_rating=Decimal("567.8"),
                                                teammate_assist_percentage=Decimal("111.1"),
                                                assist_to_turnover_ratio=Decimal("222.2"),
                                                assists_per_100_possessions=Decimal("333.3"),
                                                offensive_rebound_percentage=Decimal("444.4"),
                                                defensive_rebound_percentage=Decimal("555.5"),
                                                turnovers_per_100_possessions=Decimal("666.6"),
                                                effective_field_goal_percentage=Decimal("777.7"),
                                                true_shooting_percentage=Decimal("888.8"))
        self.assertEqual(box_score.team, Team.boston_celtics)
        self.assertEqual(box_score.seconds_played, 100)
        self.assertEqual(box_score.offensive_rating, Decimal("123.4"))
        self.assertEqual(box_score.defensive_rating, Decimal("567.8"))
        self.assertEqual(box_score.teammate_assist_percentage, Decimal("111.1"))
        self.assertEqual(box_score.assist_to_turnover_ratio, Decimal("222.2"))
        self.assertEqual(box_score.assists_per_100_possessions, Decimal("333.3"))
        self.assertEqual(box_score.offensive_rebound_percentage, Decimal("444.4"))
        self.assertEqual(box_score.defensive_rebound_percentage, Decimal("555.5"))
        self.assertEqual(box_score.turnovers_per_100_possessions, Decimal("666.6"))
        self.assertEqual(box_score.effective_field_goal_percentage, Decimal("777.7"))
        self.assertEqual(box_score.true_shooting_percentage, Decimal("888.8"))
