from datetime import datetime

from nba_data.data.date_range import DateRange


class CalendarDeserializer:
    internal_field_name = "_internal"
    start_date_field_name = "startDate"
    end_date_field_name = "endDate"
    start_date_current_season_field_name = "startDateCurrentSeason"
    fields_to_ignore = { internal_field_name, start_date_field_name, end_date_field_name, start_date_current_season_field_name }
    date_format = "%Y%M%d"

    def __init__(self):
        pass

    # TODO: @jbradley add pub date time to returned object
    @staticmethod
    def deserialize(calendar_json, date_range=DateRange()):
        calendar_values = {}
        for key, value in calendar_json:
            if key not in CalendarDeserializer.fields_to_ignore:
                date_value = datetime.datetime.strptime(key, CalendarDeserializer.date_format).date()
                if date_range.is_date_in_range(value=date_value):
                    calendar_values[date_value] = value
        return calendar_values
