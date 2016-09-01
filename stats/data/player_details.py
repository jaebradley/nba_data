from stats.data.player import Player
from stats.data.position import Position


class PlayerDetails:
    def __init__(self, player, birth_date, height, weight, jersey_number, position):
        self.player = player
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        self.jersey_number = jersey_number
        self.position = position

    @staticmethod
    def create(nba_id, name, team_id, birth_date, height, weight, jersey_number, position_name):
        return PlayerDetails(player=Player.create(nba_id=nba_id, display_first_last=name, team_id=team_id),
                             birth_date=birth_date,
                             height=height,
                             weight=weight,
                             jersey_number=jersey_number,
                             position=Position.get_position_from_name(position_name))