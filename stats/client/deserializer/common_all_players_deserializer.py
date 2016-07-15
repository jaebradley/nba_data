from player_deserializer import deserialize_player


def deserialize_all_players_json(common_all_players_json):
    deserialized_results = []
    results = common_all_players_json["resultSets"][0]["rowSet"]
    for result in results:
        deserialized_results.append(deserialize_player(str(result[2]), str(result[7]), str(result[0])))
    return deserialized_results
