class BoxScore:
    def __init__(self, game_id, player_box_scores, team_box_scores):
        assert isinstance(game_id, str)
        assert isinstance(player_box_scores, list)
        assert isinstance(team_box_scores, list)

        self.game_id = game_id
        self.player_box_scores = player_box_scores
        self.team_box_scores = team_box_scores