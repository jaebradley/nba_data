from nba_data import Client
from nba_data import CurrentSeasonOnly
from nba_data import Season


def get_players_for_2015_season():
    return Client.get_players_for_season(season=Season.season_2015)


def get_players_for_every_season():
    return Client.get_players_for_season(season=Season.season_2015, current_season_only=CurrentSeasonOnly.no)

