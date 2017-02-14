from unittest import TestCase
from datetime import datetime

from nba_data.data.scoreboard_game import ScoreboardGame
from nba_data.data.season import Season
from nba_data.data.team import Team
from nba_data.data.matchup import MatchUp


class TestScoreboardGame(TestCase):
    def test_instantiation(self):
        game_id_value = "1234"
        season_value = Season.season_2016
        start_time_value = datetime.now()
        matchup_value = MatchUp(home_team=Team.atlanta_hawks, away_team=Team.boston_celtics)
        self.assertIsNotNone(ScoreboardGame(id=game_id_value, season=season_value, start_time=start_time_value,
                                            match_up=matchup_value))
        self.assertRaises(AssertionError, ScoreboardGame, 1234, season_value, start_time_value, matchup_value)
        self.assertRaises(AssertionError, ScoreboardGame, game_id_value, 1234, start_time_value, matchup_value)
        self.assertRaises(AssertionError, ScoreboardGame, game_id_value, season_value, 1234, matchup_value)
        self.assertRaises(AssertionError, ScoreboardGame, game_id_value, season_value, start_time_value, 1234)
