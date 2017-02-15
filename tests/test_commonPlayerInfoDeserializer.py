import json
import os
from datetime import datetime
from unittest import TestCase

from nba_data.data.position import Position
from nba_data.data.team import Team
from nba_data.deserializers.common_player_info_deserializer import CommonPlayerInfoDeserializer
from tests.config import ROOT_DIRECTORY


class TestCommonPlayerInfoDeserializer(TestCase):
    def test_instantiation(self):
        deserializer = CommonPlayerInfoDeserializer()
        self.assertTrue(deserializer.__dict__ == {})

    def test_common_player_info_deserialization(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/commonplayerinfo.json')) as data_file:
            data = json.load(data_file)
            deserialized_player = CommonPlayerInfoDeserializer.deserialize(data)
            self.assertEqual(deserialized_player.player.name, "Russell Westbrook")
            self.assertEqual(deserialized_player.player.id, 201566)
            self.assertEqual(deserialized_player.player.team, Team.oklahoma_city_thunder)
            self.assertEqual(deserialized_player.birth_date, datetime(year=1988, month=11, day=12).date())
            self.assertEqual(deserialized_player.height, 75)
            self.assertEqual(deserialized_player.weight, 200)
            self.assertEqual(deserialized_player.jersey_number, 0)
            self.assertEqual(deserialized_player.position, Position.guard)

    def test_common_player_info_errored_deserialization(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/errorcommonplayerinfo.json')) as data_file:
            data = json.load(data_file)
            deserialized_player = CommonPlayerInfoDeserializer.deserialize(data)
            self.assertIsNone(deserialized_player.height)
            self.assertIsNone(deserialized_player.weight)
            self.assertIsNone(deserialized_player.jersey_number)
