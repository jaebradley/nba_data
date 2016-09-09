from decimal import Decimal, ROUND_HALF_UP


class AdvancedBoxScoreDeserializerUtils:

    default_decimal_value = Decimal("0.0")

    def __init__(self):
        pass

    @staticmethod
    def parse_float(float_value):
        if float_value is None:
            return AdvancedBoxScoreDeserializerUtils.default_decimal_value

        if not isinstance(float_value, float):
            raise ValueError("Expected a float instead of %s", float_value)

        return Decimal(Decimal(float_value).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))

    @staticmethod
    def parse_percentage(percentage):
        if percentage is None:
            return AdvancedBoxScoreDeserializerUtils.default_decimal_value

        if not isinstance(percentage, float):
            raise ValueError("Expected a float instead of %s", percentage)

        return Decimal((100 * Decimal(percentage)).quantize(Decimal(".1"), rounding=ROUND_HALF_UP))