from nba_data.deserializers.roto_wire.player_news_item import RotoWirePlayerNewsItemDeserializer


class RotoWirePlayerNewsItemsDeserializer:
    def __init__(self):
        pass

    list_items_field_name = 'ListItems'

    @staticmethod
    def deserialize(data):
        return [
            RotoWirePlayerNewsItemDeserializer.deserialize(data=player_news_item)
            for player_news_item in data[RotoWirePlayerNewsItemsDeserializer.list_items_field_name]
        ]
