import json

from player_deserializer import deserialize_player


def deserialize_json(common_all_players_json):
    deserialized_results = []
    common_all_players = json.loads(common_all_players_json)
    results = common_all_players["resultSets"]["rowSet"]
    for result in results:
        deserialized_results.append(deserialize_player(result[1], result[7]))
    return deserialized_results
