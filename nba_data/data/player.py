from nba_data.data.base_query_parameter import BaseQueryParameter
from nba_data.data.team import Team


class Player(BaseQueryParameter):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __unicode__(self):
        return '{0} | {1}'.format(self.get_additional_unicode(), self.get_base_unicode())

    def get_base_unicode(self):
        return 'name: {name} | id: {id}'.format(name=self.name, id=self.id)

    def get_additional_unicode(self):
        raise NotImplementedError('Implement in concrete classes')

    @staticmethod
    def get_query_parameter_name():
        return "PlayerId"


class TeamPlayer(Player):
    def __init__(self, name, id, team):
        self.team = team
        Player.__init__(self, name, id)

    def get_additional_unicode(self):
        return 'team: {team}'.format(team=self.team)


class SeasonPlayer(Player):
    def __init__(self, id, name, jersey, team_seasons):
        self.jersey = jersey
        self.team_seasons = team_seasons
        Player.__init__(self, name=name, id=id)

    def get_additional_unicode(self):
        return 'jersey: {jersey} | team seasons: {team_seasons}'.format(jersey=self.jersey,
                                                                        team_seasons=self.team_seasons)


class BoxScorePlayer(TeamPlayer):
    def __init__(self, name, team, id, status):
        self.status = status
        TeamPlayer.__init__(self, name=name, id=id, team=team)

    def get_additional_unicode(self):
        return 'team: {team} | status: {status}'.format(team=self.team, status=self.status)
