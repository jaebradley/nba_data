from nba_data.deserializers.advanced_player_box_score_deserializer import AdvancedPlayerBoxScoresDeserializer
from nba_data.deserializers.advanced_team_box_score_deserializer import AdvancedTeamBoxScoresDeserializer
from nba_data.deserializers.box_score_deserializer import BoxScoreDeserializer


class AdvancedBoxScoreDeserializer(BoxScoreDeserializer):

    @staticmethod
    def player_box_scores_deserializer(data):
        return AdvancedPlayerBoxScoresDeserializer.deserialize(data=data)

    @staticmethod
    def team_box_scores_deserializer(data):
        return AdvancedTeamBoxScoresDeserializer.deserialize(data=data)