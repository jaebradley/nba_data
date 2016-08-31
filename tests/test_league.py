from unittest import TestCase

from stats.client.query_parameter_generator import League


class TestLeague(TestCase):
    def test(self):
        self.assertEquals(League.get_parameter_name(), "LeagueId")
