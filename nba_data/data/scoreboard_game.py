from datetime import datetime

from nba_data.data.matchup import Matchup
from nba_data.data.season import Season

# TODO: @jbradley in the future, reconcile / deprecate Game class
# TODO: @jbradley currently this class is fulfilling needs of dfs_site_data project - in the future, add more fields


class ScoreboardGame:

    def __init__(self, game_id, season, start_time, matchup):
        assert isinstance(game_id, str)
        assert isinstance(season, Season)
        assert isinstance(start_time, datetime)
        assert isinstance(matchup, Matchup)

        self.game_id = game_id
        self.season = season
        self.start_time = start_time
        self.matchup = matchup

