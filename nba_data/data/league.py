from enum import Enum

from base_query_parameter import BaseQueryParameter


class League(BaseQueryParameter, Enum):
    nba = "00"
    aba = "01"

    @staticmethod
    def get_query_parameter_name():
        return "LeagueId"