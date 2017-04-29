# -*- coding: utf-8 -*-

import json
import os
from unittest import TestCase

from nba_data.deserializers.roto_wire.player_news_items import RotoWirePlayerNewsItemsDeserializer
from tests.config import ROOT_DIRECTORY


class TestRotoWirePlayerNewsItemsDeserializer(TestCase):
    def test_instantiation(self):
        deserializer = RotoWirePlayerNewsItemsDeserializer()
        self.assertTrue(deserializer.__dict__ == {})

    def test_deserialize_common_all_players(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/rotowire_player_news.json')) as data_file:
            data = json.load(data_file)
            deserialized_player_news = RotoWirePlayerNewsItemsDeserializer.deserialize(data)
            expected_caption = u'Mahinmi (calf) has been ruled out for Friday’s Game 6 against the Hawks, Candace Buckner of The Washington Post reports.'
            expected_description = u'There has been no word of Mahinmi being able to put together any work on the court, so the big man returning any time soon seems doubtful. With Jason Smith dealing with a left calf strain himself and being a game-time decision, the Wizards are facing serious frontcourt depth issues ahead of what could be a series-clinching Game 6. If Smith is also ruled out, Marcin Gortat would likely be forced to play heavy minutes as the starting center.'

            self.assertEqual(len(deserialized_player_news), 130)
            ian_mahinmi_new_item = deserialized_player_news[0]
            self.assertEqual(ian_mahinmi_new_item.caption, expected_caption)
            self.assertEqual(ian_mahinmi_new_item.description, expected_description)
