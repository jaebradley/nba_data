from enum import Enum

from base_query_parameter import BaseQueryParameter


class Season(BaseQueryParameter, Enum):
    season_2016 = "2016-17"
    season_2015 = "2015-16"
    season_2014 = "2014-15"
    season_2013 = "2013-14"
    season_2012 = "2012-13"
    season_2011 = "2011-12"
    season_2010 = "2010-11"
    season_2009 = "2009-10"
    season_2008 = "2008-09"
    season_2007 = "2007-08"
    season_2006 = "2006-07"
    season_2005 = "2005-06"
    season_2004 = "2004-05"
    season_2003 = "2003-04"
    season_2002 = "2002-03"
    season_2001 = "2001-02"
    season_2000 = "2000-01"
    season_1999 = "1999-00"
    season_1998 = "1998-99"
    season_1997 = "1997-98"
    season_1996 = "1996-97"
    season_1995 = "1995-96"

    @staticmethod
    def get_query_parameter_name():
        return "Season"

    @staticmethod
    def get_season_by_name(name):
        season = season_name_map.get(name)

        if season is None:
            raise ValueError("Unknown season name: %s", name)

        return season

    @staticmethod
    def get_season_by_start_year(year):
        season = start_year_to_season_map.get(year)

        if season is None:
            raise ValueError("Unknown season start year: %s", year)

        return season

    @staticmethod
    def get_season_by_end_year(year):
        season = season_end_year_map.get(year)

        if season is None:
            raise ValueError("Unknown season end year: %s", year)

        return season

    @staticmethod
    def get_season_by_start_and_end_year(start_year, end_year):
        start_year_season = Season.get_season_by_start_year(year=start_year)
        end_year_season = Season.get_season_by_end_year(year=end_year)

        if start_year_season is not end_year_season:
            raise ValueError("Cannot find season with start year: %s and end year: %s", start_year, end_year)

        return start_year_season

    @staticmethod
    def get_start_year_by_season(season):
        assert isinstance(season, Season)

        start_year = season_to_start_year_map.get(season)

        if start_year is None:
            raise ValueError("Cannot find start year for season: %s", season)

        return start_year

season_name_map = {
    "2016-17": Season.season_2016,
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
    "1999-00": Season.season_1999,
    "1998-99": Season.season_1998,
    "1997-98": Season.season_1997,
    "1996-97": Season.season_1996,
    "1995-96": Season.season_1995
}

start_year_to_season_map = {
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
    1999: Season.season_1999,
    1998: Season.season_1998,
    1997: Season.season_1997,
    1996: Season.season_1996,
    1995: Season.season_1995,
}

season_to_start_year_map = {
    Season.season_2016: 2016,
    Season.season_2015: 2015,
    Season.season_2014: 2014,
    Season.season_2013: 2013,
    Season.season_2012: 2012,
    Season.season_2011: 2011,
    Season.season_2010: 2010,
    Season.season_2009: 2009,
    Season.season_2008: 2008,
    Season.season_2007: 2007,
    Season.season_2006: 2006,
    Season.season_2005: 2005,
    Season.season_2004: 2004,
    Season.season_2003: 2003,
    Season.season_2002: 2002,
    Season.season_2001: 2001,
    Season.season_2000: 2000,
    Season.season_1999: 1999,
    Season.season_1998: 1998,
    Season.season_1997: 1997,
    Season.season_1996: 1996,
    Season.season_1995: 1995,
}

season_end_year_map = {
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
    2000: Season.season_1999,
    1999: Season.season_1998,
    1998: Season.season_1997,
    1997: Season.season_1996,
    1996: Season.season_1995,
}