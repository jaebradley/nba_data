from team import Team


class TraditionalTeamBoxScore:
    def __init__(self, team, seconds_played, field_goals_made, field_goal_attempts,
                 three_point_field_goals_made, three_point_field_goal_attempts,
                 free_throws_made, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls):

        assert isinstance(team, Team)

        self.team = team
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

    @staticmethod
    def create(team_id, seconds_played, field_goals_made, field_goal_attempts,
               three_point_field_goals_made, three_point_field_goal_attempts,
               free_throws_made, free_throw_attempts, offensive_rebounds, defensive_rebounds, assists,
               steals, blocks, turnovers, personal_fouls):

        assert isinstance(team_id, int)

        return TraditionalTeamBoxScore(team=Team.get_team_by_id(team_id=team_id),
                                       seconds_played=seconds_played,
                                       field_goals_made=field_goals_made,
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
                                       personal_fouls=personal_fouls)