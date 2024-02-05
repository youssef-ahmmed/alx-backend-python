#!/usr/bin/env python3
"""Unit testing for utils module"""
import unittest
from typing import Dict
from unittest.mock import patch, Mock

from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing nested map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test using parameterized to minimize duplications"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test Key Error exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for testing get json from a request"""

    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock):
        """Test with mock get request"""
        mock_get.json.return_value = test_payload
        mock_get.return_value = mock_get

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_with(test_url)


if __name__ == '__main__':
    unittest.main()
