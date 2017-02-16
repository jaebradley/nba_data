from decimal import Decimal
from unittest import TestCase

from nba_data.data.advanced_player_box_score import AdvancedPlayerBoxScore
from nba_data.data.player_status import PlayerStatusType
from nba_data.data.team import Team


class TestAdvancedPlayerBoxScore(TestCase):

    def test_create(self):
        test_player_name = "jae"
        test_player_nba_id = 1
        test_team_nba_id = 1610612738
        box_score = AdvancedPlayerBoxScore.create(player_name=test_player_name, player_id=test_player_nba_id,
                                                  team_id=test_team_nba_id, comment="DNP - jadley", seconds_played=123,
                                                  offensive_rating=Decimal("110.1"), defensive_rating=Decimal("110.2"),
                                                  teammate_assist_percentage=Decimal("50.0"), assist_to_turnover_ratio=Decimal("2.1"),
                                                  assists_per_100_possessions=Decimal("41.4"), offensive_rebound_percentage=Decimal("12.3"),
                                                  defensive_rebound_percentage=Decimal("45.6"), turnovers_per_100_possessions=Decimal("78.9"),
                                                  effective_field_goal_percentage=Decimal("10.1"), true_shooting_percentage=Decimal("4.56"),
                                                  usage_percentage=Decimal("7.89"))

        self.assertEqual(box_score.player.name, "jae")
        self.assertEqual(box_score.player.id, test_player_nba_id)
        self.assertEqual(box_score.player.team, Team.boston_celtics)
        self.assertEqual(box_score.player.status.type, PlayerStatusType.did_not_play)
        self.assertEqual(box_score.player.status.comment, "jadley")
        self.assertEqual(box_score.seconds_played, 123)
        self.assertEqual(box_score.offensive_rating, Decimal("110.1"))
        self.assertEqual(box_score.defensive_rating, Decimal("110.2"))
        self.assertEqual(box_score.teammate_assist_percentage, Decimal("50.0"))
        self.assertEqual(box_score.assist_to_turnover_ratio, Decimal("2.1"))
        self.assertEqual(box_score.assists_per_100_possessions, Decimal("41.4"))
        self.assertEqual(box_score.offensive_rebound_percentage, Decimal("12.3"))
        self.assertEqual(box_score.defensive_rebound_percentage, Decimal("45.6"))
        self.assertEqual(box_score.turnovers_per_100_possessions, Decimal("78.9"))
        self.assertEqual(box_score.effective_field_goal_percentage, Decimal("10.1"))
        self.assertEqual(box_score.true_shooting_percentage, Decimal("4.56"))
        self.assertEqual(box_score.usage_percentage, Decimal("7.89"))
