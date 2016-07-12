import requests

from stats.client.query_parameter import League, CurrentSeasonOnly, Team, generate_request_parameters
from deserializer.common_all_players_deserializer import deserialize_json


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
        return deserialize_json(response.json())