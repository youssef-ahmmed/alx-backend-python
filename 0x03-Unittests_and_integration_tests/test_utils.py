#!/usr/bin/env python3
"""Unit testing for utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing nested map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test using parameterized to minimize duplications"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
