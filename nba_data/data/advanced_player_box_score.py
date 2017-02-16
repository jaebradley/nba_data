from nba_data.data.advanced_box_score import AdvancedBoxScore


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