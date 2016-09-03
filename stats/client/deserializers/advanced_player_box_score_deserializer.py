from stats.data.advanced_player_box_score import AdvancedPlayerBoxScore


class AdvancedBoxScorePlayerStatsDeserializer:
    team_id_index = 1
    player_id_index = 4
    player_name_index = 5
    comment_index = 8
    minutes_index = 9
    offensive_rating_index = 10
    defensive_rating_index = 11
    teammate_assist_percentage_index = 13
    assist_to_turnover_ratio_index = 14
    assists_per_100_possessions_index = 15
    offensive_rebound_percentage_index = 16
    defensive_rebound_percentage_index = 17
    turnovers_per_100_possessions_index = 19
    effective_field_goal_percentage_index = 20
    true_shooting_percentage_index = 21
    usage_percentage_index = 22

    def __init__(self):
        pass

    @staticmethod
    def deserialize_advanced_box_score_player_stats(advanced_box_score_player_stats_json):
        deserialized_box_scores = []
        for box_score in advanced_box_score_player_stats_json["rowSet"][0]:
            deserialized_box_scores.append(
                AdvancedPlayerBoxScore.create(player_name=box_score[AdvancedBoxScorePlayerStatsDeserializer.player_name_index],
                                              player_nba_id=box_score[AdvancedBoxScorePlayerStatsDeserializer.player_id_index],
                                              team_id=box_score[AdvancedBoxScorePlayerStatsDeserializer.team_id_index],
                                              comment=box_score[AdvancedBoxScorePlayerStatsDeserializer.comment_index],
                                              seconds_played=AdvancedBoxScorePlayerStatsDeserializer.parse_minutes_to_second(box_score[AdvancedBoxScorePlayerStatsDeserializer.minutes_index]),
                                              offensive_rating=box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rating_index],
                                              defensive_rating=box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rating_index],
                                              teammate_assist_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.teammate_assist_percentage_index],
                                              assist_to_turnover_ratio=box_score[AdvancedBoxScorePlayerStatsDeserializer.assist_to_turnover_ratio_index],
                                              assists_per_100_possessions=box_score[AdvancedBoxScorePlayerStatsDeserializer.assists_per_100_possessions_index],
                                              offensive_rebound_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rebound_percentage_index],
                                              defensive_rebound_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rebound_percentage_index],
                                              turnovers_per_100_possessions=box_score[AdvancedBoxScorePlayerStatsDeserializer.turnovers_per_100_possessions_index],
                                              effective_field_goal_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.effective_field_goal_percentage_index],
                                              true_shooting_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.true_shooting_percentage_index],
                                              usage_percentage=box_score[AdvancedBoxScorePlayerStatsDeserializer.usage_percentage_index]))
        return deserialized_box_scores

    @staticmethod
    def parse_minutes_to_second(minutes):
        if minutes is None:
            return 0

        if ":" in minutes:
            minutes_parts = minutes.split(":")

            assert len(minutes_parts) == 2

            return int(minutes_parts[0]) * 60 + int(minutes_parts[1])

        raise ValueError("Unknown minutes value: %s", minutes)
