from stats.data.player import Player
from stats.data.position import Position


class PlayerDetails:
    def __init__(self, player, birth_date, height, weight, position):
        self.player = player
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        self.position = position

    @staticmethod
    def create(nba_id, name, team_id, birth_date, height, weight, position_abbreviation):
        return PlayerDetails(player=Player.create(nba_id=nba_id, display_first_last=name, team_id=team_id),
                             birth_date=birth_date,
                             height=height,
                             weight=weight,
                             position=Position.get_position_from_abbreviation(position_abbreviation))