from nba_data.data.box_score import BoxScore
from nba_data.deserializers.traditional_player_box_score_deserializer import TraditionalBoxScorePlayerStatsDeserializer
from nba_data.deserializers.traditional_team_box_score_deserializer import TraditionalBoxScoreTeamStatsDeserializer


class TraditionalBoxScoreDeserializer:

    def __init__(self):
        pass

    @staticmethod
    def deserialize_traditional_box_score(traditional_box_score_json):
        game_id = traditional_box_score_json["parameters"]["GameID"]
        box_score_player_stats = TraditionalBoxScorePlayerStatsDeserializer.deserialize_traditional_box_score_player_stats(traditional_box_score_json["resultSets"][0])
        box_score_team_stats = TraditionalBoxScoreTeamStatsDeserializer.deserialize_traditional_box_score_team_stats(traditional_box_score_json["resultSets"][1])
        return BoxScore(game_id=str(game_id), player_box_scores=box_score_player_stats, team_box_scores=box_score_team_stats)