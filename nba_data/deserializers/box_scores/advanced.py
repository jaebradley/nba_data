from decimal import Decimal

from nba_data.data.box_scores import AdvancedPlayerBoxScore
from nba_data.data.box_scores import AdvancedTeamBoxScore
from nba_data.data.player_status import PlayerStatus
from nba_data.data.players import BoxScorePlayer
from nba_data.data.team import Team
from nba_data.deserializers.utils.advanced_box_score_deserializer_utils import AdvancedBoxScoreDeserializerUtils
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class AdvancedTeamBoxScoresDeserializer:
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
        if AdvancedTeamBoxScoresDeserializer.row_set_field_name not in data:
            raise ValueError('Unable to parse row set field for %s', data)

        return [AdvancedTeamBoxScoresDeserializer.parse_box_score(data=box_score)
                for box_score in data[AdvancedTeamBoxScoresDeserializer.row_set_field_name]]

    @staticmethod
    def parse_box_score(data):
        team_id = int(data[AdvancedTeamBoxScoresDeserializer.team_id_index])
        minutes_played = data[AdvancedTeamBoxScoresDeserializer.minutes_played_index]
        offensive_rating_value = data[AdvancedTeamBoxScoresDeserializer.offensive_rating_index]
        defensive_rating_value = data[AdvancedTeamBoxScoresDeserializer.defensive_rating_index]
        teammate_assist_percentage_value = data[AdvancedTeamBoxScoresDeserializer.teammate_assist_percentage_index]
        assist_to_turnover_ratio_value = data[AdvancedTeamBoxScoresDeserializer.assist_to_turnover_ratio_index]
        assists_per_100_possessions_value = data[AdvancedTeamBoxScoresDeserializer.assists_per_100_possessions_index]
        offensive_rebound_percentage_value = data[AdvancedTeamBoxScoresDeserializer.offensive_rebound_percentage_index]
        defensive_rebound_percentage_value = data[AdvancedTeamBoxScoresDeserializer.defensive_rebound_percentage_index]
        turnovers_per_100_possessions_value = data[AdvancedTeamBoxScoresDeserializer.turnovers_per_100_possessions_index]
        effective_field_goal_percentage_value = data[AdvancedTeamBoxScoresDeserializer.effective_field_goal_percentage_index]
        true_shooting_percentage_value = data[AdvancedTeamBoxScoresDeserializer.true_shooting_percentage_index]

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


class AdvancedPlayerBoxScoresDeserializer:
    row_set_field_name = 'rowSet'

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
    def deserialize(data):
        if AdvancedPlayerBoxScoresDeserializer.row_set_field_name not in data:
            raise ValueError('Unable to parse row set field for %s', data)

        return [AdvancedPlayerBoxScoresDeserializer.parse_box_score(data=box_score)
                for box_score in data[AdvancedPlayerBoxScoresDeserializer.row_set_field_name]]

    @staticmethod
    def parse_box_score(data):
        player_name = data[AdvancedPlayerBoxScoresDeserializer.player_name_index]
        player_id = int(data[AdvancedPlayerBoxScoresDeserializer.player_id_index])
        team_id = int(data[AdvancedPlayerBoxScoresDeserializer.team_id_index])
        comment = data[AdvancedPlayerBoxScoresDeserializer.comment_index]
        minutes_played = data[AdvancedPlayerBoxScoresDeserializer.minutes_played_index]
        offensive_rating_value = data[AdvancedPlayerBoxScoresDeserializer.offensive_rating_index]
        defensive_rating_value = data[AdvancedPlayerBoxScoresDeserializer.defensive_rating_index]
        teammate_assist_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.teammate_assist_percentage_index]
        assist_to_turnover_ratio_value = data[AdvancedPlayerBoxScoresDeserializer.assist_to_turnover_ratio_index]
        assists_per_100_possessions_value = data[AdvancedPlayerBoxScoresDeserializer.assists_per_100_possessions_index]
        offensive_rebound_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.offensive_rebound_percentage_index]
        defensive_rebound_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.defensive_rebound_percentage_index]
        turnovers_per_100_possessions_value = data[AdvancedPlayerBoxScoresDeserializer.turnovers_per_100_possessions_index]
        effective_field_goal_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.effective_field_goal_percentage_index]
        true_shooting_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.true_shooting_percentage_index]
        usage_percentage_value = data[AdvancedPlayerBoxScoresDeserializer.usage_percentage_index]

        try:
            team = Team.get_team_by_id(team_id=team_id)
        except ValueError:
            team = Team.undefined
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
        usage_percentage = AdvancedBoxScoreDeserializerUtils.parse_percentage(usage_percentage_value)
        player_status = PlayerStatus.from_comment(comment=comment)

        player = BoxScorePlayer(name=player_name, team=team,id=player_id, status=player_status)
        return AdvancedPlayerBoxScore(player=player, seconds_played=seconds_played, offensive_rating=offensive_rating,
                                      defensive_rating=defensive_rating,
                                      teammate_assist_percentage=teammate_assist_percentage,
                                      assist_to_turnover_ratio=assist_to_turnover_ratio,
                                      assists_per_100_possessions=assists_per_100_possessions,
                                      offensive_rebound_percentage=offensive_rebound_percentage,
                                      defensive_rebound_percentage=defensive_rebound_percentage,
                                      turnovers_per_100_possessions=turnovers_per_100_possessions,
                                      effective_field_goal_percentage=effective_field_goal_percentage,
                                      true_shooting_percentage=true_shooting_percentage,
                                      usage_percentage=usage_percentage)
