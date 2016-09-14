from team import Team


class Matchup:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    @staticmethod
    def create(home_team_abbreviation, away_team_abbreviation):
        return Matchup(home_team=Team.get_team_by_abbreviation(home_team_abbreviation),
                       away_team=Team.get_team_by_abbreviation(away_team_abbreviation))
