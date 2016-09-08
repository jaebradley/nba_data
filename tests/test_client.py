from unittest import TestCase, skip

from stats.client.client import Client
from stats.data.advanced_box_score import AdvancedBoxScore


@skip("skip non-local testing")
class TestClient(TestCase):
    def test_get_advanced_box_score(self):
        advanced_box_score = Client.get_advanced_box_score(game_id="0021501205")
        self.assertIsNotNone(advanced_box_score)
        self.assertIsInstance(advanced_box_score, AdvancedBoxScore)


