from unittest import TestCase

from nba_data.data.season_player import SeasonPlayer


class TestPlayerData(TestCase):
    def test_instantiation(self):
        player_id = '1234'
        name = 'jae'
        jersey = 0
        team_seasons = list()
        self.assertIsNotNone(SeasonPlayer(id=player_id, name=name, jersey=jersey, team_seasons=team_seasons))