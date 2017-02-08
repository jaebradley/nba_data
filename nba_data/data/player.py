from nba_data.data.base_query_parameter import BaseQueryParameter
from nba_data.data.team import Team


class Player(BaseQueryParameter):
    def __init__(self, name, team, id):
        self.name = name
        self.team = team
        self.id = id

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"

    @staticmethod
    def create(name, team_id, id):
        assert isinstance(name, str)
        assert isinstance(team_id, int)
        assert isinstance(id, int)

        return Player(name=name,
                      team=Team.get_team_by_id(team_id=team_id),
                      id=id)