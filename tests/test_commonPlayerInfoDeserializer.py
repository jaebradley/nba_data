import json
import os
from unittest import TestCase

from stats.client.deserializers.common_player_info_deserializer import CommonPlayerInfoDeserializer
from stats.data.team import Team
from tests.config import ROOT_DIRECTORY


class TestCommonPlayerInfoDeserializer(TestCase):
    def test_common_player_info_deserialization(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/commonplayerinfo.json')) as data_file:
            data = json.load(data_file)
            deserialized_player = CommonPlayerInfoDeserializer.deserialize_common_player_info(data)
            self.assertEqual(deserialized_player.player.name, "Russell Westbrook")
            self.assertEqual(deserialized_player.player.nba_id, 201566)
            self.assertEqual(deserialized_player.player.team, Team.oklahoma_city_thunder)
