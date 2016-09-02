from game import Game
from team import Team
from player import Player


class AdvancedPlayerBoxscore:
    def __init__(self, game, team, player, comment, seconds_played, offensive_rating, defensive_rating,
                 assist_percentage, assist_to_turnover_ratio, assist_ratio, offensive_rebound_percentage,
                 defensive_rebound_percentage, rebound_percentage, team_turnover_percentage,
                 effective_field_goal_percentage, true_shooting_percentage, usage_percentage, pace):
        self.game = game
        self.team = team
        self.player = player
        self.comment = comment
        self.seconds_played = seconds_played
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating
        self.assist_percentage = assist_percentage
        self.assist_to_turnover_ratio = assist_to_turnover_ratio
        self.assist_ratio = assist_ratio
        self.offensive_rebound_percentage = offensive_rebound_percentage
        self.defensive_rebound_percentage = defensive_rebound_percentage
        self.rebound_percentage = rebound_percentage
        self.team_turnover_percentage = team_turnover_percentage
        self.effective_field_goal_percentage = effective_field_goal_percentage
        self.true_shooting_percentage = true_shooting_percentage
        self.usage_percentage = usage_percentage
        self.pace = pace

    @staticmethod
    def create():