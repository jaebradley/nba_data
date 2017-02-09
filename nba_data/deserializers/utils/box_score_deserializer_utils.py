class BoxScoreDeserializerUtils:

    def __init__(self):
        pass

    @staticmethod
    def parse_minutes_representation_to_seconds(minutes):
        if minutes is None:
            return 0

        if not isinstance(minutes, unicode):
            raise ValueError("Expected a unicode minutes representation instead of %s", minutes)

        if ":" in minutes:
            minutes_parts = minutes.split(":")

            if not len(minutes_parts) == 2:
                raise ValueError("Expected a minute and seconds part instead of %s", minutes_parts)

            return int(minutes_parts[0]) * 60 + int(minutes_parts[1])

        raise ValueError("Unknown minutes value: %s", minutes)
