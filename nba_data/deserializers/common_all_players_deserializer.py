from nba_data.data.players import CommonAllPlayer
from nba_data.data.team import Team


class CommonAllPlayersDeserializer:
    name_index = 2
    team_id_index = 7
    id_index = 0
    result_sets_field_name = 'resultSets'
    row_set_field_name = 'rowSet'
    results_index = 0

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        return [CommonAllPlayersDeserializer.deserialize_result(result=result)
                for result in CommonAllPlayersDeserializer.parse_results(data=data)]

    @staticmethod
    def deserialize_result(result):
        return CommonAllPlayer(name=result[CommonAllPlayersDeserializer.name_index],
                               team=Team.get_team_by_id(team_id=result[CommonAllPlayersDeserializer.team_id_index]),
                               id=result[CommonAllPlayersDeserializer.id_index])

    @staticmethod
    def parse_results(data):
        if CommonAllPlayersDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to identify results for %s', data)

        result_sets = data[CommonAllPlayersDeserializer.result_sets_field_name]

        if len(result_sets) < 1:
            raise ValueError('Unable to identify results for %s', data)

        if CommonAllPlayersDeserializer.row_set_field_name not in result_sets[CommonAllPlayersDeserializer.results_index]:
            raise ValueError('Unable to identify results for %s', data)

        return result_sets[CommonAllPlayersDeserializer.results_index][CommonAllPlayersDeserializer.row_set_field_name]
