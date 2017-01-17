from nba_data.data.team import Team
from nba_data.data.season_range import SeasonRange


class TeamSeasonRange:
    def __init__(self, team, season_range):
        assert isinstance(team, Team)
        assert isinstance(season_range, SeasonRange)

        self.team = team
        self.season_range = season_range
