from box_score_player import BoxScorePlayer
from player_status import PlayerStatus


class AdvancedPlayerBoxScore:
    def __init__(self, player, seconds_played, offensive_rating, defensive_rating,
                 teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
                 offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
                 effective_field_goal_percentage, true_shooting_percentage, usage_percentage):

        assert isinstance(player, BoxScorePlayer)

        self.player = player
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
        self.usage_percentage = usage_percentage

    @staticmethod
    def create(player_name, player_id, team_id, comment, seconds_played, offensive_rating, defensive_rating,
               teammate_assist_percentage, assist_to_turnover_ratio, assists_per_100_possessions,
               offensive_rebound_percentage, defensive_rebound_percentage, turnovers_per_100_possessions,
               effective_field_goal_percentage, true_shooting_percentage, usage_percentage):
        return AdvancedPlayerBoxScore(player=BoxScorePlayer.create(name=player_name, team_id=team_id, id=player_id,
                                                                   status=PlayerStatus.from_comment(comment=comment)),
                                      seconds_played=seconds_played, offensive_rating=offensive_rating,
                                      defensive_rating=defensive_rating, teammate_assist_percentage=teammate_assist_percentage,
                                      assist_to_turnover_ratio=assist_to_turnover_ratio, assists_per_100_possessions=assists_per_100_possessions,
                                      offensive_rebound_percentage=offensive_rebound_percentage, defensive_rebound_percentage=defensive_rebound_percentage,
                                      turnovers_per_100_possessions=turnovers_per_100_possessions, effective_field_goal_percentage=effective_field_goal_percentage,
                                      true_shooting_percentage=true_shooting_percentage, usage_percentage=usage_percentage)