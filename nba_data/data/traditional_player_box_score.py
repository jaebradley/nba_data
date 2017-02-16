from nba_data.data.traditional_box_score import TraditionalBoxScore


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
