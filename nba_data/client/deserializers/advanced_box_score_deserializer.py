from nba_data.client.deserializers.advanced_player_box_score_deserializer import AdvancedBoxScorePlayerStatsDeserializer
from nba_data.client.deserializers.advanced_team_box_score_deserializer import AdvancedBoxScoreTeamStatsDeserializer
from nba_data.data.advanced_box_score import AdvancedBoxScore


class AdvancedBoxScoreDeserializer:

    def __init__(self):
        pass

    @staticmethod
    def deserialize_advanced_box_score(advanced_box_score_json):
        game_id = advanced_box_score_json["parameters"]["GameID"]
        advanced_box_score_player_stats = AdvancedBoxScorePlayerStatsDeserializer.deserialize_advanced_box_score_player_stats(advanced_box_score_json["resultSets"][0])
        advanced_box_score_team_stats = AdvancedBoxScoreTeamStatsDeserializer.deserialize_advanced_box_score_team_stats(advanced_box_score_json["resultSets"][1])
        return AdvancedBoxScore(game_id=game_id, player_box_scores=advanced_box_score_player_stats, team_box_scores=advanced_box_score_team_stats)