from datetime import date


class DateRange:
    def __init__(self, start=date.today(), end=date.today()):
        assert isinstance(start, date)
        assert isinstance(end, date)
        assert start <= end

        self.start = start
        self.end = end

    def is_date_in_range(self, value):
        assert isinstance(value, date)

        return self.start <= value <= self.end