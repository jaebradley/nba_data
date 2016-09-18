from enum import Enum

from base_query_parameter import BaseQueryParameter


class Team(BaseQueryParameter, Enum):
    atlanta_hawks = "Atlanta Hawks"
    boston_celtics = "Boston Celtics"
    brooklyn_nets = "Brooklyn Nets"
    charlotte_hornets = "Charlotte Hornets"
    chicago_bulls = "Chicago Bulls"
    cleveland_cavaliers = "Cleveland Cavaliers"
    dallas_mavericks = "Dallas Mavericks"
    denver_nuggets = "Denver Nuggets"
    detroit_pistons = "Detroit Pistons"
    golden_state_warriors = "Golden State Warriors"
    houston_rockets = "Houston Rockets"
    indiana_pacers = "Indiana Pacers"
    los_angeles_clippers = "Los Angeles Clippers"
    los_angeles_lakers = "Los Angeles Lakers"
    memphis_grizzlies = "Memphis Grizzlies"
    miami_heat = "Miami Heat"
    milwaukee_bucks = "Milwaukee Bucks"
    minnesota_timberwolves = "Minnesota Timberwolves"
    new_orleans_pelicans = "New Orleans Pelicans"
    new_york_knicks = "New York Knicks"
    oklahoma_city_thunder = "Oklahoma City Thunder"
    orlando_magic = "Orlando Magic"
    philadelphia_76ers = "Philadelphia 76ers"
    phoenix_suns = "Phoenix Suns"
    portland_trail_blazers = "Portland Trail Blazers"
    sacramento_kings = "Sacramento Kings"
    san_antonio_spurs = "San Antonio Spurs"
    toronto_raptors = "Toronto Raptors"
    utah_jazz = "Utah Jazz"
    washington_wizards = "Washington Wizards"

    @staticmethod
    def get_query_parameter_name():
        return "TeamId"

    @staticmethod
    def get_team_by_id(team_id):
        assert isinstance(team_id, int)

        return team_id_to_name_map.get(team_id)

    @staticmethod
    def get_id(team):
        assert isinstance(team, Team)

        return team_name_to_id_map.get(team)

    @staticmethod
    def get_team_by_abbreviation(abbreviation):
        assert isinstance(abbreviation, str)

        return team_abbreviation_to_name_map.get(abbreviation.upper())

"""
https://github.com/seemethere/nba_py/wiki/nba_data.nba.com-Endpoint-Documentation#current-teams
"""

team_id_to_name_map = {
    1610612737: Team.atlanta_hawks,
    1610612738: Team.boston_celtics,
    1610612751: Team.brooklyn_nets,
    1610612766: Team.charlotte_hornets,
    1610612741: Team.chicago_bulls,
    1610612739: Team.cleveland_cavaliers,
    1610612742: Team.dallas_mavericks,
    1610612743: Team.denver_nuggets,
    1610612765: Team.detroit_pistons,
    1610612744: Team.golden_state_warriors,
    1610612745: Team.houston_rockets,
    1610612754: Team.indiana_pacers,
    1610612746: Team.los_angeles_clippers,
    1610612747: Team.los_angeles_lakers,
    1610612763: Team.memphis_grizzlies,
    1610612748: Team.miami_heat,
    1610612749: Team.milwaukee_bucks,
    1610612750: Team.minnesota_timberwolves,
    1610612740: Team.new_orleans_pelicans,
    1610612752: Team.new_york_knicks,
    1610612760: Team.oklahoma_city_thunder,
    1610612753: Team.orlando_magic,
    1610612755: Team.philadelphia_76ers,
    1610612756: Team.phoenix_suns,
    1610612757: Team.portland_trail_blazers,
    1610612758: Team.sacramento_kings,
    1610612759: Team.san_antonio_spurs,
    1610612761: Team.toronto_raptors,
    1610612762: Team.utah_jazz,
    1610612764: Team.washington_wizards,
}

team_name_to_id_map = {
    Team.atlanta_hawks: 1610612737,
    Team.boston_celtics: 1610612738,
    Team.brooklyn_nets: 1610612751,
    Team.charlotte_hornets: 1610612766,
    Team.chicago_bulls: 1610612741,
    Team.cleveland_cavaliers: 1610612739,
    Team.dallas_mavericks: 1610612742,
    Team.denver_nuggets: 1610612743,
    Team.detroit_pistons: 1610612765,
    Team.golden_state_warriors: 1610612744,
    Team.houston_rockets: 1610612745,
    Team.indiana_pacers: 1610612754,
    Team.los_angeles_clippers: 1610612746,
    Team.los_angeles_lakers: 1610612747,
    Team.memphis_grizzlies: 1610612763,
    Team.miami_heat: 1610612748,
    Team.milwaukee_bucks: 1610612749,
    Team.minnesota_timberwolves: 1610612750,
    Team.new_orleans_pelicans: 1610612740,
    Team.new_york_knicks: 1610612752,
    Team.oklahoma_city_thunder: 1610612760,
    Team.orlando_magic: 1610612753,
    Team.philadelphia_76ers: 1610612755,
    Team.phoenix_suns: 1610612756,
    Team.portland_trail_blazers: 1610612757,
    Team.sacramento_kings: 1610612758,
    Team.san_antonio_spurs: 1610612759,
    Team.toronto_raptors: 1610612761,
    Team.utah_jazz: 1610612762,
    Team.washington_wizards: 1610612764
}

team_abbreviation_to_name_map = {
    "ATL": Team.atlanta_hawks,
    "BOS": Team.boston_celtics,
    "BKN": Team.brooklyn_nets,
    "CHA": Team.charlotte_hornets,
    "CHI": Team.chicago_bulls,
    "CLE": Team.cleveland_cavaliers,
    "DAL": Team.dallas_mavericks,
    "DEN": Team.denver_nuggets,
    "DET": Team.detroit_pistons,
    "GSW": Team.golden_state_warriors,
    "HOU": Team.houston_rockets,
    "IND": Team.indiana_pacers,
    "LAC": Team.los_angeles_clippers,
    "LAL": Team.los_angeles_lakers,
    "MEM": Team.memphis_grizzlies,
    "MIA": Team.miami_heat,
    "MIL": Team.milwaukee_bucks,
    "MIN": Team.minnesota_timberwolves,
    "NOP": Team.new_orleans_pelicans,
    "NYK": Team.new_york_knicks,
    "OKC": Team.oklahoma_city_thunder,
    "ORL": Team.orlando_magic,
    "PHI": Team.philadelphia_76ers,
    "PHX": Team.phoenix_suns,
    "POR": Team.portland_trail_blazers,
    "SAC": Team.sacramento_kings,
    "SAS": Team.san_antonio_spurs,
    "TOR": Team.toronto_raptors,
    "UTA": Team.utah_jazz,
    "WAS": Team.washington_wizards,
}

