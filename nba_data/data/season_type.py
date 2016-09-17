from enum import Enum

from base_query_parameter import BaseQueryParameter


class SeasonType(BaseQueryParameter, Enum):
    regular_season = "Regular Season"
    pre_season = "Pre Season"
    playoffs = "Playoffs"
    all_star = "All-Star"

    @staticmethod
    def get_query_parameter_name():
        return "SeasonType"

    @staticmethod
    def get_season_type(season_type_name):
        season_type = season_type_name_map.get(season_type_name)

        if season_type is None:
            raise ValueError("Unknown season type name: %s", season_type_name)

        return season_type

season_type_name_map = {
    "Regular Season": SeasonType.regular_season,
    "Pre Season": SeasonType.pre_season,
    "Playoffs": SeasonType.playoffs,
    "All-Star": SeasonType.all_star,
}