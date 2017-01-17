from datetime import datetime
import pytz

from nba_data.data.matchup import Matchup
from nba_data.data.scoreboard_game import ScoreboardGame
from nba_data.data.season import Season
from nba_data.data.team import Team


class ScoreboardDeserializer:

    start_time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    start_time_time_zone = pytz.utc

    games_field_name = 'games'
    season_year_field_name = 'seasonYear'
    game_id_field_name = 'gameId'
    start_time_field_name = 'startTimeUTC'
    visiting_team_field_name = 'vTeam'
    home_team_field_name = 'hTeam'
    team_id_field_name = 'teamId'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(scoreboard_json):
        scoreboard_games = list()
        games = scoreboard_json[ScoreboardDeserializer.games_field_name]
        for game in games:
            scoreboard_games.append(ScoreboardDeserializer.deserialize_game(game_json=game))
        return scoreboard_games

    @staticmethod
    def deserialize_game(game_json):
        game_id = str(game_json[ScoreboardDeserializer.game_id_field_name])
        season = Season.get_season_by_start_year(year=int(game_json[ScoreboardDeserializer.season_year_field_name]))
        start_time = datetime.strptime(game_json[ScoreboardDeserializer.start_time_field_name],
                                       ScoreboardDeserializer.start_time_format)\
                             .replace(tzinfo=ScoreboardDeserializer.start_time_time_zone)
        home_team = ScoreboardDeserializer.identify_team(team_json=game_json[ScoreboardDeserializer.home_team_field_name])
        away_team = ScoreboardDeserializer.identify_team(team_json=game_json[ScoreboardDeserializer.visiting_team_field_name])
        return ScoreboardGame(game_id=game_id, season=season, start_time=start_time,
                              matchup=Matchup(home_team=home_team, away_team=away_team))

    @staticmethod
    def identify_team(team_json):
        return Team.get_team_by_id(team_id=int(team_json[ScoreboardDeserializer.team_id_field_name]))
