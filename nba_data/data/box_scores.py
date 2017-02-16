class AdvancedBoxScore:
    def __init__(self, seconds_played, offensive_rating, defensive_rating,
                 teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
                 offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
                 effective_field_goal_percentage, true_shooting_percentage):
        self.seconds_played = seconds_played
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating
        self.teammate_assist_percentage = teammate_assist_percentage
        self.assist_to_turnover_ratio = assist_to_turnover_ratio
        self.assists_per_100_possessions = assists_per_100_possessions
        self.offensive_rebound_percentage = offensive_rebound_percentage
        self.defensive_rebound_percentage = defensive_rebound_percentage
        self.turnovers_per_100_possessions = turnovers_per_100_possessions
        self.effective_field_goal_percentage = effective_field_goal_percentage
        self.true_shooting_percentage = true_shooting_percentage

    def __unicode__(self):
        return '{0} | {1}'.format(self.get_additional_unicode(), self.get_base_unicode)

    def get_base_unicode(self):
        return 'seconds played: {seconds_played} | offensive rating: {offensive_rating} | ' \
               'defensive rating: {defensive_rating} | teammate assist percentage: {teammate_assist_percentage} |' \
               'assist to turnover ratio: {assist_to_turnover_ratio} | ' \
               'assists per 100 possessions: {assists_per_100_possessions} | ' \
               'offensive rebound percentage: {offensive_rebound_percentage} |' \
               'defensive rebound percentage: {defensive_rebound_percentage} |' \
               'turnovers per 100 possessions: {turnovers_per_100_possessions} |' \
               'effective field goal percentage: {effective_field_goal_percentage} |' \
               'true shooting percentage: {true_shooting_percentage}'\
            .format(seconds_played=self.seconds_played, offensive_rating=self.offensive_rating,
                    defensive_rating=self.defensive_rating, teammate_assist_percentage=self.teammate_assist_percentage,
                    assist_to_turnover_ratio=self.assist_to_turnover_ratio,
                    assists_per_100_possessions=self.assists_per_100_possessions,
                    offensive_rebound_percentage=self.offensive_rebound_percentage,
                    defensive_rebound_percentage=self.defensive_rebound_percentage,
                    turnovers_per_100_possessions=self.turnovers_per_100_possessions,
                    effective_field_goal_percentage=self.effective_field_goal_percentage,
                    true_shooting_percentage=self.true_shooting_percentage)

    def get_additional_unicode(self):
        return NotImplementedError('Should be implemented in concrete class')


class AdvancedPlayerBoxScore(AdvancedBoxScore):
    def __init__(self, player, seconds_played, offensive_rating, defensive_rating,
                 teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
                 offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
                 effective_field_goal_percentage, true_shooting_percentage, usage_percentage):
        self.player = player
        self.usage_percentage = usage_percentage
        AdvancedBoxScore.__init__(self, seconds_played=seconds_played,
                                  offensive_rating=offensive_rating, defensive_rating=defensive_rating,
                                  teammate_assist_percentage=teammate_assist_percentage,
                                  assist_to_turnover_ratio=assist_to_turnover_ratio,
                                  assists_per_100_possessions=assists_per_100_possessions,
                                  offensive_rebound_percentage=offensive_rebound_percentage,
                                  defensive_rebound_percentage=defensive_rebound_percentage,
                                  turnovers_per_100_possessions=turnovers_per_100_possessions,
                                  effective_field_goal_percentage=effective_field_goal_percentage,
                                  true_shooting_percentage=true_shooting_percentage)

    def get_additional_unicode(self):
        return 'player: {player} | usage percentage: {usage_percentage}'.format(player=self.player,
                                                                                usage_percentage=self.usage_percentage)


class AdvancedTeamBoxScore(AdvancedBoxScore):
    def __init__(self, team, seconds_played, offensive_rating, defensive_rating,
                 teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
                 offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
                 effective_field_goal_percentage, true_shooting_percentage):
        self.team = team
        AdvancedBoxScore.__init__(self, seconds_played=seconds_played,
                                  offensive_rating=offensive_rating, defensive_rating=defensive_rating,
                                  teammate_assist_percentage=teammate_assist_percentage,
                                  assist_to_turnover_ratio=assist_to_turnover_ratio,
                                  assists_per_100_possessions=assists_per_100_possessions,
                                  offensive_rebound_percentage=offensive_rebound_percentage,
                                  defensive_rebound_percentage=defensive_rebound_percentage,
                                  turnovers_per_100_possessions=turnovers_per_100_possessions,
                                  effective_field_goal_percentage=effective_field_goal_percentage,
                                  true_shooting_percentage=true_shooting_percentage)

    def get_additional_unicode(self):
        return 'team: {team}'.format(team=self.team)


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


class TraditionalPlayerBoxScore(TraditionalBoxScore):
    def __init__(self, player, seconds_played, field_goals_made, field_goals_attempted,
                 three_point_field_goals_made, three_point_field_goals_attempted,
                 free_throws_made, free_throws_attempted, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls, plus_minus):
        self.player = player
        self.plus_minus = plus_minus
        TraditionalBoxScore.__init__(self, seconds_played=seconds_played, field_goals_made=field_goals_made,
                                     field_goals_attempted=field_goals_attempted,
                                     three_point_field_goals_made=three_point_field_goals_made,
                                     three_point_field_goals_attempted=three_point_field_goals_attempted,
                                     free_throws_made=free_throws_made, free_throws_attempted=free_throws_attempted,
                                     offensive_rebounds=offensive_rebounds, defensive_rebounds=defensive_rebounds,
                                     assists=assists, steals=steals, blocks=blocks, turnovers=turnovers,
                                     personal_fouls=personal_fouls)

    def get_additional_unicode(self):
        return 'player: {player} | plus minus: {plus_minus}'.format(player=self.player, plus_minus=self.plus_minus)


class TraditionalTeamBoxScore(TraditionalBoxScore):
    def __init__(self, team, seconds_played, field_goals_made, field_goals_attempted, free_throws_attempted,
                 three_point_field_goals_made, three_point_field_goals_attempted,
                 free_throws_made, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls):
        self.team = team
        TraditionalBoxScore.__init__(self, seconds_played=seconds_played, field_goals_made=field_goals_made,
                                     field_goals_attempted=field_goals_attempted,
                                     three_point_field_goals_made=three_point_field_goals_made,
                                     three_point_field_goals_attempted=three_point_field_goals_attempted,
                                     free_throws_made=free_throws_made, free_throws_attempted=free_throws_attempted,
                                     offensive_rebounds=offensive_rebounds, defensive_rebounds=defensive_rebounds,
                                     assists=assists, steals=steals, blocks=blocks, turnovers=turnovers,
                                     personal_fouls=personal_fouls)

    def get_additional_unicode(self):
        return 'team: {team}'.format(self.team)


class GameBoxScore:
    def __init__(self, game_id, player_box_scores, team_box_scores):
        self.game_id = game_id
        self.player_box_scores = player_box_scores
        self.team_box_scores = team_box_scores
