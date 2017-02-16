from nba_data.data.player import Player


class DetailedPlayer(Player):

    def __init__(self, name, team, id, birth_date, height, weight, jersey_number, position):
        self.team = team
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        self.jersey_number = jersey_number
        self.position = position
        Player.__init__(self, name=name, id=id)

    def __unicode__(self):
        return 'name: {0} | team: {1} | id: {2} | birth date: {3} | height: {4} | weight: {5} | ' \
               'jersey number: {6} | position: {7}'.format(self.name, self.team, self.id, self.birth_date, self.height,
                                                           self.weight, self.jersey_number, self.position)