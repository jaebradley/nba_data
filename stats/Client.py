import requests

from QueryParameter import Season, League, CurrentSeasonOnly, generate_request_parameters


class Client:
    def __init__(self):
        pass

    base_uri = "http://stats.nba.com/stats/"
    all_players_path = "commonallplayers"

    def get_all_players(self, season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        response = requests.get(self.base_uri + self.all_players_path,
                                params=generate_request_parameters(season=season,
                                                                   league=league,
                                                                   current_season_only=current_season_only))
        