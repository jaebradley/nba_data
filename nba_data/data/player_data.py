# TODO: @jbradley replace Player class with this class
# TODO: @jbradley current fields are for convenience, add more in the future


class PlayerData:
    def __init__(self, player_id, name, jersey, team_seasons):
        self.player_id = player_id
        self.name = name
        self.jersey = jersey
        self.team_seasons = team_seasons