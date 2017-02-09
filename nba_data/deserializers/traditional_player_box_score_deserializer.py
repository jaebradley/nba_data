from nba_data.data.traditional_player_box_score import TraditionalPlayerBoxScore
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class TraditionalBoxScorePlayerStatsDeserializer:
    team_id_index = 1
    player_id_index = 4
    player_name_index = 5
    comment_index = 7
    minutes_played_index = 8
    field_goals_made_index = 9
    field_goal_attempts_index = 10
    three_point_field_goals_made_index = 12
    three_point_field_goal_attempts_index = 13
    free_throws_made_index = 15
    free_throw_attempts_index = 16
    offensive_rebounds_index = 18
    defensive_rebounds_index = 19
    assists_index = 21
    steals_index = 22
    blocks_index = 23
    turnovers_index = 24
    personal_fouls_index = 25
    plus_minus_index = 27

    def __init__(self):
        pass

    @staticmethod
    def deserialize_traditional_box_score_player_stats(traditional_box_score_player_stats_json):
        deserialized_box_scores = []
        for box_score in traditional_box_score_player_stats_json["rowSet"]:
            deserialized_box_scores.append(
                TraditionalPlayerBoxScore.create(player_name=str(box_score[TraditionalBoxScorePlayerStatsDeserializer.player_name_index]),
                                                 player_id=int(box_score[TraditionalBoxScorePlayerStatsDeserializer.player_id_index]),
                                                 team_id=int(box_score[TraditionalBoxScorePlayerStatsDeserializer.team_id_index]),
                                                 comment=box_score[TraditionalBoxScorePlayerStatsDeserializer.comment_index],
                                                 seconds_played=BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(box_score[TraditionalBoxScorePlayerStatsDeserializer.minutes_played_index]),
                                                 field_goals_made=box_score[TraditionalBoxScorePlayerStatsDeserializer.field_goals_made_index],
                                                 field_goal_attempts=box_score[TraditionalBoxScorePlayerStatsDeserializer.field_goal_attempts_index],
                                                 three_point_field_goals_made=box_score[TraditionalBoxScorePlayerStatsDeserializer.three_point_field_goals_made_index],
                                                 three_point_field_goal_attempts=box_score[TraditionalBoxScorePlayerStatsDeserializer.three_point_field_goal_attempts_index],
                                                 free_throws_made=box_score[TraditionalBoxScorePlayerStatsDeserializer.free_throws_made_index],
                                                 free_throw_attempts=box_score[TraditionalBoxScorePlayerStatsDeserializer.free_throw_attempts_index],
                                                 offensive_rebounds=box_score[TraditionalBoxScorePlayerStatsDeserializer.offensive_rebounds_index],
                                                 defensive_rebounds=box_score[TraditionalBoxScorePlayerStatsDeserializer.defensive_rebounds_index],
                                                 assists=box_score[TraditionalBoxScorePlayerStatsDeserializer.assists_index],
                                                 steals=box_score[TraditionalBoxScorePlayerStatsDeserializer.steals_index],
                                                 blocks=box_score[TraditionalBoxScorePlayerStatsDeserializer.blocks_index],
                                                 turnovers=box_score[TraditionalBoxScorePlayerStatsDeserializer.turnovers_index],
                                                 personal_fouls=box_score[TraditionalBoxScorePlayerStatsDeserializer.personal_fouls_index],
                                                 plus_minus=box_score[TraditionalBoxScorePlayerStatsDeserializer.plus_minus_index]))
        return deserialized_box_scores