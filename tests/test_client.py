from unittest import TestCase
from stats.client.client import Client
from stats.client.query_parameter import Season


class TestClient(TestCase):
    def test(self):
        client = Client()
        print client.get_all_players(season=Season.season_2015)
