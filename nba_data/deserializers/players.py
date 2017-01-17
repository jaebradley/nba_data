from nba_data.data.player_data import PlayerData
from nba_data.data.season import Season
from nba_data.data.season_range import SeasonRange
from nba_data.data.team import Team
from nba_data.data.team_season_range import TeamSeasonRange


class PlayersDeserializer:
    # I don't know if there's a non-standard league
    league_field_name = 'league'
    standard_field_name = 'standard'
    first_name_field_name = 'firstName'
    last_name_field_name = 'lastName'
    player_id_field_name = 'personId'
    team_id_field_name = 'teamId'
    jersey_field_name = 'jersey'
    team_seasons_field_name = 'teams'
    team_seasons_team_id_field_name = 'teamId'
    team_season_season_start_field_name = 'seasonStart'
    team_season_season_end_field_name = 'seasonEnd'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(players_json):
        players = list()
        for player in players_json[PlayersDeserializer.league_field_name][PlayersDeserializer.standard_field_name]:
            player_id = str(player[PlayersDeserializer.player_id_field_name])
            first_name = str(player[PlayersDeserializer.first_name_field_name])
            last_name = str(player[PlayersDeserializer.last_name_field_name])
            jersey_value = player[PlayersDeserializer.jersey_field_name]
            jersey = int(jersey_value) if jersey_value.isdigit() else None

            team_seasons = list()
            for team_season_json in player[PlayersDeserializer.team_seasons_field_name]:
                team_seasons.append(PlayersDeserializer.deserialize_team_season(team_season_json=team_season_json))

            players.append(PlayerData(player_id=player_id, name=first_name + ' ' + last_name, jersey=jersey,
                                      team_seasons=team_seasons))
        return players

    @staticmethod
    def deserialize_team_season(team_season_json):
        team_id = int(team_season_json[PlayersDeserializer.team_seasons_team_id_field_name])
        season_start = int(team_season_json[PlayersDeserializer.team_season_season_start_field_name])
        season_end = int(team_season_json[PlayersDeserializer.team_season_season_end_field_name])
        return TeamSeasonRange(team=Team.get_team_by_id(team_id=team_id),
                               season_range=SeasonRange(start=Season.get_season_by_start_year(year=season_start),
                                                        end=Season.get_season_by_start_year(year=season_end)))