# TODO: @jbradley in the future, reconcile / deprecate Game class
# TODO: @jbradley currently this class is fulfilling needs of dfs_site_data project - in the future, add more fields


class ScoreboardGame:

    def __init__(self, id, season, start_time, match_up):
        self.id = id
        self.season = season
        self.start_time = start_time
        self.match_up = match_up

    def __unicode__(self):
        return 'id: {0} | season: {1} | start time: {2} | match up: {3}'.format(self.id, self.season, self.start_time,
                                                                                self.match_up)

