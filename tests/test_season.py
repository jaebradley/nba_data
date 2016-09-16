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
                             "2015-16": Season.season_2015,
                             "2014-15": Season.season_2014,
                             "2013-14": Season.season_2013,
                             "2012-13": Season.season_2012,
                             "2011-12": Season.season_2011,
                             "2010-11": Season.season_2010,
                             "2009-10": Season.season_2009,
                             "2008-09": Season.season_2008,
                             "2007-08": Season.season_2007,
                             "2006-07": Season.season_2006,
                             "2005-06": Season.season_2005,
                             "2004-05": Season.season_2004,
                             "2003-04": Season.season_2003,
                             "2002-03": Season.season_2002,
                             "2001-02": Season.season_2001,
                             "2000-01": Season.season_2000,
                         })
