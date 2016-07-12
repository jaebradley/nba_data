from unittest import TestCase

from QueryParameter import League


class TestLeague(TestCase):
    def test(self):
        self.assertEquals(League.get_parameter_name(), "LeagueId")
