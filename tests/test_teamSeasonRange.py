from unittest import TestCase

from nba_data.data.season import Season
from nba_data.data.season_range import SeasonRange
from nba_data.data.team import Team
from nba_data.data.team_season_range import TeamSeasonRange


class TestTeamSeasonRange(TestCase):
    def test_instantiation(self):
        team = Team.atlanta_hawks
        start_season = Season.season_2015
        end_season = Season.season_2016
        season_range = SeasonRange(start=start_season, end=end_season)
        self.assertIsNotNone(TeamSeasonRange(team=team, season_range=season_range))
