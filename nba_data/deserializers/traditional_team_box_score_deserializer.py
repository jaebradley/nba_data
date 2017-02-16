from nba_data.data.traditional_team_box_score import TraditionalTeamBoxScore
from nba_data.data.team import Team
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class TraditionalTeamBoxScoresDeserializer:
    row_set_field_name = 'rowSet'

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
    def deserialize(data):
        if TraditionalTeamBoxScoresDeserializer.row_set_field_name not in data:
            raise ValueError('Unable to parse row set field for %s', data)

        return [TraditionalTeamBoxScoresDeserializer.parse_box_score(data=box_score)
                for box_score in data[TraditionalTeamBoxScoresDeserializer.row_set_field_name]]

    @staticmethod
    def parse_box_score(data):
        team_id = data[TraditionalTeamBoxScoresDeserializer.team_id_index]
        minutes_played = data[TraditionalTeamBoxScoresDeserializer.minutes_played_index]
        field_goals_made = data[TraditionalTeamBoxScoresDeserializer.field_goals_made_index],
        field_goals_attempted = data[TraditionalTeamBoxScoresDeserializer.field_goal_attempts_index]
        three_point_field_goals_made = data[TraditionalTeamBoxScoresDeserializer.three_point_field_goals_made_index]
        three_point_field_goals_attempted = data[TraditionalTeamBoxScoresDeserializer.three_point_field_goal_attempts_index]
        free_throws_made = data[TraditionalTeamBoxScoresDeserializer.free_throws_made_index]
        free_throws_attempted = data[TraditionalTeamBoxScoresDeserializer.free_throw_attempts_index]
        offensive_rebounds = data[TraditionalTeamBoxScoresDeserializer.offensive_rebounds_index]
        defensive_rebounds = data[TraditionalTeamBoxScoresDeserializer.defensive_rebounds_index]
        assists = data[TraditionalTeamBoxScoresDeserializer.assists_index]
        steals = data[TraditionalTeamBoxScoresDeserializer.steals_index]
        blocks = data[TraditionalTeamBoxScoresDeserializer.blocks_index]
        turnovers = data[TraditionalTeamBoxScoresDeserializer.turnovers_index]
        personal_fouls = data[TraditionalTeamBoxScoresDeserializer.personal_fouls_index]

        team = Team.get_team_by_id(team_id=team_id)
        seconds_played = BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(minutes=minutes_played)

        return TraditionalTeamBoxScore(team=team, seconds_played=seconds_played, field_goals_made=field_goals_made,
                                       field_goals_attempted=field_goals_attempted,
                                       three_point_field_goals_made=three_point_field_goals_made,
                                       three_point_field_goals_attempted=three_point_field_goals_attempted,
                                       free_throws_made=free_throws_made, free_throws_attempted=free_throws_attempted,
                                       offensive_rebounds=offensive_rebounds, defensive_rebounds=defensive_rebounds,
                                       assists=assists, steals=steals, blocks=blocks, turnovers=turnovers,
                                       personal_fouls=personal_fouls)