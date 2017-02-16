from team import Team
from nba_data.data.advanced_box_score import AdvancedBoxScore


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