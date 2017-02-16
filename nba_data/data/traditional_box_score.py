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

    def __unicode__(self):
        return '{0} | {1}'.format(self.get_additional_unicode(), self.get_base_unicode())

    def get_base_unicode(self):
        return 'seconds played: {seconds_played} | field goals made: {field_goals_made} |' \
               'field goals attempted: {field_goals_attempted} | ' \
               'three point field goals made: {three_point_field_goals_made} | ' \
               'three point field goals attempted: {three_point_field_goals_attempted} | ' \
               'free throws made: {free_throws_made} |' 'free throws attempted: {free_throws_attempted} | ' \
               'offensive rebounds: {offensive rebounds} |' 'defensive rebounds: {defensive rebounds} | ' \
               'assists: {assists} | steals: {steals} | blocks: {blocks} | turnovers: {turnovers} | ' \
               'personal fouls: {personal_fouls}'.format(seconds_played=self.seconds_played,
                                                         field_goals_made=self.field_goals_made,
                                                         field_goals_attempted=self.field_goals_attempted,
                                                         three_point_field_goals_made=self.three_point_field_goals_made,
                                                         three_point_field_goals_attempted=self.three_point_field_goals_attempted,
                                                         free_throws_made=self.free_throws_made,
                                                         free_throws_attempted=self.free_throws_attempted,
                                                         offensive_rebounds=self.offensive_rebounds,
                                                         defensive_rebounds=self.defensive_rebounds,
                                                         assists=self.assists, steals=self.steals, blocks=self.blocks,
                                                         turnovers=self.turnovers,  personal_fouls=self.personal_fouls)

    def get_additional_unicode(self):
        raise NotImplementedError('Implement in concrete classes')
