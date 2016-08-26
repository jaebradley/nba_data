import requests

from stats.client.query_parameter import League, CurrentSeasonOnly, Team, SeasonType, generate_request_parameters
from stats.data.player import Player
from stats.client.uri_generator import UriGenerator


class Client:
    def __init__(self):
        pass

    @staticmethod
    def get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        response = requests.get(UriGenerator.generate_common_all_players_uri(),
                                params=generate_request_parameters(season=season,
                                                                   league=league,
                                                                   current_season_only=current_season_only))
        return Player.deserialize_common_all_players(response.json())

    @staticmethod
    def get_games_for_team(season, team, season_type=SeasonType.regular_season):
        response = requests.get(UriGenerator.generate_team_game_log_uri(),
                                params=generate_request_parameters(season=season,
                                                                   season_type=season_type,
                                                                   team=team))
