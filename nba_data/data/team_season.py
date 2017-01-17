from nba_data.data.team import Team
from nba_data.data.season import Season


class TeamSeason:
    def __init__(self, team, season):
        assert isinstance(team, Team)
        assert isinstance(season, Season)

        self.team = team
        self.season = season
