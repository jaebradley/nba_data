from box_score_player import BoxScorePlayer
from player_status import PlayerStatus


class TraditionalPlayerBoxScore:
    def __init__(self, player, seconds_played, field_goals_made, field_goal_attempts,
                 three_point_field_goals_made, three_point_field_goal_attempts,
                 free_throws_made, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls, plus_minus):

        assert isinstance(player, BoxScorePlayer)

        self.player = player
        self.seconds_played = seconds_played
        self.field_goals_made = field_goals_made
        self.field_goal_attempts = field_goal_attempts
        self.three_point_field_goals_made = three_point_field_goals_made
        self.three_point_field_goal_attempts = three_point_field_goal_attempts
        self.free_throws_made = free_throws_made
        self.free_throw_attempts = free_throw_attempts
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.plus_minus = plus_minus

    @staticmethod
    def create(player_name, player_id, team_id, comment, seconds_played, field_goals_made, field_goal_attempts,
               three_point_field_goals_made, three_point_field_goal_attempts,
               free_throws_made, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists,
               steals, blocks, turnovers, personal_fouls, plus_minus):
        return TraditionalPlayerBoxScore(player=BoxScorePlayer.create(name=player_name, team_id=team_id, id=player_id,
                                                                      status=PlayerStatus.from_comment(comment=comment)),
                                         seconds_played=seconds_played, field_goals_made=field_goals_made,
                                         field_goal_attempts=field_goal_attempts,
                                         three_point_field_goals_made=three_point_field_goals_made,
                                         three_point_field_goal_attempts=three_point_field_goal_attempts,
                                         free_throws_made=free_throws_made,
                                         free_throw_attempts=free_throw_attempts,
                                         offensive_rebounds=offensive_rebounds,
                                         defensive_rebounds=defensive_rebounds,
                                         assists=assists,
                                         steals=steals,
                                         blocks=blocks,
                                         turnovers=turnovers,
                                         personal_fouls=personal_fouls,
                                         plus_minus=plus_minus)