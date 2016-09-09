from unittest import TestCase

from nba_data.data.season import Season, season_name_map


class TestSeason(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(Season.get_query_parameter_name(), "Season")

    def test_get_season(self):
        self.assertEqual(Season.get_season("2015-16"), Season.season_2015)
        self.assertRaises(ValueError, Season.get_season, "jae")
        self.assertEqual(season_name_map,
                         {
                             "2015-16": Season.season_2015
                         })
