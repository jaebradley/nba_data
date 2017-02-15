from nba_data.data.base_query_parameter import BaseQueryParameter
from nba_data.data.team import Team


class Player(BaseQueryParameter):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __unicode__(self):
        return 'name: {0} | id: {1}'.format(self.name, self.id)

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"