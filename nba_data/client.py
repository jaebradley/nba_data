import requests

from nba_data.data.current_season_only import CurrentSeasonOnly
from nba_data.data.date_range import DateRange
from nba_data.data.league import League
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType
from nba_data.deserializers.calendar import CalendarDeserializer
from nba_data.deserializers.common_all_players import CommonAllPlayersDeserializer
from nba_data.deserializers.common_player_info import CommonPlayerInfoDeserializer
from nba_data.deserializers.scoreboard import ScoreboardDeserializer
from nba_data.deserializers.season_players import SeasonPlayersDeserializer
from nba_data.deserializers.team_game_log import TeamGameLogDeserializer
from nba_data.deserializers.box_scores.game import TraditionalGameBoxScoreDeserializer, AdvancedGameBoxScoreDeserializer
from nba_data.deserializers.roto_wire.player_news_items import RotoWirePlayerNewsItemsDeserializer
from nba_data.nba_stats_api_utils.query_parameter_generator import QueryParameterGenerator
from nba_data.nba_stats_api_utils.uri_generator import UriGenerator


class Client:
    advanced_box_score_deserializer = AdvancedGameBoxScoreDeserializer()
    traditional_box_score_deserializer = TraditionalGameBoxScoreDeserializer()
    headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/45.0.2454.101 Safari/537.36'),
               'referer': 'http://stats.nba.com/scores/'}

    def __init__(self):
        pass

    @staticmethod
    def get_all_nba_players():
        return Client.get_players_for_season(season=Season.season_2015, current_season_only=CurrentSeasonOnly.no)

    @staticmethod
    def get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes):
        parameters = QueryParameterGenerator.generate_request_parameters(season=season, league=league,
                                                                         current_season_only=current_season_only)
        return Client.get_deserialized_data(uri=UriGenerator.generate_common_all_players_uri(),
                                            parameters=parameters, deserializer=CommonAllPlayersDeserializer)

    @staticmethod
    def get_games_for_team(season, team, season_type=SeasonType.regular_season):
        parameters = QueryParameterGenerator.generate_request_parameters(season=season,
                                                                         season_type=season_type, team=team)
        return Client.get_deserialized_data(uri=UriGenerator.generate_team_game_log_uri(),
                                            parameters=parameters, deserializer=TeamGameLogDeserializer)

    @staticmethod
    def get_player_info(player_id):
        parameters = QueryParameterGenerator.generate_request_parameters(player_id=player_id)
        return Client.get_deserialized_data(uri=UriGenerator.generate_common_player_info_uri(),
                                            parameters=parameters, deserializer=CommonPlayerInfoDeserializer)

    @staticmethod
    def get_advanced_box_score(game_id):
        parameters = QueryParameterGenerator.generate_box_score_request_parameters(game_id=game_id)
        return Client.get_deserialized_data(uri=UriGenerator.generate_advanced_box_score_uri(),
                                            parameters=parameters, deserializer=Client.advanced_box_score_deserializer)

    @staticmethod
    def get_traditional_box_score(game_id):
        parameters = QueryParameterGenerator.generate_box_score_request_parameters(game_id=game_id)
        return Client.get_deserialized_data(uri=UriGenerator.generate_traditional_box_score_uri(),
                                            parameters=parameters,
                                            deserializer=Client.traditional_box_score_deserializer)

    @staticmethod
    def get_games_for_date(date_value):
        return Client.get_deserialized_data(uri=UriGenerator.generate_scoreboard_data_uri(date_value=date_value),
                                            deserializer=ScoreboardDeserializer)

    @staticmethod
    def get_players(season):
        return Client.get_deserialized_data(uri=UriGenerator.generate_players_data_uri(season=season),
                                            deserializer=SeasonPlayersDeserializer)

    @staticmethod
    def get_deserialized_data(uri, deserializer, parameters=None):
        response = requests.get(uri, headers=Client.headers, params=parameters)

        response.raise_for_status()

        return deserializer.deserialize(response.json())

    @staticmethod
    def get_game_counts_in_date_range(date_range=DateRange(), ignore_dates_without_games=True):
        response = requests.get(UriGenerator.generate_calendar_data_uri(),
                                headers=Client.headers)

        response.raise_for_status()

        return CalendarDeserializer.deserialize(calendar_json=response.json(), date_range=date_range,
                                                ignore_dates_without_games=ignore_dates_without_games)

    @staticmethod
    def get_player_news():
        return Client.get_deserialized_data(uri=UriGenerator.generate_roto_wire_player_news_uri(),
                                            deserializer=RotoWirePlayerNewsItemsDeserializer)
