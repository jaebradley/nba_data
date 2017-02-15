from nba_data.data.season_player import SeasonPlayer
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
    team_season_season_start_year_field_name = 'seasonStart'
    team_season_season_end_year_field_name = 'seasonEnd'

    def __init__(self):
        pass

    @staticmethod
    def deserialize(data):
        if PlayersDeserializer.league_field_name not in data:
            raise ValueError('Unable to deserialize league field for %s', data)

        league = data[PlayersDeserializer.league_field_name]

        if PlayersDeserializer.standard_field_name not in league:
            raise ValueError('Unable to deserialize standard field for %s', data)

        players = league[PlayersDeserializer.standard_field_name]

        return [PlayersDeserializer.parse_player(data=player)
                for player in players]

    @staticmethod
    def parse_player(data):
        if PlayersDeserializer.player_id_field_name not in data:
            raise ValueError('Unable to parse id field for %s', data)

        if PlayersDeserializer.first_name_field_name not in data:
            raise ValueError('Unable to parse first name field for %s', data)

        if PlayersDeserializer.last_name_field_name not in data:
            raise ValueError('Unable to parse last name field for %s', data)

        if PlayersDeserializer.jersey_field_name not in data:
            raise ValueError('Unable to parse jersey value field for %s', data)

        player_id = data[PlayersDeserializer.player_id_field_name]
        first_name = data[PlayersDeserializer.first_name_field_name]
        last_name = data[PlayersDeserializer.last_name_field_name]
        jersey_value = data[PlayersDeserializer.jersey_field_name]
        jersey = int(jersey_value) if jersey_value.isdigit() else None
        name = '{0} {1}'.format(first_name, last_name)
        team_seasons = PlayersDeserializer.parse_team_seasons(data=data)

        return SeasonPlayer(id=player_id, name=name, jersey=jersey, team_seasons=team_seasons)

    @staticmethod
    def parse_team_seasons(data):
        if PlayersDeserializer.team_seasons_field_name not in data:
            raise ValueError('Unable to parse team seasons field for %s', data)

        team_seasons = data[PlayersDeserializer.team_seasons_field_name]

        return [PlayersDeserializer.parse_team_season(data=team_season)
                for team_season in team_seasons]

    @staticmethod
    def parse_team_season(data):
        return TeamSeasonRange(team=PlayersDeserializer.parse_team(data=data),
                               season_range=PlayersDeserializer.parse_season_range(data=data))

    @staticmethod
    def parse_team(data):
        if PlayersDeserializer.team_seasons_team_id_field_name not in data:
            raise ValueError('Unable to parse team id for %s', data)

        team_id = int(data[PlayersDeserializer.team_seasons_team_id_field_name])
        return Team.get_team_by_id(team_id=team_id)

    @staticmethod
    def parse_season_range(data):
        if PlayersDeserializer.team_season_season_start_year_field_name not in data:
            raise ValueError('Unable to parse season start for %s', data)

        if PlayersDeserializer.team_season_season_end_year_field_name not in data:
            raise ValueError('Unable to parse season end for %s', data)

        season_range_start_year = int(data[PlayersDeserializer.team_season_season_start_year_field_name])
        season_range_end_year = int(data[PlayersDeserializer.team_season_season_end_year_field_name])

        # NBA API returns start year for last year in range
        return SeasonRange(start=Season.get_season_by_start_year(year=season_range_start_year),
                           end=Season.get_season_by_start_year(year=season_range_end_year))
