from stats.data.player import Player
from stats.data.team import Team


def deserialize_player(display_first_last, team_id, nba_id):
    return Player(name=display_first_last,
                  team=deserialize_team(team_id=team_id),
                  nba_id=nba_id)


def deserialize_team(team_id):
    return Team.get_team(team_id=team_id)