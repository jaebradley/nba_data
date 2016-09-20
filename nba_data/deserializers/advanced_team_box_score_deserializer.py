from decimal import Decimal

from nba_data.data.advanced_team_box_score import AdvancedTeamBoxScore
from nba_data.deserializers.utils.advanced_box_score_deserializer_utils import AdvancedBoxScoreDeserializerUtils
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class AdvancedBoxScoreTeamStatsDeserializer:
    team_id_index = 1
    minutes_played_index = 5
    offensive_rating_index = 6
    defensive_rating_index = 7
    teammate_assist_percentage_index = 9
    assist_to_turnover_ratio_index = 10
    assists_per_100_possessions_index = 11
    offensive_rebound_percentage_index = 12
    defensive_rebound_percentage_index = 13
    turnovers_per_100_possessions_index = 15
    effective_field_goal_percentage_index = 16
    true_shooting_percentage_index = 17
    default_decimal_value = Decimal("0.0")

    def __init__(self):
        pass

    @staticmethod
    def deserialize_advanced_box_score_team_stats(advanced_box_score_player_stats_json):
        deserialized_box_scores = []
        for box_score in advanced_box_score_player_stats_json["rowSet"]:
            deserialized_box_scores.append(
                AdvancedTeamBoxScore.create(team_id=int(box_score[AdvancedBoxScoreTeamStatsDeserializer.team_id_index]),
                                            seconds_played=BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(box_score[AdvancedBoxScoreTeamStatsDeserializer.minutes_played_index]),
                                            offensive_rating=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScoreTeamStatsDeserializer.offensive_rating_index]),
                                            defensive_rating=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScoreTeamStatsDeserializer.defensive_rating_index]),
                                            teammate_assist_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScoreTeamStatsDeserializer.teammate_assist_percentage_index]),
                                            assist_to_turnover_ratio=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScoreTeamStatsDeserializer.assist_to_turnover_ratio_index]),
                                            assists_per_100_possessions=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScoreTeamStatsDeserializer.assists_per_100_possessions_index]),
                                            offensive_rebound_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScoreTeamStatsDeserializer.offensive_rebound_percentage_index]),
                                            defensive_rebound_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScoreTeamStatsDeserializer.defensive_rebound_percentage_index]),
                                            turnovers_per_100_possessions=AdvancedBoxScoreDeserializerUtils.parse_float(box_score[AdvancedBoxScoreTeamStatsDeserializer.turnovers_per_100_possessions_index]),
                                            effective_field_goal_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScoreTeamStatsDeserializer.effective_field_goal_percentage_index]),
                                            true_shooting_percentage=AdvancedBoxScoreDeserializerUtils.parse_percentage(box_score[AdvancedBoxScoreTeamStatsDeserializer.true_shooting_percentage_index])))
        return deserialized_box_scores