from enum import Enum

from stats.data.team import Team as TeamObject


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

    yes = 1
    no = 0

    @staticmethod
    def get_parameter_name():
        return "isOnlyCurrentSeason"


class Team(BaseQueryParameter):
    atlanta_hawks = TeamObject.get_id(TeamObject.atlanta_hawks)
    boston_celtics = TeamObject.get_id(TeamObject.atlanta_hawks)
    brooklyn_nets = TeamObject.get_id(TeamObject.atlanta_hawks)
    charlotte_hornets = TeamObject.get_id(TeamObject.atlanta_hawks)
    chicago_bulls = TeamObject.get_id(TeamObject.atlanta_hawks)
    cleveland_cavaliers = TeamObject.get_id(TeamObject.atlanta_hawks)
    dallas_mavericks = TeamObject.get_id(TeamObject.atlanta_hawks)
    denver_nuggets = TeamObject.get_id(TeamObject.atlanta_hawks)
    detroit_pistons = TeamObject.get_id(TeamObject.atlanta_hawks)
    golden_state_warriors = TeamObject.get_id(TeamObject.atlanta_hawks)
    houston_rockets = TeamObject.get_id(TeamObject.atlanta_hawks)
    indiana_pacers = TeamObject.get_id(TeamObject.atlanta_hawks)
    los_angeles_clippers = TeamObject.get_id(TeamObject.atlanta_hawks)
    los_angeles_lakers = TeamObject.get_id(TeamObject.atlanta_hawks)
    memphis_grizzlies = TeamObject.get_id(TeamObject.atlanta_hawks)
    miami_heat = TeamObject.get_id(TeamObject.atlanta_hawks)
    milwaukee_bucks = TeamObject.get_id(TeamObject.atlanta_hawks)
    minnesota_timberwolves = TeamObject.get_id(TeamObject.atlanta_hawks)
    new_orleans_pelicans = TeamObject.get_id(TeamObject.atlanta_hawks)
    new_york_knicks = TeamObject.get_id(TeamObject.atlanta_hawks)
    oklahoma_city_thunder = TeamObject.get_id(TeamObject.atlanta_hawks)
    orlando_magic = TeamObject.get_id(TeamObject.atlanta_hawks)
    philadelphia_76ers = TeamObject.get_id(TeamObject.atlanta_hawks)
    phoenix_suns = TeamObject.get_id(TeamObject.atlanta_hawks)
    portland_trail_blazers = TeamObject.get_id(TeamObject.atlanta_hawks)
    sacramento_kings = TeamObject.get_id(TeamObject.atlanta_hawks)
    san_antonio_spurs = TeamObject.get_id(TeamObject.atlanta_hawks)
    toronto_raptors = TeamObject.get_id(TeamObject.atlanta_hawks)
    utah_jazz = TeamObject.get_id(TeamObject.atlanta_hawks)
    washington_wizards = TeamObject.get_id(TeamObject.atlanta_hawks)

    @staticmethod
    def get_parameter_name():
        return "TeamId"


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