from nba_data.data.base_query_parameter import BaseQueryParameter
from nba_data.data.team import Team


class Player(BaseQueryParameter):
    def __init__(self, name, team, id):
        self.name = name
        self.team = team
        self.id = id

    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.name, self.team, self.id)

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"

    @staticmethod
    def create(name, team_id, id):
        return Player(name=name,
                      team=Team.get_team_by_id(team_id=team_id),
                      id=id)