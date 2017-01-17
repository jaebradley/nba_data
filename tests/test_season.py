from unittest import TestCase

from nba_data.data.season import Season


class TestSeason(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(Season.get_query_parameter_name(), "Season")

    def test_get_season_by_name(self):
        self.assertEqual(Season.get_season_by_name("2015-16"), Season.season_2015)
        self.assertRaises(ValueError, Season.get_season_by_name, "jae")

    def test_get_season_by_start_year(self):
        self.assertEqual(Season.get_season_by_start_year(year=2016), Season.season_2016)
        self.assertRaises(ValueError, Season.get_season_by_start_year, "jae")

    def test_get_season_by_end_year(self):
        self.assertEqual(Season.get_season_by_end_year(year=2016), Season.season_2015)
        self.assertRaises(ValueError, Season.get_season_by_end_year, "jae")

    def test_get_season_by_start_and_end_year(self):
        self.assertEqual(Season.get_season_by_start_and_end_year(start_year=2001, end_year=2002), Season.season_2001)
        self.assertRaises(ValueError, Season.get_season_by_start_and_end_year, "jae", "jae")

    def test_get_start_year_by_season(self):
        self.assertEqual(Season.get_start_year_by_season(season=Season.season_2016), 2016)
        self.assertRaises(AssertionError, Season.get_start_year_by_season, "jae")