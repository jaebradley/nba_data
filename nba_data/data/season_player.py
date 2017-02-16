from nba_data.data.player import Player


class SeasonPlayer(Player):
    def __init__(self, id, name, jersey, team_seasons):
        self.jersey = jersey
        self.team_seasons = team_seasons
        Player.__init__(self, name=name, id=id)

    def __unicode__(self):
        return 'id: {0} | name: {1} | jersey: {2} | team seasons: {3}'.format(self.id, self.name, self.jersey,
                                                                              self.team_seasons)
