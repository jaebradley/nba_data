from datetime import date
from unittest import TestCase

from nba_data.client import Client
from nba_data.data.box_scores import GameBoxScore
from nba_data.data.game import LoggedGame
from nba_data.data.players import Player, DetailedPlayer
from nba_data.data.season import Season
from nba_data.data.team import Team


class TestClient(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(Client())

    def test_get_all_nba_players(self):
        players = Client.get_all_nba_players()
        self.assertIsNotNone(players)
        self.assertIsInstance(players, list)
        self.assertGreater(len(players), 0)

    def test_get_players_for_season(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        self.assertIsNotNone(players)
        self.assertGreater(len(players), 0)
        self.assertIsInstance(players[0], Player)

    def test_get_players_for_all_seasons(self):
        for season in Season:
            players = Client.get_players_for_season(season=season)
            self.assertIsNotNone(players)
            self.assertGreater(len(players), 0)

    def test_get_games_for_team(self):
        games = Client.get_games_for_team(season=Season.season_2015, team=Team.boston_celtics)
        self.assertIsNotNone(games)
        self.assertEqual(len(games), 82)
        self.assertIsInstance(games[0], LoggedGame)

    def test_get_player_info(self):
        player_details = Client.get_player_info(player_id=201566)
        self.assertIsNotNone(player_details)
        self.assertIsInstance(player_details, DetailedPlayer)

    # def test_all_player_info(self):
    #     for player in Client.get_players_for_season(season=Season.season_2015):
    #         player_details = Client.get_player_info(player_id=player.nba_id)
    #         self.assertIsNotNone(player_details)
    #         self.assertIsInstance(player_details, PlayerDetails)

    def test_get_advanced_box_score(self):
        advanced_box_score = Client.get_advanced_box_score(game_id="0021501205")
        self.assertIsNotNone(advanced_box_score)
        self.assertIsInstance(advanced_box_score, GameBoxScore)

    def test_get_traditional_box_score(self):
        traditional_box_score = Client.get_traditional_box_score(game_id="0021501205")
        self.assertIsNotNone(traditional_box_score)
        self.assertIsInstance(traditional_box_score, GameBoxScore)

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
        self.assertGreater(len(players), 0)

