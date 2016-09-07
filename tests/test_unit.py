from unittest import TestCase

from stats.data.unit import Unit


class TestUnit(TestCase):
    def test_get_unit_from_name(self):
        self.assertRaises(ValueError, Unit.get_unit_from_name, "bae jadley")
        self.assertEqual(Unit.bench, Unit.get_unit_from_name("bEnCh"))
