from decimal import Decimal, ROUND_HALF_UP

from stats.data.advanced_player_box_score import AdvancedPlayerBoxScore


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
                AdvancedPlayerBoxScore.create(player_name=box_score[AdvancedBoxScorePlayerStatsDeserializer.player_name_index],
                                              player_nba_id=box_score[AdvancedBoxScorePlayerStatsDeserializer.player_id_index],
                                              team_id=box_score[AdvancedBoxScorePlayerStatsDeserializer.team_id_index],
                                              comment=box_score[AdvancedBoxScorePlayerStatsDeserializer.comment_index],
                                              seconds_played=AdvancedBoxScorePlayerStatsDeserializer.parse_minutes_representation_to_seconds(box_score[AdvancedBoxScorePlayerStatsDeserializer.minutes_played_index]),
                                              offensive_rating=AdvancedBoxScorePlayerStatsDeserializer.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rating_index]),
                                              defensive_rating=AdvancedBoxScorePlayerStatsDeserializer.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rating_index]),
                                              teammate_assist_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.teammate_assist_percentage_index]),
                                              assist_to_turnover_ratio=AdvancedBoxScorePlayerStatsDeserializer.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.assist_to_turnover_ratio_index]),
                                              assists_per_100_possessions=AdvancedBoxScorePlayerStatsDeserializer.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.assists_per_100_possessions_index]),
                                              offensive_rebound_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.offensive_rebound_percentage_index]),
                                              defensive_rebound_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.defensive_rebound_percentage_index]),
                                              turnovers_per_100_possessions=AdvancedBoxScorePlayerStatsDeserializer.parse_float(box_score[AdvancedBoxScorePlayerStatsDeserializer.turnovers_per_100_possessions_index]),
                                              effective_field_goal_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.effective_field_goal_percentage_index]),
                                              true_shooting_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.true_shooting_percentage_index]),
                                              usage_percentage=AdvancedBoxScorePlayerStatsDeserializer.parse_percentage(box_score[AdvancedBoxScorePlayerStatsDeserializer.usage_percentage_index])))
        return deserialized_box_scores

    @staticmethod
    def parse_float(float_value):
        if float_value is None:
            return AdvancedBoxScorePlayerStatsDeserializer.default_decimal_value

        if not isinstance(float_value, float):
            raise ValueError("Expected a float instead of %s", float_value)

        return Decimal(Decimal(float_value).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))

    @staticmethod
    def parse_percentage(percentage):
        if percentage is None:
            return AdvancedBoxScorePlayerStatsDeserializer.default_decimal_value

        if not isinstance(percentage, float):
            raise ValueError("Expected a float instead of %s", percentage)

        return Decimal((100 * Decimal(percentage)).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))

    @staticmethod
    def parse_minutes_representation_to_seconds(minutes):
        if minutes is None:
            return 0

        if not isinstance(minutes, unicode):
            raise ValueError("Expected a unicode minutes representation instead of %s", minutes)

        if ":" in minutes:
            minutes_parts = minutes.split(":")

            if not len(minutes_parts) == 2:
                raise ValueError("Expected a minute and seconds part instead of %s", minutes_parts)

            return int(minutes_parts[0]) * 60 + int(minutes_parts[1])

        raise ValueError("Unknown minutes value: %s", minutes)