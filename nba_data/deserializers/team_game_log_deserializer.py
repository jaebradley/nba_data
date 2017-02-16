from datetime import datetime

from nba_data.data.game import LoggedGame
from nba_data.data.matchup import MatchUp
from nba_data.data.outcome import Outcome
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType


class TeamGameLogDeserializer:
    game_date_format = "%b %d, %Y"

    result_set_index = 0
    game_id_index = 1
    game_date_index = 2
    match_up_index = 3
    home_team_outcome_index = 4
    result_sets_field_name = 'resultSets'
    row_set_field_name = 'rowSet'
    parameters_field_name = 'parameters'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        season = TeamGameLogDeserializer.parse_season(data=data)
        season_type = TeamGameLogDeserializer.parse_season_type(data=data)
        return [TeamGameLogDeserializer.parse_result(data=result, season=season, season_type=season_type)
                for result in TeamGameLogDeserializer.parse_results(data=data)]

    @staticmethod
    def parse_result(data, season, season_type):
        match_up = TeamGameLogDeserializer.parse_match_up(match_up=data[TeamGameLogDeserializer.match_up_index])
        home_team_outcome = Outcome.get_outcome_from_abbreviation(abbreviation=data[TeamGameLogDeserializer.home_team_outcome_index])
        return LoggedGame(id=data[TeamGameLogDeserializer.game_id_index],
                          match_up=match_up,
                          start_date=TeamGameLogDeserializer.parse_date(date_string=data[TeamGameLogDeserializer.game_date_index]),
                          season=season,
                          season_type=season_type,
                          home_team_outcome=home_team_outcome)

    @staticmethod
    def parse_parameters(data):
        if TeamGameLogDeserializer.parameters_field_name not in data:
            raise ValueError('Unable to parse parameters from %s', data)

        return data[TeamGameLogDeserializer.parameters_field_name]

    @staticmethod
    def parse_season(data):
        parameters = TeamGameLogDeserializer.parse_parameters(data=data)

        if Season.get_query_parameter_name() not in parameters:
            raise ValueError('Unable to parse season from %s', data)

        return Season.get_season_by_name(name=parameters[Season.get_query_parameter_name()])

    @staticmethod
    def parse_season_type(data):
        parameters = TeamGameLogDeserializer.parse_parameters(data=data)

        if SeasonType.get_query_parameter_name() not in parameters:
            raise ValueError('Unable to parse season type from %s', data)

        return SeasonType.get_season_type(season_type_name=parameters[SeasonType.get_query_parameter_name()])

    @staticmethod
    def parse_results(data):
        if TeamGameLogDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse results for %s', data)

        result_sets = data[TeamGameLogDeserializer.result_sets_field_name]

        if len(result_sets) < 1:
            raise ValueError('Unable to parse results for %s', data)

        if TeamGameLogDeserializer.row_set_field_name not in result_sets[TeamGameLogDeserializer.result_set_index]:
            raise ValueError('Unable to parse results for %s', data)

        return result_sets[TeamGameLogDeserializer.result_set_index][TeamGameLogDeserializer.row_set_field_name]

    @staticmethod
    def parse_match_up(match_up):

        if " vs. " in match_up:
            teams = match_up.split(" vs. ")
            return MatchUp.create(home_team_abbreviation=str(teams[0]),
                                  away_team_abbreviation=str(teams[1]))

        elif " @ " in match_up:
            teams = match_up.split(" @ ")
            return MatchUp.create(home_team_abbreviation=str(teams[1]),
                                  away_team_abbreviation=str(teams[0]))

        else:
            raise RuntimeError("Unexpected matchup: %s", match_up)

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, TeamGameLogDeserializer.game_date_format).date()