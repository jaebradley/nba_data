from nba_data.data.traditional_team_box_score import TraditionalTeamBoxScore
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class TraditionalBoxScoreTeamStatsDeserializer:
    team_id_index = 1
    minutes_played_index = 5
    field_goals_made_index = 6
    field_goal_attempts_index = 7
    three_point_field_goals_made_index = 9
    three_point_field_goal_attempts_index = 10
    free_throws_made_index = 12
    free_throw_attempts_index = 13
    offensive_rebounds_index = 15
    defensive_rebounds_index = 16
    assists_index = 18
    steals_index = 19
    blocks_index = 20
    turnovers_index = 21
    personal_fouls_index = 22

    def __init__(self):
        pass

    @staticmethod
    def deserialize_traditional_box_score_team_stats(traditional_box_score_player_stats_json):
        deserialized_box_scores = []
        for box_score in traditional_box_score_player_stats_json["rowSet"]:
            deserialized_box_scores.append(
                TraditionalTeamBoxScore.create(team_id=box_score[TraditionalBoxScoreTeamStatsDeserializer.team_id_index],
                                               seconds_played=BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(box_score[TraditionalBoxScoreTeamStatsDeserializer.minutes_played_index]),
                                               field_goals_made=box_score[TraditionalBoxScoreTeamStatsDeserializer.field_goals_made_index],
                                               field_goal_attempts=box_score[TraditionalBoxScoreTeamStatsDeserializer.field_goal_attempts_index],
                                               three_point_field_goals_made=box_score[TraditionalBoxScoreTeamStatsDeserializer.three_point_field_goals_made_index],
                                               three_point_field_goal_attempts=box_score[TraditionalBoxScoreTeamStatsDeserializer.three_point_field_goal_attempts_index],
                                               free_throws_made=box_score[TraditionalBoxScoreTeamStatsDeserializer.free_throws_made_index],
                                               free_throws_attempts=box_score[TraditionalBoxScoreTeamStatsDeserializer.free_throw_attempts_index],
                                               offensive_rebounds=box_score[TraditionalBoxScoreTeamStatsDeserializer.offensive_rebounds_index],
                                               defensive_rebounds=box_score[TraditionalBoxScoreTeamStatsDeserializer.defensive_rebounds_index],
                                               assists=box_score[TraditionalBoxScoreTeamStatsDeserializer.assists_index],
                                               steals=box_score[TraditionalBoxScoreTeamStatsDeserializer.steals_index],
                                               blocks=box_score[TraditionalBoxScoreTeamStatsDeserializer.blocks_index],
                                               turnovers=box_score[TraditionalBoxScoreTeamStatsDeserializer.turnovers_index],
                                               personal_fouls=box_score[TraditionalBoxScoreTeamStatsDeserializer.personal_fouls_index]))
        return deserialized_box_scores