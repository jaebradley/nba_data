from enum import Enum


class Position(Enum):
    guard = "GUARD"
    guard_forward = "GUARD-FORWARD"
    forward_guard = "FORWARD-GUARD"
    forward = "FORWARD"
    center = "CENTER"
    forward_center = "FORWARD-CENTER"

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
    "G-F": Position.guard_forward,
    "F-G": Position.forward_guard,
    "F": Position.forward,
    "C": Position.center,
    "F-C": Position.forward_center,
}

name_to_position_map = {
    "GUARD": Position.guard,
    "GUARD-FORWARD": Position.guard_forward,
    "FORWARD-GUARD": Position.forward_guard,
    "FORWARD": Position.forward,
    "CENTER": Position.center,
    "FORWARD-CENTER": Position.forward_center,
}