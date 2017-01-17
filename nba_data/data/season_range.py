from nba_data.data.season import Season


class SeasonRange:
    def __init__(self, start, end):
        assert isinstance(start, Season)
        assert isinstance(end, Season)

        self.start = start
        self.end = end
