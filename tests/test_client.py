from unittest import TestCase

from stats.client.client import Client
from stats.client.query_parameter_generator import Season, Team


class TestClient(TestCase):
    def test_players_for_season(self):
        Client.get_players_for_season(season=Season.season_2015)

    def test_games_for_team(self):
        Client.get_games_for_team(Season.season_2015, Team.boston_celtics)