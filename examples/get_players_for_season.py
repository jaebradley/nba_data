from nba_data.client import Client
from nba_data.data.season import Season
from nba_data.data.current_season_only import CurrentSeasonOnly


def get_players_for_2015_season():
    return Client.get_players_for_season(season=Season.season_2015)


def get_players_for_every_season():
    return Client.get_players_for_season(season=Season.season_2015, current_season_only=CurrentSeasonOnly.no)

