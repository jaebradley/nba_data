from datetime import datetime

from nba_data.data.matchup import MatchUp
from nba_data.data.season import Season

# TODO: @jbradley in the future, reconcile / deprecate Game class
# TODO: @jbradley currently this class is fulfilling needs of dfs_site_data project - in the future, add more fields


class ScoreboardGame:

    def __init__(self, id, season, start_time, match_up):
        assert isinstance(id, basestring)
        assert isinstance(season, Season)
        assert isinstance(start_time, datetime)
        assert isinstance(match_up, MatchUp)

        self.id = id
        self.season = season
        self.start_time = start_time
        self.match_up = match_up

