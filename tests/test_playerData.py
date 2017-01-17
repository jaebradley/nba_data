from unittest import TestCase

from nba_data.data.player_data import PlayerData


class TestPlayerData(TestCase):
    def test_instantiation(self):
        player_id = '1234'
        name = 'jae'
        jersey = 0
        team_seasons = list()
        self.assertIsNotNone(PlayerData(player_id=player_id, name=name, jersey=jersey, team_seasons=team_seasons))
        self.assertIsNotNone(PlayerData(player_id=player_id, name=name, jersey=None, team_seasons=team_seasons))
        self.assertRaises(AssertionError, PlayerData, 1, name, jersey, team_seasons)
        self.assertRaises(AssertionError, PlayerData, player_id, 1, jersey, team_seasons)
        self.assertRaises(AssertionError, PlayerData, player_id, name, '1', team_seasons)
        self.assertRaises(AssertionError, PlayerData, player_id, name, jersey, 1)
