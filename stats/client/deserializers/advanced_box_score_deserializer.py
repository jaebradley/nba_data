from decimal import Decimal, ROUND_HALF_UP


class AdvancedBoxScoreDeserializer:

    default_decimal_value = Decimal("0.0")

    def __init__(self):
        pass

    @staticmethod
    def parse_float(float_value):
        if float_value is None:
            return AdvancedBoxScoreDeserializer.default_decimal_value

        if not isinstance(float_value, float):
            raise ValueError("Expected a float instead of %s", float_value)

        return Decimal(Decimal(float_value).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))

    @staticmethod
    def parse_percentage(percentage):
        if percentage is None:
            return AdvancedBoxScoreDeserializer.default_decimal_value

        if not isinstance(percentage, float):
            raise ValueError("Expected a float instead of %s", percentage)

        return Decimal((100 * Decimal(percentage)).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))

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