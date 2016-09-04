from stats.data.team import Team
from stats.data.base_query_parameter import BaseQueryParameter


class Player(BaseQueryParameter):
    def __init__(self, name, team, nba_id):
        self.name = name
        self.team = team
        self.nba_id = nba_id

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"

    @staticmethod
    def create(name, team_id, nba_id):
        try:
            team = Team.get_team_by_id(team_id=team_id)
        except ValueError:
            team = Team.undefined

        return Player(name=name,
                      team=team,
                      nba_id=nba_id)