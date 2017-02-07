from enum import Enum


class PlayerStatus:
    def __init__(self, type, reason):
        assert isinstance(type, PlayerStatusType)
        assert isinstance(reason, basestr)

        self.type = type
        self.reason = reason

    @staticmethod
    def from_comment(comment):
        comment_parts = comment.split(' - ')
        assert len(comment_parts) == 2

        return PlayerStatus(type=PlayerStatusType.from_abbreviation(abbreviation=comment_parts[0]),
                            reason=comment_parts[1])


class PlayerStatusType(Enum):
    active = 'active'
    did_not_play = 'did not play'
    did_not_dress = 'did not dress'

    @staticmethod
    def from_abbreviation(abbreviation):
        if abbreviation is None:
            return PlayerStatusType.active

        player_status_type = player_status_type_abbreviation_map.get(abbreviation)

        if player_status_type is None:
            raise ValueError('Unknown player status abbreviation: %s', abbreviation)

        return player_status_type


player_status_type_abbreviation_map = {
    'DNP': PlayerStatusType.did_not_play,
    'DND': PlayerStatusType.did_not_dress
}