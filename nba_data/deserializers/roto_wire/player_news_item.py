import datetime
from pytz import timezone, utc

from nba_data.data.injury_details import InjuryDetails, Status
from nba_data.data.player_news_item import PlayerNewsItem
from nba_data.data.position import Position
from nba_data.data.team import Team


class RotoWirePlayerNewsItemDeserializer:

    def __init__(self):
        pass

    caption_field_name = 'ListItemCaption'
    description_field_name = 'ListItemDescription'
    list_item_publish_date_field_name = 'ListItemPubDate'
    last_updated_field_name = 'lastUpdate'
    update_id_field_name = 'UpdateId'
    roto_id_field_name = 'RotoId'
    player_id_field_name = 'PlayerID'
    first_name_field_name = 'FirstName'
    last_name_field_name = 'LastName'
    position_abbreviation_field_name = 'Position'
    team_abbreviation_field_name = 'Team'
    team_code_field_name = 'TeamCode'
    date_field_name = 'Date'
    priority_field_name = 'Priority'
    player_code_field_name = 'player_code'
    headline_field_name = 'Headline'
    injured_field_name = 'Injured'
    injured_status_field_name = 'Injured_Status'
    injury_location_field_name = 'Injury_Location'
    injury_type_field_name = 'Injury_Type'
    injury_detail_field_name = 'Injury_Detail'
    injury_side_field_name = 'Injury_Side'
    date_time_format = '%m/%d/%Y %H:%M:%S %p'
    timezone = timezone('US/Central')

    @staticmethod
    def deserialize(data):
        position_abbreviation = data[RotoWirePlayerNewsItemDeserializer.position_abbreviation_field_name]
        caption = unicode(data[RotoWirePlayerNewsItemDeserializer.caption_field_name])
        date = data[RotoWirePlayerNewsItemDeserializer.date_field_name]
        description = unicode(data[RotoWirePlayerNewsItemDeserializer.description_field_name])

        is_injured = False
        if data[RotoWirePlayerNewsItemDeserializer.injured_field_name] == 'YES':
            is_injured = True

        team_abbreviation = data[RotoWirePlayerNewsItemDeserializer.team_abbreviation_field_name]
        team = Team.get_team_by_abbreviation(abbreviation=team_abbreviation)
        player_news_item_date = datetime.datetime.fromtimestamp(int(date), utc)
        source_update_id = int(data[RotoWirePlayerNewsItemDeserializer.update_id_field_name])
        source_id = int(data[RotoWirePlayerNewsItemDeserializer.roto_id_field_name])
        source_player_id = data[RotoWirePlayerNewsItemDeserializer.player_id_field_name]
        first_name = unicode(data[RotoWirePlayerNewsItemDeserializer.first_name_field_name])
        last_name = unicode(data[RotoWirePlayerNewsItemDeserializer.last_name_field_name])
        priority = int(data[RotoWirePlayerNewsItemDeserializer.priority_field_name])
        headline = unicode(data[RotoWirePlayerNewsItemDeserializer.headline_field_name])

        status = Status.from_value(data[RotoWirePlayerNewsItemDeserializer.injured_status_field_name])
        affected_area = unicode(data[RotoWirePlayerNewsItemDeserializer.injury_type_field_name])
        detail = unicode(data[RotoWirePlayerNewsItemDeserializer.injury_detail_field_name])
        side = unicode(data[RotoWirePlayerNewsItemDeserializer.injury_side_field_name])
        position = Position.get_position_from_abbreviation(abbreviation=position_abbreviation)

        injury_details = InjuryDetails(is_injured=is_injured, status=status, affected_area=affected_area,
                                       detail=detail, side=side)

        return PlayerNewsItem(caption=caption, description=description, source_update_id=source_update_id,
                              source_id=source_id, source_player_id=source_player_id, first_name=first_name,
                              last_name=last_name, position=position, team=team, published_at=player_news_item_date,
                              priority=priority, headline=headline, injury=injury_details)
