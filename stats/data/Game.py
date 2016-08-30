from outcome import Outcome
from team import Team


class Game:

    game_date_format = "MMM DD, YYYY"

    def __init__(self, home_team, away_team, date, season, season_type, home_team_outcome):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.season = season
        self.season_type = season_type
        self.home_team_outcome = home_team_outcome

    @staticmethod
    def deserialize_team_game_log(team_game_log_json):
        game_id_index = 1
        game_date_index = 2
        matchup_index = 3
        home_team_outcome_index = 4
        deserialized_results = []
        results = team_game_log_json["resultSets"][0]["rowSet"]
        for result in results:
            parsed_matchup = Game.parse_matchup(result[matchup_index])
            

    @staticmethod
    def parse_matchup(matchup):
        if " vs. " in matchup:
            teams = matchup.split(" vs. ")
            return {
                "home_team": Team.get_team(teams[0]),
                "away_team": Team.get_team(teams[2]),
            }

        elif " @ " in matchup:
            teams = matchup.split(" @ ")
            return {
                "home_team": Team.get_team(teams[2]),
                "away_team": Team.get_team(teams[0]),
            }

        else:
            raise RuntimeError("Unexpected matchup: %s", matchup)