from unittest import TestCase

from stats.data.season_type import SeasonType, season_type_name_map


class TestSeasonType(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(SeasonType.get_query_parameter_name(), "SeasonType")

    def test_get_season_typea(self):
        self.assertEqual(SeasonType.get_season_type("Regular Season"), SeasonType.regular_season)
        self.assertRaises(ValueError, SeasonType.get_season_type, "regular season")
        self.assertEqual(season_type_name_map,
                         {
                            "Regular Season": SeasonType.regular_season,
                            "Pre Season": SeasonType.pre_season,
                            "Playoffs": SeasonType.playoffs,
                            "All-Star": SeasonType.all_star,
                         })

