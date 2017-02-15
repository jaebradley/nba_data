from unittest import TestCase

from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.league import League
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.team import Team
from nba_data.nba_stats_api_utils.query_parameter_generator import QueryParameterGenerator


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
        self.assertEqual(QueryParameterGenerator.generate_box_score_request_parameters(game_id="1234"),
                         {
                             "GameId": "1234",
                             "RangeType": 0,
                             "StartPeriod": 0,
                             "StartRange": 0,
                             "EndPeriod": 0,
                             "EndRange": 0,
                         })

    def test_assertion_checking_for_box_score_request_parameters(self):
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", start_period=-1)
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", end_period=-1)
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", start_range=-1)
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", end_range=-1)
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", range_type=-1)

        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", start_period=5, end_period=1)
        self.assertRaises(AssertionError, QueryParameterGenerator.generate_box_score_request_parameters, game_id="foo", start_range=5, end_range=1)

