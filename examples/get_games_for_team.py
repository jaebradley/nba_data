from nba_data.client import Client
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.data.team import Team


def get_regular_season_games_for_2015_boston_celtics():
    return Client.get_games_for_team(season=Season.season_2015, team=Team.boston_celtics)


def get_playoff_for_2015_boston_celtics():
    return Client.get_games_for_team(season=Season.season_2015, team=Team.boston_celtics, season_type=SeasonType.playoffs)