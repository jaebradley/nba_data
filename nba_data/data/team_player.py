from nba_data.data.player import Player


class TeamPlayer(Player):
    def __init__(self, name, id, team):
        self.team = team
        Player.__init__(self, name, id)

    def __unicode__(self):
        return 'id: {0} | name: {1} | team: {2}'.format(self.id, self.name, self.team)
