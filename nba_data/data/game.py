import datetime

from nba_data.data.matchup import MatchUp
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.outcome import Outcome


class Game:

    def __init__(self, id, match_up, date, season, season_type, home_team_outcome):
        assert isinstance(id, basestring)
        assert isinstance(match_up, MatchUp)
        assert isinstance(date, datetime.date)
        assert isinstance(season, Season)
        assert isinstance(season_type, SeasonType)
        assert isinstance(home_team_outcome, Outcome)

        self.id = id
        self.match_up = match_up
        self.date = date
        self.season = season
        self.season_type = season_type
        self.home_team_outcome = home_team_outcome
