from unittest import TestCase

from nba_data.data.current_season_only import CurrentSeasonOnly


class TestCurrentSeasonOnly(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(CurrentSeasonOnly.get_query_parameter_name(), "isOnlyCurrentSeason")
