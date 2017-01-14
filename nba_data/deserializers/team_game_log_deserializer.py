from datetime import datetime

from nba_data.data.game import Game
from nba_data.data.matchup import Matchup
from nba_data.data.outcome import Outcome
from nba_data.data.season import Season
from nba_data.data.season_type import SeasonType


class TeamGameLogDeserializer:
    game_date_format = "%b %d, %Y"

    result_set_index = 0
    game_id_index = 1
    game_date_index = 2
    matchup_index = 3
    home_team_outcome_index = 4

    def __init__(self):
        pass

    @staticmethod
    def deserialize_team_game_log(team_game_log_json):
        deserialized_results = []
        results = team_game_log_json["resultSets"][TeamGameLogDeserializer.result_set_index]["rowSet"]
        season = Season.get_season_by_name(team_game_log_json["parameters"][Season.get_query_parameter_name()])
        season_type = SeasonType.get_season_type(team_game_log_json["parameters"][SeasonType.get_query_parameter_name()])
        for result in results:
            matchup = TeamGameLogDeserializer.parse_matchup(result[TeamGameLogDeserializer.matchup_index])
            home_team_outcome = Outcome.get_outcome_from_abbreviation(result[TeamGameLogDeserializer.home_team_outcome_index])
            deserialized_results.append(
                Game(nba_id=str(result[TeamGameLogDeserializer.game_id_index]),
                     matchup=matchup,
                     date=TeamGameLogDeserializer.parse_date(result[TeamGameLogDeserializer.game_date_index]),
                     season=season,
                     season_type=season_type,
                     home_team_outcome=home_team_outcome))
        return deserialized_results

    @staticmethod
    def parse_matchup(matchup):

        if " vs. " in matchup:
            teams = matchup.split(" vs. ")
            return Matchup.create(home_team_abbreviation=str(teams[0]),
                                  away_team_abbreviation=str(teams[1]))

        elif " @ " in matchup:
            teams = matchup.split(" @ ")
            return Matchup.create(home_team_abbreviation=str(teams[1]),
                                  away_team_abbreviation=str(teams[0]))

        else:
            raise RuntimeError("Unexpected matchup: %s", matchup)

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, TeamGameLogDeserializer.game_date_format).date()