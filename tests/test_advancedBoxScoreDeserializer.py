import json
import os
from decimal import Decimal
from unittest import TestCase

from nba_data.data.player_status import PlayerStatusType
from nba_data.data.team import Team
from nba_data.deserializers.advanced_box_score_deserializer import AdvancedBoxScoreDeserializer
from tests.config import ROOT_DIRECTORY


class TestAdvancedBoxScoreDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(AdvancedBoxScoreDeserializer())

    def test_deserialize_advanced_box_score(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/boxscoreadvanced.json')) as data_file:
            data = json.load(data_file)
            advanced_box_score = AdvancedBoxScoreDeserializer().deserialize(data)
            self.assertEqual(advanced_box_score.game_id, "0021501205")
            self.assertEqual(len(advanced_box_score.player_box_scores), 26)

            nicolas_batum_box_score = advanced_box_score.player_box_scores[0]
            self.assertEqual(nicolas_batum_box_score.player.id, 201587)
            self.assertEqual(nicolas_batum_box_score.player.name, "Nicolas Batum")
            self.assertEqual(nicolas_batum_box_score.player.team, Team.charlotte_hornets)
            self.assertEqual(nicolas_batum_box_score.player.status.type, PlayerStatusType.active)
            self.assertIsNone(nicolas_batum_box_score.player.status.comment)
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

            self.assertEqual(len(advanced_box_score.team_box_scores), 2)
            charlotte_hornets_box_score = advanced_box_score.team_box_scores[0]
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
