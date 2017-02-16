from nba_data.data.traditional_player_box_score import TraditionalPlayerBoxScore
from nba_data.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils
from nba_data.data.box_score_player import BoxScorePlayer
from nba_data.data.player_status import PlayerStatus


class TraditionalPlayerBoxScoreDeserializer:
    row_set_field_name = 'rowSet'

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
    def deserialize(data):
        if TraditionalPlayerBoxScoreDeserializer.row_set_field_name not in data:
            raise ValueError('Unable to parse row set field for %s', data)

        return [TraditionalPlayerBoxScoreDeserializer.deserialize(data=box_score)
                for box_score in data[TraditionalPlayerBoxScoreDeserializer.row_set_field_name]]

    @staticmethod
    def parse_box_score(data):
        player_name = data[TraditionalPlayerBoxScoreDeserializer.player_name_index]
        player_id = int(data[TraditionalPlayerBoxScoreDeserializer.player_id_index])
        team_id = int(data[TraditionalPlayerBoxScoreDeserializer.team_id_index])
        comment = data[TraditionalPlayerBoxScoreDeserializer.comment_index]
        minutes_played = data[TraditionalPlayerBoxScoreDeserializer.minutes_played_index]
        field_goals_made = data[TraditionalPlayerBoxScoreDeserializer.field_goals_made_index]
        field_goals_attempted = data[TraditionalPlayerBoxScoreDeserializer.field_goal_attempts_index]
        three_point_field_goals_made = data[TraditionalPlayerBoxScoreDeserializer.three_point_field_goals_made_index]
        three_point_field_goals_attempted = data[TraditionalPlayerBoxScoreDeserializer.three_point_field_goal_attempts_index]
        free_throws_made = data[TraditionalPlayerBoxScoreDeserializer.free_throws_made_index]
        free_throws_attempted = data[TraditionalPlayerBoxScoreDeserializer.free_throw_attempts_index]
        offensive_rebounds = data[TraditionalPlayerBoxScoreDeserializer.offensive_rebounds_index]
        defensive_rebounds = data[TraditionalPlayerBoxScoreDeserializer.defensive_rebounds_index]
        assists = data[TraditionalPlayerBoxScoreDeserializer.assists_index]
        steals = data[TraditionalPlayerBoxScoreDeserializer.steals_index]
        blocks = data[TraditionalPlayerBoxScoreDeserializer.blocks_index]
        turnovers = data[TraditionalPlayerBoxScoreDeserializer.turnovers_index]
        personal_fouls = data[TraditionalPlayerBoxScoreDeserializer.personal_fouls_index]
        plus_minus = data[TraditionalPlayerBoxScoreDeserializer.plus_minus_index]

        player = BoxScorePlayer.create(name=player_name, team_id=team_id, id=player_id)
        player_status = PlayerStatus.from_comment(comment=comment)
        seconds_played = BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(minutes=minutes_played)

        return TraditionalPlayerBoxScore(player=player, status=player_status, plus_minus=plus_minus,
                                         seconds_played=seconds_played, field_goals_made=field_goals_made,
                                         field_goals_attempted=field_goals_attempted,
                                         three_point_field_goals_made=three_point_field_goals_made,
                                         three_point_field_goals_attempted=three_point_field_goals_attempted,
                                         free_throws_made=free_throws_made, free_throws_attempted=free_throws_attempted,
                                         offensive_rebounds=offensive_rebounds, defensive_rebounds=defensive_rebounds,
                                         assists=assists, steals=steals, blocks=blocks, turnovers=turnovers,
                                         personal_fouls=personal_fouls)