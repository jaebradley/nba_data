from stats.data.team import Team


class Player:
    def __init__(self, name, team, nba_id):
        self.name = name
        self.team = team
        self.nba_id = nba_id

    @staticmethod
    def create(display_first_last, team_id, nba_id):
        return Player(name=display_first_last,
                      team=Team.get_team_by_id(team_id=team_id),
                      nba_id=nba_id)