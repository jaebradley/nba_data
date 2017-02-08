from nba_data.data.team import Team


class BoxScorePlayer:
    def __init__(self, name, team, id, status):
        self.name = name
        self.team = team
        self.id = id
        self.status = status

    @staticmethod
    def create(name, team_id, id, status):
        try:
            team = Team.get_team_by_id(team_id=team_id)
        except ValueError:
            team = Team.undefined

        return BoxScorePlayer(name=name,
                              team=team,
                              id=id,
                              status=status)