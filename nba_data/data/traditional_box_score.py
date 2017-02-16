class TraditionalBoxScore:
    def __init__(self, seconds_played, field_goals_made, field_goals_attempted,
                 three_point_field_goals_made, three_point_field_goals_attempted,
                 free_throws_made, free_throws_attempted, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls):
        self.seconds_played = seconds_played
        self.field_goals_made = field_goals_made
        self.field_goals_attempted = field_goals_attempted
        self.three_point_field_goals_made = three_point_field_goals_made
        self.three_point_field_goals_attempted = three_point_field_goals_attempted
        self.free_throws_made = free_throws_made
        self.free_throws_attempted = free_throws_attempted
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
