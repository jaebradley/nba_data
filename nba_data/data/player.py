from nba_data.data.base_query_parameter import BaseQueryParameter
from nba_data.data.team import Team


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
        assert isinstance(name, str)
        assert isinstance(team_id, int)
        assert isinstance(nba_id, int)

        return Player(name=name,
                      team=Team.get_team_by_id(team_id=team_id),
                      nba_id=nba_id)