from nba_data.deserializers.box_score_deserializer import BoxScoreDeserializer
from nba_data.deserializers.traditional_player_box_score_deserializer import TraditionalPlayerBoxScoresDeserializer
from nba_data.deserializers.traditional_team_box_score_deserializer import TraditionalTeamBoxScoresDeserializer


class TraditionalBoxScoreDeserializer(BoxScoreDeserializer):

    def team_box_scores_deserializer(self, data):
        return TraditionalTeamBoxScoresDeserializer.deserialize(data=data)

    def player_box_scores_deserializer(self, data):
        return TraditionalPlayerBoxScoresDeserializer.deserialize(data=data)