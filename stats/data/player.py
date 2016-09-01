from base_query_parameter import BaseQueryParameter
from stats.data.team import Team


class Player(BaseQueryParameter):
    def __init__(self, name, team, nba_id):
        self.name = name
        self.team = team
        self.nba_id = nba_id

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"

    @staticmethod
    def create(display_first_last, team_id, nba_id):
        return Player(name=display_first_last,
                      team=Team.get_team_by_id(team_id=team_id),
                      nba_id=nba_id)