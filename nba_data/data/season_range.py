from nba_data.data.season import Season

# TODO: @jbradley add assertions to compare start and end


class SeasonRange:
    def __init__(self, start, end):
        assert isinstance(start, Season)
        assert isinstance(end, Season)

        self.start = start
        self.end = end
