from stats.data.team import Team


class Player:
    name_index = 2
    team_id_index = 7
    id_index = 0

    def __init__(self, name, team, nba_id):
        self.name = name
        self.team = team
        self.nba_id = nba_id

    @staticmethod
    def create(display_first_last, team_id, nba_id):
        return Player(name=display_first_last,
                      team=Team.get_team_by_id(team_id=team_id),
                      nba_id=nba_id)

    @staticmethod
    def deserialize_common_all_players(common_all_players_json):
        deserialized_results = []
        results = common_all_players_json["resultSets"][0]["rowSet"]
        for result in results:
            deserialized_results.append(Player.create(display_first_last=str(result[Player.name_index]),
                                                      team_id=str(result[Player.team_id_index]),
                                                      nba_id=str(result[Player.id_index])))
        return deserialized_results