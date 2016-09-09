from unittest import TestCase

from nba_data.client.query_parameter_generator import League


class TestLeague(TestCase):
    def test(self):
        self.assertEquals(League.get_query_parameter_name(), "LeagueId")
