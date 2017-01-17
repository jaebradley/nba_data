from unittest import TestCase

from nba_data.data.season import Season
from nba_data.data.season_range import SeasonRange


class TestSeasonRange(TestCase):
    def test_instantiation(self):
        start_season = Season.season_2015
        end_season = Season.season_2016
        self.assertIsNotNone(SeasonRange(start=start_season, end=end_season))
        self.assertRaises(AssertionError, SeasonRange, 1, end_season)
        self.assertRaises(AssertionError, SeasonRange, start_season, 1)
