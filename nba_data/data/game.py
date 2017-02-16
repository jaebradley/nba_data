class Game:

    def __init__(self, id, match_up):
        self.id = id
        self.match_up = match_up

    def __unicode__(self):
        return '{0} - {1}'.format(self.get_additional_unicode(), self.get_base_unicode())

    def get_base_unicode(self):
        return 'id: {id} | match up: {match_up}'.format(self.id, self.match_up)

    def get_additional_unicode(self):
        raise NotImplementedError('Implement in concrete classes')


class SeasonGame(Game):
    def __init__(self, id, match_up, season):
        self.season = season
        Game.__init__(self, id, match_up)

    def get_base_unicode(self):
        return 'season: {season} | {base_unicode}'.format(season=self.season, base_unicode=Game.get_base_unicode(self))

    def get_additional_unicode(self):
        raise NotImplementedError('Implement in concrete classes')


class LoggedGame(SeasonGame):

    def __init__(self, id, match_up, season, start_date, season_type, home_team_outcome):
        self.start_date = start_date
        self.season_type = season_type
        self.home_team_outcome = home_team_outcome
        SeasonGame.__init__(self, id=id, match_up=match_up, season=season)

    def get_additional_unicode(self):
        return 'start_date: {start_date} | season type: {season_type} | home team outcome: {home_team_outcome}'\
            .format(date=self.start_date, season_type=self.season_type, home_team_outcome=self.home_team_outcome)


class ScoreboardGame(SeasonGame):
    def __init__(self, id, season, start_time, match_up):
        self.start_time = start_time
        SeasonGame.__init__(self, id=id, match_up=match_up, season=season)

    def get_additional_unicode(self):
        return 'start time: {start_time}'.format(start_time=self.start_time)
