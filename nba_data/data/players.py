from nba_data.data.base_query_parameter import BaseQueryParameter


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

    def get_base_unicode(self):
        return 'team: {team} | {base_unicode}'.format(team=self.team, base_unicode=Player.get_base_unicode(self))

    def get_additional_unicode(self):
        raise NotImplementedError('Implement in concrete classes')


class SeasonPlayer(Player):
    def __init__(self, id, name, jersey, team_seasons):
        self.jersey = jersey
        self.team_seasons = team_seasons
        Player.__init__(self, name=name, id=id)

    def get_additional_unicode(self):
        return 'jersey: {jersey} | team seasons: {team_seasons}'.format(jersey=self.jersey,
                                                                        team_seasons=self.team_seasons)


class CommonAllPlayer(TeamPlayer):
    def __init__(self, name, id, team):
        TeamPlayer.__init__(self, name, id, team)

    def get_additional_unicode(self):
        return ''


class DetailedPlayer(TeamPlayer):

    def __init__(self, name, team, id, birth_date, height, weight, jersey, position):
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        self.jersey = jersey
        self.position = position
        self.jersey = jersey
        TeamPlayer.__init__(self, name=name, id=id, team=team)

    def get_additional_unicode(self):
        return 'birth date: {birth_date} | height: {height} | weight: {weight} | ' 'jersey: {jersey} | ' \
               'position: {position}'.format(birth_data=self.birth_date, height=self.height, weight=self.weight,
                                             jersey=self.jersey, position=self.position)


class BoxScorePlayer(TeamPlayer):
    def __init__(self, name, team, id, status):
        self.status = status
        TeamPlayer.__init__(self, name=name, id=id, team=team)

    def get_additional_unicode(self):
        return 'status: {status}'.format(status=self.status)
