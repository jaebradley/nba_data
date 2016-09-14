from unittest import TestCase

from nba_data.data.position import Position, abbreviation_to_position_map, name_to_position_map


class TestPosition(TestCase):
    def test_get_position_from_abbreviation(self):
        guard = Position.get_position_from_abbreviation("g")
        self.assertEqual(guard, Position.guard)

        another_guard = Position.get_position_from_abbreviation("G")
        self.assertEqual(another_guard, Position.guard)

        self.assertRaises(ValueError, Position.get_position_from_abbreviation, "jae")

        self.assertEqual(abbreviation_to_position_map,
                         {
                            "G": Position.guard,
                            "F": Position.forward,
                            "C": Position.center,
                         })

    def test_get_position_from_name(self):
        guard = Position.get_position_from_name("GUARD")
        self.assertEqual(guard, Position.guard)

        another_guard = Position.get_position_from_name("guard")
        self.assertEqual(another_guard, Position.guard)

        self.assertRaises(ValueError, Position.get_position_from_name, "jae")

        self.assertEqual(name_to_position_map,
                         {
                            "GUARD": Position.guard,
                            "FORWARD": Position.forward,
                            "CENTER": Position.center,
                         })
