import json
import os
from datetime import datetime
from unittest import TestCase

from nba_data.client.deserializers.team_game_log_deserializer import TeamGameLogDeserializer
from nba_data.data.outcome import Outcome
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.team import Team
from tests.config import ROOT_DIRECTORY


class TestTeamGameLogDeserializer(TestCase):
    def test_instantiation(self):
        deserializer = TeamGameLogDeserializer()
        self.assertTrue(deserializer.__dict__ == {})

    def test_deserialize_team_game_log(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/teamgamelog.json')) as data_file:
            data = json.load(data_file)
            deserialized_games = TeamGameLogDeserializer.deserialize_team_game_log(data)
            game = deserialized_games[0]
            self.assertEqual(game.nba_id, "0021501217")
            self.assertEqual(game.matchup.home_team, Team.boston_celtics)
            self.assertEqual(game.matchup.away_team, Team.miami_heat)
            self.assertEqual(game.season, Season.season_2015)
            self.assertEqual(game.season_type, SeasonType.regular_season)
            self.assertEqual(game.home_team_outcome, Outcome.win)
            self.assertEqual(game.date, datetime(year=2016, month=4, day=13).date())

    def test_parse_home_matchup(self):
        home_matchup = TeamGameLogDeserializer.parse_matchup("LAL vs. LAC")
        self.assertEqual(home_matchup.home_team, Team.los_angeles_lakers)
        self.assertEqual(home_matchup.away_team, Team.los_angeles_clippers)

    def test_parse_away_matchup(self):
        away_matchup = TeamGameLogDeserializer.parse_matchup("LAL @ LAC")
        self.assertEqual(away_matchup.home_team, Team.los_angeles_clippers)
        self.assertEqual(away_matchup.away_team, Team.los_angeles_lakers)

    def test_parse_exceptional_matchup(self):
        self.assertRaises(RuntimeError, TeamGameLogDeserializer.parse_matchup, "Jae Bradley")

    def test_parse_date(self):
        self.assertEqual(TeamGameLogDeserializer.parse_date("SEP 19, 1991"), datetime(year=1991, month=9, day=19).date())
