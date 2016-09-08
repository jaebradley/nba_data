from unittest import TestCase

from stats.client.uri_generator import UriGenerator


class TestUriGenerator(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(UriGenerator())

    def test_generate_common_all_players_uri(self):
        self.assertEqual(UriGenerator.generate_common_all_players_uri(), "http://stats.nba.com/stats/commonallplayers")

    def test_generate_team_game_log_uri(self):
        self.assertEqual(UriGenerator.generate_team_game_log_uri(), "http://stats.nba.com/stats/teamgamelog")

    def test_generate_common_player_info_uri(self):
        self.assertEqual(UriGenerator.generate_common_player_info_uri(), "http://stats.nba.com/stats/commonplayerinfo")

    def test_generate_advanced_box_score_uri(self):
        self.assertEqual(UriGenerator.generate_advanced_box_score_uri(), "http://stats.nba.com/stats/boxscoreadvancedv2")
