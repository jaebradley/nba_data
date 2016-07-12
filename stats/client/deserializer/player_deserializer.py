from stats.data.player import Player


def deserialize_player(display_last_comma_first, team_id):
    comma_delimited_player_name = str.split(display_last_comma_first, ",")
    Player(comma_delimited_player_name[0], comma_delimited_player_name[1], deserialize_team(team_id=team_id))


def deserialize_team(team_id):
    pass