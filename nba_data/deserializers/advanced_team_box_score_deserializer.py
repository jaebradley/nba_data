from nba_data.data.team import Team
from nba_data.data.advanced_team_box_score import AdvancedTeamBoxScore
from nba_data.deserializers.utils.advanced_box_score_deserializer_utils import AdvancedBoxScoreDeserializerUtils
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class AdvancedBoxScoreTeamStatsDeserializer:
    row_set_field_name = 'rowSet'

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

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        if AdvancedBoxScoreTeamStatsDeserializer.row_set_field_name not in data:
            raise ValueError('Unable to parse row set field for %s', data)

        return [AdvancedBoxScoreTeamStatsDeserializer.parse_box_score(data=box_score)
                for box_score in data[AdvancedBoxScoreTeamStatsDeserializer.row_set_field_name]]

    @staticmethod
    def parse_box_score(data):
        team_id = int(data[AdvancedBoxScoreTeamStatsDeserializer.team_id_index])
        minutes_played = data[AdvancedBoxScoreTeamStatsDeserializer.minutes_played_index]
        offensive_rating_value = data[AdvancedBoxScoreTeamStatsDeserializer.offensive_rating_index]
        defensive_rating_value = data[AdvancedBoxScoreTeamStatsDeserializer.defensive_rating_index]
        teammate_assist_percentage_value = data[AdvancedBoxScoreTeamStatsDeserializer.teammate_assist_percentage_index]
        assist_to_turnover_ratio_value = data[AdvancedBoxScoreTeamStatsDeserializer.assist_to_turnover_ratio_index]
        assists_per_100_possessions_value = data[AdvancedBoxScoreTeamStatsDeserializer.assists_per_100_possessions_index]
        offensive_rebound_percentage_value = data[AdvancedBoxScoreTeamStatsDeserializer.offensive_rebound_percentage_index]
        defensive_rebound_percentage_value = data[AdvancedBoxScoreTeamStatsDeserializer.defensive_rebound_percentage_index]
        turnovers_per_100_possessions_value = data[AdvancedBoxScoreTeamStatsDeserializer.turnovers_per_100_possessions_index]
        effective_field_goal_percentage_value = data[AdvancedBoxScoreTeamStatsDeserializer.effective_field_goal_percentage_index]
        true_shooting_percentage_value = data[AdvancedBoxScoreTeamStatsDeserializer.true_shooting_percentage_index]

        team = Team.get_team_by_id(team_id=team_id)
        seconds_played = BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(minutes=minutes_played)
        offensive_rating = AdvancedBoxScoreDeserializerUtils.parse_float(offensive_rating_value)
        defensive_rating = AdvancedBoxScoreDeserializerUtils.parse_float(defensive_rating_value)
        teammate_assist_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(teammate_assist_percentage_value)
        assist_to_turnover_ratio = AdvancedBoxScoreDeserializerUtils.parse_float(assist_to_turnover_ratio_value)
        assists_per_100_possessions = AdvancedBoxScoreDeserializerUtils.parse_float(assists_per_100_possessions_value)
        offensive_rebound_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(offensive_rebound_percentage_value)
        defensive_rebound_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(defensive_rebound_percentage_value)
        turnovers_per_100_possessions = AdvancedBoxScoreDeserializerUtils.parse_float(turnovers_per_100_possessions_value)
        effective_field_goal_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(effective_field_goal_percentage_value)
        true_shooting_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(true_shooting_percentage_value)

        return AdvancedTeamBoxScore(team=team, seconds_played=seconds_played, offensive_rating=offensive_rating,
                                    defensive_rating=defensive_rating,
                                    teammate_assist_percentage=teammate_assist_percentage,
                                    assist_to_turnover_ratio=assist_to_turnover_ratio,
                                    assists_per_100_possessions=assists_per_100_possessions,
                                    offensive_rebound_percentage=offensive_rebound_percentage,
                                    defensive_rebound_percentage=defensive_rebound_percentage,
                                    turnovers_per_100_possessions=turnovers_per_100_possessions,
                                    effective_field_goal_percentage=effective_field_goal_percentage,
                                    true_shooting_percentage=true_shooting_percentage)