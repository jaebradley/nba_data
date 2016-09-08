from unittest import TestCase, skip

from stats.data.season import Season
from stats.client.client import Client
from stats.data.advanced_box_score import AdvancedBoxScore
from stats.data.player import Player
from stats.data.player_details import PlayerDetails
from stats.data.team import Team
from stats.data.game import Game


@skip("skip non-local testing")
class TestClient(TestCase):
    def test_get_players_for_season(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        self.assertIsNotNone(players)
        self.assertEqual(len(players), 2000)
        self.assertIsInstance(players[0], Player)

    def test_get_games_for_team(self):
        games = Client.get_games_for_team(season=Season.season_2015, team=Team.boston_celtics)
        self.assertIsNotNone(games)
        self.assertEqual(len(games), 82)
        self.assertIsInstance(games[0], Game)

    def test_get_player_info(self):
        player_details = Client.get_player_info(player_id=201566)
        self.assertIsNotNone(player_details)
        self.assertIsInstance(player_details, PlayerDetails)
    
    def test_get_advanced_box_score(self):
        advanced_box_score = Client.get_advanced_box_score(game_id="0021501205")
        self.assertIsNotNone(advanced_box_score)
        self.assertIsInstance(advanced_box_score, AdvancedBoxScore)


