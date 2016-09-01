from enum import Enum


class Position(Enum):
    guard = "G"
    forward = "F"
    center = "C"

    @staticmethod
    def get_position_from_abbreviation(abbreviation):
        position = abbreviation_to_position_map.get(abbreviation)

        if position is None:
            raise ValueError("Unknown position abbreviation: %s", abbreviation)

        return position

abbreviation_to_position_map = {
    "G": Position.guard,
    "F": Position.forward,
    "C": Position.center,
}