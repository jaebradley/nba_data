from unittest import TestCase

from nba_data.data.base_query_parameter import BaseQueryParameter


class TestBaseQueryParameter(TestCase):
    def test_get_query_parameter_name(self):
        self.assertEqual(BaseQueryParameter.get_query_parameter_name(), "")
