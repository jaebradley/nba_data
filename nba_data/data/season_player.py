from nba_data.data.player import Player


class SeasonPlayer(Player):
    def __init__(self, id, name, jersey, team_seasons):
        self.jersey = jersey
        self.team_seasons = team_seasons
        Player.__init__(self, name=name, id=id)
