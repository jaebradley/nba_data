from decimal import Decimal
from unittest import TestCase

from stats.client.deserializers.advanced_box_score_deserializer import AdvancedBoxScoreDeserializer


class TestAdvancedBoxScorePlayerStatsDeserializer(TestCase):
    def test_instantiation(self):
        self.assertIsNotNone(AdvancedBoxScoreDeserializer())

    def test_parse_float(self):
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_float(None), Decimal("0.0"))
        self.assertRaises(ValueError, AdvancedBoxScoreDeserializer.parse_float, "jae")
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_float(1.50), Decimal("1.5"))

    def test_parse_percentage(self):
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_percentage(None), Decimal("0.0"))
        self.assertRaises(ValueError, AdvancedBoxScoreDeserializer.parse_percentage, "jae")
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_percentage(1.50), Decimal("150.0"))

    def test_parse_minutes(self):
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_minutes_representation_to_seconds(None), 0)
        self.assertEqual(AdvancedBoxScoreDeserializer.parse_minutes_representation_to_seconds(u"12:34"), 754)
        self.assertRaises(ValueError, AdvancedBoxScoreDeserializer.parse_minutes_representation_to_seconds, 1234)
        self.assertRaises(ValueError, AdvancedBoxScoreDeserializer.parse_minutes_representation_to_seconds, u"12:34:56")
        self.assertRaises(ValueError, AdvancedBoxScoreDeserializer.parse_minutes_representation_to_seconds, u"jae")
