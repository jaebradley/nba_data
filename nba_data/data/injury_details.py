from enum import Enum


class InjuryDetails:
    def __init__(self, is_injured, status, affected_area, detail, side):
        self.is_injured = is_injured
        self.status = status
        self.affected_area = affected_area
        self.detail = detail
        self.side = side


class Status(Enum):
    out = 'Out'
    game_time_decision = 'Game Time Decision'
    healthy = 'Healthy'

    @staticmethod
    def from_value(value):
        return status_mapping.get(value)


status_mapping = {
    'Out': Status.out,
    'GTD': Status.game_time_decision,
    'Healthy': Status.healthy
}
