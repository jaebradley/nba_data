from enum import Enum


class BaseQueryParameter(Enum):
    @staticmethod
    def get_query_parameter_name():
        return ""