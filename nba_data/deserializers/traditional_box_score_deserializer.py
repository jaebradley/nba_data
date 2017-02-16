from nba_data.data.box_score import BoxScore
from nba_data.deserializers.traditional_player_box_score_deserializer import TraditionalBoxScorePlayerStatsDeserializer
from nba_data.deserializers.traditional_team_box_score_deserializer import TraditionalTeamBoxScoresDeserializer


class TraditionalBoxScoreDeserializer:
    parameters_field_name = 'parameters'
    game_id_field_name = 'GameID'
    result_sets_field_name = 'resultSets'
    player_box_scores_index = 0
    team_box_scores_index = 1

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        if TraditionalBoxScoreDeserializer.parameters_field_name not in data:
            raise ValueError('Unable to parse parameters field for %s', data)

        parameters = data[TraditionalBoxScoreDeserializer.parameters_field_name]

        if TraditionalBoxScoreDeserializer.game_id_field_name not in parameters:
            raise ValueError('Unable to parse game id field for %s', data)

        game_id = parameters[TraditionalBoxScoreDeserializer.game_id_field_name]
        player_box_scores = TraditionalBoxScoreDeserializer.parse_player_box_scores(data=data)
        team_box_scores = TraditionalBoxScoreDeserializer.parse_team_box_scores(data=data)

        return BoxScore(game_id=game_id, player_box_scores=player_box_scores, team_box_scores=team_box_scores)

    @staticmethod
    def parse_player_box_scores(data):
        if TraditionalBoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[TraditionalBoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 1:
            raise ValueError('Expected at least one field for %s', data)

        return TraditionalBoxScorePlayerStatsDeserializer.deserialize(
            data=result_sets[TraditionalBoxScoreDeserializer.player_box_scores_index])

    @staticmethod
    def parse_team_box_scores(data):
        if TraditionalBoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[TraditionalBoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 2:
            raise ValueError('Expected at least two fields for %s', data)

        return TraditionalTeamBoxScoresDeserializer.deserialize(
            data=result_sets[TraditionalBoxScoreDeserializer.team_box_scores_index])