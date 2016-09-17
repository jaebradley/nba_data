from enum import Enum

from base_query_parameter import BaseQueryParameter


class CurrentSeasonOnly(BaseQueryParameter, Enum):
    yes = 1
    no = 0

    @staticmethod
    def get_query_parameter_name():
        return "isOnlyCurrentSeason"