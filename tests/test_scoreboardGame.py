from datetime import datetime
from unittest import TestCase

from nba_data.data.game import ScoreboardGame
from nba_data.data.matchup import MatchUp
from nba_data.data.season import Season
from nba_data.data.team import Team


class TestScoreboardGame(TestCase):
    def test_instantiation(self):
        game_id_value = "1234"
        season_value = Season.season_2016
        start_time_value = datetime.now()
        matchup_value = MatchUp(home_team=Team.atlanta_hawks, away_team=Team.boston_celtics)
        self.assertIsNotNone(ScoreboardGame(id=game_id_value, season=season_value, start_time=start_time_value,
                                            match_up=matchup_value))
