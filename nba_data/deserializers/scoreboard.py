from datetime import datetime

import pytz

from nba_data.data.game import ScoreboardGame
from nba_data.data.matchup import MatchUp
from nba_data.data.season import Season
from nba_data.data.team import Team


class ScoreboardDeserializer:

    datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    date_format = '%Y-%m-%d'
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
    def deserialize(data):
        if ScoreboardDeserializer.games_field_name not in data:
            raise ValueError('Unable to parse games field for %s', data)

        return [ScoreboardDeserializer.parse_game(data=game)
                for game in data[ScoreboardDeserializer.games_field_name]]

    @staticmethod
    def parse_game(data):
        if ScoreboardDeserializer.game_id_field_name not in data:
            raise ValueError('Unable to parse game id field for %s', data)

        if ScoreboardDeserializer.season_year_field_name not in data:
            raise ValueError('Unable to parse season year field for %s', data)

        if ScoreboardDeserializer.start_time_field_name not in data:
            raise ValueError('Unable to parse start time field for %s', data)

        game_id = data[ScoreboardDeserializer.game_id_field_name]
        season = Season.get_season_by_start_year(year=int(data[ScoreboardDeserializer.season_year_field_name]))
        start_time_value = data[ScoreboardDeserializer.start_time_field_name]

        # If start time is not a datetime then use date formatting
        try:
            start_time = datetime.strptime(start_time_value, ScoreboardDeserializer.datetime_format)
        except ValueError:
            start_time = datetime.strptime(start_time_value, ScoreboardDeserializer.date_format)

        start_time = start_time.replace(tzinfo=ScoreboardDeserializer.start_time_time_zone)

        match_up = ScoreboardDeserializer.parse_match_up(data=data)

        return ScoreboardGame(id=game_id, season=season, start_time=start_time, match_up=match_up)

    @staticmethod
    def parse_match_up(data):
        if ScoreboardDeserializer.home_team_field_name not in data:
            raise ValueError('Unable to parse home team field for %s', data)

        if ScoreboardDeserializer.visiting_team_field_name not in data:
            raise ValueError('Unable to parse visiting team field for %s', data)

        home_team = ScoreboardDeserializer.parse_team(data=data[ScoreboardDeserializer.home_team_field_name])
        away_team = ScoreboardDeserializer.parse_team(data=data[ScoreboardDeserializer.visiting_team_field_name])

        return MatchUp(home_team=home_team, away_team=away_team)

    @staticmethod
    def parse_team(data):
        if ScoreboardDeserializer.team_id_field_name not in data:
            raise ValueError('Unable to parse team id for %s', data)

        return Team.get_team_by_id(team_id=int(data[ScoreboardDeserializer.team_id_field_name]))
