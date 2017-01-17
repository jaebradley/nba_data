from unittest import TestCase
from datetime import date

from nba_data.client import Client
from nba_data.data.box_score import BoxScore
from nba_data.data.game import Game
from nba_data.data.player import Player
from nba_data.data.player_details import PlayerDetails
from nba_data.data.season import Season
from nba_data.data.team import Team


class TestClient(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(Client())

    def test_get_players_for_season_arguments(self):
        self.assertRaises(AssertionError, Client.get_players_for_season, season=None)
        self.assertRaises(AssertionError, Client.get_players_for_season, season=Season.season_2015, league=None)
        self.assertRaises(AssertionError, Client.get_players_for_season, season=Season.season_2015, current_season_only=None)

    def test_get_all_nba_players(self):
        players = Client.get_all_nba_players()
        self.assertIsNotNone(players)
        self.assertIsInstance(players, list)
        self.assertGreater(len(players), 0)

    def test_get_players_for_season(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        self.assertIsNotNone(players)
        self.assertEqual(len(players), 124)
        self.assertIsInstance(players[0], Player)

    def test_get_players_for_all_seasons(self):
        for season in Season:
            players = Client.get_players_for_season(season=season)
            self.assertIsNotNone(players)
            self.assertGreater(len(players), 0)

    def test_get_games_for_team_arguments(self):
        self.assertRaises(AssertionError, Client.get_games_for_team, season=None, team=Team.boston_celtics)
        self.assertRaises(AssertionError, Client.get_games_for_team, season=Season.season_2015, team=None)
        self.assertRaises(AssertionError, Client.get_games_for_team, season=Season.season_2015, team=Team.boston_celtics, season_type=None)

    def test_get_games_for_team(self):
        games = Client.get_games_for_team(season=Season.season_2015, team=Team.boston_celtics)
        self.assertIsNotNone(games)
        self.assertEqual(len(games), 82)
        self.assertIsInstance(games[0], Game)

    def test_get_player_info_arguments(self):
        self.assertRaises(AssertionError, Client.get_player_info, player_id="bae jadley")

    def test_get_player_info(self):
        player_details = Client.get_player_info(player_id=201566)
        self.assertIsNotNone(player_details)
        self.assertIsInstance(player_details, PlayerDetails)

    # def test_all_player_info(self):
    #     for player in Client.get_players_for_season(season=Season.season_2015):
    #         player_details = Client.get_player_info(player_id=player.nba_id)
    #         self.assertIsNotNone(player_details)
    #         self.assertIsInstance(player_details, PlayerDetails)

    def test_get_advanced_box_score_arguments(self):
        self.assertRaises(AssertionError, Client.get_advanced_box_score, game_id=1234)

    def test_get_advanced_box_score(self):
        advanced_box_score = Client.get_advanced_box_score(game_id="0021501205")
        self.assertIsNotNone(advanced_box_score)
        self.assertIsInstance(advanced_box_score, BoxScore)

    def test_get_traditional_box_score_arguments(self):
        self.assertRaises(AssertionError, Client.get_traditional_box_score, game_id=1234)

    def test_get_traditional_box_score(self):
        traditional_box_score = Client.get_traditional_box_score(game_id="0021501205")
        self.assertIsNotNone(traditional_box_score)
        self.assertIsInstance(traditional_box_score, BoxScore)

    def test_get_game_counts_in_date_range(self):
        game_counts = Client.get_game_counts_in_date_range()
        self.assertIsNotNone(game_counts)

    def test_get_games_for_date(self):
        date_value = date(year=2016, month=1, day=1)
        games = Client.get_games_for_date(date_value=date_value)
        self.assertIsNotNone(games)
        self.assertIsNot(len(games), 0)

    def test_get_players(self):
        players = Client.get_players(season=Season.season_2016)
        self.assertIsNotNone(players)
        self.assertEqual(len(players), 778)

