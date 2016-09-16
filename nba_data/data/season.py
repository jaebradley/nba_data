from base_query_parameter import BaseQueryParameter
from enum import Enum


class Season(BaseQueryParameter, Enum):
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

    @staticmethod
    def get_query_parameter_name():
        return "Season"

    @staticmethod
    def get_season(season_name):
        season = season_name_map.get(season_name)

        if season is None:
            raise ValueError("Unknown season name: %s", season_name)

        return season

season_name_map = {
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
}