# TODO: @jbradley replace Player class with this class
# TODO: @jbradley current fields are for convenience, add more in the future


class PlayerData:
    def __init__(self, player_id, name, jersey, season_teams):
        assert isinstance(player_id, str)
        assert isinstance(name, str)
        assert isinstance(jersey, int)
        assert isinstance(season_teams, list)

        self.player_id = player_id
        self.name = name
        self.jersey = jersey
        self.season_teams = season_teams