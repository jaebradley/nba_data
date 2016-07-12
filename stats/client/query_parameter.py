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


class Team(BaseQueryParameter):
    atlanta_hawks = 1610612737
    boston_celtics = 1610612738
    brooklyn_nets = 1610612751
    charlotte_hornets = 1610612766
    chicago_bulls = 1610612741
    cleveland_cavaliers = 1610612739
    dallas_mavericks = 1610612742
    denver_nuggets = 1610612743
    detroit_pistons = 1610612765
    golden_state_warriors = 1610612744
    houston_rockets = 1610612745
    indiana_pacers = 1610612754
    los_angeles_clippers = 1610612746
    los_angeles_lakers = 1610612747
    memphis_grizzlies = 1610612763
    miami_heat = 1610612748
    milwaukee_bucks = 1610612749
    minnesota_timberwolves = 1610612750
    new_orleans_pelicans = 1610612740
    new_york_knicks = 1610612752
    oklahoma_city_thunder = 1610612760
    orlando_magic = 1610612753
    philadelphia_76ers = 1610612755
    phoenix_suns = 1610612756
    portland_trail_blazers = 1610612757
    sacramento_kings = 1610612758
    san_antonio_spurs = 1610612759
    toronto_raptors = 1610612761
    utah_jazz = 1610612762
    washington_wizards = 1610612764

    @staticmethod
    def get_parameter_name():
        return "TeamId"


def generate_request_parameters(league=None, season_type=None, season=None, current_season_only=None, team=None):
    return {
        League.get_parameter_name(): league,
        SeasonType.get_parameter_name(): season_type,
        Season.get_parameter_name(): season,
        CurrentSeasonOnly.get_parameter_name(): current_season_only,
        Team.get_parameter_name(): team,
    }