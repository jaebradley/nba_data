from nba_data.data.box_scores import GameBoxScore
from nba_data.deserializers.box_scores.traditional import TraditionalTeamBoxScoresDeserializer, \
    TraditionalPlayerBoxScoresDeserializer
from nba_data.deserializers.box_scores.advanced import AdvancedTeamBoxScoresDeserializer, \
    AdvancedPlayerBoxScoresDeserializer


class BoxScoreDeserializer:

    parameters_field_name = 'parameters'
    game_id_field_name = 'GameID'
    result_sets_field_name = 'resultSets'
    player_box_scores_index = 0
    team_box_scores_index = 1

    def __init__(self):
        pass

    def deserialize(self, data):
        if BoxScoreDeserializer.parameters_field_name not in data:
            raise ValueError('Unable to parse parameters field for %s', data)

        parameters = data[BoxScoreDeserializer.parameters_field_name]

        if BoxScoreDeserializer.game_id_field_name not in parameters:
            raise ValueError('Unable to parse game id field for %s', data)

        game_id = parameters[BoxScoreDeserializer.game_id_field_name]
        player_box_scores = self.parse_player_box_scores(data=data)
        team_box_scores = self.parse_team_box_scores(data=data)

        return GameBoxScore(game_id=game_id, player_box_scores=player_box_scores, team_box_scores=team_box_scores)

    def parse_player_box_scores(self, data):
        if BoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[BoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 1:
            raise ValueError('Expected at least one field for %s', data)

        data = result_sets[BoxScoreDeserializer.player_box_scores_index]

        return self.player_box_scores_deserializer(data=data)

    def parse_team_box_scores(self, data):
        if BoxScoreDeserializer.result_sets_field_name not in data:
            raise ValueError('Unable to parse result sets field for %s', data)

        result_sets = data[BoxScoreDeserializer.result_sets_field_name]

        if len(result_sets) < 2:
            raise ValueError('Expected at least two fields for %s', data)

        data = result_sets[BoxScoreDeserializer.team_box_scores_index]

        return self.team_box_scores_deserializer(data=data)

    def player_box_scores_deserializer(self, data):
        raise NotImplementedError()

    def team_box_scores_deserializer(self, data):
        raise NotImplementedError()


class TraditionalGameBoxScoreDeserializer(BoxScoreDeserializer):

    def team_box_scores_deserializer(self, data):
        return TraditionalTeamBoxScoresDeserializer.deserialize(data=data)

    def player_box_scores_deserializer(self, data):
        return TraditionalPlayerBoxScoresDeserializer.deserialize(data=data)


class AdvancedGameBoxScoreDeserializer(BoxScoreDeserializer):

    def player_box_scores_deserializer(self, data):
        return AdvancedPlayerBoxScoresDeserializer.deserialize(data=data)

    def team_box_scores_deserializer(self, data):
        return AdvancedTeamBoxScoresDeserializer.deserialize(data=data)