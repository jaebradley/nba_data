from unittest import TestCase

from stats.client.client import Client
from stats.client.query_parameter import Season
from stats.data.team import Team


class TestClient(TestCase):
    def test(self):
        players = Client.get_players_for_season(season=Season.season_2015)
        quincy_acy = players[0]
        quincy_acy.name = "Quincy Acy"
        quincy_acy.id = 203112
        quincy_acy.team = Team.sacramento_kings
