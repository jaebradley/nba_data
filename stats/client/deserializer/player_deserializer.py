from stats.data.player import Player
from stats.data.team import Team


def deserialize_player(display_first_last, team_id):
    return Player(display_first_last, deserialize_team(team_id=team_id))


def deserialize_team(team_id):
    return Team.get_team(team_id=team_id)