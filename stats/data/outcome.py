from enum import Enum


class Outcome(Enum):
    win = "win"
    loss = "loss"

    @staticmethod
    def get_outcome_from_abbreviation(abbreviation):
        lookup_value = outcome_abbreviation_to_outcome_map.get(abbreviation)
        if lookup_value is None:
            raise KeyError("unknown abbreviation: %s", abbreviation)

        return lookup_value


outcome_abbreviation_to_outcome_map = {
    "w": Outcome.win,
    "l": Outcome.loss,
}