from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.league import League
from nba_data.data.player import Player
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.team import Team


class QueryParameterGenerator:

    game_id_parameter_name = "GameId"
    start_period_parameter_name = "StartPeriod"
    end_period_parameter_name = "EndPeriod"
    start_range_parameter_name = "StartRange"
    end_range_parameter_name = "EndRange"
    range_type_parameter_name = "RangeType"

    def __init__(self):
        pass

    @staticmethod
    def generate_request_parameters(league=None, season_type=None, season=None, current_season_only=None, team=None,
                                    player_id=None):
        parameters = {}

        if league is not None:
            assert isinstance(league, League)

            parameters[League.get_query_parameter_name()] = league.value

        if season_type is not None:
            assert isinstance(season_type, SeasonType)

            parameters[SeasonType.get_query_parameter_name()] = season_type.value

        if season is not None:
            assert isinstance(season, Season)

            parameters[Season.get_query_parameter_name()] = season.value

        if current_season_only is not None:
            assert isinstance(current_season_only, CurrentSeasonOnly)

            parameters[CurrentSeasonOnly.get_query_parameter_name()] = current_season_only.value

        if team is not None:
            assert isinstance(team, Team)

            parameters[Team.get_query_parameter_name()] = Team.get_id(team=team)

        if player_id is not None:
            assert isinstance(player_id, int)

            parameters[Player.get_query_parameter_name()] = player_id

        return parameters

    @staticmethod
    def generate_box_score_request_parameters(game_id, start_period=0, end_period=0, start_range=0, end_range=0,
                                              range_type=0):
        assert isinstance(game_id, str)
        assert isinstance(start_period, int)
        assert isinstance(end_period, int)
        assert isinstance(start_range, int)
        assert isinstance(end_range, int)
        assert isinstance(range_type, int)

        assert start_period >= 0
        assert end_period >= 0
        assert end_period >= start_period
        assert start_range >= 0
        assert end_range >= 0
        assert end_range >= start_range
        assert range_type >= 0

        parameters = {}

        parameters[QueryParameterGenerator.game_id_parameter_name] = game_id
        parameters[QueryParameterGenerator.start_period_parameter_name] = start_period
        parameters[QueryParameterGenerator.end_period_parameter_name] = end_period
        parameters[QueryParameterGenerator.start_range_parameter_name] = start_range
        parameters[QueryParameterGenerator.end_range_parameter_name] = end_range
        parameters[QueryParameterGenerator.range_type_parameter_name] = range_type

        return parameters
