from enum import Enum


class Unit(Enum):
    starters = "starters"
    bench = "bench"

    @staticmethod
    def get_unit_from_name(unit_name):
        unit = unit_name_to_unit_map.get(unit_name.upper())

        if unit is None:
            raise ValueError("Unknown unit name: %s", unit_name)

        return unit

unit_name_to_unit_map = {
    "STARTERS": Unit.starters,
    "BENCH": Unit.bench,
}
