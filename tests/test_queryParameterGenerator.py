from unittest import TestCase

from nba_data.client.query_parameter_generator import QueryParameterGenerator
from nba_data.data.league import League
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.team import Team


class TestQueryParameterGenerator(TestCase):
    def test_instantiation(self):
        self.assertEqual(QueryParameterGenerator().__dict__, {})

    def test_generate_request_parameters(self):
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(), {})
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(league=League.nba),
                         {
                             "LeagueId": "00"
                         })
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(season_type=SeasonType.regular_season),
                         {
                             "SeasonType": "Regular Season"
                         })
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(season=Season.season_2015),
                         {
                             "Season": "2015-16"
                         })
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(current_season_only=CurrentSeasonOnly.yes),
                         {
                             "isOnlyCurrentSeason": 1
                         })
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(team=Team.boston_celtics),
                         {
                             "TeamId": 1610612738
                         })
        self.assertEqual(QueryParameterGenerator.generate_request_parameters(player_id=1),
                         {
                             "PlayerId": 1
                         })

    def test_generate_box_score_request_parameters(self):
        self.assertEqual(QueryParameterGenerator.generate_box_score_request_parameters(game_id=1),
                         {
                             "GameId": 1,
                             "RangeType": 0,
                             "StartPeriod": 0,
                             "StartRange": 0,
                             "EndPeriod": 0,
                             "EndRange": 0,
                         })
