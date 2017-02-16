from datetime import datetime

from nba_data.data.players import DetailedPlayer
from nba_data.data.position import Position
from nba_data.data.team import Team


class CommonPlayerInfoDeserializer:
    game_date_format = "%Y-%m-%dT%H:%M:%S"
    unknown_value = ""

    results_set_field_name = 'resultSets'
    row_set_field_name = 'rowSet'

    result_set_index = 0
    row_set_index = 0
    nba_id_index = 0
    name_index = 3
    birth_date_index = 6
    height_index = 10
    weight_index = 11
    jersey_number_index = 13
    position_name_index = 14
    team_id_index = 16

    def __init__(self):
        pass

    @staticmethod
    def parse_result(data):
        if CommonPlayerInfoDeserializer.results_set_field_name not in data:
            raise ValueError('Unable to parse results from %s', data)

        results_set = data[CommonPlayerInfoDeserializer.results_set_field_name]

        if len(results_set) < 1:
            raise ValueError('Unable to parse results from %s', data)

        result_set = results_set[CommonPlayerInfoDeserializer.result_set_index]

        if CommonPlayerInfoDeserializer.row_set_field_name not in result_set:
            raise ValueError('Unable to parse results from %s', data)

        row_set = result_set[CommonPlayerInfoDeserializer.row_set_field_name]

        if len(row_set) < 1:
            raise ValueError('Unable to parse row set from %s', data)

        return row_set[CommonPlayerInfoDeserializer.row_set_index]

    @staticmethod
    def deserialize(data):
        result = CommonPlayerInfoDeserializer.parse_result(data=data)

        weight = result[CommonPlayerInfoDeserializer.weight_index]
        if weight is not None:
            weight = int(weight)

        height_value = result[CommonPlayerInfoDeserializer.height_index]
        if height_value is not None:
            height = CommonPlayerInfoDeserializer.parse_height(height_value=height_value)
        else:
            height = None

        jersey_number = result[CommonPlayerInfoDeserializer.jersey_number_index]
        if jersey_number is not None:
            jersey_number = int(jersey_number)

        id = int(result[CommonPlayerInfoDeserializer.nba_id_index])
        name = result[CommonPlayerInfoDeserializer.name_index]
        team = Team.get_team_by_id(team_id=int(result[CommonPlayerInfoDeserializer.team_id_index]))
        birth_date = CommonPlayerInfoDeserializer.parse_date(result[CommonPlayerInfoDeserializer.birth_date_index])
        position = Position.get_position_from_name(name=str(result[CommonPlayerInfoDeserializer.position_name_index]))

        return DetailedPlayer(id=id, name=name, team=team, birth_date=birth_date, height=height, weight=weight,
                              jersey=jersey_number, position=position)

    @staticmethod
    def parse_height(height_value):
        height_components = height_value.split("-")

        assert len(height_components) == 2

        inches = 0
        inches += int(height_components[0]) * 12
        inches += int(height_components[1])

        return inches

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, CommonPlayerInfoDeserializer.game_date_format).date()
