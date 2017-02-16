import json
import os
from datetime import date
from unittest import TestCase

from nba_data.data.date_range import DateRange
from nba_data.deserializers.calendar import CalendarDeserializer
from tests.config import ROOT_DIRECTORY


class TestCalendarDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(CalendarDeserializer())

    def test_deserialize(self):
        start = date(year=2016, month=12, day=1)
        end = date(year=2017, month=2, day=15)
        date_range = DateRange(start=start, end=end)
        very_beginning = date(year=2015, month=10, day=2)
        very_end = date(year=2017, month=4, day=12)
        complete_date_range = DateRange(start=very_beginning, end=very_end)

        # TODO: @jbradley make this piss-poor test slightly more robust in the future
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/calendar.json')) as data_file:
            data = json.load(data_file)
            calendar = CalendarDeserializer.deserialize(calendar_json=data, date_range=date_range)
            self.assertIsNotNone(calendar)
            self.assertEqual(len(calendar), 76)

            complete_calendar_ignoring_dates_without_games = CalendarDeserializer.deserialize(calendar_json=data,
                                                                                              date_range=complete_date_range)
            self.assertIsNotNone(complete_calendar_ignoring_dates_without_games)
            self.assertEqual(len(complete_calendar_ignoring_dates_without_games), 416)

            complete_calendar = CalendarDeserializer.deserialize(calendar_json=data, date_range=complete_date_range,
                                                                 ignore_dates_without_games=False)
            self.assertIsNotNone(complete_calendar)
            self.assertEqual(len(complete_calendar), 559)