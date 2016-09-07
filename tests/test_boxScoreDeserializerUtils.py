from unittest import TestCase

from stats.client.deserializers.utils.box_score_deserializer_utils import BoxScoreDeserializerUtils


class TestBoxScoreDeserializerUtils(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(BoxScoreDeserializerUtils())

    def test_parse_minutes_representation_to_seconds(self):
        self.assertEqual(BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(None), 0)
        self.assertEqual(BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds(u"12:34"), 754)
        self.assertRaises(ValueError, BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds, 1234)
        self.assertRaises(ValueError, BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds, u"12:34:56")
        self.assertRaises(ValueError, BoxScoreDeserializerUtils.parse_minutes_representation_to_seconds, u"jae")
