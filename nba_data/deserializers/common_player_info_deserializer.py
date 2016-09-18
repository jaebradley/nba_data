from datetime import datetime

from nba_data.data.player_details import PlayerDetails


class CommonPlayerInfoDeserializer:
    game_date_format = "%Y-%m-%dT%H:%M:%S"
    unknown_value = ""

    result_set_index = 0
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
    def deserialize_common_player_info(common_player_info_deserializer):
        results = common_player_info_deserializer["resultSets"][CommonPlayerInfoDeserializer.result_set_index]["rowSet"]

        assert len(results) == 1

        result = results[0]

        weight = None
        try:
            weight = int(result[CommonPlayerInfoDeserializer.weight_index])
        except ValueError:
            pass

        height = None
        try:
            height = CommonPlayerInfoDeserializer.parse_height(result[CommonPlayerInfoDeserializer.height_index])
        except (ValueError, AssertionError):
            pass

        jersey_number = None
        try:
            jersey_number = int(result[CommonPlayerInfoDeserializer.jersey_number_index])
        except ValueError:
            pass

        return PlayerDetails.create(nba_id=int(result[CommonPlayerInfoDeserializer.nba_id_index]),
                                    name=str(result[CommonPlayerInfoDeserializer.name_index]),
                                    team_id=int(result[CommonPlayerInfoDeserializer.team_id_index]),
                                    birth_date=CommonPlayerInfoDeserializer.parse_date(result[CommonPlayerInfoDeserializer.birth_date_index]),
                                    height=height,
                                    weight=weight,
                                    jersey_number=jersey_number,
                                    position_name=str(result[CommonPlayerInfoDeserializer.position_name_index]))

    @staticmethod
    def parse_height(height_string):
        height_components = height_string.split("-")

        assert len(height_components) == 2

        inches = 0
        inches += int(height_components[0]) * 12
        inches += int(height_components[1])

        return inches

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, CommonPlayerInfoDeserializer.game_date_format).date()