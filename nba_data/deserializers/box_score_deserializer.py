from nba_data.data.box_score import BoxScore


class BoxScoreDeserializer:

    parameters_field_name = 'parameters'
    game_id_field_name = 'GameID'
    result_sets_field_name = 'resultSets'
    player_box_scores_index = 0
    team_box_scores_index = 1

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        if BoxScoreDeserializer.parameters_field_name not in data:
            raise ValueError('Unable to parse parameters field for %s', data)

        parameters = data[BoxScoreDeserializer.parameters_field_name]

        if BoxScoreDeserializer.game_id_field_name not in parameters:
            raise ValueError('Unable to parse game id field for %s', data)

        game_id = parameters[BoxScoreDeserializer.game_id_field_name]
        player_box_scores = BoxScoreDeserializer.parse_player_box_scores(data=data)
        team_box_scores = BoxScoreDeserializer.parse_team_box_scores(data=data)

        return BoxScore(game_id=game_id, player_box_scores=player_box_scores, team_box_scores=team_box_scores)

    @staticmethod
    def parse_player_box_scores(data):
        if BoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[BoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 1:
            raise ValueError('Expected at least one field for %s', data)

        data = result_sets[BoxScoreDeserializer.player_box_scores_index]

        return BoxScoreDeserializer.player_box_scores_deserializer(data=data)

    @staticmethod
    def parse_team_box_scores(data):
        if BoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[BoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 2:
            raise ValueError('Expected at least two fields for %s', data)

        data = result_sets[BoxScoreDeserializer.team_box_scores_index]

        return BoxScoreDeserializer.team_box_scores_deserializer(data=data)

    @staticmethod
    def player_box_scores_deserializer(data):
        raise NotImplementedError()

    @staticmethod
    def team_box_scores_deserializer(data):
        raise NotImplementedError()
