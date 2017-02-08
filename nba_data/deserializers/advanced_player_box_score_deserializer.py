from decimal import Decimal

from nba_data.data.advanced_player_box_score import AdvancedPlayerBoxScore
from nba_data.deserializers.utils.advanced_box_score_deserializer_utils import AdvancedBoxScoreDeserializerUtils
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class AdvancedBoxScorePlayerStatsDeserializer:
    team_id_index = 1
    player_id_index = 4
    player_name_index = 5
    comment_index = 7
    minutes_played_index = 8
    offensive_rating_index = 9
    defensive_rating_index = 10
    teammate_assist_percentage_index = 12
    assist_to_turnover_ratio_index = 13
    assists_per_100_possessions_index = 14
    offensive_rebound_percentage_index = 15
    defensive_rebound_percentage_index = 16
    turnovers_per_100_possessions_index = 18
    effective_field_goal_percentage_index = 19
    true_shooting_percentage_index = 20
    usage_percentage_index = 21
    default_decimal_value = Decimal("0.0")

    def __init__(self):
        pass

    @staticmethod
    def deserialize_advanced_box_score_player_stats(advanced_box_score_player_stats_json):
        deserialized_box_scores = []
        for box_score in advanced_box_score_player_stats_json["rowSet"]:
            deserialized_box_scores.append(
                AdvancedPlayerBoxScore.create(player_name=str(box_score[AdvancedBoxScorePlayerStatsDeserializer.player_name_index]),
                                              player_id=int(box_score[AdvancedBoxScorePlayerStatsDeserializer.player_id_index]),
                                              team_id=int(box_score[AdvancedBoxScorePlayerStatsDeserializer.team_id_index]),
                                              comment=str(box_score[AdvancedBoxScorePlayerStatsDeserializer.comment_index]),
                                              seconds_played=BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(box_score[AdvancedBoxScorePlayerStatsDeserializer.minutes_played_index]),
                                              offensive_rating=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rating_index]),
                                              defensive_rating=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rating_index]),
                                              teammate_assist_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.teammate_assist_percentage_index]),
                                              assist_to_turnover_ratio=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.assist_to_turnover_ratio_index]),
                                              assists_per_100_possessions=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.assists_per_100_possessions_index]),
                                              offensive_rebound_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rebound_percentage_index]),
                                              defensive_rebound_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rebound_percentage_index]),
                                              turnovers_per_100_possessions=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.turnovers_per_100_possessions_index]),
                                              effective_field_goal_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.effective_field_goal_percentage_index]),
                                              true_shooting_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.true_shooting_percentage_index]),
                                              usage_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.usage_percentage_index])))
        return deserialized_box_scores