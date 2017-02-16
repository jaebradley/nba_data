from nba_data.data.traditional_box_score import TraditionalBoxScore


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
