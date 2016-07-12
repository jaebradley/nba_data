from enum import Enum


class Team(Enum):
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
    undefined = "Undefined"

    @staticmethod
    def get_team(team_id):
        if team_id in team_id_map:
            return team_id_map.get(team_id)

        return Team.undefined

"""
https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation#current-teams
"""

team_id_map = {
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

