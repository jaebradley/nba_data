from nba_data.data.player import Player


class CommonAllPlayersDeserializer:
    name_index = 2
    team_id_index = 7
    id_index = 0

    def __init__(self):
        pass

    @staticmethod
    def deserialize_common_all_players(common_all_players_json):
        deserialized_results = []
        results = common_all_players_json["resultSets"][0]["rowSet"]
        for result in results:
            deserialized_results.append(Player.create(name=str(result[CommonAllPlayersDeserializer.name_index]),
                                                      team_id=result[CommonAllPlayersDeserializer.team_id_index],
                                                      id=result[CommonAllPlayersDeserializer.id_index]))
        return deserialized_results