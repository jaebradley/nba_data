from enum import Enum


class Position(Enum):
    guard = "GUARD"
    forward = "FORWARD"
    center = "CENTER"

    @staticmethod
    def get_position_from_abbreviation(abbreviation):
        position = abbreviation_to_position_map.get(abbreviation.upper())

        if position is None:
            raise ValueError("Unknown position abbreviation: %s", abbreviation)

        return position

    @staticmethod
    def get_position_from_name(name):
        position = name_to_position_map.get(name.upper())

        if position is None:
            raise ValueError("Unknown position name: %s", name)

        return position

abbreviation_to_position_map = {
    "G": Position.guard,
    "F": Position.forward,
    "C": Position.center,
}

name_to_position_map = {
    "GUARD": Position.guard,
    "FORWARD": Position.forward,
    "CENTER": Position.center,
}