from unittest import TestCase

from nba_data.nba_stats_api_utils.uri_generator import UriGenerator


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

    def test_generate_traditional_box_score_uri(self):
        self.assertEqual(UriGenerator.generate_traditional_box_score_uri(), "http://stats.nba.com/stats/boxscoretraditionalv2")

    def test_generate_calendar_data_uri(self):
        self.assertEqual(UriGenerator.generate_calendar_data_uri(), "http://data.nba.net/data/10s/prod/v1/calendar.json")
