from datetime import datetime
from unittest import TestCase

from stats.data.outcome import Outcome
from stats.data.season_type import SeasonType
from stats.client.client import Client
from stats.client.query_parameter_generator import Season, Team


class TestClient(TestCase):
    def test_players_for_season(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        self.assertTrue(players.__len__() > 0)

        quincy_acy = players[0]
        self.assertEqual(quincy_acy.name, "Quincy Acy")
        self.assertEqual(quincy_acy.nba_id, 203112)
        self.assertEqual(quincy_acy.team, Team.sacramento_kings)

    def test_games_for_team(self):
        games = Client.get_games_for_team(Season.season_2015, Team.boston_celtics)
        self.assertTrue(games.__len__() > 0)

        game = games[0]
        self.assertEqual(game.nba_id, "0021501217")
        self.assertEqual(game.home_team, Team.boston_celtics)
        self.assertEqual(game.away_team, Team.miami_heat)
        self.assertEqual(game.season, Season.season_2015)
        self.assertEqual(game.season_type, SeasonType.regular_season)
        self.assertEqual(game.home_team_outcome, Outcome.win)
        self.assertEqual(game.date, datetime(year=2016, month=4, day=13).date())
