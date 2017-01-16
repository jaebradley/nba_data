class UriGenerator:
    stats_base_uri = "http://stats.nba.com/stats/"
    data_base_uri = "http://data.nba.net/"

    common_all_players_path = "commonallplayers"
    team_game_log_path = "teamgamelog"
    common_player_info_path = "commonplayerinfo"
    advanced_box_score_path = "boxscoreadvancedv2"
    traditional_box_score_path = "boxscoretraditionalv2"
    calendar_path = "calendar"

    def __init__(self):
        pass

    @staticmethod
    def generate_common_all_players_uri():
        return UriGenerator.stats_base_uri + UriGenerator.common_all_players_path

    @staticmethod
    def generate_team_game_log_uri():
        return UriGenerator.stats_base_uri + UriGenerator.team_game_log_path

    @staticmethod
    def generate_common_player_info_uri():
        return UriGenerator.stats_base_uri + UriGenerator.common_player_info_path

    @staticmethod
    def generate_advanced_box_score_uri():
        return UriGenerator.stats_base_uri + UriGenerator.advanced_box_score_path

    @staticmethod
    def generate_traditional_box_score_uri():
        return UriGenerator.stats_base_uri + UriGenerator.traditional_box_score_path

    @staticmethod
    def generate_data_uri(path):
        return UriGenerator.data_base_uri + "/data/10s/prod/v1/" + path

    @staticmethod
    def generate_calendar_data_uri():
        return UriGenerator.generate_data_uri(UriGenerator.calendar_path)
