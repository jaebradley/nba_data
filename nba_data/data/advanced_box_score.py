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
