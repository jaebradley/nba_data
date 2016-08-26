import requests

from stats.client.query_parameter import League, CurrentSeasonOnly, Team, SeasonType, generate_request_parameters
from stats.data.player import Player


class Client:
    def __init__(self):
        pass

    base_uri = "http://stats.nba.com/stats/"
    players_path = "commonallplayers"
    team_game_log_path = "teamgamelog"

    def get_players_for_season(self, season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        response = requests.get(self.base_uri + self.players_path,
                                params=generate_request_parameters(season=season,
                                                                   league=league,
                                                                   current_season_only=current_season_only))
        return Player.deserialize_common_all_players(response.json())

    def get_games_fodr_team(self, season, team, season_type=SeasonType.regular_season):
        response = requests.get(self.base_uri + self.team_game_log_path,
                                params=generate_request_parameters(season=season,
                                                                   season_type=season_type,
                                                                   team=team))
