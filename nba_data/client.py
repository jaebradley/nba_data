import requests

from nba_data.client.deserializers.common_all_players_deserializer import CommonAllPlayersDeserializer
from nba_data.client.deserializers.team_game_log_deserializer import TeamGameLogDeserializer
from nba_data.client.deserializers.common_player_info_deserializer import CommonPlayerInfoDeserializer
from nba_data.client.deserializers.advanced_box_score_deserializer import AdvancedBoxScoreDeserializer
from nba_data.client.query_parameter_generator import QueryParameterGenerator
from nba_data.client.uri_generator import UriGenerator
from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.league import League
from nba_data.data.season_type import SeasonType


class Client:
    def __init__(self):
        pass

    @staticmethod
    def get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        response = requests.get(UriGenerator.generate_common_all_players_uri(),
                                params=QueryParameterGenerator.generate_request_parameters(season=season,
                                                                                           league=league,
                                                                                           current_season_only=current_season_only))
        return CommonAllPlayersDeserializer.deserialize_common_all_players(response.json())

    @staticmethod
    def get_games_for_team(season, team, season_type=SeasonType.regular_season):
        response = requests.get(UriGenerator.generate_team_game_log_uri(),
                                params=QueryParameterGenerator.generate_request_parameters(season=season,
                                                                                           season_type=season_type,
                                                                                           team=team))
        return TeamGameLogDeserializer.deserialize_team_game_log(response.json())

    @staticmethod
    def get_player_info(player_id):
        response = requests.get(UriGenerator.generate_common_player_info_uri(),
                                params=QueryParameterGenerator.generate_request_parameters(player_id=player_id))

        return CommonPlayerInfoDeserializer.deserialize_common_player_info(response.json())

    @staticmethod
    def get_advanced_box_score(game_id):
        response = requests.get(UriGenerator.generate_advanced_box_score_uri(),
                                params=QueryParameterGenerator.generate_box_score_request_parameters(game_id=game_id))

        return AdvancedBoxScoreDeserializer.deserialize_advanced_box_score(response.json())

