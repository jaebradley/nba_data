import requests
from nba_data.nba_stats_api_utils.uri_generator import UriGenerator

from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.league import League
from nba_data.data.season_type import SeasonType
from nba_data.deserializers.advanced_box_score_deserializer import AdvancedBoxScoreDeserializer
from nba_data.deserializers.common_all_players_deserializer import CommonAllPlayersDeserializer
from nba_data.deserializers.common_player_info_deserializer import CommonPlayerInfoDeserializer
from nba_data.deserializers.team_game_log_deserializer import TeamGameLogDeserializer
from nba_data.nba_stats_api_utils.query_parameter_generator import QueryParameterGenerator


class Client:

    headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/45.0.2454.101 Safari/537.36'),
               'referer': 'http://stats.nba.com/scores/'}

    def __init__(self):
        pass

    @staticmethod
    def get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        response = requests.get(UriGenerator.generate_common_all_players_uri(),
                                headers=Client.headers,
                                params=QueryParameterGenerator.generate_request_parameters(season=season,
                                                                                           league=league,
                                                                                           current_season_only=current_season_only))

        response.raise_for_status()

        return CommonAllPlayersDeserializer.deserialize_common_all_players(response.json())


    @staticmethod
    def get_games_for_team(season, team, season_type=SeasonType.regular_season):
        response = requests.get(UriGenerator.generate_team_game_log_uri(),
                                headers=Client.headers,
                                params=QueryParameterGenerator.generate_request_parameters(season=season,
                                                                                           season_type=season_type,
                                                                                           team=team))
        response.raise_for_status()

        return TeamGameLogDeserializer.deserialize_team_game_log(response.json())

    @staticmethod
    def get_player_info(player_id):
        response = requests.get(UriGenerator.generate_common_player_info_uri(),
                                headers=Client.headers,
                                params=QueryParameterGenerator.generate_request_parameters(player_id=player_id))
        response.raise_for_status()

        return CommonPlayerInfoDeserializer.deserialize_common_player_info(response.json())

    @staticmethod
    def get_advanced_box_score(game_id):
        response = requests.get(UriGenerator.generate_advanced_box_score_uri(),
                                headers=Client.headers,
                                params=QueryParameterGenerator.generate_box_score_request_parameters(game_id=game_id))

        response.raise_for_status()

        return AdvancedBoxScoreDeserializer.deserialize_advanced_box_score(response.json())