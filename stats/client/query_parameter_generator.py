from stats.data.team import Team
from stats.data.current_season_only import CurrentSeasonOnly
from stats.data.season import Season
from stats.data.season_type import SeasonType
from stats.data.league import League


class QueryParameterGenerator:

    @staticmethod
    def generate_request_parameters(league=None, season_type=None, season=None, current_season_only=None, team=None):
        parameters = {}

        if league is not None:
            parameters[League.get_parameter_name()] = league.value

        if season_type is not None:
            parameters[SeasonType.get_parameter_name()] = season_type.value

        if season is not None:
            parameters[Season.get_parameter_name()] = season.value

        if current_season_only is not None:
            parameters[CurrentSeasonOnly.get_parameter_name()] = current_season_only.value

        if team is not None:
            parameters[Team.get_parameter_name()] = team.value

        return parameters