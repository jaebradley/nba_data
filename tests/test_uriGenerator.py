from unittest import TestCase

from nba_data.client.uri_generator import UriGenerator


class TestUriGenerator(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(UriGenerator())

    def test_generate_common_all_players_uri(self):
        self.assertEqual(UriGenerator.generate_common_all_players_uri(), "http://nba_data.nba.com/nba_data/commonallplayers")

    def test_generate_team_game_log_uri(self):
        self.assertEqual(UriGenerator.generate_team_game_log_uri(), "http://nba_data.nba.com/nba_data/teamgamelog")

    def test_generate_common_player_info_uri(self):
        self.assertEqual(UriGenerator.generate_common_player_info_uri(), "http://nba_data.nba.com/nba_data/commonplayerinfo")

    def test_generate_advanced_box_score_uri(self):
        self.assertEqual(UriGenerator.generate_advanced_box_score_uri(), "http://nba_data.nba.com/nba_data/boxscoreadvancedv2")
