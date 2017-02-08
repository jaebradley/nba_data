from nba_data.data.player import Player
from nba_data.data.position import Position


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
        return PlayerDetails(player=Player.create(id=nba_id, name=name, team_id=team_id),
                             birth_date=birth_date,
                             height=height,
                             weight=weight,
                             jersey_number=jersey_number,
                             position=Position.get_position_from_name(position_name))