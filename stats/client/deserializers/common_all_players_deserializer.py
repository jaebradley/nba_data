from stats.data.player import Player


class CommonAllPlayersDeserializer:
    name_index = 2
    team_id_index = 7
    id_index = 0

    @staticmethod
    def deserialize_common_all_players(common_all_players_json):
        deserialized_results = []
        results = common_all_players_json["resultSets"][0]["rowSet"]
        for result in results:
            deserialized_results.append(Player.create(display_first_last=str(result[Player.name_index]),
                                                      team_id=str(result[Player.team_id_index]),
                                                      nba_id=str(result[Player.id_index])))
        return deserialized_results