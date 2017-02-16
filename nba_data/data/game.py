class Game:

    def __init__(self, id, match_up):
        self.id = id
        self.match_up = match_up


class SeasonGame(Game):
    def __init__(self, id, match_up, season):
        self.season = season
        Game.__init__(self, id, match_up)


class LoggedGame(SeasonGame):

    def __init__(self, id, match_up, season, date, season_type, home_team_outcome):
        self.date = date
        self.season_type = season_type
        self.home_team_outcome = home_team_outcome
        SeasonGame.__init__(self, id=id, match_up=match_up, season=season)


class ScoreboardGame(SeasonGame):
    def __init__(self, id, season, start_time, match_up):
        self.start_time = start_time
        SeasonGame.__init__(self, id=id, match_up=match_up, season=season)
