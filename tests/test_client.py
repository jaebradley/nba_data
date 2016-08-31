from unittest import TestCase

from stats.client.client import Client
from stats.client.query_parameter_generator import Season, Team


class TestClient(TestCase):
    def test(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        quincy_acy = players[0]
        quincy_acy.name = "Quincy Acy"
        quincy_acy.id = 203112
        quincy_acy.team = Team.sacramento_kings

        games = Client.get_games_for_team(Season.season_2015, Team.boston_celtics)
