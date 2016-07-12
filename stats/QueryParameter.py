from enum import Enum


class BaseQueryParameter(Enum):
    @staticmethod
    def get_parameter_name():
        return ""


class League(BaseQueryParameter):

    nba = "00"
    aba = "01"

    @staticmethod
    def get_parameter_name():
        return "LeagueId"


class SeasonType(BaseQueryParameter):

    regular_season = "Regular Season"
    pre_season = "Pre Season"
    playoffs = "Playoffs"
    all_star = "All-Star"

    @staticmethod
    def get_parameter_name():
        return "Season Type"


class Season(BaseQueryParameter):

    season_2015 = "2015-16"

    @staticmethod
    def get_parameter_name():
        return "Season"


class CurrentSeasonOnly(BaseQueryParameter):

    yes = "1"
    no = "0"

    @staticmethod
    def get_parameter_name():
        return "isOnlyCurrentSeason"


def generate_request_parameters(league=None, season_type=None, season=None, current_season_only=None):
    return {
        League.get_parameter_name(): league,
        SeasonType.get_parameter_name(): season_type,
        Season.get_parameter_name(): season,
        CurrentSeasonOnly.get_parameter_name(): current_season_only
    }