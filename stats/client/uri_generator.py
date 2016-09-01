class UriGenerator:
    base_uri = "http://stats.nba.com/stats/"
    common_all_players_path = "commonallplayers"
    team_game_log_path = "teamgamelog"
    common_player_info_path = "commonplayerinfo"

    def __init__(self):
        pass

    @staticmethod
    def generate_common_all_players_uri():
        return UriGenerator.base_uri + UriGenerator.common_all_players_path

    @staticmethod
    def generate_team_game_log_uri():
        return UriGenerator.base_uri + UriGenerator.team_game_log_path

    @staticmethod
    def generate_common_player_info_uri():
        return UriGenerator.base_uri + UriGenerator.common_player_info_path
