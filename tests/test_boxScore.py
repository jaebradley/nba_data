from unittest import TestCase

from nba_data.data.box_score import BoxScore


class TestBoxScore(TestCase):
    def test_instantiation(self):
        test_box_score = BoxScore(game_id="bae", player_box_scores=[], team_box_scores=[])
        self.assertIsNotNone(test_box_score)
        self.assertEqual(test_box_score.game_id, "bae")
        self.assertEqual(test_box_score.player_box_scores, [])
        self.assertEqual(test_box_score.team_box_scores, [])
