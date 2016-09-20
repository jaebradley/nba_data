from team import Team


class AdvancedTeamBoxScore:
    def __init__(self, team, seconds_played, offensive_rating, defensive_rating,
                 teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
                 offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
                 effective_field_goal_percentage, true_shooting_percentage):

        assert isinstance(team, Team)

        self.team = team
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

    @staticmethod
    def create(team_id, seconds_played, offensive_rating, defensive_rating, teammate_assist_percentage,
               assist_to_turnover_ratio, assists_per_100_possessions, offensive_rebound_percentage,
               defensive_rebound_percentage, turnovers_per_100_possessions, effective_field_goal_percentage,
               true_shooting_percentage):

        assert isinstance(team_id, int)

        return AdvancedTeamBoxScore(team=Team.get_team_by_id(team_id=team_id), seconds_played=seconds_played,
                                    offensive_rating=offensive_rating, defensive_rating=defensive_rating,
                                    teammate_assist_percentage=teammate_assist_percentage,
                                    assist_to_turnover_ratio=assist_to_turnover_ratio,
                                    assists_per_100_possessions=assists_per_100_possessions,
                                    offensive_rebound_percentage=offensive_rebound_percentage,
                                    defensive_rebound_percentage=defensive_rebound_percentage,
                                    turnovers_per_100_possessions=turnovers_per_100_possessions,
                                    effective_field_goal_percentage=effective_field_goal_percentage,
                                    true_shooting_percentage=true_shooting_percentage)