from unittest import TestCase

from nba_data.data.season import Season, season_name_map, season_start_year_map, season_end_year_map


class TestSeason(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(Season.get_query_parameter_name(), "Season")

    def test_get_season_by_name(self):
        self.assertEqual(Season.get_season_by_name("2015-16"), Season.season_2015)
        self.assertRaises(ValueError, Season.get_season_by_name, "jae")
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

    def test_get_season_by_start_year(self):
        self.assertEqual(Season.get_season_by_start_year(year=2016), Season.season_2016)
        self.assertRaises(ValueError, Season.get_season_by_start_year, "jae")
        self.assertEqual(season_start_year_map,
                         {
                            2016: Season.season_2016,
                            2015: Season.season_2015,
                            2014: Season.season_2014,
                            2013: Season.season_2013,
                            2012: Season.season_2012,
                            2011: Season.season_2011,
                            2010: Season.season_2010,
                            2009: Season.season_2009,
                            2008: Season.season_2008,
                            2007: Season.season_2007,
                            2006: Season.season_2006,
                            2005: Season.season_2005,
                            2004: Season.season_2004,
                            2003: Season.season_2003,
                            2002: Season.season_2002,
                            2001: Season.season_2001,
                            2000: Season.season_2000,
                        })

    def test_get_season_by_end_year(self):
        self.assertEqual(Season.get_season_by_end_year(year=2016), Season.season_2015)
        self.assertRaises(ValueError, Season.get_season_by_end_year, "jae")
        self.assertEqual(season_end_year_map,
                         {
                            2017: Season.season_2016,
                            2016: Season.season_2015,
                            2015: Season.season_2014,
                            2014: Season.season_2013,
                            2013: Season.season_2012,
                            2012: Season.season_2011,
                            2011: Season.season_2010,
                            2010: Season.season_2009,
                            2009: Season.season_2008,
                            2008: Season.season_2007,
                            2007: Season.season_2006,
                            2006: Season.season_2005,
                            2005: Season.season_2004,
                            2004: Season.season_2003,
                            2003: Season.season_2002,
                            2002: Season.season_2001,
                            2001: Season.season_2000,
                        })

    def test_get_season_by_start_and_end_year(self):
        self.assertEqual(Season.get_season_by_start_and_end_year(start_year=2001, end_year=2002). Season.season_2001)
        self.assertRaises(ValueError, Season.get_season_by_start_and_end_year(start_year="jae", end_year="jae"))