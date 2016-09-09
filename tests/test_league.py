from unittest import TestCase

from nba_data.nba_stats_api_utils.query_parameter_generator import League


class TestLeague(TestCase):
    def test(self):
        self.assertEquals(League.get_query_parameter_name(), "LeagueId")
