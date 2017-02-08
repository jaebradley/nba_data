from enum import Enum


class PlayerStatus:
    def __init__(self, type, reason):
        assert isinstance(type, PlayerStatusType)

        self.type = type
        self.reason = reason

    @staticmethod
    def from_comment(comment):
        assert isinstance(comment, basestring)

        if not comment:
            return PlayerStatus(type=PlayerStatusType.active, reason=None)

        comment_parts = comment.split(' - ')

        if len(comment_parts) != 2:
            raise ValueError('Expected two comment parts for comment: %s', comment)

        return PlayerStatus(type=PlayerStatusType.from_abbreviation(abbreviation=comment_parts[0]),
                            reason=comment_parts[1])


class PlayerStatusType(Enum):
    active = 'active'
    did_not_play = 'did not play'
    did_not_dress = 'did not dress'

    @staticmethod
    def from_abbreviation(abbreviation):
        player_status_type = player_status_type_abbreviation_map.get(abbreviation)

        if player_status_type is None:
            raise ValueError('Unknown player status abbreviation: %s', abbreviation)

        return player_status_type


player_status_type_abbreviation_map = {
    'DNP': PlayerStatusType.did_not_play,
    'DND': PlayerStatusType.did_not_dress
}