from stats.data.season import Season
from stats.data.season_type import SeasonType
from stats.data.game import Game
from stats.data.team import Team
from stats.data.outcome import Outcome


class TeamGameLogDeserializer:
    game_date_format = "%b %d, %Y"
    game_id_index = 1
    game_date_index = 2
    matchup_index = 3
    home_team_outcome_index = 4

    @staticmethod
    def deserialize_team_game_log(team_game_log_json):
        deserialized_results = []
        results = team_game_log_json["resultSets"][0]["rowSet"]
        season = Season.get_season(team_game_log_json["parameters"]["Season"])
        season_type = SeasonType.get_season_type(team_game_log_json["parameters"]["SeasonType"])
        for result in results:
            parsed_matchup = TeamGameLogDeserializer.parse_matchup(result[TeamGameLogDeserializer.matchup_index])
            home_team = Team.get_team_by_id(parsed_matchup["home_team"])
            away_team = Team.get_team_by_id(parsed_matchup["away_team"])
            home_team_outcome = Outcome.get_outcome_from_abbreviation(result[TeamGameLogDeserializer.home_team_outcome_index])
            deserialized_results.append(
                Game(nba_id=result[TeamGameLogDeserializer.game_id_index],
                     home_team=home_team,
                     away_team=away_team,
                     date=TeamGameLogDeserializer.parse_date(result[TeamGameLogDeserializer.game_date_index]),
                     season=season,
                     season_type=season_type,
                     home_team_outcome=home_team_outcome))
        return deserialized_results

    @staticmethod
    def parse_matchup(matchup):
        if " vs. " in matchup:
            teams = matchup.split(" vs. ")
            return {
                "home_team": Team.get_team_by_abbreviation(teams[0]),
                "away_team": Team.get_team_by_abbreviation(teams[1]),
            }

        elif " @ " in matchup:
            teams = matchup.split(" @ ")
            return {
                "home_team": Team.get_team_by_abbreviation(teams[1]),
                "away_team": Team.get_team_by_abbreviation(teams[0]),
            }

        else:
            raise RuntimeError("Unexpected matchup: %s", matchup)

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, Game.game_date_format).date()