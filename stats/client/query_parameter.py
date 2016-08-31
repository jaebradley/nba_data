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
        return "SeasonType"


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
    boston_celtics = TeamObject.get_id(TeamObject.boston_celtics)
    brooklyn_nets = TeamObject.get_id(TeamObject.brooklyn_nets)
    charlotte_hornets = TeamObject.get_id(TeamObject.charlotte_hornets)
    chicago_bulls = TeamObject.get_id(TeamObject.chicago_bulls)
    cleveland_cavaliers = TeamObject.get_id(TeamObject.cleveland_cavaliers)
    dallas_mavericks = TeamObject.get_id(TeamObject.dallas_mavericks)
    denver_nuggets = TeamObject.get_id(TeamObject.denver_nuggets)
    detroit_pistons = TeamObject.get_id(TeamObject.detroit_pistons)
    golden_state_warriors = TeamObject.get_id(TeamObject.golden_state_warriors)
    houston_rockets = TeamObject.get_id(TeamObject.houston_rockets)
    indiana_pacers = TeamObject.get_id(TeamObject.indiana_pacers)
    los_angeles_clippers = TeamObject.get_id(TeamObject.los_angeles_clippers)
    los_angeles_lakers = TeamObject.get_id(TeamObject.los_angeles_lakers)
    memphis_grizzlies = TeamObject.get_id(TeamObject.memphis_grizzlies)
    miami_heat = TeamObject.get_id(TeamObject.miami_heat)
    milwaukee_bucks = TeamObject.get_id(TeamObject.milwaukee_bucks)
    minnesota_timberwolves = TeamObject.get_id(TeamObject.minnesota_timberwolves)
    new_orleans_pelicans = TeamObject.get_id(TeamObject.new_orleans_pelicans)
    new_york_knicks = TeamObject.get_id(TeamObject.new_york_knicks)
    oklahoma_city_thunder = TeamObject.get_id(TeamObject.oklahoma_city_thunder)
    orlando_magic = TeamObject.get_id(TeamObject.orlando_magic)
    philadelphia_76ers = TeamObject.get_id(TeamObject.philadelphia_76ers)
    phoenix_suns = TeamObject.get_id(TeamObject.phoenix_suns)
    portland_trail_blazers = TeamObject.get_id(TeamObject.portland_trail_blazers)
    sacramento_kings = TeamObject.get_id(TeamObject.sacramento_kings)
    san_antonio_spurs = TeamObject.get_id(TeamObject.san_antonio_spurs)
    toronto_raptors = TeamObject.get_id(TeamObject.toronto_raptors)
    utah_jazz = TeamObject.get_id(TeamObject.utah_jazz)
    washington_wizards = TeamObject.get_id(TeamObject.washington_wizards)

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